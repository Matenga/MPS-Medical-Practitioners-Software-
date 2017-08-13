import cherrypy
from models import model0
from passlib.hash import pbkdf2_sha256
import time
import os
import random
import chilkat,sys
from systemAdminMIS.helpers import ascii_generator
from systemAdminMIS.helpers import accountManagementHelper
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
Crypto = chilkat.CkCrypt2()
success = Crypto.UnlockComponent("MPS-Crypto")
if (success != True):
    sys.exit()
Crypto.put_CryptAlgorithm("aes")
Crypto.put_CipherMode("cbc")
Crypto.put_KeyLength(256)
Crypto.put_PaddingScheme(0)
Crypto.put_EncodingMode("hex")
ivHex = "000102030405060708090A0B0C0D0E0F"
Crypto.SetEncodedIV(ivHex,"hex")
CryptoKeyHex = "000102030405060708090A0B0C0DDD0E0F101112131415161718191A1B1C1D1E1F"
Crypto.SetEncodedKey(CryptoKeyHex,"hex")
class RetrieveAvailableHospitalStorePersonnel(object):
    def __init__(self):
        super(RetrieveAvailableHospitalStorePersonnel, self).__init__()
        self.dataStaffDemographics=model0.StaffDemographics()
        self.dataUsers=model0.Users()
        self.dataStaffDemographicsUsersRel=model0.StaffDemographicsUsersRel()
        self.dataStaffState=model0.StaffState()
        self.dataStaffLeaveStatus=model0.StaffLeaveStatus()
        self.dataStaffCurrentAccountState=model0.StaffCurrentAccountState()
        self.dataDepartmentStaffRel=model0.DepartmentStaffRel()
        self.dataDeparment=model0.Department()
        self.message=[]
        self.idPrefix=accountManagementHelper.GenerateIdPrefix()
        raw_data0=[]
        raw_data00=self.dataUsers.getAllUsers()
        for a,b,c,d,e in raw_data00:
            if d!="Head Pharmacy" and d!="Pharmacist" and d!="Head Clinic" and d!="Head Padeatrics" and d!="Head Surgery" and d!="Principle Nurse Officer" and d!="Senior Principle Nurse Officer" and d!="System Administrator" and d!="Clinician" and d!="Laboratorist" and d!="Head Laboratory" and d!="Nurse" and d!="Head Front Desk" and d!="Human Resource" and d!="Doctor" and d!="This is list should be extended as development proceeds":
                raw_data11=self.dataStaffDemographicsUsersRel.getStaffDemographicsUsersRelByUsername(username=a)
                for f,g in raw_data11:
                    check0=self.dataStaffState.getStaffState(staff_id=f)
                    if len(check0)==0:
                        raw_data0.append([a,b,c,d,e])
        for a,b,c,d,e in raw_data0:
            messageCrude=[]
            raw_data1=self.dataStaffDemographicsUsersRel.getStaffDemographicsUsersRelByUsername(username=a)
            for f,g in raw_data1:
                raw_data2=self.dataStaffDemographics.getStaffDemographicsByStaffId(staff_id=f)
                for h,i,j,k,l,m,n,o,p,q,r,s,t,u,v in raw_data2:
                    messageCrude.append(self.idPrefix.idPrefix+"-"+h)
                    messageCrude.append(i)
                    messageCrude.append(v)
                    raw_data3=self.dataStaffLeaveStatus.getStaffLeaveStatus(staff_id=h)
                    if len(raw_data3)==0:
                        messageCrude.append(["Account Not Activated",q])
                    else:
                        for w,x,xx in raw_data3:
                            if x=='on':
                                messageCrude.append(["On Leave",xx])
                            else:
                                raw_data4=self.dataStaffCurrentAccountState.getStaffCurrentAccountState(staff_id=h)
                                for y,z,aa in raw_data4:
                                    messageCrude.append([z,aa])
                    raw_data5=self.dataDepartmentStaffRel.getDepartmentStaffRelByStaffId(staff_id=h)
                    if len(raw_data5)==0:
                        if d!="Head Store":
                            messageCrude.append("Not Assigned Yet")
                        else:
                            messageCrude.append(d)
                    else:
                        for bb,cc,dd in raw_data5:
                            raw_data6=self.dataDeparment.getDepartment(department_id=bb)
                            for ee,ff in raw_data6:
                                messageCrude.append(ff)
                    self.message.append(messageCrude)
        self.dataDeparment.conn.close()
        self.dataStaffDemographics.conn.close()
        self.dataUsers.conn.close()
        self.dataStaffDemographicsUsersRel.conn.close()
        self.dataStaffState.conn.close()
        self.dataStaffLeaveStatus.conn.close()
        self.dataStaffCurrentAccountState.conn.close()
        self.dataDepartmentStaffRel.conn.close()
