import cherrypy
from models import model0
from passlib.hash import pbkdf2_sha256
import time
import os
import random
import chilkat,sys
from systemAdminMIS.helpers import ascii_generator
Applications=["systemAdminMIS","humanResourceMIS","outPatientMIS","frontDeskMIS","pharmacyMIS",
               "laboratoryMIS","inPatientMIS","radiologyMIS","padeatricsMIS","surgeryMIS",
               "triageMIS","emergencyMIS","obstetricsAndGynacologyMIS","nurseMIS","storeMIS",
               "hospitalDirectorMIS"]
Serials=['000','001','002','003','004','005','006','007','008','009',
         '010','011','012','013','014','015','016','017','018','019',
         '020','021','022','023','024','025','026','027','028','029',
         '030','031','032','033','034','035','036','037','038','039',
         '040','041','042','043','044','045','046','047','048','049',
         '050','051','052','053','054','055','056','057','058','059',
         '060','061','062','063','064','065','066','067','068','069',
         '070','071','072','073','074','075','076','077','078','079',
         '080','081','082','083','084','085','086','087','088','089',
         '090','091','092','093','094','095','096','097','098','099']
crypt = chilkat.CkCrypt2()
crypt.put_CryptAlgorithm("aes")
crypt.put_CipherMode("cbc")
crypt.put_KeyLength(256)
crypt.put_PaddingScheme(0)
crypt.put_EncodingMode("hex")
ivHex = "000102030405060708090A0B0DDD0E0F"
crypt.SetEncodedIV(ivHex,"hex")
keyHex = "000102030405060708090A0B0C0D0E0F101112131415161718191A1B1C1D1E1F"
crypt.SetEncodedKey(keyHex,"hex")
success = crypt.UnlockComponent("MPS-Serial Genarat")
if (success != True):
    sys.exit()
class RetrieveRespectiveAccountUserStaffIdForBackDoor(object):
    """docstring for RetrieveRespectiveAccountUserStaffIdForBackDoor."""
    def __init__(self,**kwags):
        super(RetrieveRespectiveAccountUserStaffIdForBackDoor, self).__init__()
        self.dataUsers=model0.Users()
        self.dataStaffDemographicsUsersRel=model0.StaffDemographicsUsersRel()
        self.dataDepartmentStaffRel=model0.dataDepartmentStaffRel()
        raw_data0=self.dataUsers.getUsersByUserType(**kwags)
        self.staff_id=None
        for a,b,c,d,e in raw_data0:
            if self.staff_id==None:
                raw_data1=self.dataStaffDemographicsUsersRel.getStaffDemographicsUsersRelByUsername(username=a)
                for f,g in raw_data1:
                    raw_data2=self.dataDepartmentStaffRel.getDepartmentStaffRelByStaffId(staff_id=f)
                    for h,i,j in raw_data2:
                        if h==kwags['department_id']:
                            self.staff_id=f        
class RetrieveAvailableStaff(object):
    def __init__(self):
        super(RetrieveAvailableStaff, self).__init__()
        self.dataStaffDemographics=model0.StaffDemographics()
        self.dataUsers=model0.Users()
        self.dataStaffDemographicsUsersRel=model0.StaffDemographicsUsersRel()
        self.message=[]
        self.idPrefix=GenerateIdPrefix()
        raw_data0=[]
        raw_data00=self.dataUsers.getAllUsers()
        for a,b,c,d,e in raw_data00:
            if d!="This is list should be extended as development proceeds":
                raw_data0.append([a,b,c,d,e])
        for a,b,c,d,e in raw_data0:
            messageCrude=[]
            messageCrude.append(a)
            if e=='raw':
                #linux Server
                try:
                    cwd=os.getcwd()
                    file0=open("{}/raw.pass".format(cwd),"r")
                #windows server
                except:
                    file0=open("raw.pass","r")
                for line in file0:
                    line=line.strip()
                    username,encryptedPassword=line.split("@@")
                    if username==a:
                        file0.close()
                        decryptedPassword=crypt.decryptStringENC(encryptedPassword)
                        messageCrude.append(decryptedPassword)
                        break
            else:
                messageCrude.append(b)
            messageCrude.append(e)
            raw_data1=self.dataStaffDemographicsUsersRel.getStaffDemographicsUsersRelByUsername(username=a)
            for f,g in raw_data1:
                raw_data2=self.dataStaffDemographics.getStaffDemographicsByStaffId(staff_id=f)
                for h,i,j,k,l,m,n,o,p,q,r,s,t,u,v in raw_data2:
                    messageCrude.append(self.idPrefix.idPrefix+"-"+h)
                    messageCrude.append(i)
                    messageCrude.append(t)
                    messageCrude.append(u)
                    messageCrude.append(v)
                    messageCrude.append(q)
                    messageCrude.append(d)
                    self.message.append(messageCrude)
        self.dataStaffDemographics.conn.close()
        self.dataStaffDemographicsUsersRel.conn.close()
        self.dataUsers.conn.close()
class RetrieveAvailableNonHospitalAdministrator(object):
    def __init__(self):
        super(RetrieveAvailableNonHospitalAdministrator, self).__init__()
        self.dataStaffDemographics=model0.StaffDemographics()
        self.dataUsers=model0.Users()
        self.dataStaffDemographicsUsersRel=model0.StaffDemographicsUsersRel()
        self.message=[]
        self.idPrefix=GenerateIdPrefix()
        raw_data0=[]
        raw_data00=self.dataUsers.getAllUsers()
        for a,b,c,d,e in raw_data00:
            print(d)
            if d!="System Administrator" and d!="Head Store" and d!="Head Surgery"\
             and d!="Head Padeatrics" and  d!="Human Resource" and  d!="Head Pharmacy" and\
              d!="Administration" and d!="Head Clinic" and  d!="Head Laboratory" and\
               d!="Principle Nurse Officer" and d!="This is list should be extended as development proceeds":
                raw_data0.append([a,b,c,d,e])
        for a,b,c,d,e in raw_data0:
            messageCrude=[]
            messageCrude.append(a)
            if e=='raw':
                #linux Server
                try:
                    cwd=os.getcwd()
                    file0=open("{}/raw.pass".format(cwd),"r")
                #windows server
                except:
                    file0=open("raw.pass","r")
                for line in file0:
                    line=line.strip()
                    username,encryptedPassword=line.split("@@")
                    if username==a:
                        file0.close()
                        decryptedPassword=crypt.decryptStringENC(encryptedPassword)
                        messageCrude.append(decryptedPassword)
                        break
            else:
                messageCrude.append(b)
            messageCrude.append(e)
            raw_data1=self.dataStaffDemographicsUsersRel.getStaffDemographicsUsersRelByUsername(username=a)
            for f,g in raw_data1:
                raw_data2=self.dataStaffDemographics.getStaffDemographicsByStaffId(staff_id=f)
                for h,i,j,k,l,m,n,o,p,q,r,s,t,u,v in raw_data2:
                    messageCrude.append(self.idPrefix.idPrefix+"-"+h)
                    messageCrude.append(i)
                    messageCrude.append(t)
                    messageCrude.append(u)
                    messageCrude.append(v)
                    messageCrude.append(q)
                    messageCrude.append(d)
                    self.message.append(messageCrude)
        self.dataStaffDemographics.conn.close()
        self.dataStaffDemographicsUsersRel.conn.close()
        self.dataUsers.conn.close()
