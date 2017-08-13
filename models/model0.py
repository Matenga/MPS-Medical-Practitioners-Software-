import serverConfiguration as databaseServer
class PatientDemographics(object):
    def __init__(self):
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addPatientDemographics(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO patient_demographics(patient_id,nid,fullname,dob,home_district,physical_address,marital_status,email,phone_number,photo\
        ,gender,date_of_registration,occupation,nationality,social_security_number)VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')"\
        .format(kwags['patient_id'],kwags['nid'],kwags['fullname'],kwags['dob'],kwags['home_district'],kwags['physical_address'],kwags['marital_status'],\
        kwags['email'],kwags['phone_number'],kwags['photo'],kwags['gender'],kwags['date_of_registration'],kwags['occupation'],kwags['nationality'],\
        kwags['social_security_number'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getPatientDemographicsByPatientId(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_demographics WHERE patient_id='{}'".format(kwags['patient_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getPatientDemographicsBySocialSecurityNumber(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_demographics WHERE social_security_number='{}'".format(kwags['social_security_number'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getPatientDemographicsByFullName(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_demographics WHERE full_name='{}'".format(kwags['full_name'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getPatientDemographicsByNID(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_demographics WHERE nid='{}'".format(kwags['nid'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getPatientDemographicsWhereNameBeginsWith(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_demographics WHERE full_name LIKE '{}%'".format(kwags['full_name'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getPatientDemographicsWhereNameEndsWith(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_demographics WHERE full_name LIKE '%{}'".format(kwags['full_name'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getPatientDemographicsWhereNameHas(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_demographics WHERE full_name LIKE '%{}%'".format(kwags['full_name'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllPatientDemographics(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_demographics WHERE full_name LIKE '{}%'".format(kwags['full_name'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def updatePhoto(self,**kwags):
        cur=self.conn.cursor()
        sql="UPDATE patient_demographics SET photo='{}' WHERE patient_id='{}'".format(kwags['photo'],kwags['patient_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def updateMaritalStatus(self,**kwags):
        cur=self.conn.cursor()
        sql="UPDATE patient_demographics SET marital_status='{}' WHERE patient_id='{}'".format(kwags['marital_status'],kwags['patient_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def updateEmail(self,**kwags):
        cur=self.conn.cursor()
        sql="UPDATE patient_demographics SET email='{}' WHERE patient_id='{}'".format(kwags['email'],kwags['patient_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def updatePhoneNumber(self,**kwags):
        cur=self.conn.cursor()
        sql="UPDATE patient_demographics SET phone_number='{}' WHERE patient_id='{}'".format(kwags['phone_number'],kwags['patient_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def updateNextOfKeen(self,**kwags):
        cur=self.conn.cursor()
        sql="UPDATE patient_demographics SET next_of_keen='{}' WHERE patient_id='{}'".format(kwags['next_of_keen'],kwags['patient_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def updateOccupation(self,**kwags):
        cur=self.conn.cursor()
        sql="UPDATE patient_demographics SET occupation='{}' WHERE patient_id='{}'".format(kwags['occupation'],kwags['patient_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removePatientDemographics(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_demographics WHERE patient_id='{}'".format(kwags['patient_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllPatientDemographics(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_demographics"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class PatientVisit(object):
    def __init__(self):
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addPatientVisit(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO patient_visit(visit_id,patient_id,date_of_visit,visit_type)VALUES('{}','{}','{}','{}')".format(kwags['visit_id'],kwags['patient_id'],kwags['date_of_visit'],kwags['visit_type'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getPatientVisitByVisitId(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_visit WHERE visit_id='{}'".format(kwags['visit_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getPatientVisitByPatientId(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_visit WHERE patient_id='{}'".format(kwags['patient_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllPatientVisit(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_visit"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def removePatientVisit(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_visit WHERE visit_id='{}'".format(kwags['visit_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllPatientVisit(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_visit"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class PatientAge(object):
    def __init__(self):
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addPatientAge(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO patient_age(visit_id,patient_age,date_of_record)VALUES('{}','{}','{}')".format(kwags['visit_id'],kwags['patient_age'],kwags['date_of_record'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getPatientAge(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_age WHERE visit_id='{}'".format(kwags['visit_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllPatientAge(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_age"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def removePatientAge(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_age WHERE visit_id='{}'".format(kwags['visit_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllPatientAge(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_age"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class PatientWeight(object):
    def __init__(self):
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addPatientWeight(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO patient_weight(visit_id,patient_weight,date_of_record)VALUES('{}','{}','{}')".format(kwags['visit_id'],kwags['patient_weight'],kwags['date_of_record'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getPatientWeight(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_weight WHERE visit_id='{}'".format(kwags['visit_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllPatientWeight(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_weight"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def removePatientWeight(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_weight WHERE visit_id='{}'".format(kwags['visit_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllPatientWeight(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_weight"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class PatientTemperature(object):
    def __init__(self):
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addPatientAge(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO patient_temperature(visit_id,patient_temperature,date_of_record)VALUES('{}','{}','{}')".format(kwags['visit_id'],kwags['patient_temperature'],kwags['date_of_record'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getPatientTemperature(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_temperature WHERE visit_id='{}'".format(kwags['visit_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllPatientTemperature(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_temperature"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def removePatientTemperature(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_temperature WHERE visit_id='{}'".format(kwags['visit_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllPatientTemperature(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_temperature"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class PatientVisitState(object):
    def __init__(self):
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addPatientVisitState(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO patient_visit_state(visit_id,patient_visits_state)VALUES('{}','{}')".format(kwags['visit_id'],kwags['patient_visit_state'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getPatientVisitState(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_visit_state WHERE visit_id='{}'".format(kwags['visit_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllPatientVisitState(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_visit_state"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def removePatientVisitState(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_visit_state WHERE visit_id='{}'".format(kwags['visit_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllPatientVisitState(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_visit_state"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class PatientStatus(object):
    def __init__(self,**kwags):
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addPatientStatus(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO patient_status(patient_id,patient_status,date_of_status)VALUES('{}','{}','{}')".format(kwags['patient_id'],kwags['patient_status'],kwags['date_of_status'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getPatientStatusByPatientId(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_status  WHERE patient_id='{}'".format(kwags['patient_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllPatientStatus(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_status"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def removePatientStatusByPatientId(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_status WHERE patient_id='{}'".format(kwags['patient_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removePatientStatusByVisitId(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_status WHERE visit_id='{}'".format(kwags['visit_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllPatientStatus(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_status"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class StaffDemographics(object):
    def __init__(self):
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addStaffDemographics(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO staff_demographics(staff_id,full_name,gender,marital_status,\
        dob,physical_address,date_of_employment,job_designation,phone_number,date_of_registration,\
        nationality,home_district,nid,appointment_id,photo)VALUES('{}','{}','{}','{}','{}','{}','{}',\
        '{}','{}','{}','{}','{}','{}','{}','{}')".format(kwags['staff_id'],kwags['full_name'],\
        kwags['gender'],kwags['marital_status'],kwags['dob'],kwags['physical_address'],\
        kwags['date_of_employment'],kwags['job_designation'],kwags['phone_number'],\
        kwags['date_of_registration'],kwags['nationality'],kwags['home_district'],kwags['nid'],\
        kwags['appointment_id'],kwags['photo'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getStaffDemographicsByStaffId(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM staff_demographics WHERE staff_id='{}'".format(kwags['staff_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getStaffDemographicsByMaritalStatu(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM staff_demographics WHERE marital_status='{}'".format(kwags['marital_status'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getStaffDemographicsByGender(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM staff_demographics WHERE gender='{}'".format(kwags['gender'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getStaffDemographicsByJobDesignation(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM staff_demographics WHERE job_designation='{}'".format(kwags['job_designation'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getStaffDemographicsByNID(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM staff_demographics WHERE nid='{}'".format(kwags['nid'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getStaffDemographicsByFullName(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM staff_demographics WHERE full_name='{}'".format(kwags['full_name'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getStaffDemographicsWhereFullNameBeginsWith(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM staff_demographics WHERE full_name='{}%'".format(kwags['full_name'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getStaffDemographicsWhereFullNameEndsWith(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM staff_demographics WHERE full_name='%{}'".format(kwags['full_name'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getStaffDemographicsWhereFullNameHas(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM staff_demographics WHERE full_name='%{}%'".format(kwags['full_name'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllStaffDemographics(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM staff_demographics"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def updateMaritalStatus(self,**kwags):
        cur=self.conn.cursor()
        sql="UPDATE staff_demographics SET marital_status='{}' WHERE staff_id='{}'".format(kwags['marital_status'],kwags['staff_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def updatePhysicalAddress(self,**kwags):
        cur=self.conn.cursor()
        sql="UPDATE staff_demographics SET physical_address='{}' WHERE staff_id='{}'".format(kwags['physical_address'],kwags['staff_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def updatePhoneNumber(self,**kwags):
        cur=self.conn.cursor()
        sql="UPDATE staff_demographics SET phone_number='{}' WHERE staff_id='{}'".format(kwags['phone_number'],kwags['staff_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeStaffDemographics(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM staff_demographics WHERE staff_id='{}'".format(kwags['staff_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllStaffDemographics(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM staff_demographics"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class Department(object):
    def __init__(self):
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addDepartment(self,**kwags):
        cur=self.db.cursor()
        sql="INSERT INTO department(department_id,department_name)VALUES('{}','{}')".format(kwags['department_id'],kwags['department_name'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getDepartment(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM department WHERE department_id='{}'".format(kwags['department_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllDepartment(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM department"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def updateDepartmentName(self,**kwags):
        cur=self.conn.cursor()
        sql="UPDATE department SET department_name='{}' WHERE department_id='{}'".format(kwags['department_name'],kwags['department_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeDepartment(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM department WHERE department_id='{}'".format(department_id)
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllDepartment(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM department"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class DepartmentHead(object):
    def __init__(self):
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addDepartmentHead(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO department_head(department_id,staff_id,date_of_assignment)VALUES('{}','{}','{}')".format(kwags['department_id'],kwags['staff_id'],kwags['date_of_assignment'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getDepartmentHeadByDepartmentId(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM department_head WHERE department_id'{}'".format(kwags['department_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getDepartmentHeadByStaffId(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM department_head WHERE staff_id'{}'".format(kwags['staff_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllDepartmentHead(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM department_head"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def removeDepartmentHead(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM department_head WHERE department_id='{}'".format(kwags['department_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        self.conn.commit()
    def removeAllDepartmentHead(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM department_head"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        self.conn.commit()
class CurrentDepartmentHead(object):
    def __init__(self):
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addCurrentDepartmentHead(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO current_department_head(department_id,staff_id,date_of_assignment)VALUES('{}','{}','{}')".format(kwags['department_id'],kwags['staff_id'],kwags['date_of_assignment'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getDepartmentHeadByDepartmentId(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM current_department_head WHERE department_id'{}'".format(kwags['department_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getCurrentDepartmentHeadByStaffId(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM current_department_head WHERE staff_id'{}'".format(kwags['staff_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllCurrentDepartmentHead(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM current_department_head"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def removeCurrentDepartmentHead(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM current_department_head WHERE department_id='{}'".format(kwags['department_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        self.conn.commit()
    def removeAllCurrentDepartmentHead(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM current_department_head"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        self.conn.commit()
class DepartmentStaffRel(object):
    def __init__(self):
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addDepartmentStaffRel(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO department_staff_rel(department_id,staff_id,date_of_assignment)VALUES('{}','{}','{}')".format(kwags['department_id'],kwags['staff_id'],kwags['date_of_assignment'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getDepartmentStaffRelByDepartmentId(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM department_staff_rel WHERE department_id'{}'".format(kwags['department_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getDepartmentStaffRelByStaffId(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM department_staff_rel WHERE staff_id='{}'".format(kwags['staff_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllDepartmentStaffRel(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM department_staff_rel"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def removeDepartmentStaffRel(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM department_staff_rel WHERE department_id='{}'".format(kwags['department_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        self.conn.commit()
    def removeAllDepartmentStaffRel(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM department_staff_rel"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        self.conn.commit()
class StaffMedicalDetail(object):
    def __init__(self):
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addStaffMedicalDetail(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO staff_medical_detail(staff_id,hiv_aids,blood_group,sickle_cells,asthma,other_complication)VALUES('{}','{}','{}','{}','{}','{}')".format(kwags['staff_id'],kwags['hiv_aids'],kwags['blood_group'],kwags['sickle_cells'],kwags['asthma'],kwags['other_complication'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getStaffMedicalDetail(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM staff_medical_detail WHERE staff_id='{}'".format(kwags['staff_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllStaffMedicalDetail(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM staff_medical_detail"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def updateOtherComplication(self,**kwags):
        cur=self.conn.cursor()
        sql="UPDATE staff_medical_detail SET other_complication='{}' WHERE staff_id='{}'".format(kwags['other_complication'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeStaffMedicalDetail(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM staff_medical_detail WHERE staff_id='{}'".format(kwags['staff_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllStaffMedicalDetail(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM staff_medical_detail"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class OutGoingCall(object):
    def __init__(self):
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addOutGoingCall(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO out_going_call(call_id,caller,reciever,time_of_call)VALUES('{}','{}','{}','{}')".format(kwags['call_id'],kwags['caller'],kwags['reciever'],kwags['time_of_call'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getOutGoingCallByCallId(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM out_going_call WHERE call_id='{}'".format(kwags['call_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getOutGoingCallByCaller(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM out_going_call WHERE caller='{}'".format(kwags['caller'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllOutGoingCall(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM out_going_call"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def removeOutGoingCallByCallId(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM out_going_call WHERE call_id='{}'".format(kwags['call_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeOutGoingCallByCaller(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM out_going_call WHERE caller='{}'".format(kwags['caller'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllOutGoingCall(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM out_going_call WHERE call_id='{}'".format(kwags['call_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class InComingCall(object):
    def __init__(self):
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addOutGoingCall(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO in_coming_call(call_id,caller,reciever,time_of_call)VALUES('{}','{}','{}','{}')".format(kwags['call_id'],kwags['caller'],kwags['reciever'],kwags['time_of_call'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getOutGoingCallByCallId(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM in_coming_call WHERE call_id='{}'".format(kwags['call_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getOutGoingCallByReciever(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM in_coming_call WHERE reciever='{}'".format(kwags['reciever'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllInComingCall(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM in_coming_call"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def removeInComingCallByCallId(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM in_coming_call WHERE call_id='{}'".format(kwags['call_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeInComingCallByReciever(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM in_coming_call WHERE reciever='{}'".format(kwags['reciever'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllInComingCall(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM in_coming_call WHERE reciever='{}'".format(kwags['reciever'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class Message(object):
    def __init__(self):
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addMessage(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO message(message_id,sender,reciever,message_subject,message_body,date_of_send,date_of_reception)VALUES('{}','{}','{}','{}','{}','{}','{}')".format(kwags['message_id'],kwags['sender'],kwags['reciever'],kwags['message_subject'],kwags['message_body'],kwag['date_of_send'],kwags['date_of_reception'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getMessageByMessageId(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM message WHERE message_id='{}'".format(kwags['message_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getMessageBySender(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM message WHERE sender='{}'".format(kwags['sender'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getMessageByReciever(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM message WHERE reciever='{}'".format(kwags['reciever'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllMessage(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM message"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def removeMessage(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM message WHERE message_id='{}'".format(kwags['message_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllMessage(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM message"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class MessageRecieverDeleteStatus(object):
    """docstring for MessageRecieverDeleteStatus."""
    def __init__(self):
        super(MessageRecieverDeleteStatus, self).__init__()
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addMessageRecieverDeleteStatus(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO message_reciever_delete_status(message_id,delete_status)VALUES('{}','{}')".format(kwags['message_id'],kwags['delete_status'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getMessageRecieverDeleteStatus(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM message_reciever_delete_status WHERE message_id='{}'".format(kwags['message_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllMessageRecieverDeleteStatus(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM message_reciever_delete_status"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def removeMessageRecieverDeleteStatus(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM message_reciever_delete_status WHERE message_id='{}'".format(kwags['message_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllMessageRecieverDeleteStatus(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM message_reciever_delete_status"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class MessageSenderDeleteStatus(object):
    """docstring for MessageSenderDeleteStatus."""
    def __init__(self):
        super(MessageSenderDeleteStatus, self).__init__()
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addMessageSenderDeleteStatus(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO message_sender_delete_status(message_id,delete_status)VALUES('{}','{}')".format(kwags['message_id'],kwags['delete_status'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getMessageSenderDeleteStatus(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM message_sender_delete_status WHERE message_id='{}'".format(kwags['message_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllMessageSenderDeleteStatus(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM message_sender_delete_status"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def removeMessageSenderDeleteStatus(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM message_sender_delete_status WHERE message_id='{}'".format(kwags['message_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllMessageSenderDeleteStatus(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM message_sender_delete_status"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class StaffQualification(object):
    """docstring for StaffQualification."""
    def __init__(self):
        super(StaffQualification, self).__init__()
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addStaffQualification(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO staff_qualification(staff_id,qualification_name,document_name,date_of_upload,qualification_note,qualification_id)VALUES('{}','{}','{}','{}','{}','{}')".format(kwags['staff_id'],kwags['qualification_name'],kwags['document_name'],kwags['date_of_upload'],kwags['qualification_note'],kwags['qualification_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getStaffQualificationByStaffId(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM staff_qualification WHERE staff_id='{}'".format(kwags['staff_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getStaffQualificationByQualificationId(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM staff_qualification WHERE qualification_id='{}'".format(kwags['qualification_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllStaffQualification(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM staff_qualification"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def updateQualificationName(self,**kwags):
        cur=self.conn.cursor()
        sql="UPDATE staff_qualification SET qualification_name='{}' WHERE qualification_id='{}'".format(kwags['qualification_name'],kwags['qualification_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def deleteStaffQualificationByStaffId(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM staff_qualification WHERE staff_id='{}'".format(kwags['staff_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def deleteStaffQualificationByQualificationId(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM staff_qualification WHERE qualification_id='{}'".format(kwags['qualification_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def deleteAllStaffQualification(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM staff_qualification"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class PatientCurrentStatus(object):
    """docstring for PatientCurrentStatus."""
    def __init__(self):
        super(PatientCurrentStatus, self).__init__()
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addPatientCurrentStatus(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO patient_current_status(patient_id,current_status)VALUES('{}','{}')".format(kwags['patient_id'],kwags['current_status'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getPatientCurrentStatus(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_current_status WHERE patient_id='{}'".format(kwags['patient_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllPatientCurrentStatus(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_current_status"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def updateCurrentStatus(self,**kwags):
        cur=self.conn.cursor()
        sql="UPDATE patient_current_status SET current_status='{}' WHERE patient_id='{}'".format(kwags['current_status'],kwags['patient_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removePatientCurrentStatus(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_current_status WHERE patient_id='{}'".format(kwags['patient_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllPatientCurrentStatus(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_current_status"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class Queue(object):
    """docstring for Queue."""
    def __init__(self):
        super(Queue, self).__init__()
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addQueue(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO queue(queue_id,staff_id,queue_type,date_of_creation,queue_size)VALUES('{}','{}','{}','{}','{}')".format(kwags['queue_id'],kwags['staff_id'],kwags['queue_type'],kwags['date_of_creation'],kwags['queue_size'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getQueueByQueueId(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM queue WHERE queue_id='{}'".format(kwags['queue_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getQueueByStaffId(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM queue WHERE staff_id='{}'".format(kwags['staff_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAlQueue(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM queue"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def updateQueueSize(self,**kwags):
        cur=self.conn.cursor()
        sql="UPDATE queue SET queue_size='{}' WHERE queue_id='{}'".format(kwags['queue_size'],kwags['queue_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeQueue(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM queue WHERE queue_id='{}'".format(kwags['queue_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllQueue(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM queue WHERE queue_id='{}'".format(kwags['queue_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class QueuePatientRel(object):
    """docstring for QueuePatientRel."""
    def __init__(self):
        super(QueuePatientRel, self).__init__()
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addQueuePatientRel(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO queue_patient_rel(queue_id,visit_id)VALUES('{}','{}')".format(kwags['queue_id'],kwags['visit_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getQueuePatientRelByQueueId(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM queue_patient_rel WHERE queue_id='{}'".format(kwags['queue_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getQueuePatientRelByVisitId(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM queue_patient_rel WHERE visit_id='{}'".format(kwags['visit_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllQueuePatientRel(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM queue_patient_rel"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def removeQueuePatientRelByQueueId(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM queue_patient_rel WHERE queue_id='{}'".format(kwags['queue_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeQueuePatientRelByVisitId(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM queue_patient_rel WHERE visit_id='{}'".format(kwags['visit_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllQueuePatientRel(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM queue_patient_rel"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class QueueStatus(object):
    """docstring for QueueStatus"""
    def __init__(self):
        super(QueueStatus, self).__init__()
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addQueueStatus(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO queue_status(queue_id,queue_status)VALUES('{}','{}')".format(kwags['queue_id'],kwags['queue_status'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getQueueStatus(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM queue_status WHERE queue_id='{}'".format(kwags['queue_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllQueueStatus(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM queue_status"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def updateQueueStatus(self,**kwags):
        cur=self.conn.cursor()
        sql="UPDATE queue_status SET queue_status='{}' WHERE queue_id='{}'".format(kwags['queue_status'],kwags['queue_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeQueueStatus(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM queue_status WHERE queue_id='{}'".format(kwags['queue_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllQueueStatus(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM queue_status"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class StaffLeaveStatus(object):
    """docstring for StaffLeaveStatus."""
    def __init__(self):
        super(StaffLeaveStatus, self).__init__()
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addStaffLeaveStatus(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO staff_leave_status(staff_id,staff_leave_status,leave_status_date)VALUES('{}','{}','{}')".format(kwags['staff_id'],kwags['staff_leave_status'],kwags['leave_status_date'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getStaffLeaveStatus(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM staff_leave_status WHERE staff_id='{}'".format(kwags['staff_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllStaffLeaveStatus(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM staff_leave_status"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def updateStaffLeaveStatus(self,**kwags):
        cur=self.conn.cursor()
        sql="UPDATE staff_leave_status SET staff_leave_status='{}' WHERE staff_id='{}'".format(kwags['staff_leave_status'],kwags['staff_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeStaffLeaveStatus(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM staff_leave_status WHERE staff_id='{}'".format(kwags['staff_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllStaffLeaveStatus(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM staff_leave_status"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class StaffLeaveApplication(object):
    """docstring for StaffLeaveApplication."""
    def __init__(self):
        super(StaffLeaveApplication, self).__init__()
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addStaffLeaveApplication(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO staff_leave_application(leave_id,staff_id,application_date,leave_reason)VALUES('{}','{}','{}','{}')".format(kwags['leave_id'],kwags['staff_id'],kwags['application_date'],kwags['leave_reason'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getStaffLeaveApplicationByLeaveId(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM staff_leave_application WHERE leave_id='{}'".format(kwags['leave_id'])
        cur.execute(sql)
        out=cur,fetchall()
        cur.close()
        return out
    def getStaffLeaveApplicationByStaffId(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM staff_leave_application WHERE staff_id='{}'".format(kwags['staff_id'])
        cur.execute(sql)
        out=cur,fetchall()
        cur.close()
        return out
    def getAllStaffLeaveApplication(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM staff_leave_application"
        cur.execute(sql)
        out=cur,fetchall()
        cur.close()
        return out
    def updateLeaveReason(self,**kwags):
        cur=self.conn.cursor()
        sql="UPDATE staff_leave_application SET leave_reason='{}' WHERE leave_id='{}'".format(kwags['leave_reason'],kwags['leave_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeStaffLeaveApplicationByLeaveId(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM staff_leave_application WHERE leave_id='{}'".format(kwags['leave_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeStaffLeaveApplicationStaffId(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM staff_leave_application WHERE staff_id='{}'".format(kwags['staff_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllStaffLeaveApplication(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM staff_leave_application"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class LeaveForward(object):
    """docstring for LeaveForward."""
    def __init__(self):
        super(LeaveForward, self).__init__()
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addLeaveForward(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO leave_forward(leave_id,staff_id,forward_state,forward_reason,forward_date)VALUES('{}','{}','{}','{}','{}')".format(kwags['leave_id'],kwags['staff_id'],kwags['forward_state'],kwags['forward_reason'],kwags['forward_date'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getLeaveForwardByLeaveId(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM leave_forward WHERE leave_id='{}'".format(kwags['leave_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getLeaveForwardByStaffId(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM leave_forward WHERE staff_id='{}'".format(kwags['staff_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllLeaveForward(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM leave_forward"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def updateForwardReason(self,**kwags):
        cur=self.conn.cursor()
        sql="UPDATE leave_forward SET forward_reason='{}' WHEE leave_id='{}'".format(kwags['forward_reason'],kwags['leave_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeLeaveForwardByLeaveId(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM leave_forward WHERE leave_id='{}'".format(kwags['leave_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeLeaveForwardByStaffId(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM leave_forward WHERE staff_id='{}'".format(kwags['staff_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllLeaveForward(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM leave_forward"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class AcceptedLeaveDetail(object):
    """docstring for AcceptedLeaveDetail."""
    def __init__(self):
        super(AcceptedLeaveDetail, self).__init__()
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addAcceptedLeaveDetail(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO accepted_leave_detail(leave_id,on_set_date,off_set_date,leave_state,date_of_acceptance)VALUES('{}','{}','{}','{}','{}')".format(kwags['leave_id'],kwags['on_set_date'],kwags['off_set_date'],kwags['leave_state'],kwags['date_of_acceptance'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getAcceptedLeaveDetail(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM accepted_leave_detail WHERE leave_id='{}'".format(kwags['leave_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllAcceptedLeaveDetail(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM accepted_leave_detail"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def updateOnSetDate(self,**kwags):
        cur=self.conn.cursor()
        sql="UPDATE accepted_leave_detail SET on_set_date='{}'".format(kwags['on_set_date'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def updateOffSetDate(self,**kwags):
        cur=self.conn.cursor()
        sql="UPDATE accepted_leave_detail SET off_set_date='{}'".format(kwags['off_set_date'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAcceptedLeaveDetail(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM accepted_leave_detail WHERE leave_id='{}'".format(kwags['leave_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllAcceptedLeaveDetail(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM accepted_leave_detail"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class RejectedLeaveDetail(object):
    """docstring for RejectedLeaveDetail."""
    def __init__(self):
        super(RejectedLeaveDetail, self).__init__()
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addRejectedLeaveDetail(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO rejected_leave_detail(leave_id,rejection_reason,date_of_reject)VALUES('{}','{}','{}')".format(kwags['leave_id'],kwags['rejection_reason'],kwags['date_of_reject'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getRejectedLeaveDetail(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM rejected_leave_detail WHERE leave_id='{}'".format(kwags['leave_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllRejectedLeaveDetail(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM rejected_leave_detail"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def updateRejectionReason(self,**kwags):
        cur=self.conn.cursor()
        sql="UPDATE rejected_leave_detail SET rejection_reason='{}' WHERE leave_id='{}'".format(kwags['rejection_reason'],kwags['leave_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeRejectedLeaveDetail(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM rejected_leave_detail WHERE leave_id='{}'".format(kwags['leave_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllRejectedLeaveDetail(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM rejected_leave_detail"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class PatientAllergy(object):
    """docstring for PatientAllergy."""
    def __init__(self):
        super(PatientAllergy, self).__init__()
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addPatientAllergy(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO patient_allergy(patient_id,allergy_name,allergy_description,date_of_record,allergy_id)VALUES('{}','{}','{}','{}','{}')".format(kwags['patient_id'],kwags['allergy_name'],kwags['allergy_description'],kwags['date_of_record'],kwags['allergy_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getPatientAllergyByPatientId(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_allergy WHERE patient_id='{}'".format(kwags['patient_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getPatientAllergyByAllergyId(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_allergy WHERE allergy_id='{}'".format(kwags['allergy_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllPatientAllergy(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_allergy"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def updateAllergyName(self,**kwags):
        cur=self.conn.cursor()
        sql="UPDATE patient_allergy SET allergy_name='{}' WHERE allergy_id='{}'".format(kwags['allergy_name'],kwags['allergy_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def updateAllergyDescription(self,**kwags):
        cur=self.conn.cursor()
        sql="UPDATE patient_allergy SET allergy_description='{}' WHERE allergy_id='{}'".format(kwags['allergy_description'],kwags['allergy_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removePatientAllergyByAllergyId(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_allergy WHERE allergy_id='{}'".format(kwags['allergy_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removePatientAllergybyPatientId(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_allergy WHERE patient_id='{}'".format(kwags['patient_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllPatientAllergy(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_allergy"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class PatientTriageDetail(object):
    """docstring for PatientTriageDetail."""
    def __init__(self):
        super(PatientTriageDetail, self).__init__()
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addPatientTriageDetail(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO patient_triage_detail(visit_id,patient_complaint,earlier_medication,other_physician)VALUES('{}','{}','{}','{}')".format(kwags['visit_id'],kwags['patient_complaint'],kwags['earlier_medication'],kwags['other_physician'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getPatientTriageDetail(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_triage_detail WHERE visit_id='{}'".format(kwags['visit_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllPatientTriageDetail(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_triage_detail"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def updatePatientCompliant(self,**kwags):
        cur=self.conn.cursor()
        sql="UPDATE patient_triage_detail SET patient_complaint='{}' WHERE visit_id='{}'".format(kwags['patient_complaint'],kwags['visit_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def updateEarlierMedication(self,**kwags):
        cur=self.conn.cursor()
        sql="UPDATE patient_triage_detail SET earlier_medication='{}' WHERE visit_id='{}'".format(kwags['earlier_medication'],kwags['visit_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def updateOtherPhysician(self,**kwags):
        cur=self.conn.cursor()
        sql="UPDATE patient_triage_detail SET other_physician='{}' WHERE visit_id='{}'".format(kwags['other_physician'],kwags['visit_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removePatientTriageDetail(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_triage_detail WHERE visit_id='{}'".format(kwags['visit_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removePatientTriageDetail(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_triage_detail WHERE visit_id='{}'".format(kwags['visit_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class PatientLNMP(object):
    """docstring for PatientLNMP."""
    def __init__(self):
        super(PatientLNMP, self).__init__()
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addPatientLNMP(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO patient_lnmp(visit_id,lnmp,date_of_record)VALUES('{}','{}','{}')".format(kwags['visit_id'],kwags['lnmp'],kwags['date_of_record'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getPatientLNMP(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_lnmp WHERE visit_id='{}'".format(kwags['visit_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllPatientLNMP(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_lnmp"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def updateLNMP(self,**kwags):
        cur=self.conn.cursor()
        sql="UPDATE patient_lnmp SET lnmp='{}' WHERE visit_id='{}'".format(kwags['lnmp'],kwags['visit_id'])
        cur.execute(sql)
        cur,close()
        self.conn.commit()
    def removePaientLNMP(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_lnmp WHERE visit_id='{}'".format(kwags['visit_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllPaientLNMP(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_lnmp"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class PatientMedicalDetail(object):
    """docstring for PatientMedicalDetail."""
    def __init__(self):
        super(PatientMedicalDetail, self).__init__()
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addPatientMedicalDetail(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO patient_medical_detail(patient_id,hiv_aids,blood_group,sickle_cells,asthma,other_complication)VALUES('{}','{}','{}','{}','{}','{}')".format(kwags['patient_id'],kwags['hiv_aids'],kwags['blood_group'],kwags['sickle_cells'],kwags['asthma'],kwags['other_complication'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getPatientMedicalDetail(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_medical_detail WHERE patient_id='{}'".format(kwags['patient_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllPatientMedicalDetail(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_medical_detail"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def updateHIVAIDS(self,**kwags):
        cur=self.conn.cursor()
        sql="UPDATE patient_medical_detail SET hiv_aids='{}' WHERE patient_id='{}'".format(kwags['hiv_aids'],kwags['patient_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def updateBloodGroup(self,**kwags):
        cur=self.conn.cursor()
        sql="UPDATE patient_medical_detail SET blood_group='{}' WHERE patient_id='{}'".format(kwags['blood_group'],kwags['patient_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def updateSickleCells(self,**kwags):
        cur=self.conn.cursor()
        sql="UPDATE patient_medical_detail SET sickle_cells='{}' WHERE patient_id='{}'".format(kwags['sickle_cells'],kwags['patient_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def updateAsthma(self,**kwags):
        cur=self.conn.cursor()
        sql="UPDATE patient_medical_detail SET asthma='{}' WHERE patient_id='{}'".format(kwags['asthma'],kwags['patient_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def updateOtherComplication(self,**kwags):
        cur=self.conn.cursor()
        sql="UPDATE patient_medical_detail SET other_complication='{}' WHERE patient_id='{}'".format(kwags['other_complication'],kwags['patient_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removePatientmedicalDetail(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_medical_detail WHERE patient_id='{}'".format(kwags['patient_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllPatientmedicalDetail(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_medical_detail"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class Users(object):
    """docstring for Users."""
    def __init__(self):
        super(Users, self).__init__()
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addUsers(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO users(username,password_,date_of_creation,user_type,password_state)VALUES('{}','{}','{}','{}','{}')".format(kwags['username'],kwags['password_'],kwags['date_of_creation'],kwags['user_type'],kwags['password_state'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getUsers(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM users WHERE username='{}'".format(kwags['username'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getUsersByUserType(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM users WHERE user_type='{}'".format(kwags['user_type'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllUsers(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM users"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def updateUsername(self,**kwags):
        cur=self.conn.cursor()
        sql="UPDATE users SET username='{}' WHERE username='{}'".format(kwags['usernameNew'],kwags['usernameOld'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def updatePassword_(self,**kwags):
        cur=self.conn.cursor()
        sql="UPDATE users SET password_='{}' WHERE username='{}'".format(kwags['password_'],kwags['usernameOld'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def updateUserType(self,**kwags):
        cur=self.conn.cursor()
        sql="UPDATE users SET user_type='{}' WHERE username='{}'".format(kwags['user_type'],kwags['usernameOld'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeUsers(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM users WHERE username='{}'".format(kwags['username'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllUsers(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM users"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class HospitalDetail(object):
    """docstring for HospitalDetails."""
    def __init__(self):
        super(HospitalDetail, self).__init__()
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addHospitalDetail(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO hospital_detail(hospital_name,hospital_physical_address,hospital_registration_no,license_no,date_of_business_onset,date_of_creation,hospital_logo,hospital_email,hospital_tel,hospital_box_no)VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(kwags['hospital_name'],kwags['hospital_physical_address'],kwags['hospital_registration_no'],kwags['license_no'],kwags['date_of_business_onset'],kwags['date_of_creation'],kwags['hospital_logo'],kwags['hospital_email'],kwags['hospital_tel'],kwags['hospital_box_no'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getHospitalDetail(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM hospital_detail"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def updateHospitalName(self,**kwags):
        cur=self.conn.cursor()
        sql="UPDATE hospital_detail SET hospital_name='{}'".format(kwags['hospital_name'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def updateHospitalPhysicalAddress(self,**kwags):
        cur=self.conn.cursor()
        sql="UPDATE hospital_detail SET hospital_physical_address='{}'".format(kwags['hospital_physical_address'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def updateHospitalRegistrationNo(self,**kwags):
        cur=self.conn.cursor()
        sql="UPDATE hospital_detail SET hospital_registration_no='{}'".format(kwags['hospital_registration_no'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def updateLicenceNo(self,**kwags):
        cur=self.conn.cursor()
        sql="UPDATE hospital_detail SET license_no='{}'".format(kwags['license_no'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def updateDateOfBusinessOnset(self,**kwags):
        cur=self.conn.cursor()
        sql="UPDATE hospital_detail SET date_of_business_onset='{}'".format(kwags['date_of_business_onset'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def updateHospitalEmail(self,**kwags):
        cur=self.conn.cursor()
        sql="UPDATE hospital_detail SET hospital_email='{}'".format(kwags['hospital_email'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def updateHospitalTel(self,**kwags):
        cur=self.conn.cursor()
        sql="UPDATE hospital_detail SET hospital_tel='{}'".format(kwags['hospital_tel'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def updateHospitalBoxNo(self,**kwags):
        cur=self.conn.cursor()
        sql="UPDATE hospital_detail SET hospital_box_no='{}'".format(kwags['hospital_box_no'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeHospitalDetail(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM hospital_detail"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class StaffPhoto(object):
    """docstring for StaffPhoto."""
    def __init__(self):
        super(StaffPhoto, self).__init__()
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addStaffPhoto(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO staff_photo(staff_id,photo,date_of_creation)VALUES('{}','{}','{}')".format(kwags['staff_id'],kwags['photo'],kwags['date_of_creation'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getStaffPhoto(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM staff_photo WHERE staff_id='{}'".format(kwags['staff_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getStaffPhotoByPhoto(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM staff_photo WHERE photo='{}'".format(kwags['photo'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllStaffPhoto(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM staff_photo"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def removeStaffPhotoByStaffId(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM staff_photo WHERE staff_id='{}'".format(kwags['staff_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeStaffPhotoByPhoto(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM staff_photo WHERE photo='{}'".format(kwags['photo'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllStaffPhoto(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM staff_photo"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class PatientPhoto(object):
    """docstring for PatientPhoto."""
    def __init__(self):
        super(StaffPhoto, self).__init__()
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addPatientPhoto(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO patient_photo(patient_id,photo,date_of_creation)VALUES('{}','{}','{}')".format(kwags['patient_id'],kwags['photo'],kwags['date_of_creation'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getPatientPhoto(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_photo WHERE patient_id='{}'".format(kwags['patient_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllPatientPhoto(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_photo"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def removePatientPhotoByPatientId(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_photo WHERE patient_id='{}'".format(kwags['patient_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removePatientPhotoByPhoto(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_photo WHERE photo='{}'".format(kwags['photo'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllPatientPhoto(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_photo"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class UserLogState(object):
    """docstring for UserLogState."""
    def __init__(self):
        super(UserLogState, self).__init__()
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addUserLogState(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO user_log_state(username,log_state,date_of_state)VALUES('{}','{}','{}')".format(kwags['username'],kwags['log_state'],kwags['date_of_state'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getUserLogState(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM user_log_state WHERE username='{}'".format(kwags['username'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllUserLogState(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM user_log_state"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def updateLogState(self,**kwags):
        cur=self.conn.cursor()
        sql="UPDATE user_log_state SET log_state='{}' WHERE username='{}'".format(kwags['log_state'],kwags['username'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def updateDateOfState(self,**kwags):
        cur=self.conn.cursor()
        sql="UPDATE user_log_state SET date_of_state='{}' WHERE username='{}'".format(kwags['date_of_state'],kwags['username'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeUserLogState(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM user_log_state WHERE username='{}'".format(kwags['username'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllUserLogState(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM user_log_state"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class StaffDemographicsUsersRel(object):
    """docstring for StaffDemographicsUsersRel."""
    def __init__(self):
        super(StaffDemographicsUsersRel, self).__init__()
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addStaffDemographicsUsersRel(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO staff_demographics_users_rel(staff_id,username)VALUES('{}','{}')".format(kwags['staff_id'],kwags['username'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getStaffDemographicsUsersRelByStaffId(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM staff_demographics_users_rel WHERE staff_id='{}'".format(kwags['staff_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getStaffDemographicsUsersRelByUsername(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM staff_demographics_users_rel WHERE username='{}'".format(kwags['username'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllStaffDemographicsUsersRel(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM staff_demographics_users_rel"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def removeStaffDemographicsUsersRelByStaffId(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM staff_demographics_users_rel WHERE staff_id='{}'".format(kwags['staff_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeStaffDemographicsUsersRelByUsername(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM staff_demographics_users_rel WHERE username='{}'".format(kwags['username'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllStaffDemographicsUsersRel(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM staff_demographics_users_rel WHERE staff_id='{}'".format(kwags['staff_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class StaffState(object):
    """docstring for StaffState."""
    def __init__(self):
        super(StaffState, self).__init__()
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addStaffState(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO staff_state(staff_id,staff_state,state_description, date_of_onset)VALUES('{}','{}','{}','{}')".format(kwags['staff_id'],kwags['staff_state'],kwags['state_description'],kwags['date_of_onset'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getStaffState(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM staff_state WHERE staff_id='{}'".format(kwags['staff_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllStaffState(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM staff_state WHERE staff_id='{}'".format(kwags['staff_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def updateStaffState(self,**kwags):
        cur=self.conn.cursor()
        sql="UPDATE staff_state SET staff_state='{}' WHERE staff_id='{}'".format(kwags['staff_state'],kwags['staff_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def updateStateDescription(self,**kwags):
        cur=self.conn.cursor()
        sql="UPDATE staff_state SET state_description='{}' WHERE staff_id='{}'".format(kwags['state_description'],kwags['staff_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def updateDateOfOnset(self,**kwags):
        cur=self.conn.cursor()
        sql="UPDATE staff_state SET date_of_onset='{}' WHERE staff_id='{}'".format(kwags['date_of_onset'],kwags['staff_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeStaffState(self,**kwags):
        cur=self.conn.commit()
        sql="DELETE  FROM staff_state WHERE staff_id='{}'".format(kwags['staff_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllStaffState(self,**kwags):
        cur=self.conn.commit()
        sql="DELETE  FROM staff_state WHERE staff_id='{}'".format(kwags['staff_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class StaffAccountState(object):
    """docstring for StaffAccountState."""
    def __init__(self):
        super(StaffAccountState, self).__init__()
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addStaffAccountState(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO staff_account_state(staff_id,account_state,date_of_state)VALUES('{}','{}','{}')".format(kwags['staff_id'],kwags['account_state'],kwags['date_of_state'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getStaffAccountState(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM staff_account_state WHERE staff_id='{}'".format(kwags['staff_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllStaffAccountState(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM staff_account_state"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def removeStaffAccountState(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM staff_account_state WHERE staff_id='{}'".format(kwags['staff_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllStaffAccountState(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM staff_account_state"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class StaffCurrentAccountState(object):
    """docstring for StaffAccountState."""
    def __init__(self):
        super(StaffCurrentAccountState, self).__init__()
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addStaffCurrentAccountState(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO staff_current_account_state(staff_id,account_state,date_of_state)VALUES('{}','{}','{}')".format(kwags['staff_id'],kwags['account_state'],kwags['date_of_state'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getStaffCurrentAccountState(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM staff_current_account_state WHERE staff_id='{}'".format(kwags['staff_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllStaffCurrentAccountState(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM staff_current_account_state"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def updateStaffCurrentAccountState(self,**kwags):
        cur=self.conn.cursor()
        sql="UPDATE staff_current_account_state SET account_state='{}' WHERE staff_id='{}'".format(kwags['account_state'],kwags['staff_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeStaffCurrentAccountState(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM staff_current_account_state WHERE staff_id='{}'".format(kwags['staff_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllStaffCurrentAccountState(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM staff_current_account_state"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class PatientVisitStaffRel(object):
    """docstring for PatientVisitStaffRel."""
    def __init__(self):
        super(PatientVisitStaffRel, self).__init__()
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addPatientVisitStaffRel(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO patient_visit_staff_rel(visit_id,staff_id)VALUES('{}','{}')".format(kwags['visit_id'],kwags['staff_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getPatientVisitStaffRelByVisitId(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_visit_staff_rel WHERE visit_id='{}'".format(kwags['visit_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getPatientVisitStaffRelByStaffId(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_visit_staff_rel WHERE staff_id='{}'".format(kwags['staff_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllPatientVisitStaffRel(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_visit_staff_rel"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def removePatientVisitStaffRelByVisitId(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_visit_staff_rel WHERE visit_id='{}'".format(kwags['visit_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removePatientVisitStaffRelByStaffId(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_visit_staff_rel WHERE staff_id='{}'".format(kwags['staff_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllPatientVisitStaffRel(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_visit_staff_rel"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class PatientDemographicsStaffRel(object):
    """docstring for PatientVisitStaffRel."""
    def __init__(self):
        super(PatientDemographicsStaffRel, self).__init__()
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addPatientDemographicsStaffRel(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO patient_demographics_staff_rel(patient_id,staff_id)VALUES('{}','{}')".format(kwags['patient_id'],kwags['staff_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getPatientDemographicsStaffRelByPatientId(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_demographics_staff_rel WHERE patient_id='{}'".format(kwags['patient_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getPatientDemographicsStaffRelByStaffId(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_demographics_staff_rel WHERE staff_id='{}'".format(kwags['staff_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllPatientDemographicsStaffRel(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_demographics_staff_rel"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def removePatientDemographicsStaffRelByPatientId(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_demographics_staff_rel WHERE patient_id='{}'".format(kwags['patient_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removePatientDemographicsStaffRelByStaffId(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_demographics_staff_rel WHERE staff_id='{}'".format(kwags['staff_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllPatientDemographicsStaffRel(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_demographics_staff_rel"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class PatientSystemReview(object):
    """docstring for PatientSystemReview."""
    def __init__(self):
        super(PatientSystemReview, self).__init__()
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addPatientSystemReview(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO patient_system_review(visit_id,review_category,review_name,review_detail,date_of_record)VALUES('{}','{}','{}','{}','{}')".format(kwags['visit_id'],kwags['review_category'],kwags['review_name'],kwags['review_detail'],kwags['date_of_record'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getPatientSystemReview(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_system_review WHERE visit_id='{}'".format(kwags['visit_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllPatientSystemReview(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_system_review"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def removePatientSystemReview(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_system_review WHERE visit_id='{}'".format(kwags['visit_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllPatientSystemReview(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_system_review"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class PatientPreviousMedication(object):
    """docstring for PatientPreviousMedication."""
    def __init__(self):
        super(PatientPreviousMedication, self).__init__()
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addPatientPreviousMedication(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO patient_previous_medication(patient_id,visit_id,medicine,dose,date_of_medication_onset,date_of_medication_offset,date_of_record)VALUES('{}','{}','{}','{}','{}','{}','{}')".format(kwags['patient_id'],kwags['visit_id'],kwags['medicine'],kwags['dose'],kwags['date_of_medication_onset'],kwags['date_of_medication_offset'],kwags['date_of_record'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getPatientPreviousMedicationByPatientId(self,**kwags):
        cur=self.conn.commit()
        sql="SELECT * FROM patient_previous_medication WHERE patient_id='{}'".format(kwags['patient_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getPatientPreviousMedicationByVisitId(self,**kwags):
        cur=self.conn.commit()
        sql="SELECT * FROM patient_previous_medication WHERE visit_id='{}'".format(kwags['visit_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllPatientPreviousMedication(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_previous_medication"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def removePatientPreviousMedicationByPatientId(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_previous_medication WHERE patient_id='{}'".format(kwags['patient_id'])
        cur.execute(sql)
        cur.close
        self.conn.commit()
    def removePatientPreviousMedicationByVisitId(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_previous_medication WHERE visit_id='{}'".format(kwags['visit_id'])
        cur.execute(sql)
        cur.close
        self.conn.commit()
    def removeAllPatientPreviousMedication(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_previous_medication"
        cur.execute(sql)
        cur.close
        self.conn.commit()
class PatientCurrentSystemReview(object):
    """docstring for PatientCurrentSystemReview."""
    def __init__(self):
        super(PatientCurrentSystemReview, self).__init__()
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addPatientCurrentSystemReview(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO patient_current_system_review(visit_id,review_category,review_name,review_detail,date_of_record)VALUES('{}','{}','{}','{}','{}')".format(kwags['visit_id'],kwags['review_category'],kwags['review_name'],kwags['review_detail'],kwags['date_of_record'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getPatientCurrentSystemReview(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_current_system_review WHERE visit_id='{}'".format(kwags['visit_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllPatientCurrentSystemReview(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_current_system_review"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def removePatientCurrentSystemReview(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_current_system_review WHERE visit_id='{}'".format(kwags['visit_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllPatientCurrentSystemReview(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_current_system_review"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class PatientLaboratoryHistory(object):
    """docstring for PatientLaboratoryHistory."""
    def __init__(self):
        super(PatientLaboratoryHistory, self).__init__()
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addPatientLaboratoryHistory(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO patient_laboratory_history(patient_id,visit_id,test_name,test_detail,date_of_record)VALUES('{}','{}','{}','{}','{}')".format(kwags['patient_id'],kwags['visit_id'],kwags['test_name'],kwags['test_detail'],kwags['date_of_record'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getPatientLaboratoryHistoryByPatientId(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_laboratory_history WHERE patient_id='{}'".format(kwags['patient_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getPatientLaboratoryHistoryByVisitId(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_laboratory_history WHERE visit_id='{}'".format(kwags['visit_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllPatientLaboratoryHistory(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_laboratory_history"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def removePatientLaboratoryHistoryByPatientId(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_laboratory_history WHERE patient_id='{}'".format(kwags['patient_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removePatientLaboratoryHistoryByVisitId(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_laboratory_history WHERE visit_id='{}'".format(kwags['visit_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllPatientLaboratoryHistory(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_laboratory_history"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class PatientCurrentLaboratoryHistory(object):
    """docstring for PatientCurrentLaboratoryHistory."""
    def __init__(self):
        super(PatientCurrentLaboratoryHistory, self).__init__()
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addPatientCurrentLaboratoryHistory(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO patient_current_laboratory_history(patient_id,visit_id,test_name,test_detail,date_of_record)VALUES('{}','{}','{}','{}','{}')".format(kwags['patient_id'],kwags['visit_id'],kwags['test_name'],kwags['test_detail'],kwags['date_of_record'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getPatientCurrentLaboratoryHistoryByPatientId(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_current_laboratory_history WHERE patient_id='{}'".format(kwags['patient_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getPatientCurrentLaboratoryHistoryByVisitId(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_current_laboratory_history WHERE visit_id='{}'".format(kwags['visit_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllPatientCurrentLaboratoryHistory(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_current_laboratory_history"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def removePatientCurrentLaboratoryHistoryByPatientId(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_current_laboratory_history WHERE patient_id='{}'".format(kwags['patient_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removePatientCurrentLaboratoryHistoryByVisitId(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_current_laboratory_history WHERE visit_id='{}'".format(kwags['visit_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllPatientCurrentLaboratoryHistory(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_current_laboratory_history"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class PatientOtherPhysicianDetail(object):
    """docstring for PatientOtherPhysicianDetail."""
    def __init__(self):
        super(PatientOtherPhysicianDetail, self).__init__()
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addPatientOtherPhysicianDetail(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO patient_other_physician_detail(patient_id,visit_id,physician_fullname,physical_address,mobile_phone_number,email_address,date_of_record)VALUES('{}','{}','{}','{}','{}','{}','{}')".format(kwags['patient_id'],kwags['visit_id'],kwags['physician_fullname'],kwags['physical_address'],kwags['mobile_phone_number'],kwags['email_address'],kwags['date_of_record'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getPatientOtherPhysicianDetailByPatientId(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_other_physician_detail WHERE patient_id='{}'".format(kwags['patient_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getPatientOtherPhysicianDetailByVisitId(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_other_physician_detail WHERE visit_id='{}'".format(kwags['visit_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllPatientOtherPhysicianDetail(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_other_physician_detail"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def removePatientOtherPhysicianDetailByPatientId(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_other_physician_detail WHERE patient_id='{}'".format(kwags['patient_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removePatientOtherPhysicianDetailByVisitId(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_other_physician_detail WHERE visit_id='{}'".format(kwags['visit_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removePatientOtherPhysicianDetail(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_laboratory_history"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class PatientMedicalInsuranceInfo(object):
    """docstring for PatientMedicalInsuranceInfo."""
    def __init__(self):
        super(PatientMedicalInsuranceInfo, self).__init__()
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addPatientMedicalInsuranceInfo(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO patient_medical_insurance_info(patient_id,visit_id,insurance_company_name,insurance_state,date_of_record)VALUES('{}','{}','{}','{}','{}')".format(kwags['patient_id'],kwags['visit_id'],kwags['insurance_company_name'],kwags['insurance_state'],kwags['date_of_record'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getPatientMedicalInsuranceInfoByPatientId(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_medical_insurance_info WHERE patient_id='{}'".format(kwags['patient_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getPatientMedicalInsuranceInfoByVisitId(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_medical_insurance_info WHERE visit_id='{}'".format(kwags['visit_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllPatientMedicalInsuranceInfo(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_medical_insurance_info"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def removePatientMedicalInsuranceInfoByPatientId(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_medical_insurance_info WHERE patient_id='{}'".format(kwags['patient_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removePatientMedicalInsuranceInfoByVisitId(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_medical_insurance_info WHERE visit_id='{}'".format(kwags['visit_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removePatientMedicalInsuranceInfo(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_medical_insurance_info"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class PatientCurrentMedicalInsuranceInfo(object):
    """docstring for PatientCurrentMedicalInsuranceInfo."""
    def __init__(self):
        super(PatientCurrentMedicalInsuranceInfo, self).__init__()
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addPatientCurrentMedicalInsuranceInfo(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO patient_current_medical_insurance_info(patient_id,visit_id,insurance_company_name,insurance_state,date_of_record)VALUES('{}','{}','{}','{}','{}')".format(kwags['patient_id'],kwags['visit_id'],kwags['insurance_company_name'],kwags['insurance_state'],kwags['date_of_record'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getPatientCurrentMedicalInsuranceInfoByPatientId(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_current_medical_insurance_info WHERE patient_id='{}'".format(kwags['patient_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getPatientCurrentMedicalInsuranceInfoByVisitId(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_current_medical_insurance_info WHERE visit_id='{}'".format(kwags['visit_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllPatientCurrentMedicalInsuranceInfo(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_current_medical_insurance_info"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def removePatientCurrentMedicalInsuranceInfoByPatientId(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_current_medical_insurance_info WHERE patient_id='{}'".format(kwags['patient_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removePatientCurrentMedicalInsuranceInfoByVisitId(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_current_medical_insurance_info WHERE visit_id='{}'".format(kwags['visit_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removePatientCurrentMedicalInsuranceInfo(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_current_medical_insurance_info"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class PatientCurrentAge(object):
    """docstring for PatientCurrentAge."""
    def __init__(self):
        super(PatientCurrentAge, self).__init__()
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addPatientCurrentAge(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO patient_current_age(visit_id,age,date_of_record)VALUES('{}','{}','{}')".format(kwags['visit_id'],kwags['age'],kwags['date_of_record'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getPatientCurrentAge(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_current_age WHERE visit_id='{}'".format(kwags['visit_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllPatientCurrentAge(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_current_age "
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def removePatientCurrentAge(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_current_age WHERE visit_id='{}'".format(kwags['visit_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllPatientCurrentAge(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_current_age"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class PatientCurrentWeight(object):
    """docstring for PatientCurrentWeight."""
    def __init__(self):
        super(PatientCurrentWeight, self).__init__()
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addPatientCurrentWeight(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO patient_current_weight(visit_id,patient_weight,date_of_record)VALUES('{}','{}','{}')".format(kwags['visit_id'],kwags['patient_weight'],kwags['date_of_record'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getPatientCurrentWeight(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_current_weight WHERE visit_id='{}'".format(kwags['visit_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllPatientCurrentWeight(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_current_weight"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def removePatientCurrentWeight(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_current_weight WHERE visit_id='{}'".format(kwags['visit_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllPatientCurrentWeight(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_current_weight"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class PatientCurrentTemperature(object):
    """docstring for PatientCurrentTemperature."""
    def __init__(self):
        super(PatientCurrentTemperature, self).__init__()
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addPatientCurrentTemperature(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO patient_current_temperature(visit_id,patient_temperature,date_of_record)VALUES('{}','{}','{}')".format(kwags['visit_id'],kwags['patient_temperature'],kwags['date_of_record'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getPatientCurrentTemperature(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_current_temperature WHERE visit_id='{}'".format(kwags['visit_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllPatientCurrentTemperature(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_current_temperature"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def removePatientCurrentTemperature(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_current_temperature WHERE visit_id='{}'".format(kwags['visit_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllPatientCurrentTemperature(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_current_temperature"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class PatientCurrentBloodPressure(object):
    """docstring for PatientCurrentBloodPressure."""
    def __init__(self):
        super(PatientCurrentBloodPressure, self).__init__()
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addPatientCurrentBloodPressure(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO patient_current_blood_pressure(visit_id,patient_blood_pressure,date_of_record)VALUES('{}','{}','{}')".format(kwags['visit_id'],kwags['patient_blood_pressure'],kwags['date_of_record'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getPatientCurrentBloodPressure(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_current_blood_pressure WHERE visit_id='{}'".format(kwags['visit_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllPatientCurrentBloodPressure(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_current_blood_pressure"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def removePatientCurrentBloodPressure(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_current_blood_pressure WHERE visit_id='{}'".format(kwags['visit_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllPatientCurrentBloodPressure(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_current_blood_pressure"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class PatientEmployer(object):
    """docstring for PatientEmployer."""
    def __init__(self):
        super(PatientEmployer, self).__init__()
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addPatientEmployer(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO patient_employer(patient_id,employer_name,employer_address,date_of_record)VALUES('{}','{}','{}','{}')".format(kwags['patient_id'],kwags['employer_name'],kwags['employer_address'],kwags['date_of_record'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getPatientEmplyer(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_employer WHERE patient_id='{}'".format(kwags['patient_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllPatientEmplyer(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_employer"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def removePatientEmployer(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_employer WHERE patient_id='{}'".format(kwags['patient_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllPatientEmployer(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_employer"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class PatientCurrentEmployer(object):
    """docstring for PatientCurrentEmployer."""
    def __init__(self):
        super(PatientCurrentEmployer, self).__init__()
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addPatientCurrentEmployer(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO patient_current_employer(patient_id,employer_name,employer_address,date_of_record)VALUES('{}','{}','{}','{}')".format(kwags['patient_id'],kwags['employer_name'],kwags['employer_address'],kwags['date_of_record'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getPatientCurrentEmployer(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_current_employer WHERE patient_id='{}'".format(kwags['patient_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllPatientCurrentEmployer(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_current_employer"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def removePatientCurrentEmployer(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_current_employer WHERE patient_id='{}'".format(kwags['patient_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllPatientCurrentEmployer(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_current_employer"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class PatientNextOfKeen(object):
    """docstring for PatientNextOfKeen."""
    def __init__(self):
        super(PatientNextOfKeen, self).__init__()
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addPatientNextOfKeen(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO patient_next_of_keen(patient_id,fullname,physical_address,mobile_phone,date_of_record)VALUES('{}','{}','{}','{}','{}')".format(kwags['patient_id'],kwags['fullname'],kwags['physical_address'],kwags['mobile_phone'],kwags['date_of_record'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getPatientNextOfKeen(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_next_of_keen WHERE patient_id='{}'".format(kwags['patient_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllPatientNextOfKeen(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_next_of_keen"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def removePatientNextOfKeen(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_next_of_keen WHERE patient_id='{}'".format(kwags['patient_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllPatientNextOfKeen(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_next_of_keen"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class PatientCurrentNextOfKeen(object):
    """docstring for PatientCurrentNextOfKeen."""
    def __init__(self):
        super(PatientCurrentNextOfKeen, self).__init__()
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addPatientCurrentNextOfKeen(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO patient_current_next_of_keen(patient_id,fullname,physical_address,mobile_phone,date_of_record)VALUES('{}','{}','{}','{}','{}')".format(kwags['patient_id'],kwags['fullname'],kwags['physical_address'],kwags['mobile_phone'],kwags['date_of_record'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getPatientCurrentNextOfKeen(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_current_next_of_keen WHERE patient_id='{}'".format(kwags['patient_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllPatientCurrentNextOfKeen(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_current_next_of_keen"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def removePatientCurrentNextOfKeen(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_current_next_of_keen WHERE patient_id='{}'".format(kwags['patient_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllPatientCurrentNextOfKeen(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_current_next_of_keen"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class PatientPhysicalAddress(object):
    """docstring for PatientPhysicalAddress."""
    def __init__(self):
        super(PatientPhysicalAddress, self).__init__()
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addPatientPhysicalAddress(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO patient_physical_address(visit_id,physical_address,date_of_record)VALUES('{}','{}','{}')".format(kwags['visit_id'],kwags['physical_address'],kwags['date_of_record'])
        cur.execute(sql)
        cur.close()
        self.conn.commt()
    def getPatientPhysicalAddress(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_physical_address WHERE visit_id='{}'".format(kwags['visit_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllPatientPhysicalAddress(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_physical_address"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def removePatientPhysicalAddress(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_physical_address WHERE visit_id='{}'".format(kwags['visit_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllPatientPhysicalAddress(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_physical_address"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class PatientEmailAddress(object):
    """docstring for PatientEmailAddress."""
    def __init__(self):
        super(PatientEmailAddress, self).__init__()
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addPatientEmailAddress(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO patient_email_address(visit_id,email_address,date_of_record)VALUES('{}','{}','{}')".format(kwags['visit_id'],kwags['email_address'],kwags['date_of_record'])
        cur.execute(sql)
        cur.close()
        self.conn.commt()
    def getPatientEmailAddress(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_email_address WHERE visit_id='{}'".format(kwags['visit_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllPatientEmailAddress(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_email_address"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def removePatientEmailAddress(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_email_address WHERE visit_id='{}'".format(kwags['visit_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllPatientEmailAddress(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_email_address"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class PatientPhoneNumber(object):
    """docstring for PatientPhoneNumber."""
    def __init__(self):
        super(PatientPhoneNumber, self).__init__()
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addPatientPhoneNumber(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO patient_phone_number(visit_id,phone_number,date_of_record)VALUES('{}','{}','{}')".format(kwags['visit_id'],kwags['phone_number'],kwags['date_of_record'])
        cur.execute(sql)
        cur.close()
        self.conn.commt()
    def getPatientPhoneNumber(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_phone_number WHERE visit_id='{}'".format(kwags['visit_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllPatientPhoneNumber(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_phone_number"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def removePatientPhoneNumber(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_phone_number WHERE visit_id='{}'".format(kwags['visit_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllPatientPhoneNumber(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_phone_number"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class PatientIPHI(object):
    """docstring for PatientIPHI."""
    def __init__(self, arg):
        super(PatientIPHI, self).__init__()
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addPatientIPHI(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO patient_iphi(patient_id,visit_id,social_security_number,dob,gender,fullname,physical_address,home_phone,work_phone,email_address,employer,relationship_to_patient,date_of_record)VALUES('{}','{}')\
        '{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}'".format(kwags['patient_id'],kwags['visit_id'],kwags['social_security_number'],kwags['dob'],kwags['gender'],kwags['fullname'],kwags['physical_address']\
        ,kwags['home_phone'],kwags['work_phone'],kwags['email_address'],kwags['employer'],kwags['relationship_to_patient'],kwags['date_of_record'])
        cur.execute(sql)
        cur.close()
        self.conn.commt()
    def getPatientIPHIByPatientId(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_iphi WHERE patient_id='{}'".format(kwags['patient_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getPatientIPHIByVisitId(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_iphi WHERE visit_id='{}'".format(kwags['visit_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllPatientIPHI(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_iphi"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def removePatientIPHIByPatientId(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_iphi WHERE patient_id='{}'".format(kwags['patient_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removePatientIPHIByVisitId(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_iphi WHERE visit_id='{}'".format(kwags['visit_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllPatientIPHI(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_iphi"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class PatientCurrentIPHI(object):
    """docstring for PatientCurrentIPHI."""
    def __init__(self):
        super(PatientCurrentIPHI, self).__init__()
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addPatientCurrentIPHI(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO patient_current_iphi(patient_id,social_security_number,date_of_record)VALUES('{}','{}','{}')".format(kwags['patient_id'],kwags['social_security_number'],kwags['date_of_record'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getPatientCurrentIPHIByPatientId(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_current_iphi WHERE patient_id='{}'".format(kwags['patient_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
    def getPatientCurrentIPHIBySocialSecurityNumber(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_current_iphi WHERE social_security_number='{}'".format(kwags['social_security_number'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
    def getAllPatientCurrentIPHI(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_current_iphi"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
    def removePatientCurrentIPHI(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_current_iphi WHERE patient_id='{}'".format(kwags['patient_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllPatientCurrentIPHI(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_current_iphi"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class PatientInsuranceState(object):
    """docstring for PatientInsuranceState."""
    def __init__(self):
        super(PatientInsuranceState, self).__init__()
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addPatientInsuranceState(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO patient_insurance_state(patient_id,patient_insurance_state,date_of_record)VALUES('{}','{}','{}')".format(kwags['patient_id'],kwags['patient_insurance_state'],kwags['date_of_record'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getPatientInsuranceStateByPatientId(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_insurance_state WHERE patient_id='{}'".format(kwags['patient_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
    def getAllPatientInsuranceState(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_insurance_state"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
    def removePatientInsuranceState(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_insurance_state WHERE patient_id='{}'".format(kwags['patient_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllPatientInsuranceState(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_insurance_state"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class PatientSpouseDetail(object):
    """docstring for PatientSpouseDetail."""
    def __init__(self):
        super(PatientSpouseDetail, self).__init__()
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addPatientSpouseDetail(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO patient_spouse_detail(patient_id,spouse_name,spouse_address,spouse_phone_number,date_of_record)VALUES('{}','{}','{}','{}','{}')".format(kwags['patient_id'],kwags['spouse_name'],kwags['spouse_address'],kwags['spouse_phone_number'],kwags['date_of_record'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getPatientSpouseDetailByPatiantId(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_spouse_detail WHERE patient_id='{}'".format(kwags['[patient_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getPatientSpouseDetailByVisitId(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_spouse_detail WHERE visit_id='{}'".format(kwags['[visit_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllPatientSpouseDetail(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_spouse_detail"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def removePatientSpouseDetailByPatientId(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_spouse_detail WHERE patient_id='{}'".format(kwags['patient_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removePatientSpouseDetailByVisitId(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_spouse_detail WHERE visit_id='{}'".format(kwags['visit_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllPatientSpouseDetail(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_spouse_detail"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
class PatientCurrentSpouseDetail(object):
    """docstring for PatientCurrentSpouseDetail."""
    def __init__(self):
        super(PatientCurrentSpouseDetail, self).__init__()
        db=databaseServer.databaseConfig()
        self.conn=db.db
    def addPatientCurrentSpouseDetail(self,**kwags):
        cur=self.conn.cursor()
        sql="INSERT INTO patient_current_spouse_detail(patient_id,spouse_name,spouse_address,spouse_phone_number,date_of_record)VALUES('{}','{}','{}','{}','{}')".format(kwags['patient_id'],kwags['spouse_name'],kwags['spouse_address'],kwags['spouse_phone_number'],kwags['date_of_record'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def getPatientCurrentSpouseDetailByPatiantId(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_current_spouse_detail WHERE patient_id='{}'".format(kwags['[patient_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getPatientCurrentSpouseDetailByVisitId(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_current_spouse_detail WHERE visit_id='{}'".format(kwags['[visit_id'])
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def getAllPatientCurrentSpouseDetail(self,**kwags):
        cur=self.conn.cursor()
        sql="SELECT * FROM patient_current_spouse_detail"
        cur.execute(sql)
        out=cur.fetchall()
        cur.close()
        return out
    def removePatientCurrentSpouseDetailByPatientId(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_current_spouse_detail WHERE patient_id='{}'".format(kwags['patient_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removePatientCurrentSpouseDetailByVisitId(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_current_spouse_detail WHERE visit_id='{}'".format(kwags['visit_id'])
        cur.execute(sql)
        cur.close()
        self.conn.commit()
    def removeAllPatientCurrentSpouseDetail(self,**kwags):
        cur=self.conn.cursor()
        sql="DELETE FROM patient_current_spouse_detail"
        cur.execute(sql)
        cur.close()
        self.conn.commit()
