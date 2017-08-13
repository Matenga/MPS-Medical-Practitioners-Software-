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
NurseDepartments=["D000","D001","D002","D003","D004","D006","D007","D008","D009"]
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
class AssignNurseToOneMoreDepartment(object):
    def __init__(self, **kwags):
        super(AssignNurseToOneMoreDepartment, self).__init__()
        self.dataDepartmentStaffRel=model0.DepartmentStaffRel()
        check0=self.dataDepartmentStaffRel.getDepartmentStaffRelByStaffId(**kwags)
        if len(check0)==1:
            tm=time.ctime()
            kwags['date_of_assignment']=tm
            self.dataDepartmentStaffRel.addDepartmentStaffRel(**kwags)
        self.dataDepartmentStaffRel.conn.close()
class RetrieveAssignedHospitalNurses(object):
    def __init__(self):
        super(RetrieveAssignedHospitalNurses, self).__init__()
        self.dataStaffDemographics=model0.StaffDemographics()
        self.dataUsers=model0.Users()
        self.dataStaffDemographicsUsersRel=model0.StaffDemographicsUsersRel()
        self.dataStaffState=model0.StaffState()
        self.dataStaffLeaveStatus=model0.StaffLeaveStatus()
        self.dataStaffCurrentAccountState=model0.StaffCurrentAccountState()
        self.dataDepartmentStaffRel=model0.DepartmentStaffRel()
        self.dataDeparment=model0.Department()
        self.message=[]
        self.departments=[]
        self.idPrefix=accountManagementHelper.GenerateIdPrefix()
        raw_data0=[]
        raw_data00=self.dataUsers.getAllUsers()
        for a,b,c,d,e in raw_data00:
            if d!="Principle Nurse Officer" and d!="Head Padeatrics" and d!="Head Surgery" and d!="System Administrator" and d!="Store Personnel" and d!="Laboratorist" and d!="Clinician" and d!="Pharmacist" and d!="Head Pharmacy" and d!="Head Clinic" and d!="Head Laboratory" and d!="Head Front Desk"\
             and d!="Head Store" and d!="Human Resource" and d!="Doctor" and d!="This is list should be extended as development proceeds":
                raw_data11=self.dataStaffDemographicsUsersRel.getStaffDemographicsUsersRelByUsername(username=a)
                for f,g in raw_data11:
                    departments=[]
                    check0=self.dataDepartmentStaffRel.getDepartmentStaffRelByStaffId(staff_id=f)
                    if len(check0)!=0:
                        for h,i,j in check0:
                            raw_data11=self.dataDeparment.getDepartment(department_id=h)
                            for k,l in raw_data11:
                                departments.append(l)
                    if len(departments)!=0:
                        raw_data0.append([a,b,c,d,e,departments])
        for a,b,c,d,e,ee in raw_data0:
            messageCrude=[]
            raw_data1=self.dataStaffDemographicsUsersRel.getStaffDemographicsUsersRelByUsername(username=a)
            for f,g in raw_data1:
                raw_data2=self.dataStaffDemographics.getStaffDemographicsByStaffId(staff_id=f)
                for h,i,j,k,l,m,n,o,p,q,r,s,t,u,v in raw_data2:
                    messageCrude.append(self.idPrefix.idPrefix+"-"+h)
                    messageCrude.append(h)
                    messageCrude.append(i)
                    messageCrude.append(v)
                    messageCrude.append(ee)
                    check1=self.dataStaffLeaveStatus.getStaffLeaveStatus(staff_id=h)
                    for w,x,xx in check1:
                        if x=="off":
                            raw_data3=self.dataStaffCurrentAccountState.getStaffCurrentAccountState(staff_id=h)
                            for y,z,zz in raw_data3:
                                messageCrude.append([z,zz])
                        else:
                            messageCrude.append([x,xx])
                    self.message.append(messageCrude)
        raw_data3=self.dataDeparment.getAllDepartment()
        for a,b in raw_data3:
            if a in NurseDepartments:
                self.departments.append([a,b])
        self.dataDeparment.conn.close()
        self.dataStaffDemographics.conn.close()
        self.dataUsers.conn.close()
        self.dataStaffDemographicsUsersRel.conn.close()
        self.dataStaffState.conn.close()
        self.dataStaffLeaveStatus.conn.close()
        self.dataStaffCurrentAccountState.conn.close()
        self.dataDepartmentStaffRel.conn.close()