class AddHospitalStorePersonnel(object):
    def __init__(self, **kwags):
        super(AddHospitalStorePersonnel, self).__init__()
        self.message=[]
        kwags['marital_status']=''
        kwags['physical_address']=''
        kwags['user_type']="Store Personnel"
        kwags['full_name']="{} {}".format(kwags['first_name'],kwags['other_name'])
        self.message.append(kwags['full_name'])
        pref=accountManagementHelper.GenerateIdPrefix()
        self.prefix=pref.idPrefix
        init=accountManagementHelper.GenerateIdInitials(**kwags)
        initials=init.initials
        kwag={"state":"staff_id","initials":initials}
        staffId=accountManagementHelper.GenerateId(**kwag)
        staff_id=staffId.id
        kwags['staff_id']=staff_id
        self.message.append(self.prefix+"-"+staff_id)
        usrName=accountManagementHelper.GenerateUserName(**kwags)
        if usrName.username==None:
            kwags['username']=kwags['staff_id']
            self.message.append(kwags['staff_id'])
        else:
            kwags['username']=usrName.username
        self.message.append(kwags['appointment_id'])
        addStaff=accountManagementHelper.AddHighLevelStaff(**kwags)
        self.message.append(kwags['phone_number'])
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
        self.message.append(kwags['user_type'])