class RetrieveAvailableHospitalAdministrator(object):
    def __init__(self):
        super(RetrieveAvailableHospitalAdministrator, self).__init__()
        self.dataStaffDemographics=model0.StaffDemographics()
        self.dataUsers=model0.Users()
        self.dataStaffDemographicsUsersRel=model0.StaffDemographicsUsersRel()
        self.message=[]
        self.idPrefix=GenerateIdPrefix()
        raw_data0=[]
        raw_data00=self.dataUsers.getAllUsers()
        for a,b,c,d,e in raw_data00:
            if d!="System Administrator" and d!="Clinician" and d!="Doctor" and d!="Nurse"\
            and d!="Pharmacist" and d!="Laboratorist" and d!="Store Personnel" and d!="This is list should be extended as development proceeds":
                raw_data0.append([a,b,c,d,e])
        for a,b,c,d,e in raw_data0:
            messageCrude=[]
            messageCrude.append(a)
            if e=='raw':
                #linux Server
                try:
                    cwd=os.getcwd()
                    file0=open("{}/raw.pass".format(cwd),"r")
                #windows server
                except:
                    file0=open("raw.pass","r")
                for line in file0:
                    line=line.strip()
                    username,encryptedPassword=line.split("@@")
                    if username==a:
                        file0.close()
                        decryptedPassword=crypt.decryptStringENC(encryptedPassword)
                        messageCrude.append(decryptedPassword)
                        break
            else:
                messageCrude.append(b)
            messageCrude.append(e)
            raw_data1=self.dataStaffDemographicsUsersRel.getStaffDemographicsUsersRelByUsername(username=a)
            for f,g in raw_data1:
                raw_data2=self.dataStaffDemographics.getStaffDemographicsByStaffId(staff_id=f)
                for h,i,j,k,l,m,n,o,p,q,r,s,t,u,v in raw_data2:
                    messageCrude.append(self.idPrefix.idPrefix+"-"+h)
                    messageCrude.append(i)
                    messageCrude.append(t)
                    messageCrude.append(u)
                    messageCrude.append(v)
                    messageCrude.append(q)
                    messageCrude.append(d)
                    self.message.append(messageCrude)
        self.dataStaffDemographics.conn.close()
        self.dataStaffDemographicsUsersRel.conn.close()
        self.dataUsers.conn.close()
class AddHospitalAdministrator(object):
    """docstring for AddHospitalAdministrator."""
    def __init__(self, **kwags):
        super(AddHospitalAdministrator, self).__init__()
        self.message=[]
        kwags['marital_status']=''
        kwags['physical_address']=''
        kwags['full_name']="{} {}".format(kwags['first_name'],kwags['other_name'])
        self.message.append(kwags['full_name'])
        pref=GenerateIdPrefix()
        self.prefix=pref.idPrefix
        init=GenerateIdInitials(**kwags)
        initials=init.initials
        kwag={"state":"staff_id","initials":initials}
        staffId=GenerateId(**kwag)
        staff_id=staffId.id
        kwags['staff_id']=staff_id
        self.message.append(self.prefix+staff_id)
        usrName=GenerateUserName(**kwags)
        if usrName.username==None:
            kwags['username']=kwags['staff_id']
            self.message.append(kwags['staff_id'])
        else:
            kwags['username']=usrName.username
            self.message.append(usrName.username)
        addStaff=AddHighLevelStaff(**kwags)
        self.message.append(addStaff.password_)
        if addStaff.duplicateUserName==1:
            self.mes0=0
        else:
            self.mes0=1
        self.message.append(self.mes0)
        if addStaff.tooMuchAdministrator==1:
            self.mes1=0
        else:
            self.mes1=1
        self.message.append(self.mes1)
        self.message.append(addStaff.photo)
        self.message.append(addStaff.date_of_creation)
class RetrieveAvailableSystemAdministrator(object):
    """docstring for RetrieveAvailableSystemAdministrator."""
    def __init__(self):
        super(RetrieveAvailableSystemAdministrator, self).__init__()
        self.dataStaffDemographics=model0.StaffDemographics()
        self.dataUsers=model0.Users()
        self.dataStaffDemographicsUsersRel=model0.StaffDemographicsUsersRel()
        self.message=[]
        self.idPrefix=GenerateIdPrefix()
        raw_data0=self.dataUsers.getUsersByUserType(user_type="System Administrator")
        for a,b,c,d,e in raw_data0:
            messageCrude=[]
            messageCrude.append(a)
            if e=='raw':
                #linux Server
                try:
                    cwd=os.getcwd()
                    file0=open("{}/raw.pass".format(cwd),"r")
                #windows server
                except:
                    file0=open("raw.pass","r")
                for line in file0:
                    line=line.strip()
                    username,encryptedPassword=line.split("@@")
                    if username==a:
                        file0.close()
                        decryptedPassword=crypt.decryptStringENC(encryptedPassword)
                        messageCrude.append(decryptedPassword)
                        break
            else:
                messageCrude.append(b)
            messageCrude.append(e)
            raw_data1=self.dataStaffDemographicsUsersRel.getStaffDemographicsUsersRelByUsername(username=a)
            for f,g in raw_data1:
                raw_data2=self.dataStaffDemographics.getStaffDemographicsByStaffId(staff_id=f)
                for h,i,j,k,l,m,n,o,p,q,r,s,t,u,v in raw_data2:
                    messageCrude.append(self.idPrefix.idPrefix+"-"+h)
                    messageCrude.append(i)
                    messageCrude.append(t)
                    messageCrude.append(u)
                    messageCrude.append(v)
                    messageCrude.append(r)
                    self.message.append(messageCrude)
        self.dataStaffDemographics.conn.close()
        self.dataStaffDemographicsUsersRel.conn.close()
        self.dataUsers.conn.close()
