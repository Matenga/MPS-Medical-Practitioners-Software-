import model0
import time
import os
from triageMIS.helpers import ascii_generator
from systemAdminMIS.helpers import accountManagementHelper
class AgeCalculator(object):
    """docstring for AgeCalculator."""
    def __init__(self,**kwags):
        super(AgeCalculator, self).__init__()

class AddNewPatient(object):
    """docstring for AddNewPatient."""
    def __init__(self,**kwags):
        super(AddNewPatient, self).__init__()
        self.dataPatientCurrentStatus=model0.PatientCurrentStatus()
        self.dataPatientStatus=model0.PatientStatus()
        self.dataPatientPhoto=model0.PatientPhoto()
        self.dataPatientDemographics=model0.PatientDemographics()
        self.dataPatientNextOfKeen=model0.PatientNextOfKeen()
        self.dataPatientCurrentNextOfKeen=model0.PatientCurrentNextOfKeen()
        self.dataPatientEmployer=model0.PatientEmployer()
        self.dataPatientCurrentEmployer=model0.PatientCurrentEmployer()
        self.dataPatientPhysicalAddress=model0.PatientPhysicalAddress()
        self.dataPatientEmailAddress=model0.PatientEmailAddress()
        self.dataPatientPhoneNumber=model0.PatientPhoneNumber()
        self.dataPatientSpouseDetail=model0.PatientSpouseDetail()
        self.dataPatientCurrentSpouseDetail=model0.PatientCurrentSpouseDetail()
        self.dataPatientDemographicsStaffRel=model0.PatientDemographicsStaffRel()
        self.message=[]
        tm=time.ctime()
        kwags['phone_number']="{}@{}@{}".format(kwags['home_phone'].strip(),kwags['work_phone'].strip(),kwags['cell_phone'].strip())
        kwags['date_of_registration']=tm
        kwags['date_of_record']=tm
        kwags['email_address']=kwags['email']
        kwags['date_of_creation']=tm
        kwags['date_of_status']=tm
        kwagsEmmergency=dict()
        kwagsEmmergency['patient_id']=kwags['patient_id']
        kwagsEmmergency['fullname']=kwags['emmergence_name']
        kwagsEmmergency['physical_address']=kwags['emmergency_address']
        kwagsEmmergency['mobile_phone']=kwags['emmergency_phone_number']
        kwagsEmmergency['date_of_record']=tm
        kwags['current_status']="float"
        kwags['patient_status']="out patient"
        kwags['fullname']="{} {}".format(kwags['first_name'].strip().lower(),kwags['other_name'].strip().lower())
        if len(kwags['nid'].strip())!=0:
            check0=self.dataPatientDemographics.getPatientDemographicsByNID(**kwags)
            if len(check0)!=0:
                self.mes0=0
            else:
                self.mes0=1
                check1=self.dataPatientDemographics.getPatientDemographicsBySocialSecurityNumber(**kwags)
                if len(check1)!=0:
                    self.mes1=0
                else:
                    self.mes1=1
        elif len(kwags['social_security_number'].strip())!=0:
            check0=self.dataPatientDemographics.getPatientDemographicsBySocialSecurityNumber(**kwags)
            if len(check0)!=0:
                self.mes1=0
            else:
                self.mes1=1
                check1=self.dataPatientDemographics.getPatientDemographicsByNID(**kwags)
                if len(check1)!=0:
                    self.mes0=0
                else:
                    self.mes0=1
        else:
            self.mes0=1
            self.mes1=1
        if self.mes0!=1 or self.mes1!=1:
            self.mes=0
        else:
            self.mes=1
            self.message.append(kwags['fullname'])
            pref=accountManagementHelper.GenerateIdPrefix()
            self.prefix=pref.idPrefix
            init=accountManagementHelper.GenerateIdInitials(**kwags)
            initials=init.initials
            kwag={"state":"patient_id","initials":initials}
            patientId=accountManagementHelper.GenerateId(**kwag)
            patient_id=patientId.id
            kwags['patient_id']=patient_id
            self.message.append(self.prefix+patient_id)
            self.dataPatientDemographics.addPatientDemographics(**kwags)
            self.dataPatientPhoto.addPatientPhoto(**kwags)
            self.dataPatientPhysicalAddress.addPatientPhysicalAddress(**kwags)
            self.dataPatientEmailAddress.addPatientEmailAddress(**kwags)
            self.dataPatientPhoneNumber.addPatientPhoneNumber(**kwags)
            self.dataPatientDemographicsStaffRel.addPatientDemographicsStaffRel(**kwags)
            self.dataPatientEmployer.addPatientEmployer(**kwags)
            self.dataPatientCurrentEmployer.addPatientCurrentEmployer(**kwags)
            self.dataPatientSpouseDetail.addPatientSpouseDetail(**kwags)
            self.dataPatientCurrentSpouseDetail.addPatientCurrentSpouseDetail(**kwags)
            self.dataPatientCurrentStatus.addPatientCurrentStatus(**kwags)
            self.dataPatientStatus.addPatientStatus(**kwags)
            self.dataPatientNextOfKeen.addPatientNextOfKeen(**kwagsEmmergency)
            self.dataPatientCurrentNextOfKeen.addPatientCurrentNextOfKeen(**kwagsEmmergency)
        self.dataPatientDemographics.conn.close()
        self.dataPatientPhoto.conn.close()
        self.dataPatientPhysicalAddress.conn.close()
        self.dataPatientEmailAddress.conn.close()
        self.dataPatientPhoneNumber.conn.close()
        self.dataPatientDemographicsStaffRel.conn.close()
        self.dataPatientEmployer.conn.close()
        self.dataPatientCurrentEmployer.conn.close()
        self.dataPatientSpouseDetail.conn.close()
        self.dataPatientCurrentSpouseDetail.conn.close()
        self.dataPatientCurrentStatus.conn.close()
        self.dataPatientStatus.conn.close()
        self.dataPatientNextOfKeen.conn.close()
        self.dataPatientCurrentNextOfKeen.conn.close()