class RetrieveAvailableHospitalPharmacists(object):
    def __init__(self):
        super(RetrieveAvailableHospitalPharmacists, self).__init__()
        self.dataStaffDemographics=model0.StaffDemographics()
        self.dataUsers=model0.Users()
        self.dataStaffDemographicsUsersRel=model0.StaffDemographicsUsersRel()
        self.dataStaffState=model0.StaffState()
        self.dataStaffLeaveStatus=model0.StaffLeaveStatus()
        self.dataStaffCurrentAccountState=model0.StaffCurrentAccountState()
        self.dataDepartmentStaffRel=model0.DepartmentStaffRel()
        self.dataDeparment=model0.Department()
        self.message=[]
        self.idPrefix=accountManagementHelper.GenerateIdPrefix()
        raw_data0=[]
        raw_data00=self.dataUsers.getAllUsers()
        for a,b,c,d,e in raw_data00:
            if d!="Head Clinic" and d!="Head Padeatrics" and d!="Head Surgery" and d!="Principle Nurse Officer" and d!="Senior Principle Nurse Officer" and d!="System Administrator" and d!="Store Personnel" and d!="Clinician" and d!="Laboratorist" and d!="Head Laboratory" and d!="Nurse" and d!="Head Front Desk" and d!="Head Store" and d!="Human Resource" and d!="Doctor" and d!="This is list should be extended as development proceeds":
                raw_data11=self.dataStaffDemographicsUsersRel.getStaffDemographicsUsersRelByUsername(username=a)
                for f,g in raw_data11:
                    check0=self.dataStaffState.getStaffState(staff_id=f)
                    if len(check0)==0:
                        raw_data0.append([a,b,c,d,e])
        for a,b,c,d,e in raw_data0:
            messageCrude=[]
            raw_data1=self.dataStaffDemographicsUsersRel.getStaffDemographicsUsersRelByUsername(username=a)
            for f,g in raw_data1:
                raw_data2=self.dataStaffDemographics.getStaffDemographicsByStaffId(staff_id=f)
                for h,i,j,k,l,m,n,o,p,q,r,s,t,u,v in raw_data2:
                    messageCrude.append(self.idPrefix.idPrefix+"-"+h)
                    messageCrude.append(i)
                    messageCrude.append(v)
                    raw_data3=self.dataStaffLeaveStatus.getStaffLeaveStatus(staff_id=h)
                    if len(raw_data3)==0:
                        messageCrude.append(["Account Not Activated",q])
                    else:
                        for w,x,xx in raw_data3:
                            if x=='on':
                                messageCrude.append(["On Leave",xx])
                            else:
                                raw_data4=self.dataStaffCurrentAccountState.getStaffCurrentAccountState(staff_id=h)
                                for y,z,aa in raw_data4:
                                    messageCrude.append([z,aa])
                    raw_data5=self.dataDepartmentStaffRel.getDepartmentStaffRelByStaffId(staff_id=h)
                    if len(raw_data5)==0:
                        if d!="Head Pharmacy":
                            messageCrude.append("Not Assigned Yet")
                        else:
                            messageCrude.append(d)
                    else:
                        for bb,cc,dd in raw_data5:
                            raw_data6=self.dataDeparment.getDepartment(department_id=bb)
                            for ee,ff in raw_data6:
                                messageCrude.append(ff)
                    self.message.append(messageCrude)
        self.dataDeparment.conn.close()
        self.dataStaffDemographics.conn.close()
        self.dataUsers.conn.close()
        self.dataStaffDemographicsUsersRel.conn.close()
        self.dataStaffState.conn.close()
        self.dataStaffLeaveStatus.conn.close()
        self.dataStaffCurrentAccountState.conn.close()
        self.dataDepartmentStaffRel.conn.close()
class AddHospitalPharmacist(object):
    def __init__(self, **kwags):
        super(AddHospitalPharmacist, self).__init__()
        self.message=[]
        kwags['marital_status']=''
        kwags['physical_address']=''
        kwags['user_type']="Pharmacist"
        kwags['full_name']="{} {}".format(kwags['first_name'],kwags['other_name'])
        self.message.append(kwags['full_name'])
        pref=accountManagementHelper.GenerateIdPrefix()
        self.prefix=pref.idPrefix
        init=accountManagementHelper.GenerateIdInitials(**kwags)
        initials=init.initials
        kwag={"state":"staff_id","initials":initials}
        staffId=accountManagementHelper.GenerateId(**kwag)
        staff_id=staffId.id
        kwags['staff_id']=staff_id
        self.message.append(self.prefix+"-"+staff_id)
        usrName=accountManagementHelper.GenerateUserName(**kwags)
        if usrName.username==None:
            kwags['username']=kwags['staff_id']
            self.message.append(kwags['staff_id'])
        else:
            kwags['username']=usrName.username
        self.message.append(kwags['appointment_id'])
        addStaff=accountManagementHelper.AddHighLevelStaff(**kwags)
        self.message.append(kwags['phone_number'])
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
        self.message.append(kwags['user_type'])