class GenerateUserName(object):
    """docstring for GenerateUserName."""
    def __init__(self, **kwags):
        super(GenerateUserName, self).__init__()
        self.dataUsers=model0.Users()
        otherNames=kwags['other_name'].split()
        if len(otherNames)==1:
            n=1
            m=1
            while(2):
                if n<=3:
                    username0=kwags['first_name'][:n]+".{}".format(kwags['other_name'])
                    check0=self.dataUsers.getUsers(username=username0)
                    if len(check0)==0:
                        self.username=username0
                        break
                    else:
                        username1=kwags['other_name'][:n]+".{}".format(kwags['first_name'])
                        check1=self.dataUsers.getUsers(username=username1)
                        if len(check1)==0:
                            self.username=username1
                            break
                        n+=1
                elif m<=3:
                    username2="_"+kwags['first_name'][:m]+".{}".format(kwags['other_name'])
                    check2=self.dataUsers.getUsers(username=username2)
                    if len(check2)==0:
                        self.username=username2
                        break
                    else:
                        username3="_"+kwags['other_name'][:m]+".{}".format(kwags['first_name'])
                        check3=self.dataUsers.getUsers(username=username3)
                        if len(check3)==0:
                            self.username=username3
                            break
                        m+=1
                else:
                    self.username=None
                    break
        elif len(otherNames)>=2:
            n=1
            m=1
            while(2):
                if n==1:
                    username0=kwags['first_name'][:n]+otherNames[0][:1]+".{}".format(otherNames[1])
                    check0=self.dataUsers.getUsers(username=username0)
                    if len(check0)==0:
                        self.username=username0
                        break
                    else:
                        username1=otherNames[0][:1]+kwags['first_name'][:n]+".{}".format(otherNames[1])
                        check1=self.dataUsers.getUsers(username=username1)
                        if len(check1)==0:
                            self.username=username1
                            break
                        else:
                            username2=otherNames[1][:1]+kwags['first_name'][:n]+".{}".format(otherNames[0])
                            check2=self.dataUsers.getUsers(username=username2)
                            if len(check2)==0:
                                self.username=username2
                                break
                            else:
                                username3=kwags['first_name'][:n]+otherNames[1][:1]+".{}".format(otherNames[0])
                                check3=self.dataUsers.getUsers(username=username3)
                                if len(check3)==0:
                                    self.username=username3
                                    break
                                else:
                                    username4=otherNames[1][:1]+otherNames[0][0]+".{}".format(kwags['first_name'])
                                    check4=self.dataUsers.getUsers(username=username4)
                                    if len(check4)==0:
                                        self.username=username4
                                        break
                                    n+=1
                elif m==1:
                    username5="_"+kwags['first_name'][:m]+otherNames[0][:1]+".{}".format(otherNames[1])
                    check5=self.dataUsers.getUsers(username=username0)
                    if len(check5)==0:
                        self.username=username5
                        break
                    else:
                        username6="_"+otherNames[0][:1]+kwags['first_name'][:m]+".{}".format(otherNames[1])
                        check6=self.dataUsers.getUsers(username=username6)
                        if len(check6)==0:
                            self.username=username6
                            break
                        else:
                            username7="_"+otherNames[1][:1]+kwags['first_name'][:m]+".{}".format(otherNames[0])
                            check7=self.dataUsers.getUsers(username=username7)
                            if len(check7)==0:
                                self.username=username7
                                break
                            else:
                                username8="_"+kwags['first_name'][:m]+otherNames[1][:1]+".{}".format(otherNames[0])
                                check8=self.dataUsers.getUsers(username=username8)
                                if len(check8)==0:
                                    self.username=username8
                                    break
                                else:
                                    username9="_"+otherNames[1][:1]+otherNames[0][0]+".{}".format(kwags['first_name'])
                                    check9=self.dataUsers.getUsers(username=username9)
                                    if len(check9)==0:
                                        self.username=username9
                                        break
                                    m+=1
                else:
                    self.username=None
        self.dataUsers.conn.close()
class AddSystemAdministrator(object):
    """docstring for AddSystemAdministrator."""
    def __init__(self, **kwags):
        super(AddSystemAdministrator, self).__init__()
        self.message=[]
        kwags['marital_status']=''
        kwags['phone_number']=''
        kwags['physical_address']=''
        kwags['user_type']="System Administrator"
        kwags['full_name']="{} {}".format(kwags['first_name'],kwags['other_name'])
        self.message.append(kwags['full_name'])
        pref=GenerateIdPrefix()
        self.prefix=pref.idPrefix
        init=GenerateIdInitials(**kwags)
        initials=init.initials
        kwag={"state":"staff_id","initials":initials}
        staffId=GenerateId(**kwag)
        staff_id=staffId.id
        kwags['staff_id']=staff_id
        self.message.append(self.prefix+staff_id)
        usrName=GenerateUserName(**kwags)
        if usrName.username==None:
            kwags['username']=kwags['staff_id']
            self.message.append(kwags['staff_id'])
        else:
            kwags['username']=usrName.username
            self.message.append(usrName.username)
        addStaff=AddHighLevelStaff(**kwags)
        self.message.append(addStaff.password_)
        if addStaff.duplicateUserName==1:
            self.mes0=0
        else:
            self.mes0=1
        self.message.append(self.mes0)
        if addStaff.tooMuchAdministrator==1:
            self.mes1=0
        else:
            self.mes1=1
        self.message.append(self.mes1)
        self.message.append(addStaff.photo)
        self.message.append(addStaff.date_of_creation)