class AssignNurseToDepartment(object):
    """docstring for AssignNurseToDepartment."""
    def __init__(self, **kwags):
        super(AssignNurseToDepartment, self).__init__()
        self.dataStaffAccountState=model0.StaffAccountState()
        self.dataStaffCurrentAccountState=model0.StaffCurrentAccountState()
        self.dataDepartmentStaffRel=model0.DepartmentStaffRel()
        self.dataStaffLeaveStatus=model0.StaffLeaveStatus()
        check0=self.dataDepartmentStaffRel.getDepartmentStaffRelByStaffId(**kwags)
        if len(check0)==0:
            tm=time.ctime()
            kwags['date_of_assignment']=tm
            kwags['staff_leave_status']="off"
            kwags['date_of_state']=tm
            kwags['account_state']="inactive"
            self.dataDepartmentStaffRel.addDepartmentStaffRel(**kwags)
            self.dataStaffLeaveStatus.addStaffLeaveStatus(**kwags)
            self.dataStaffAccountState.addStaffAccountState(**kwags)
            self.dataStaffCurrentAccountState.addStaffCurrentAccountState(**kwags)
        self.dataStaffAccountState.conn.close()
        self.dataStaffCurrentAccountState.conn.close()
        self.dataDepartmentStaffRel.conn.close()
        self.dataStaffLeaveStatus.conn.close()
class RetrieveUnsignedHospitalNurses(object):
    def __init__(self):
        super(RetrieveUnsignedHospitalNurses, self).__init__()
        self.dataStaffDemographics=model0.StaffDemographics()
        self.dataUsers=model0.Users()
        self.dataStaffDemographicsUsersRel=model0.StaffDemographicsUsersRel()
        self.dataStaffState=model0.StaffState()
        self.dataStaffLeaveStatus=model0.StaffLeaveStatus()
        self.dataStaffCurrentAccountState=model0.StaffCurrentAccountState()
        self.dataDepartmentStaffRel=model0.DepartmentStaffRel()
        self.dataDeparment=model0.Department()
        self.message=[]
        self.departments=[]
        self.idPrefix=accountManagementHelper.GenerateIdPrefix()
        raw_data0=[]
        raw_data00=self.dataUsers.getAllUsers()
        for a,b,c,d,e in raw_data00:
            if d!="Principle Nurse Officer" and d!="Head Padeatrics" and d!="Head Surgery" and d!="System Administrator" and d!="Store Personnel" and d!="Laboratorist" and d!="Clinician" and d!="Pharmacist" and d!="Head Pharmacy" and d!="Head Clinic" and d!="Head Laboratory" and d!="Head Front Desk"\
             and d!="Head Store" and d!="Human Resource" and d!="Doctor" and d!="This is list should be extended as development proceeds":
                raw_data11=self.dataStaffDemographicsUsersRel.getStaffDemographicsUsersRelByUsername(username=a)
                for f,g in raw_data11:
                    check0=self.dataDepartmentStaffRel.getDepartmentStaffRelByStaffId(staff_id=f)
                    if len(check0)==0:
                        raw_data0.append([a,b,c,d,e])
        for a,b,c,d,e in raw_data0:
            messageCrude=[]
            raw_data1=self.dataStaffDemographicsUsersRel.getStaffDemographicsUsersRelByUsername(username=a)
            for f,g in raw_data1:
                raw_data2=self.dataStaffDemographics.getStaffDemographicsByStaffId(staff_id=f)
                for h,i,j,k,l,m,n,o,p,q,r,s,t,u,v in raw_data2:
                    messageCrude.append(self.idPrefix.idPrefix+"-"+h)
                    messageCrude.append(h)
                    messageCrude.append(i)
                    messageCrude.append(v)
                    messageCrude.append(q)
                    check1=self.dataStaffLeaveStatus.getStaffLeaveStatus(staff_id=h)
                    for w,x,xx in check1:
                        if x=="off":
                            raw_data3=self.dataStaffCurrentAccountState.getStaffCurrentAccountState(staff_id=h)
                            for y,z,zz in raw_data3:
                                messageCrude.append([z,zz])
                        else:
                            messageCrude.append([x,xx])
                    self.message.append(messageCrude)
        raw_data3=self.dataDeparment.getAllDepartment()
        for a,b in raw_data3:
            if a in NurseDepartments:
                self.departments.append([a,b])
        self.dataDeparment.conn.close()
        self.dataStaffDemographics.conn.close()
        self.dataUsers.conn.close()
        self.dataStaffDemographicsUsersRel.conn.close()
        self.dataStaffState.conn.close()
        self.dataStaffLeaveStatus.conn.close()
        self.dataStaffCurrentAccountState.conn.close()
        self.dataDepartmentStaffRel.conn.close()