class RetrieveAvailableHospitalLaboratorists(object):
    def __init__(self):
        super(RetrieveAvailableHospitalLaboratorists, self).__init__()
        self.dataStaffDemographics=model0.StaffDemographics()
        self.dataUsers=model0.Users()
        self.dataStaffDemographicsUsersRel=model0.StaffDemographicsUsersRel()
        self.dataStaffState=model0.StaffState()
        self.dataStaffLeaveStatus=model0.StaffLeaveStatus()
        self.dataStaffCurrentAccountState=model0.StaffCurrentAccountState()
        self.dataDepartmentStaffRel=model0.DepartmentStaffRel()
        self.dataDeparment=model0.Department()
        self.message=[]
        self.idPrefix=accountManagementHelper.GenerateIdPrefix()
        raw_data0=[]
        raw_data00=self.dataUsers.getAllUsers()
        for a,b,c,d,e in raw_data00:
            if d!="Head Clinic" and d!="Head Padeatrics" and d!="Head Surgery" and d!="Principle Nurse Officer" and d!="Senior Principle Nurse Officer" and d!="System Administrator" and d!="Store Personnel" and d!="Clinician" and d!="Pharmacist" and d!="Head Pharmacy" and d!="Nurse" and d!="Head Front Desk" and d!="Head Store" and d!="Human Resource" and d!="Doctor" and d!="This is list should be extended as development proceeds":
                raw_data11=self.dataStaffDemographicsUsersRel.getStaffDemographicsUsersRelByUsername(username=a)
                for f,g in raw_data11:
                    check0=self.dataStaffState.getStaffState(staff_id=f)
                    if len(check0)==0:
                        raw_data0.append([a,b,c,d,e])
        for a,b,c,d,e in raw_data0:
            messageCrude=[]
            raw_data1=self.dataStaffDemographicsUsersRel.getStaffDemographicsUsersRelByUsername(username=a)
            for f,g in raw_data1:
                raw_data2=self.dataStaffDemographics.getStaffDemographicsByStaffId(staff_id=f)
                for h,i,j,k,l,m,n,o,p,q,r,s,t,u,v in raw_data2:
                    messageCrude.append(self.idPrefix.idPrefix+"-"+h)
                    messageCrude.append(i)
                    messageCrude.append(v)
                    raw_data3=self.dataStaffLeaveStatus.getStaffLeaveStatus(staff_id=h)
                    if len(raw_data3)==0:
                        messageCrude.append(["Account Not Activated",q])
                    else:
                        for w,x,xx in raw_data3:
                            if x=='on':
                                messageCrude.append(["On Leave",xx])
                            else:
                                raw_data4=self.dataStaffCurrentAccountState.getStaffCurrentAccountState(staff_id=h)
                                for y,z,aa in raw_data4:
                                    messageCrude.append([z,aa])
                    raw_data5=self.dataDepartmentStaffRel.getDepartmentStaffRelByStaffId(staff_id=h)
                    if len(raw_data5)==0:
                        if d!="Head Laboratory":
                            messageCrude.append("Not Assigned Yet")
                        else:
                            messageCrude.append(d)
                    else:
                        for bb,cc,dd in raw_data5:
                            raw_data6=self.dataDeparment.getDepartment(department_id=bb)
                            for ee,ff in raw_data6:
                                messageCrude.append(ff)
                    self.message.append(messageCrude)
        self.dataDeparment.conn.close()
        self.dataStaffDemographics.conn.close()
        self.dataUsers.conn.close()
        self.dataStaffDemographicsUsersRel.conn.close()
        self.dataStaffState.conn.close()
        self.dataStaffLeaveStatus.conn.close()
        self.dataStaffCurrentAccountState.conn.close()
        self.dataDepartmentStaffRel.conn.close()
class AddHospitalLaboratorist(object):
    def __init__(self, **kwags):
        super(AddHospitalLaboratorist, self).__init__()
        self.message=[]
        kwags['marital_status']=''
        kwags['physical_address']=''
        kwags['user_type']="Laboratorist"
        kwags['full_name']="{} {}".format(kwags['first_name'],kwags['other_name'])
        self.message.append(kwags['full_name'])
        pref=accountManagementHelper.GenerateIdPrefix()
        self.prefix=pref.idPrefix
        init=accountManagementHelper.GenerateIdInitials(**kwags)
        initials=init.initials
        kwag={"state":"staff_id","initials":initials}
        staffId=accountManagementHelper.GenerateId(**kwag)
        staff_id=staffId.id
        kwags['staff_id']=staff_id
        self.message.append(self.prefix+"-"+staff_id)
        usrName=accountManagementHelper.GenerateUserName(**kwags)
        if usrName.username==None:
            kwags['username']=kwags['staff_id']
            self.message.append(kwags['staff_id'])
        else:
            kwags['username']=usrName.username
        self.message.append(kwags['appointment_id'])
        addStaff=accountManagementHelper.AddHighLevelStaff(**kwags)
        self.message.append(kwags['phone_number'])
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
        self.message.append(kwags['user_type'])