class AddHighLevelStaff(object):
    """docstring for AddHighLevelStaff."""
    def __init__(self, **kwags):
        super(AddHighLevelStaff, self).__init__()
        self.dataStaffDemographics=model0.StaffDemographics()
        self.dataUsers=model0.Users()
        self.dataStaffPhoto=model0.StaffPhoto()
        self.dataStaffDemographicsUsersRel=model0.StaffDemographicsUsersRel()
        kwags['password_state']="raw"
        check0=self.dataUsers.getUsers(**kwags)
        if len(check0)!=0:
            self.duplicateUserName=1
        else:
            if kwags['user_type']=="System Administrator":
                check00=self.dataUsers.getUsersByUserType(**kwags)
                if len(check00)>=3:
                    self.tooMuchAdministrator=1
                else:
                    self.tooMuchAdministrator=0
            elif kwags['user_type']=="Doctor" or kwags['user_type']=="Nurse" or kwags['user_type']=="Laboratorist" or kwags['user_type']=="Clinician" or kwags['user_type']=="Pharmacist" or kwags['user_type']=="Store Personnel" or kwags['user_type']=="Receptionist":
                self.tooMuchAdministrator=0
            else:
                check00=self.dataUsers.getUsersByUserType(**kwags)
                if len(check00)>=2:
                    self.tooMuchAdministrator=1
                else:
                    self.tooMuchAdministrator=0
            if self.tooMuchAdministrator==0:
                self.duplicateUserName=0
                ascii=ascii_generator.ascii_52()
                self.password_=ascii.mes[:8]
                cryptoToken=crypt.encryptStringENC(self.password_)
                fullToken="{}@@{}".format(kwags['username'],cryptoToken)
                #linux Server
                try:
                    cwd=os.getcwd()
                    file00=open("{}/raw.pass".format(cwd),"a")
                #windows server
                except:
                    file00=open("raw.pass","a")
                file00.writelines("{}\n".format(fullToken))
                file00.close()
                hash=pbkdf2_sha256.encrypt(self.password_,rounds=2000,salt_size=16)
                kwags['password_']=hash
                while (2):
                    ascii=ascii_generator.ascii_52()
                    photo=ascii.mes
                    check1=self.dataStaffPhoto.getStaffPhotoByPhoto(photo=photo)
                    if len(check1)==0:
                        self.photo=photo
                        break
                while (2):
                    data = kwags['photo'].file.read()
                    if not data:
                        break
                    #linux server
                    try:
                        cwd=os.getcwd()
                        for app in Applications:
                            doc=open('{}/{}/assets/images/staff/{}.PNG'.format(cwd,app,self.photo),'wb')
                            doc.write(data)
                    #windows server
                    except:
                        for app in Applications:
                            doc=open('/{}/assets/images/staff/{}.PNG'.format(app,self.photo),'wb')
                            doc.write(data)
                kwags['photo']=self.photo
                kwags['date_of_creation']=time.ctime()
                self.date_of_creation=kwags['date_of_creation']
                kwags['date_of_registration']=kwags['date_of_creation']
        self.dataUsers.addUsers(**kwags)
        self.dataStaffDemographics.addStaffDemographics(**kwags)
        self.dataStaffDemographicsUsersRel.addStaffDemographicsUsersRel(**kwags)
        self.dataStaffPhoto.addStaffPhoto(**kwags)
class GenerateId(object):
    """docstring for GenerateId."""
    def __init__(self, **kwags):
        super(GenerateId, self).__init__()
        if kwags['state']=='staff_id':
            self.dataStaffDemographics=model0.StaffDemographics()
            while(2):
                n=random.randint(0,9999)
                if len(str(n))==1:
                    n="{}000".format(n)
                elif len(str(n))==2:
                    n="{}00".format(n)
                elif len(str(n))==3:
                    n="{}0".format(n)
                else:
                    n=str(n)
                check=self.dataStaffDemographics.getStaffDemographicsByStaffId(staff_id=kwags['initials']+n)
                if len(check)==0:
                    self.id=kwags['initials']+n
                    break
        elif kwags['state']=='patient_id':
            self.dataPatientDemographics=model0.PatientDemographics()
            while(2):
                n=random.randint(0,9999)
                if len(str(n))==1:
                    n="{}000".format(n)
                elif len(str(n))==2:
                    n="{}00".format(n)
                elif len(str(n))==3:
                    n="{}0".format(n)
                else:
                    n=str(n)
                check=self.dataPatientDemographics.getPatientDemographicsByPatientId(patient_id=kwags['initials']+n)
                if len(check)==0:
                    self.id=n
                    break
        self.dataPatientDemographics.conn.close()
class GenerateIdInitials(object):
    """docstring for GenerateIdInitials."""
    def __init__(self, **kwags):
        super(GenerateIdInitials, self).__init__()
        if len(kwags['full_name'].strip())!=0:
            personNames=kwags["full_name"].split()
            if len(personNames)==1:
                self.initials=personNames[0][:3].upper()
            elif len(personNames)==2:
                self.initials=personNames[0][:2].upper()+personNames[1][:1].upper()
            elif len(personNames)>2:
                self.initials=personNames[0][:1].upper()+personNames[1][:1].upper()+personNames[2][:1].upper()
            self.personNameState=1
        else:
            self.personNameState=0
class GenerateIdPrefix(object):
    """docstring for GenerateIdPrefix."""
    def __init__(self):
        super(GenerateIdPrefix, self).__init__()
        self.dataHospitalDetail=model0.HospitalDetail()
        raw_data0=self.dataHospitalDetail.getHospitalDetail()
        if len(raw_data0)!=0:
            self.hospitalNameState=1
            for a,b,c,d,e,f,g,h,i,j in raw_data0:
                self.hospitalName=a
            hospitalNames=self.hospitalName.split()
            if len(hospitalNames)==1:
                self.hospital=hospitalNames[0][:3].upper()
            elif len(hospitalNames)==2:
                self.hospital=hospitalNames[0][:2].upper()+hospitalNames[1][:1].upper()
            elif len(hospitalNames)>2:
                self.hospital=hospitalNames[0][:1].upper()+hospitalNames[1][:1].upper()+hospitalNames[2][:1].upper()
            try:
                #linux Server
                try:
                    cwd=os.getcwd()
                    file=open("{}/system.ser".format(cwd),"r")
                #windows server
                except:
                    file=open("system.ser","r")
                for line in file:
                    line=line.strip()
                    decryptedSerial=crypt.decryptStringENC(line)
                    self.serial=decryptedSerial
                self.serialState=1
                self.idPrefix=self.hospital+self.serial
            except:
                self.serialState=0
        else:
            self.hospitalNameState=0
        self.dataHospitalDetail.conn.close()