class RetrieveAvailableHospitalClinicians(object):
    def __init__(self):
        super(RetrieveAvailableHospitalClinicians, self).__init__()
        self.dataStaffDemographics=model0.StaffDemographics()
        self.dataUsers=model0.Users()
        self.dataStaffDemographicsUsersRel=model0.StaffDemographicsUsersRel()
        self.dataStaffState=model0.StaffState()
        self.dataStaffLeaveStatus=model0.StaffLeaveStatus()
        self.dataStaffCurrentAccountState=model0.StaffCurrentAccountState()
        self.dataDepartmentStaffRel=model0.DepartmentStaffRel()
        self.dataDeparment=model0.Department()
        self.message=[]
        self.idPrefix=accountManagementHelper.GenerateIdPrefix()
        raw_data0=[]
        raw_data00=self.dataUsers.getAllUsers()
        for a,b,c,d,e in raw_data00:
            if d!="Head Padeatrics" and d!="Head Surgery" and d!="Principle Nurse Officer" and d!="Senior Principle Nurse Officer" and d!="System Administrator" and d!="Store Personnel" and d!="Laboratorist" and d!="Pharmacist" and d!="Head Pharmacy" and d!="Nurse" and d!="Head Laboratory" and d!="Head Front Desk" and d!="Head Store" and d!="Human Resource" and d!="Doctor" and d!="This is list should be extended as development proceeds":
                raw_data11=self.dataStaffDemographicsUsersRel.getStaffDemographicsUsersRelByUsername(username=a)
                for f,g in raw_data11:
                    check0=self.dataStaffState.getStaffState(staff_id=f)
                    if len(check0)==0:
                        raw_data0.append([a,b,c,d,e])
        for a,b,c,d,e in raw_data0:
            messageCrude=[]
            raw_data1=self.dataStaffDemographicsUsersRel.getStaffDemographicsUsersRelByUsername(username=a)
            for f,g in raw_data1:
                raw_data2=self.dataStaffDemographics.getStaffDemographicsByStaffId(staff_id=f)
                for h,i,j,k,l,m,n,o,p,q,r,s,t,u,v in raw_data2:
                    messageCrude.append(self.idPrefix.idPrefix+"-"+h)
                    messageCrude.append(i)
                    messageCrude.append(v)
                    raw_data3=self.dataStaffLeaveStatus.getStaffLeaveStatus(staff_id=h)
                    if len(raw_data3)==0:
                        messageCrude.append(["Account Not Activated",q])
                    else:
                        for w,x,xx in raw_data3:
                            if x=='on':
                                messageCrude.append(["On Leave",xx])
                            else:
                                raw_data4=self.dataStaffCurrentAccountState.getStaffCurrentAccountState(staff_id=h)
                                for y,z,aa in raw_data4:
                                    messageCrude.append([z,aa])
                    raw_data5=self.dataDepartmentStaffRel.getDepartmentStaffRelByStaffId(staff_id=h)
                    if len(raw_data5)==0:
                        if d!="Head Clinic":
                            messageCrude.append("Not Assigned Yet")
                        else:
                            messageCrude.append(d)
                    else:
                        for bb,cc,dd in raw_data5:
                            raw_data6=self.dataDeparment.getDepartment(department_id=bb)
                            for ee,ff in raw_data6:
                                messageCrude.append(ff)
                    self.message.append(messageCrude)
        self.dataDeparment.conn.close()
        self.dataStaffDemographics.conn.close()
        self.dataUsers.conn.close()
        self.dataStaffDemographicsUsersRel.conn.close()
        self.dataStaffState.conn.close()
        self.dataStaffLeaveStatus.conn.close()
        self.dataStaffCurrentAccountState.conn.close()
        self.dataDepartmentStaffRel.conn.close()
class AddHospitalClinician(object):
    def __init__(self, **kwags):
        super(AddHospitalClinician, self).__init__()
        self.message=[]
        kwags['marital_status']=''
        kwags['physical_address']=''
        kwags['user_type']="Clinician"
        kwags['full_name']="{} {}".format(kwags['first_name'],kwags['other_name'])
        self.message.append(kwags['full_name'])
        pref=accountManagementHelper.GenerateIdPrefix()
        self.prefix=pref.idPrefix
        init=accountManagementHelper.GenerateIdInitials(**kwags)
        initials=init.initials
        kwag={"state":"staff_id","initials":initials}
        staffId=accountManagementHelper.GenerateId(**kwag)
        staff_id=staffId.id
        kwags['staff_id']=staff_id
        self.message.append(self.prefix+"-"+staff_id)
        usrName=accountManagementHelper.GenerateUserName(**kwags)
        if usrName.username==None:
            kwags['username']=kwags['staff_id']
            self.message.append(kwags['staff_id'])
        else:
            kwags['username']=usrName.username
        self.message.append(kwags['appointment_id'])
        addStaff=accountManagementHelper.AddHighLevelStaff(**kwags)
        self.message.append(kwags['phone_number'])
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
        self.message.append(kwags['user_type'])
class RetrieveAvailableHospitalNurses(object):
    def __init__(self):
        super(RetrieveAvailableHospitalNurses, self).__init__()
        self.dataStaffDemographics=model0.StaffDemographics()
        self.dataUsers=model0.Users()
        self.dataStaffDemographicsUsersRel=model0.StaffDemographicsUsersRel()
        self.dataStaffState=model0.StaffState()
        self.dataStaffLeaveStatus=model0.StaffLeaveStatus()
        self.dataStaffCurrentAccountState=model0.StaffCurrentAccountState()
        self.dataDepartmentStaffRel=model0.DepartmentStaffRel()
        self.dataDeparment=model0.Department()
        self.message=[]
        self.idPrefix=accountManagementHelper.GenerateIdPrefix()
        raw_data0=[]
        raw_data00=self.dataUsers.getAllUsers()
        for a,b,c,d,e in raw_data00:
            if d!="Head Padeatrics" and d!="Head Surgery" and d!="System Administrator" and d!="Store Personnel" and d!="Laboratorist" and d!="Clinician" and d!="Pharmacist" and d!="Head Pharmacy" and d!="Head Clinic" and d!="Head Laboratory" and d!="Head Front Desk" and d!="Head Store" and d!="Human Resource" and d!="Doctor" and d!="This is list should be extended as development proceeds":
                raw_data11=self.dataStaffDemographicsUsersRel.getStaffDemographicsUsersRelByUsername(username=a)
                for f,g in raw_data11:
                    check0=self.dataStaffState.getStaffState(staff_id=f)
                    if len(check0)==0:
                        raw_data0.append([a,b,c,d,e])
        for a,b,c,d,e in raw_data0:
            messageCrude=[]
            raw_data1=self.dataStaffDemographicsUsersRel.getStaffDemographicsUsersRelByUsername(username=a)
            for f,g in raw_data1:
                raw_data2=self.dataStaffDemographics.getStaffDemographicsByStaffId(staff_id=f)
                for h,i,j,k,l,m,n,o,p,q,r,s,t,u,v in raw_data2:
                    messageCrude.append(self.idPrefix.idPrefix+"-"+h)
                    messageCrude.append(i)
                    messageCrude.append(v)
                    raw_data3=self.dataStaffLeaveStatus.getStaffLeaveStatus(staff_id=h)
                    if len(raw_data3)==0:
                        messageCrude.append(["Account Not Activated",q])
                    else:
                        for w,x,xx in raw_data3:
                            if x=='on':
                                messageCrude.append(["On Leave",xx])
                            else:
                                raw_data4=self.dataStaffCurrentAccountState.getStaffCurrentAccountState(staff_id=h)
                                for y,z,aa in raw_data4:
                                    messageCrude.append([z,aa])
                    raw_data5=self.dataDepartmentStaffRel.getDepartmentStaffRelByStaffId(staff_id=h)
                    if len(raw_data5)==0:
                        if d!="Principle Nurse Officer" and d!="Senior Principle Nurse Officer":
                            messageCrude.append("Not Assigned Yet")
                        else:
                            messageCrude.append(d)
                    else:
                        for bb,cc,dd in raw_data5:
                            raw_data6=self.dataDeparment.getDepartment(department_id=bb)
                            for ee,ff in raw_data6:
                                messageCrude.append(ff)
                    self.message.append(messageCrude)
        self.dataDeparment.conn.close()
        self.dataStaffDemographics.conn.close()
        self.dataUsers.conn.close()
        self.dataStaffDemographicsUsersRel.conn.close()
        self.dataStaffState.conn.close()
        self.dataStaffLeaveStatus.conn.close()
        self.dataStaffCurrentAccountState.conn.close()
        self.dataDepartmentStaffRel.conn.close()