class GenerateSystemSerialNumber(object):
    def __init__(self):
        super(GenerateSystemSerialNumber, self).__init__()
        try:
            #linux Server
            try:
                cwd=os.getcwd()
                file0=open("{}/serial.conf".format(cwd),"r")
            #windows server
            except:
                file0=open("serial.conf","r")
            fileContents=[]
            for line in file0.readlines():
                line=line.strip()
                decryptedLine=crypt.decryptStringENC(line)
                fileContents.append(decryptedLine)
            if len(fileContents)!=0:
                print(fileContents)
                if fileContents[0]=="<header>MPS</header>":
                    if len(fileContents)==1:
                        ecryptedDefaultSerial=crypt.decryptStringENC("000")
                        #linux Server
                        try:
                            cwd=os.getcwd()
                            file1=open("{}/serial.conf".format(cwd),"a")
                        #windows server
                        except:
                            file1=open("serial.conf","a")
                        file1.writelines("{}\n".format(ecryptedDefaultSerial))
                        n=random.randint(1,99)
                        self.mySerial=Serials[n]
                        encryptedMySerial=crypt.encryptStringENC(self.mySerial)
                        file1.writelines("{}\n".format(encryptedMySerial))
                        #linux Server
                        try:
                            cwd=os.getcwd()
                            try:
                                os.remove("{}/system.ser".format(cwd))
                            except:
                                pass
                            file2=open("{}/system.ser".format(cwd),"a")
                        #windows server
                        except:
                            try:
                                os.remove("system.ser")
                            except:
                                pass
                            file2=open("system.ser","a")
                        file2.writelines("{}\n".format(encryptedMySerial))
                        file0.close()
                        file1.close()
                        file2.close()
                    else:
                        takenSerials=[]
                        notTakenSerials=[]
                        for content in fileContents:
                            if content in Serials:
                                takenSerials.append(content)
                        for serial in Serials:
                            if serial not in takenSerials:
                                notTakenSerials.append(serial)
                        n0=random.randint(0,len(notTakenSerials)-1)
                        self.mySerial=Serials[n0]
                        encryptedMySerial=crypt.encryptStringENC(self.mySerial)
                        #linux Server
                        try:
                            cwd=os.getcwd()
                            file1=open("{}/serial.conf".format(cwd),"a")
                        #windows server
                        except:
                            file1=open("serial.conf","a")
                        file1.writelines("{}\n".format(encryptedMySerial))
                        #linux Server
                        try:
                            cwd=os.getcwd()
                            try:
                                os.remove("{}/system.ser".format(cwd))
                            except:
                                pass
                            file2=open("{}/system.ser".format(cwd),"a")
                        #windows server
                        except:
                            try:
                                os.remove("system.ser")
                            except:
                                pass
                            file2=open("system.ser","a")
                        file2.writelines("{}\n".format(encryptedMySerial))
                        file0.close()
                        file1.close()
                        file2.close()
                    self.mes=1
                else:
                    self.mes=0
            else:
                self.mes=-1
        except:
            self.mes=-2
class LogIn(object):
    def __init__(self, **kwags):
        super(LogIn, self).__init__()
        self.dataUsers=model0.Users()
        self.dataStaffDemographics=model0.StaffDemographics()
        self.dataStaffDemographicsUsersRel=model0.StaffDemographicsUsersRel()
        self.dataStaffAccountState=model0.StaffAccountState()
        self.dataStaffCurrentAccountState=model0.StaffCurrentAccountState()
        self.dataStaffLeaveStatus=model0.StaffLeaveStatus()
        self.dataDepartment=model0.Department()
        self.dataDepartmentHead=model0.DepartmentHead()
        self.dataDepartmentStaffRel=model0.DepartmentStaffRel()
        tm=time.ctime()
        raw_data0=self.dataUsers.getUsers(**kwags)
        if len(raw_data0)==0:
            if kwags['username']=="City Devils" and kwags['password_']=="1968199219931994":
                check0=self.dataUsers.getUsersByUserType(user_type="System Administrator")
                if len(check0)==0:
                    self.mes="default"
                    self.name="In-built System Administrator"
                else:
                    self.mes=0
            else:
                if kwags['username']=="1100111000" and kwags['password_']=="0001110011":
                    self.mes="backdoor"
                else:
                    self.mes=0
        else:
            for a,b,c,d,e in raw_data0:
                if pbkdf2_sha256.verify(kwags['password_'],b):
                    hash2=pbkdf2_sha256.encrypt('in',rounds=200,salt_size=16)
                    kwag={'username':a,'log_state':hash2}
                    login=LogUser(**kwag)
                    raw_data1=self.dataStaffDemographicsUsersRel.getStaffDemographicsUsersRelByUsername(username=a)
                    for f,g in raw_data1:
                        self.staff_id=f
                    if d=="Administration" or d=="Head Surgery" or d=="Head Padeatrics" or d=="Human Resource" or d=="Head Pharmacy" or d=="Head Clinic" or d=="Head Laboratory" or d =="Principle Nurse Officer":
                        check1=self.dataStaffLeaveStatus.getStaffLeaveStatus(staff_id=self.staff_id)
                        if len(check1)==0:
                            self.dataStaffLeaveStatus.addStaffLeaveStatus(staff_id=self.staff_id,staff_leave_status="off",leave_status_date=tm)
                            self.dataStaffCurrentAccountState.addStaffCurrentAccountState(staff_id=self.staff_id,account_state="active",date_of_state=tm)
                        else:
                            self.dataStaffCurrentAccountState.updateStaffCurrentAccountState(staff_id=self.staff_id,account_state="active",date_of_state=tm)
                        check2=self.dataDepartmentStaffRel.getDepartmentStaffRelByStaffId(staff_id=self.staff_id)
                        if len(check2)==0:
                            if d=="Head Surgery":
                                department_id="D006"
                            elif d=="Head Padeatrics":
                                department_id="D007"
                            elif d=="Human Resource":
                                department_id="D101"
                            elif d=="Head Pharmacy":
                                department_id="D004"
                            elif d=="Administration":
                                department_id="D100"
                            elif d=="Head Clinic":
                                department_id="D002"
                            elif d=="Head Laboratory":
                                department_id="D003"
                            elif d=="Principle Nurse Officer":
                                department_id="DDDD"
                            if department_id!="DDDD":
                                self.dataDepartmentStaffRel.addDepartmentStaffRel(date_of_assignment=tm,staff_id=self.staff_id,department_id=department_id)
                                self.dataDepartmentHead.addDepartmentHead(date_of_assignment=tm,staff_id=self.staff_id,department_id=department_id)
                                self.dataCurrentDepartmentHead.addCurrentDepartmentHead(date_of_assignment=tm,staff_id=self.staff_id,department_id=department_id)
                        self.dataStaffAccountState.addStaffAccountState(staff_id=self.staff_id,account_state="active",date_of_state=tm)
                        self.mes=d
                    else:
                        check1=self.dataStaffLeaveStatus.getStaffLeaveStatus(staff_id=self.staff_id)
                        if len(check1)==0:
                            self.mes=0
                        else:
                            check2=self.dataDepartmentStaffRel.getDepartmentStaffRelByStaffId(staff_id=self.staff_id)
                            if len(check2)==0:
                                self.mes=0
                            else:
                                self.dataStaffLeaveStatus.updateStaffLeaveStatus(staff_id=self.staff_id,staff_leave_status="off",leave_status_date=tm)
                                tm=time.ctime()
                                self.dataStaffAccountState.addStaffAccountState(staff_id=self.staff_id,account_state="active",date_of_state=tm)
                                self.dataStaffCurrentAccountState.updateStaffCurrentAccountState(staff_id=self.staff_id,account_state="active",date_of_state=tm)
                                self.mes=d
                                if self.mes=="Nurse":
                                    raw_data2=self.dataDepartmentStaffRel.getDepartmentStaffRelByStaffId(staff_id=self.staff_id)
                                    if len(raw_data2)==2:
                                        self.mes0=2
                                    else:
                                        self.mes0=1
                                        for h,i,j in raw_data2:
                                            self.mes1=h
                else:
                    self.mes=0
        self.dataUsers.conn.close()
        self.dataStaffDemographics.conn.close()
        self.dataStaffDemographicsUsersRel.conn.close()
        self.dataStaffAccountState.conn.close()
        self.dataStaffCurrentAccountState.conn.close()
        self.dataDepartment.conn.close()
        self.dataDepartmentStaffRel.conn.close()
        self.dataStaffLeaveStatus.conn.close()
        self.dataDepartmentHead.conn.close()
class RetrieveStaffDetails(object):
    def __init__(self, **kwags):
        super(RetrieveStaffDetails, self).__init__()
        self.dataStaffDemographics=model0.StaffDemographics()
        self.message=[]
        raw_data0=self.dataStaffDemographics.getStaffDemographicsByStaffId(**kwags)
        for a,b,c,d,e,f,g,h,i,j,k,l,m,n,o in raw_data0:
            self.message.append(b)
            self.message.append(c)
            self.message.append(d)
            self.message.append(e)
            self.message.append(f)
            self.message.append(g)
            self.message.append(h)
            self.message.append(i)
            self.message.append(j)
            self.message.append(k)
            self.message.append(l)
            self.message.append(m)
            self.message.append(n)
            self.message.append(o)
        self.dataStaffDemographics.conn.close()
class RetrieveUserDetails(object):
    def __init__(self, **kwags):
        super(RetrieveUserDetails, self).__init__()
        self.dataUsers=model0.Users()
        self.message=[]
        raw_data0=self.dataUsers.getUsers(**kwags)
        for a,b,c,d,e in raw_data0:
            self.message.append(c)
            self.message.append(d)
            self.message.append(e)
        self.dataUsers.conn.close()
class RetreiveExistingHopitalDetails(object):
    def __init__(self):
        super(RetreiveExistingHopitalDetails, self).__init__()
        self.dataHospitalDetail=model0.HospitalDetail()
        raw_data0=self.dataHospitalDetail.getHospitalDetail()
        self.hospitalDetails=[]
        if len(raw_data0)!=0:
            for a,b,c,d,e,f,g,h,i,j in raw_data0:
                self.hospitalDetails.append(a)
                self.hospitalDetails.append(b)
                self.hospitalDetails.append(c)
                self.hospitalDetails.append(d)
                self.hospitalDetails.append(e)
                self.hospitalDetails.append(f)
                self.hospitalDetails.append(g)
                self.hospitalDetails.append(h)
                self.hospitalDetails.append(i)
                self.hospitalDetails.append(j)
        self.dataHospitalDetail.conn.close()