class AddHospitalNurse(object):
    def __init__(self, **kwags):
        super(AddHospitalNurse, self).__init__()
        self.message=[]
        kwags['marital_status']=''
        kwags['physical_address']=''
        kwags['user_type']="Nurse"
        kwags['full_name']="{} {}".format(kwags['first_name'],kwags['other_name'])
        self.message.append(kwags['full_name'])
        pref=accountManagementHelper.GenerateIdPrefix()
        self.prefix=pref.idPrefix
        init=accountManagementHelper.GenerateIdInitials(**kwags)
        initials=init.initials
        kwag={"state":"staff_id","initials":initials}
        staffId=accountManagementHelper.GenerateId(**kwag)
        staff_id=staffId.id
        kwags['staff_id']=staff_id
        self.message.append(self.prefix+"-"+staff_id)
        usrName=accountManagementHelper.GenerateUserName(**kwags)
        if usrName.username==None:
            kwags['username']=kwags['staff_id']
            self.message.append(kwags['staff_id'])
        else:
            kwags['username']=usrName.username
        self.message.append(kwags['appointment_id'])
        addStaff=accountManagementHelper.AddHighLevelStaff(**kwags)
        self.message.append(kwags['phone_number'])
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
        self.message.append(kwags['user_type'])
class RetrieveAvailableHospitalDoctors(object):
    def __init__(self):
        super(RetrieveAvailableHospitalDoctors, self).__init__()
        self.dataStaffDemographics=model0.StaffDemographics()
        self.dataUsers=model0.Users()
        self.dataStaffDemographicsUsersRel=model0.StaffDemographicsUsersRel()
        self.dataStaffState=model0.StaffState()
        self.dataStaffLeaveStatus=model0.StaffLeaveStatus()
        self.dataStaffCurrentAccountState=model0.StaffCurrentAccountState()
        self.dataDepartmentStaffRel=model0.DepartmentStaffRel()
        self.dataDeparment=model0.Department()
        self.message=[]
        self.idPrefix=accountManagementHelper.GenerateIdPrefix()
        raw_data0=[]
        raw_data00=self.dataUsers.getAllUsers()
        for a,b,c,d,e in raw_data00:
            if d!="System Administrator" and d!="Laboratorist" and d!="Clinician" and d!="Pharmacist" and d!="Principle Nurse Officer" and d!="Head Pharmacy" and d!="Store Personnel" and d!="Head Clinic" and d!="Head Laboratory" and d!="Head Front Desk" and d!="Head Store" and d!="Senior Principle Nurse Officer" and d!="Human Resource" and d!="Nurse" and d!="This is list should be extended as development proceeds":
                raw_data11=self.dataStaffDemographicsUsersRel.getStaffDemographicsUsersRelByUsername(username=a)
                for f,g in raw_data11:
                    check0=self.dataStaffState.getStaffState(staff_id=f)
                    if len(check0)==0:
                        raw_data0.append([a,b,c,d,e])
        for a,b,c,d,e in raw_data0:
            messageCrude=[]
            raw_data1=self.dataStaffDemographicsUsersRel.getStaffDemographicsUsersRelByUsername(username=a)
            for f,g in raw_data1:
                raw_data2=self.dataStaffDemographics.getStaffDemographicsByStaffId(staff_id=f)
                for h,i,j,k,l,m,n,o,p,q,r,s,t,u,v in raw_data2:
                    messageCrude.append(self.idPrefix.idPrefix+"-"+h)
                    messageCrude.append(i)
                    messageCrude.append(v)
                    raw_data3=self.dataStaffLeaveStatus.getStaffLeaveStatus(staff_id=h)
                    if len(raw_data3)==0:
                        messageCrude.append(["Account Not Activated",q])
                    else:
                        for w,x,xx in raw_data3:
                            if x=='on':
                                messageCrude.append(["On Leave",xx])
                            else:
                                raw_data4=self.dataStaffCurrentAccountState.getStaffCurrentAccountState(staff_id=h)
                                for y,z,aa in raw_data4:
                                    messageCrude.append([z,aa])
                    raw_data5=self.dataDepartmentStaffRel.getDepartmentStaffRelByStaffId(staff_id=h)
                    if len(raw_data5)==0:
                        if d!="Head Padeatrics" and d!="Head Surgery":
                            messageCrude.append("Not Assigned Yet")
                        else:
                            messageCrude.append(d)
                    else:
                        for bb,cc,dd in raw_data5:
                            raw_data6=self.dataDeparment.getDepartment(department_id=bb)
                            for ee,ff in raw_data6:
                                messageCrude.append(ff)
                    self.message.append(messageCrude)
        self.dataDeparment.conn.close()
        self.dataStaffDemographics.conn.close()
        self.dataUsers.conn.close()
        self.dataStaffDemographicsUsersRel.conn.close()
        self.dataStaffState.conn.close()
        self.dataStaffLeaveStatus.conn.close()
        self.dataStaffCurrentAccountState.conn.close()
        self.dataDepartmentStaffRel.conn.close()
class AddHospitalDoctor(object):
    def __init__(self, **kwags):
        super(AddHospitalDoctor, self).__init__()
        self.message=[]
        kwags['marital_status']=''
        kwags['physical_address']=''
        kwags['user_type']="Doctor"
        kwags['full_name']="{} {}".format(kwags['first_name'],kwags['other_name'])
        self.message.append(kwags['full_name'])
        pref=accountManagementHelper.GenerateIdPrefix()
        self.prefix=pref.idPrefix
        init=accountManagementHelper.GenerateIdInitials(**kwags)
        initials=init.initials
        kwag={"state":"staff_id","initials":initials}
        staffId=accountManagementHelper.GenerateId(**kwag)
        staff_id=staffId.id
        kwags['staff_id']=staff_id
        self.message.append(self.prefix+"-"+staff_id)
        usrName=accountManagementHelper.GenerateUserName(**kwags)
        if usrName.username==None:
            kwags['username']=kwags['staff_id']
            self.message.append(kwags['staff_id'])
        else:
            kwags['username']=usrName.username
        self.message.append(kwags['appointment_id'])
        addStaff=accountManagementHelper.AddHighLevelStaff(**kwags)
        self.message.append(kwags['phone_number'])
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
        self.message.append(kwags['user_type'])