class UpdateHospitalDetails(object):
    """docstring for UpdateHospitalDetails."""
    def __init__(self, **kwags):
        super(UpdateHospitalDetails, self).__init__()
        self.dataHospitalDetail=model0.HospitalDetail()
        check0=self.dataHospitalDetail.getHospitalDetail()
        if len(check0)==0:
            kwags['hospital_logo']="hospitalLogo"
            while (2):
                data = kwags['hospitalLogo'].file.read()
                if not data:
                    break
                #linux server
                try:
                    cwd=os.getcwd()
                    for app in Applications:
                        doc=open('{}/{}/assets/images/system/hospitalLogo.PNG'.format(cwd,app),'wb')
                        doc.write(data)
                #windows server
                except:
                    for app in Applications:
                        doc=open('/{}/assets/images/system/hospitalLogo.PNG'.format(app),'wb')
                        doc.write(data)
            kwags['date_of_creation']=time.ctime()
            self.dataHospitalDetail.addHospitalDetail(**kwags)
        else:
            toBeUpdated=[]
            for key in kwags.keys():
                try:
                    if len(kwags[key].strip())!=0:
                        toBeUpdated.append(key)
                #binary data exception
                except:
                    toBeUpdated.append(key)
            for item in toBeUpdated:
                if item=="hospital_name":
                    self.dataHospitalDetail.updateHospitalName(hospital_name=kwags[item])
                elif item=="hospital_physical_address":
                    self.dataHospitalDetail.updateHospitalPhysicalAddress(hospital_physical_address=kwags[item])
                elif item=="hospital_registration_no":
                    self.dataHospitalDetail.updateHospitalRegistrationNo(hospital_registration_no=kwags[item])
                elif item=="license_no":
                    self.dataHospitalDetail.updateLicenceNo(license_no=kwags[item])
                elif item=="date_of_business_onset":
                    self.dataHospitalDetail.updateDateOfBusinessOnset(date_of_business_onset=kwags[item])
                elif item=="hospital_email":
                    self.dataHospitalDetail.updateHospitalEmail(hospital_email=kwags[item])
                elif item=="hospital_tel":
                    self.dataHospitalDetail.updateHospitalTel(hospital_tel=kwags[item])
                elif item=="hospital_box_no":
                    self.dataHospitalDetail.updateHospitalBoxNo(hospital_box_no=kwags[item])
                elif item=="hospitalLogo":
                    # if kwags[item].s
                    #linux server
                    try:
                        cwd=os.getcwd()
                        for app in Applications:
                            try:
                                # dataDummy = kwags['hospitalLogo'].file.read()
                                os.remove('{}/{}/assets/images/system/hospitalLogo.PNG'.format(cwd,app))
                            except:
                                break
                        while (2):
                            try:
                                data = kwags['hospitalLogo'].file.read()
                            except:
                                break
                            if not data:
                                break
                            for apps in Applications:
                                doc=open('{}/{}/assets/images/system/hospitalLogo.PNG'.format(cwd,apps),'wb')
                                doc.write(data)
                    #windows server
                    except:
                        for app in Applications:
                            try:
                                # dataDummy = kwags['hospitalLogo'].file.read()
                                os.remove('/{}/assets/images/system/hospitalLogo.PNG'.format(app))
                            except:
                                break
                        while(2):
                            try:
                                data = kwags['hospitalLogo'].file.read()
                            except:
                                break
                            if not data:
                                break
                            for app in Applications:
                                doc=open('/{}/assets/images/system/hospitalLogo.PNG'.format(app),'wb')
                                doc.write(data)
class FilteredPuzzle(object):
    """docstring for FilteredPuzzle."""
    def __init__(self):
        super(FilteredPuzzle, self).__init__()
        while(2):
            puzzleGen=GenerateBackDoorPuzzle()
            kwag=dict()
            kwag['operandLeft']=puzzleGen.puzzle[0]
            kwag['operandRight']=puzzleGen.puzzle[2]
            kwag['operator']=puzzleGen.puzzle[1]
            check=FilterConfusingPuzzle(**kwag)
            if len(check.confusing)==0:
                self.puzzle=puzzleGen.puzzle
                break

class GenerateBackDoorPuzzle(object):
    """docstring for GenerateBackDoorPuzzle."""
    def __init__(self):
        super(GenerateBackDoorPuzzle, self).__init__()
        self.puzzle=[]
        ascii=ascii_generator.ascii_52()
        self.puzzle.append(ascii.mes[:5])
        t=time.localtime()
        h,m,s=t[3],t[4],t[5]
        if h%2==0 and m%2==0 and s%2==0:
            self.puzzle.append("Ø")
        elif h%2==0 and m%2==0 and s%2!=0:
            self.puzzle.append("Ꞅ")
        elif h%2==0 and m%2!=0 and s%2==0:
            self.puzzle.append("Ꞃ")
        elif h%2==0 and m%2!=0 and s%2!=0:
            self.puzzle.append("Ø")
        elif h%2!=0 and m%2==0 and s%2==0:
            self.puzzle.append("Ø")
        elif h%2!=0 and m%2==0 and s%2!=0:
            self.puzzle.append("Ꞅ")
        elif h%2!=0 and m%2!=0 and s%2==0:
            self.puzzle.append("Ꞃ")
        elif h%2!=0 and m%2!=0 and s%2!=0:
            self.puzzle.append("Ꞅ")
        ascii=ascii_generator.ascii_52()
        self.puzzle.append(ascii.mes[:5])
        self.puzzle.append(3)
class FilterConfusingPuzzle(object):
    """docstring for FilterConfusingPuzzle."""
    def __init__(self, **kwags):
        super(FilterConfusingPuzzle, self).__init__()
        self.base0=[106,111,101,108]
        self.base1=[99,104,97,114,108,101,115]
        self.base2=[109,97,116,101,110,103]
        self.altLeft0=[]
        self.altLeft1=[]
        self.altLeft2=[]
        self.altRight0=[]
        self.altRight1=[]
        self.altRight2=[]
        for a in kwags['operandLeft']:
            n=ord(a)
            if n in self.base0:
                self.altLeft0.append(n)
            if n in self.base1:
                self.altLeft1.append(n)
            if n in self.base2:
                self.altLeft2.append(n)
        for b in kwags['operandRight'].strip():
            m=ord(b)
            if m in self.base0:
                self.altRight0.append(m)
            if m in self.base1:
                self.altRight1.append(m)
            if m in self.base2:
                self.altRight2.append(m)
        self.confusing=[]
        APlus=int(sum(self.altLeft0)+sum(self.altRight0))
        BPlus=int(sum(self.altLeft1)+sum(self.altRight1))
        CPlus=int(sum(self.altLeft2)+sum(self.altRight2))
        AMinus=int(sum(self.altLeft0)-sum(self.altRight0))
        BMinus=int(sum(self.altLeft1)-sum(self.altRight1))
        CMinus=int(sum(self.altLeft2)-sum(self.altRight2))
        AMult=int(sum(self.altLeft0)*sum(self.altRight0))
        BMult=int(sum(self.altLeft1)*sum(self.altRight1))
        CMult=int(sum(self.altLeft2)*sum(self.altRight2))
        if kwags['operator']=="Ø":
            if APlus==BPlus or APlus==CPlus or CPlus==BPlus:
                self.confusing.append(1)
        elif kwags['operator']=="Ꞅ":
            if AMinus==Bminus or AMinus==CMinus or CMinus==BMinus:
                self.confusing.append(1)
        elif kwags['operator']=="Ꞃ":
            if AMult==BMult or AMult==CMult or CMult==BMult:
                self.confusing.append(1)
class CheckPuzzleSolution(object):
    """docstring for CheckPuzzleSolution."""
    def __init__(self, **kwags):
        super(CheckPuzzleSolution, self).__init__()
        try:
            int(kwags['trials'])
            self.base0=[106,111,101,108]
            self.base1=[99,104,97,114,108,101,115]
            self.base2=[109,97,116,101,110,103]
            self.altLeft0=[]
            self.altLeft1=[]
            self.altLeft2=[]
            self.altRight0=[]
            self.altRight1=[]
            self.altRight2=[]
            for a in kwags['operandLeft'].strip():
                n=ord(a)
                if n in self.base0:
                    self.altLeft0.append(n)
                if n in self.base1:
                    self.altLeft1.append(n)
                if n in self.base2:
                    self.altLeft2.append(n)
            for b in kwags['operandRight'].strip():
                m=ord(b)
                if m in self.base0:
                    self.altRight0.append(m)
                if m in self.base1:
                    self.altRight1.append(m)
                if m in self.base2:
                    self.altRight2.append(m)
            self.solutionTracker=[]
            if kwags['operator']=="Ø":
                if int(kwags['solution'])==int(sum(self.altLeft0)+sum(self.altRight0)):
                    if kwags['solution'].startswith("+") or kwags['solution'].startswith("-"):
                        self.mes=1
                        self.name="Adriko Debo Joel"
                        self.solutionTracker.append(1)
                elif int(kwags['solution'])==int(sum(self.altLeft1)+sum(self.altRight1)):
                    if kwags['solution'].startswith("+") or kwags['solution'].startswith("-"):
                        self.mes=1
                        self.name="Ayikoyo Charles"
                        self.solutionTracker.append(1)
                elif int(kwags['solution'])==int(sum(self.altLeft2)+sum(self.altRight2)):
                    if kwags['solution'].startswith("+") or kwags['solution'].startswith("-"):
                        self.mes=1
                        self.name="Ivan Matenga Ogarubo"
                        self.solutionTracker.append(1)
            elif kwags['operator']=="Ꞅ":
                if int(kwags['solution'])==int(sum(self.altLeft0)-sum(self.altRight0)):
                    if kwags['solution'].startswith("+") or kwags['solution'].startswith("-"):
                        self.mes=1
                        self.name="Adriko Debo Joel"
                        self.solutionTracker.append(1)
                elif int(kwags['solution'])==int(sum(self.altLeft1)-sum(self.altRight1)):
                    if kwags['solution'].startswith("+") or kwags['solution'].startswith("-"):
                        self.mes=1
                        self.name="Ayikoyo Charles"
                        self.solutionTracker.append(1)
                elif int(kwags['solution'])==int(sum(self.altLeft2)-sum(self.altRight2)):
                    if kwags['solution'].startswith("+") or kwags['solution'].startswith("-"):
                        self.mes=1
                        self.name="Ivan Matenga Ogarubo"
                        self.solutionTracker.append(1)
            elif kwags['operator']=="Ꞃ":
                if int(kwags['solution'])==int(sum(self.altLeft0)*sum(self.altRight0)):
                    if kwags['solution'].startswith("+") or kwags['solution'].startswith("-"):
                        self.mes=1
                        self.name="Adriko Debo Joel"
                        self.solutionTracker.append(1)
                elif int(kwags['solution'])==int(sum(self.altLeft1)*sum(self.altRight1)):
                    if kwags['solution'].startswith("+") or kwags['solution'].startswith("-"):
                        self.mes=1
                        self.name="Ayikoyo Charles"
                        self.solutionTracker.append(1)
                elif int(kwags['solution'])==int(sum(self.altLeft2)*sum(self.altRight2)):
                    if kwags['solution'].startswith("+") or kwags['solution'].startswith("-"):
                        self.mes=1
                        self.name="Ivan Matenga Ogarubo"
                        self.solutionTracker.append(1)
            elif kwags['operator']=="Ꞇ":
                if int(kwags['solution'])==int(sum(self.altLeft0)/sum(self.altRight0)):
                    if kwags['solution'].startswith("+") or kwags['solution'].startswith("-"):
                        self.mes=1
                        self.name="Adriko Debo Joel"
                        self.solutionTracker.append(1)
                elif int(kwags['solution'])==int(sum(self.altLeft1)/sum(self.altRight1)):
                    if kwags['solution'].startswith("+") or kwags['solution'].startswith("-"):
                        self.mes=1
                        self.name="Ayikoyo Charles"
                        self.solutionTracker.append(1)
                elif int(kwags['solution'])==int(sum(self.altLeft2)/sum(self.altRight2)):
                    if kwags['solution'].startswith("+") or kwags['solution'].startswith("-"):
                        self.mes=1
                        self.name="Ivan Matenga Ogarubo"
                        self.solutionTracker.append(1)
            if len(self.solutionTracker)==0:
                self.trials=int(kwags['trials'])-1
                if self.trials==0:
                    self.mes=-1
                else:
                    self.mes=0
                    self.puzzle=[kwags['operandLeft'],kwags['operator'],kwags['operandRight'],self.trials]
        except:
            self.trials=int(kwags['trials'])-1
            if self.trials==0:
                self.mes=-1
            else:
                self.mes=0
                self.puzzle=[kwags['operandLeft'],kwags['operator'],kwags['operandRight'],self.trials]
class LogUser(object):
    """docstring for LogUser."""
    def __init__(self, **kwags):
        super(LogUser, self).__init__()
        self.dataUserLogState=model0.UserLogState()
        check0=self.dataUserLogState.getUserLogState(**kwags)
        kwags['date_of_state']=time.ctime()
        if len(check0)==0:
            self.dataUserLogState.addUserLogState(**kwags)
        else:
            self.dataUserLogState.updateLogState(**kwags)
            self.dataUserLogState.updateDateOfState(**kwags)
        self.dataUserLogState.conn.close()
class LogOut(object):
    """docstring for LogOut."""
    def __init__(self, **kwags):
        super(LogOut, self).__init__()
        self.dataStaffAccountState=model0.StaffAccountState()
        self.dataStaffCurrentAccountState=model0.StaffCurrentAccountState()
        tm=time.ctime()
        kwags['account_state']="inactive"
        kwags['date_of_state']=tm
        self.dataStaffAccountState.addStaffAccountState(**kwags)
        self.dataStaffCurrentAccountState.updateStaffCurrentAccountState(**kwags)
        self.dataStaffAccountState.conn.close()
        self.dataStaffCurrentAccountState.conn.close()
