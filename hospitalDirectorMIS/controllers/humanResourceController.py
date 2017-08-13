import cherrypy
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('humanResourceMIS/templates'))
from systemAdminMIS.helpers import accountManagementHelper
from humanResourceMIS.helpers import humanResourceHelper
class HRMIS(object):
    @cherrypy.expose
    def index(self):
        hosp=accountManagementHelper.RetreiveExistingHopitalDetails()
        cookie = cherrypy.request.cookie
        mes=[]
        for key in cookie.keys():
            if key=="MPS-DefaultAdmin":
                if len(cookie[key])!=0:
                    mes.append(key)
            elif key=="MPS-Admin":
                if len(cookie[key])!=0:
                    mes.append(key)
            elif key=="MPS-BackDoor":
                if len(cookie[key])!=0:
                    mes.append(key)
            elif key=="MPS-HumanR":
                if len(cookie[key])!=0:
                    mes.append(key)
        if len(mes)!=0:
            if mes[0]=="MPS-DefaultAdmin" or mes[0]=="MPS-Admin":
                if mes[0]=="MPS-Admin":
                    staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Admin-Id"].value)
                    message0=staffDtl.message
                elif mes[0]=="MPS-DefaultAdmin":
                    message0=["MPS-DefaultAdmin"]
                tmpl = env.get_template('pageNotFoundHumanResource.html')
                return tmpl.render(title="page not found",message0=message0)
            elif mes[0]=="MPS-BackDoor" or mes[0]=="MPS-HumanR":
                if mes[0]=="MPS-BackDoor":
                    message0=["MPS-BackDoor",cookie["MPS-BackDoor"].value]
                elif mes[0]=="MPS-HumanR":
                    staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-HumanR-Id"].value)
                    message0=staffDtl.message
                tmpl = env.get_template('index.html')
                return tmpl.render(hospitalDetails=hosp.hospitalDetails,title="Home HR",message0=message0)
            else:
                tmpl = env.get_template('login.html')
                return tmpl.render(title="login")
        else:
            tmpl = env.get_template('login.html')
            return tmpl.render(title="login")
    @cherrypy.expose
    def recruitDoctor(self):
        hosp=accountManagementHelper.RetreiveExistingHopitalDetails()
        cookie = cherrypy.request.cookie
        mes=[]
        for key in cookie.keys():
            if key=="MPS-DefaultAdmin":
                if len(cookie[key])!=0:
                    mes.append(key)
            elif key=="MPS-Admin":
                if len(cookie[key])!=0:
                    mes.append(key)
            elif key=="MPS-BackDoor":
                if len(cookie[key])!=0:
                    mes.append(key)
            elif key=="MPS-HumanR":
                if len(cookie[key])!=0:
                    mes.append(key)
        if len(mes)!=0:
            if mes[0]=="MPS-DefaultAdmin" or mes[0]=="MPS-Admin":
                if mes[0]=="MPS-Admin":
                    staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Admin-Id"].value)
                    message0=staffDtl.message
                elif mes[0]=="MPS-DefaultAdmin":
                    message0=["MPS-DefaultAdmin"]
                tmpl = env.get_template('pageNotFoundHumanResource.html')
                return tmpl.render(title="page not found",message0=message0)
            elif mes[0]=="MPS-BackDoor" or mes[0]=="MPS-HumanR":
                if mes[0]=="MPS-BackDoor":
                    message0=["MPS-BackDoor",cookie["MPS-BackDoor"].value]
                elif mes[0]=="MPS-HumanR":
                    staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-HumanR-Id"].value)
                    message0=staffDtl.message
                tmpl = env.get_template('recruitDoctor.html')
                return tmpl.render(hospitalDetails=hosp.hospitalDetails,title="recruit doctor",message0=message0)
            else:
                tmpl = env.get_template('login.html')
                return tmpl.render(title="login")
        else:
            tmpl = env.get_template('login.html')
            return tmpl.render(title="login")
    @cherrypy.expose
    def addDoctorResult(self,**kwags):
        try:
            hosp=accountManagementHelper.RetreiveExistingHopitalDetails()
            cookie = cherrypy.request.cookie
            mes=[]
            for key in cookie.keys():
                if key=="MPS-DefaultAdmin":
                    if len(cookie[key])!=0:
                        mes.append(key)
                elif key=="MPS-Admin":
                    if len(cookie[key])!=0:
                        mes.append(key)
                elif key=="MPS-BackDoor":
                    if len(cookie[key])!=0:
                        mes.append(key)
                elif key=="MPS-HumanR":
                    if len(cookie[key])!=0:
                        mes.append(key)
            if len(mes)!=0:
                if mes[0]=="MPS-DefaultAdmin" or mes[0]=="MPS-Admin":
                    if mes[0]=="MPS-Admin":
                        staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Admin-Id"].value)
                        message0=staffDtl.message
                    elif mes[0]=="MPS-DefaultAdmin":
                        message0=["MPS-DefaultAdmin"]
                    tmpl = env.get_template('pageNotFoundHumanResource.html')
                    return tmpl.render(title="page not found",message0=message0)
                elif mes[0]=="MPS-BackDoor" or mes[0]=="MPS-HumanR":
                    if mes[0]=="MPS-BackDoor":
                        message0=["MPS-BackDoor",cookie["MPS-BackDoor"].value]
                    elif mes[0]=="MPS-HumanR":
                        staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-HumanR-Id"].value)
                        message0=staffDtl.message
                    addNewDoctor=humanResourceHelper.AddHospitalDoctor(**kwags)
                    tmpl = env.get_template('staffAddResult.html')
                    return tmpl.render(message=addNewDoctor.message,hospitalDetails=hosp.hospitalDetails,title="Add Doctor Results",message0=message0)
                else:
                    tmpl = env.get_template('login.html')
                    return tmpl.render(title="login")
            else:
                tmpl = env.get_template('login.html')
                return tmpl.render(title="login")
        except:
            hosp=accountManagementHelper.RetreiveExistingHopitalDetails()
            cookie = cherrypy.request.cookie
            mes=[]
            for key in cookie.keys():
                if key=="MPS-DefaultAdmin":
                    if len(cookie[key])!=0:
                        mes.append(key)
                elif key=="MPS-Admin":
                    if len(cookie[key])!=0:
                        mes.append(key)
                elif key=="MPS-BackDoor":
                    if len(cookie[key])!=0:
                        mes.append(key)
                elif key=="MPS-HumanR":
                    if len(cookie[key])!=0:
                        mes.append(key)
            if len(mes)!=0:
                if mes[0]=="MPS-DefaultAdmin" or mes[0]=="MPS-Admin":
                    if mes[0]=="MPS-Admin":
                        staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Admin-Id"].value)
                        message0=staffDtl.message
                    elif mes[0]=="MPS-DefaultAdmin":
                        message0=["MPS-DefaultAdmin"]
                    tmpl = env.get_template('pageNotFoundHumanResource.html')
                    return tmpl.render(title="page not found",message0=message0)
                elif mes[0]=="MPS-BackDoor" or mes[0]=="MPS-HumanR":
                    if mes[0]=="MPS-BackDoor":
                        message0=["MPS-BackDoor",cookie["MPS-BackDoor"].value]
                    elif mes[0]=="MPS-HumanR":
                        staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-HumanR-Id"].value)
                        message0=staffDtl.message
                    tmpl = env.get_template('index.html')
                    return tmpl.render(hospitalDetails=hosp.hospitalDetails,title="Home ",message0=message0)
                else:
                    tmpl = env.get_template('login.html')
                    return tmpl.render(title="login")
            else:
                tmpl = env.get_template('login.html')
                return tmpl.render(title="login")
    @cherrypy.expose
    def viewAvailableDoctors(self):
        hosp=accountManagementHelper.RetreiveExistingHopitalDetails()
        cookie = cherrypy.request.cookie
        mes=[]
        for key in cookie.keys():
            if key=="MPS-DefaultAdmin":
                if len(cookie[key])!=0:
                    mes.append(key)
            elif key=="MPS-Admin":
                if len(cookie[key])!=0:
                    mes.append(key)
            elif key=="MPS-BackDoor":
                if len(cookie[key])!=0:
                    mes.append(key)
            elif key=="MPS-HumanR":
                if len(cookie[key])!=0:
                    mes.append(key)
        if len(mes)!=0:
            if mes[0]=="MPS-DefaultAdmin" or mes[0]=="MPS-Admin":
                if mes[0]=="MPS-Admin":
                    staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Admin-Id"].value)
                    message0=staffDtl.message
                elif mes[0]=="MPS-DefaultAdmin":
                    message0=["MPS-DefaultAdmin"]
                tmpl = env.get_template('pageNotFoundHumanResource.html')
                return tmpl.render(title="page not found",message0=message0)
            elif mes[0]=="MPS-BackDoor" or mes[0]=="MPS-HumanR":
                if mes[0]=="MPS-BackDoor":
                    message0=["MPS-BackDoor",cookie["MPS-BackDoor"].value]
                elif mes[0]=="MPS-HumanR":
                    staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-HumanR-Id"].value)
                    message0=staffDtl.message
                availableDoctors=humanResourceHelper.RetrieveAvailableHospitalDoctors()
                tmpl = env.get_template('availableDoctors.html')
                return tmpl.render(message=availableDoctors.message,hospitalDetails=hosp.hospitalDetails,title="Add Doctor Results",message0=message0)
            else:
                tmpl = env.get_template('login.html')
                return tmpl.render(title="login")
        else:
            tmpl = env.get_template('login.html')
            return tmpl.render(title="login")
    @cherrypy.expose
    def recruitNurse(self):
        hosp=accountManagementHelper.RetreiveExistingHopitalDetails()
        cookie = cherrypy.request.cookie
        mes=[]
        for key in cookie.keys():
            if key=="MPS-DefaultAdmin":
                if len(cookie[key])!=0:
                    mes.append(key)
            elif key=="MPS-Admin":
                if len(cookie[key])!=0:
                    mes.append(key)
            elif key=="MPS-BackDoor":
                if len(cookie[key])!=0:
                    mes.append(key)
            elif key=="MPS-HumanR":
                if len(cookie[key])!=0:
                    mes.append(key)
        if len(mes)!=0:
            if mes[0]=="MPS-DefaultAdmin" or mes[0]=="MPS-Admin":
                if mes[0]=="MPS-Admin":
                    staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Admin-Id"].value)
                    message0=staffDtl.message
                elif mes[0]=="MPS-DefaultAdmin":
                    message0=["MPS-DefaultAdmin"]
                tmpl = env.get_template('pageNotFoundHumanResource.html')
                return tmpl.render(title="page not found",message0=message0)
            elif mes[0]=="MPS-BackDoor" or mes[0]=="MPS-HumanR":
                if mes[0]=="MPS-BackDoor":
                    message0=["MPS-BackDoor",cookie["MPS-BackDoor"].value]
                elif mes[0]=="MPS-HumanR":
                    staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-HumanR-Id"].value)
                    message0=staffDtl.message
                tmpl = env.get_template('recruitNurse.html')
                return tmpl.render(hospitalDetails=hosp.hospitalDetails,title="recruit Nurse",message0=message0)
            else:
                tmpl = env.get_template('login.html')
                return tmpl.render(title="login")
        else:
            tmpl = env.get_template('login.html')
            return tmpl.render(title="login")
    @cherrypy.expose
    def addNurseResult(self,**kwags):
        try:
            hosp=accountManagementHelper.RetreiveExistingHopitalDetails()
            cookie = cherrypy.request.cookie
            mes=[]
            for key in cookie.keys():
                if key=="MPS-DefaultAdmin":
                    if len(cookie[key])!=0:
                        mes.append(key)
                elif key=="MPS-Admin":
                    if len(cookie[key])!=0:
                        mes.append(key)
                elif key=="MPS-BackDoor":
                    if len(cookie[key])!=0:
                        mes.append(key)
                elif key=="MPS-HumanR":
                    if len(cookie[key])!=0:
                        mes.append(key)
            if len(mes)!=0:
                if mes[0]=="MPS-DefaultAdmin" or mes[0]=="MPS-Admin":
                    if mes[0]=="MPS-Admin":
                        staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Admin-Id"].value)
                        message0=staffDtl.message
                    elif mes[0]=="MPS-DefaultAdmin":
                        message0=["MPS-DefaultAdmin"]
                    tmpl = env.get_template('pageNotFoundHumanResource.html')
                    return tmpl.render(title="page not found",message0=message0)
                elif mes[0]=="MPS-BackDoor" or mes[0]=="MPS-HumanR":
                    if mes[0]=="MPS-BackDoor":
                        message0=["MPS-BackDoor",cookie["MPS-BackDoor"].value]
                    elif mes[0]=="MPS-HumanR":
                        staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-HumanR-Id"].value)
                        message0=staffDtl.message
                    addNewNurse=humanResourceHelper.AddHospitalNurse(**kwags)
                    tmpl = env.get_template('staffAddResult.html')
                    return tmpl.render(message=addNewNurse.message,hospitalDetails=hosp.hospitalDetails,title="Add Doctor Results",message0=message0)
                else:
                    tmpl = env.get_template('login.html')
                    return tmpl.render(title="login")
            else:
                tmpl = env.get_template('login.html')
                return tmpl.render(title="login")
        except:
            hosp=accountManagementHelper.RetreiveExistingHopitalDetails()
            cookie = cherrypy.request.cookie
            mes=[]
            for key in cookie.keys():
                if key=="MPS-DefaultAdmin":
                    if len(cookie[key])!=0:
                        mes.append(key)
                elif key=="MPS-Admin":
                    if len(cookie[key])!=0:
                        mes.append(key)
                elif key=="MPS-BackDoor":
                    if len(cookie[key])!=0:
                        mes.append(key)
                elif key=="MPS-HumanR":
                    if len(cookie[key])!=0:
                        mes.append(key)
            if len(mes)!=0:
                if mes[0]=="MPS-DefaultAdmin" or mes[0]=="MPS-Admin":
                    if mes[0]=="MPS-Admin":
                        staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Admin-Id"].value)
                        message0=staffDtl.message
                    elif mes[0]=="MPS-DefaultAdmin":
                        message0=["MPS-DefaultAdmin"]
                    tmpl = env.get_template('pageNotFoundHumanResource.html')
                    return tmpl.render(title="page not found",message0=message0)
                elif mes[0]=="MPS-BackDoor" or mes[0]=="MPS-HumanR":
                    if mes[0]=="MPS-BackDoor":
                        message0=["MPS-BackDoor",cookie["MPS-BackDoor"].value]
                    elif mes[0]=="MPS-HumanR":
                        staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-HumanR-Id"].value)
                        message0=staffDtl.message
                    tmpl = env.get_template('index.html')
                    return tmpl.render(hospitalDetails=hosp.hospitalDetails,title="Home ",message0=message0)
                else:
                    tmpl = env.get_template('login.html')
                    return tmpl.render(title="login")
            else:
                tmpl = env.get_template('login.html')
                return tmpl.render(title="login")
    @cherrypy.expose
    def viewAvailableNurses(self):
        hosp=accountManagementHelper.RetreiveExistingHopitalDetails()
        cookie = cherrypy.request.cookie
        mes=[]
        for key in cookie.keys():
            if key=="MPS-DefaultAdmin":
                if len(cookie[key])!=0:
                    mes.append(key)
            elif key=="MPS-Admin":
                if len(cookie[key])!=0:
                    mes.append(key)
            elif key=="MPS-BackDoor":
                if len(cookie[key])!=0:
                    mes.append(key)
            elif key=="MPS-HumanR":
                if len(cookie[key])!=0:
                    mes.append(key)
        if len(mes)!=0:
            if mes[0]=="MPS-DefaultAdmin" or mes[0]=="MPS-Admin":
                if mes[0]=="MPS-Admin":
                    staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Admin-Id"].value)
                    message0=staffDtl.message
                elif mes[0]=="MPS-DefaultAdmin":
                    message0=["MPS-DefaultAdmin"]
                tmpl = env.get_template('pageNotFoundHumanResource.html')
                return tmpl.render(title="page not found",message0=message0)
            elif mes[0]=="MPS-BackDoor" or mes[0]=="MPS-HumanR":
                if mes[0]=="MPS-BackDoor":
                    message0=["MPS-BackDoor",cookie["MPS-BackDoor"].value]
                elif mes[0]=="MPS-HumanR":
                    staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-HumanR-Id"].value)
                    message0=staffDtl.message
                availableNurses=humanResourceHelper.RetrieveAvailableHospitalNurses()
                tmpl = env.get_template('availableNurses.html')
                return tmpl.render(message=availableNurses.message,hospitalDetails=hosp.hospitalDetails,title="Add Doctor Results",message0=message0)
            else:
                tmpl = env.get_template('login.html')
                return tmpl.render(title="login")
        else:
            tmpl = env.get_template('login.html')
            return tmpl.render(title="login")
    @cherrypy.expose
    def recruitClinician(self):
        hosp=accountManagementHelper.RetreiveExistingHopitalDetails()
        cookie = cherrypy.request.cookie
        mes=[]
        for key in cookie.keys():
            if key=="MPS-DefaultAdmin":
                if len(cookie[key])!=0:
                    mes.append(key)
            elif key=="MPS-Admin":
                if len(cookie[key])!=0:
                    mes.append(key)
            elif key=="MPS-BackDoor":
                if len(cookie[key])!=0:
                    mes.append(key)
            elif key=="MPS-HumanR":
                if len(cookie[key])!=0:
                    mes.append(key)
        if len(mes)!=0:
            if mes[0]=="MPS-DefaultAdmin" or mes[0]=="MPS-Admin":
                if mes[0]=="MPS-Admin":
                    staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Admin-Id"].value)
                    message0=staffDtl.message
                elif mes[0]=="MPS-DefaultAdmin":
                    message0=["MPS-DefaultAdmin"]
                tmpl = env.get_template('pageNotFoundHumanResource.html')
                return tmpl.render(title="page not found",message0=message0)
            elif mes[0]=="MPS-BackDoor" or mes[0]=="MPS-HumanR":
                if mes[0]=="MPS-BackDoor":
                    message0=["MPS-BackDoor",cookie["MPS-BackDoor"].value]
                elif mes[0]=="MPS-HumanR":
                    staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-HumanR-Id"].value)
                    message0=staffDtl.message
                tmpl = env.get_template('recruitClinician.html')
                return tmpl.render(hospitalDetails=hosp.hospitalDetails,title="recruit Clinician",message0=message0)
            else:
                tmpl = env.get_template('login.html')
                return tmpl.render(title="login")
        else:
            tmpl = env.get_template('login.html')
            return tmpl.render(title="login")
    @cherrypy.expose
    def addClinicanResult(self,**kwags):
        try:
            hosp=accountManagementHelper.RetreiveExistingHopitalDetails()
            cookie = cherrypy.request.cookie
            mes=[]
            for key in cookie.keys():
                if key=="MPS-DefaultAdmin":
                    if len(cookie[key])!=0:
                        mes.append(key)
                elif key=="MPS-Admin":
                    if len(cookie[key])!=0:
                        mes.append(key)
                elif key=="MPS-BackDoor":
                    if len(cookie[key])!=0:
                        mes.append(key)
                elif key=="MPS-HumanR":
                    if len(cookie[key])!=0:
                        mes.append(key)
            if len(mes)!=0:
                if mes[0]=="MPS-DefaultAdmin" or mes[0]=="MPS-Admin":
                    if mes[0]=="MPS-Admin":
                        staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Admin-Id"].value)
                        message0=staffDtl.message
                    elif mes[0]=="MPS-DefaultAdmin":
                        message0=["MPS-DefaultAdmin"]
                    tmpl = env.get_template('pageNotFoundHumanResource.html')
                    return tmpl.render(title="page not found",message0=message0)
                elif mes[0]=="MPS-BackDoor" or mes[0]=="MPS-HumanR":
                    if mes[0]=="MPS-BackDoor":
                        message0=["MPS-BackDoor",cookie["MPS-BackDoor"].value]
                    elif mes[0]=="MPS-HumanR":
                        staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-HumanR-Id"].value)
                        message0=staffDtl.message
                    addNewClinician=humanResourceHelper.AddHospitalClinician(**kwags)
                    tmpl = env.get_template('staffAddResult.html')
                    return tmpl.render(message=addNewClinician.message,hospitalDetails=hosp.hospitalDetails,title="Add Doctor Results",message0=message0)
                else:
                    tmpl = env.get_template('login.html')
                    return tmpl.render(title="login")
            else:
                tmpl = env.get_template('login.html')
                return tmpl.render(title="login")
        except:
            hosp=accountManagementHelper.RetreiveExistingHopitalDetails()
            cookie = cherrypy.request.cookie
            mes=[]
            for key in cookie.keys():
                if key=="MPS-DefaultAdmin":
                    if len(cookie[key])!=0:
                        mes.append(key)
                elif key=="MPS-Admin":
                    if len(cookie[key])!=0:
                        mes.append(key)
                elif key=="MPS-BackDoor":
                    if len(cookie[key])!=0:
                        mes.append(key)
                elif key=="MPS-HumanR":
                    if len(cookie[key])!=0:
                        mes.append(key)
            if len(mes)!=0:
                if mes[0]=="MPS-DefaultAdmin" or mes[0]=="MPS-Admin":
                    if mes[0]=="MPS-Admin":
                        staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Admin-Id"].value)
                        message0=staffDtl.message
                    elif mes[0]=="MPS-DefaultAdmin":
                        message0=["MPS-DefaultAdmin"]
                    tmpl = env.get_template('pageNotFoundHumanResource.html')
                    return tmpl.render(title="page not found",message0=message0)
                elif mes[0]=="MPS-BackDoor" or mes[0]=="MPS-HumanR":
                    if mes[0]=="MPS-BackDoor":
                        message0=["MPS-BackDoor",cookie["MPS-BackDoor"].value]
                    elif mes[0]=="MPS-HumanR":
                        staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-HumanR-Id"].value)
                        message0=staffDtl.message
                    tmpl = env.get_template('index.html')
                    return tmpl.render(hospitalDetails=hosp.hospitalDetails,title="Home ",message0=message0)
                else:
                    tmpl = env.get_template('login.html')
                    return tmpl.render(title="login")
            else:
                tmpl = env.get_template('login.html')
                return tmpl.render(title="login")
    @cherrypy.expose
    def viewAvailableClinicians(self):
        hosp=accountManagementHelper.RetreiveExistingHopitalDetails()
        cookie = cherrypy.request.cookie
        mes=[]
        for key in cookie.keys():
            if key=="MPS-DefaultAdmin":
                if len(cookie[key])!=0:
                    mes.append(key)
            elif key=="MPS-Admin":
                if len(cookie[key])!=0:
                    mes.append(key)
            elif key=="MPS-BackDoor":
                if len(cookie[key])!=0:
                    mes.append(key)
            elif key=="MPS-HumanR":
                if len(cookie[key])!=0:
                    mes.append(key)
        if len(mes)!=0:
            if mes[0]=="MPS-DefaultAdmin" or mes[0]=="MPS-Admin":
                if mes[0]=="MPS-Admin":
                    staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Admin-Id"].value)
                    message0=staffDtl.message
                elif mes[0]=="MPS-DefaultAdmin":
                    message0=["MPS-DefaultAdmin"]
                tmpl = env.get_template('pageNotFoundHumanResource.html')
                return tmpl.render(title="page not found",message0=message0)
            elif mes[0]=="MPS-BackDoor" or mes[0]=="MPS-HumanR":
                if mes[0]=="MPS-BackDoor":
                    message0=["MPS-BackDoor",cookie["MPS-BackDoor"].value]
                elif mes[0]=="MPS-HumanR":
                    staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-HumanR-Id"].value)
                    message0=staffDtl.message
                availableClinicians=humanResourceHelper.RetrieveAvailableHospitalClinicians()
                tmpl = env.get_template('availableClinicians.html')
                return tmpl.render(message=availableClinicians.message,hospitalDetails=hosp.hospitalDetails,title="Add Doctor Results",message0=message0)
            else:
                tmpl = env.get_template('login.html')
                return tmpl.render(title="login")
        else:
            tmpl = env.get_template('login.html')
            return tmpl.render(title="login")
    @cherrypy.expose
    def recruitLaboratorist(self):
        hosp=accountManagementHelper.RetreiveExistingHopitalDetails()
        cookie = cherrypy.request.cookie
        mes=[]
        for key in cookie.keys():
            if key=="MPS-DefaultAdmin":
                if len(cookie[key])!=0:
                    mes.append(key)
            elif key=="MPS-Admin":
                if len(cookie[key])!=0:
                    mes.append(key)
            elif key=="MPS-BackDoor":
                if len(cookie[key])!=0:
                    mes.append(key)
            elif key=="MPS-HumanR":
                if len(cookie[key])!=0:
                    mes.append(key)
        if len(mes)!=0:
            if mes[0]=="MPS-DefaultAdmin" or mes[0]=="MPS-Admin":
                if mes[0]=="MPS-Admin":
                    staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Admin-Id"].value)
                    message0=staffDtl.message
                elif mes[0]=="MPS-DefaultAdmin":
                    message0=["MPS-DefaultAdmin"]
                tmpl = env.get_template('pageNotFoundHumanResource.html')
                return tmpl.render(title="page not found",message0=message0)
            elif mes[0]=="MPS-BackDoor" or mes[0]=="MPS-HumanR":
                if mes[0]=="MPS-BackDoor":
                    message0=["MPS-BackDoor",cookie["MPS-BackDoor"].value]
                elif mes[0]=="MPS-HumanR":
                    staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-HumanR-Id"].value)
                    message0=staffDtl.message
                tmpl = env.get_template('recruitLaboratorist.html')
                return tmpl.render(hospitalDetails=hosp.hospitalDetails,title="recruit Clinician",message0=message0)
            else:
                tmpl = env.get_template('login.html')
                return tmpl.render(title="login")
        else:
            tmpl = env.get_template('login.html')
            return tmpl.render(title="login")
    @cherrypy.expose
    def addLaboratoristResult(self,**kwags):
        try:
            hosp=accountManagementHelper.RetreiveExistingHopitalDetails()
            cookie = cherrypy.request.cookie
            mes=[]
            for key in cookie.keys():
                if key=="MPS-DefaultAdmin":
                    if len(cookie[key])!=0:
                        mes.append(key)
                elif key=="MPS-Admin":
                    if len(cookie[key])!=0:
                        mes.append(key)
                elif key=="MPS-BackDoor":
                    if len(cookie[key])!=0:
                        mes.append(key)
                elif key=="MPS-HumanR":
                    if len(cookie[key])!=0:
                        mes.append(key)
            if len(mes)!=0:
                if mes[0]=="MPS-DefaultAdmin" or mes[0]=="MPS-Admin":
                    if mes[0]=="MPS-Admin":
                        staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Admin-Id"].value)
                        message0=staffDtl.message
                    elif mes[0]=="MPS-DefaultAdmin":
                        message0=["MPS-DefaultAdmin"]
                    tmpl = env.get_template('pageNotFoundHumanResource.html')
                    return tmpl.render(title="page not found",message0=message0)
                elif mes[0]=="MPS-BackDoor" or mes[0]=="MPS-HumanR":
                    if mes[0]=="MPS-BackDoor":
                        message0=["MPS-BackDoor",cookie["MPS-BackDoor"].value]
                    elif mes[0]=="MPS-HumanR":
                        staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-HumanR-Id"].value)
                        message0=staffDtl.message
                    addNewLaboratorist=humanResourceHelper.AddHospitalLaboratorist(**kwags)
                    tmpl = env.get_template('staffAddResult.html')
                    return tmpl.render(message=addNewLaboratorist.message,hospitalDetails=hosp.hospitalDetails,title="Add Doctor Results",message0=message0)
                else:
                    tmpl = env.get_template('login.html')
                    return tmpl.render(title="login")
            else:
                tmpl = env.get_template('login.html')
                return tmpl.render(title="login")
        except:
            hosp=accountManagementHelper.RetreiveExistingHopitalDetails()
            cookie = cherrypy.request.cookie
            mes=[]
            for key in cookie.keys():
                if key=="MPS-DefaultAdmin":
                    if len(cookie[key])!=0:
                        mes.append(key)
                elif key=="MPS-Admin":
                    if len(cookie[key])!=0:
                        mes.append(key)
                elif key=="MPS-BackDoor":
                    if len(cookie[key])!=0:
                        mes.append(key)
                elif key=="MPS-HumanR":
                    if len(cookie[key])!=0:
                        mes.append(key)
            if len(mes)!=0:
                if mes[0]=="MPS-DefaultAdmin" or mes[0]=="MPS-Admin":
                    if mes[0]=="MPS-Admin":
                        staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Admin-Id"].value)
                        message0=staffDtl.message
                    elif mes[0]=="MPS-DefaultAdmin":
                        message0=["MPS-DefaultAdmin"]
                    tmpl = env.get_template('pageNotFoundHumanResource.html')
                    return tmpl.render(title="page not found",message0=message0)
                elif mes[0]=="MPS-BackDoor" or mes[0]=="MPS-HumanR":
                    if mes[0]=="MPS-BackDoor":
                        message0=["MPS-BackDoor",cookie["MPS-BackDoor"].value]
                    elif mes[0]=="MPS-HumanR":
                        staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-HumanR-Id"].value)
                        message0=staffDtl.message
                    tmpl = env.get_template('index.html')
                    return tmpl.render(hospitalDetails=hosp.hospitalDetails,title="Home ",message0=message0)
                else:
                    tmpl = env.get_template('login.html')
                    return tmpl.render(title="login")
            else:
                tmpl = env.get_template('login.html')
                return tmpl.render(title="login")
    @cherrypy.expose
    def viewAvailableLaboratorists(self):
        hosp=accountManagementHelper.RetreiveExistingHopitalDetails()
        cookie = cherrypy.request.cookie
        mes=[]
        for key in cookie.keys():
            if key=="MPS-DefaultAdmin":
                if len(cookie[key])!=0:
                    mes.append(key)
            elif key=="MPS-Admin":
                if len(cookie[key])!=0:
                    mes.append(key)
            elif key=="MPS-BackDoor":
                if len(cookie[key])!=0:
                    mes.append(key)
            elif key=="MPS-HumanR":
                if len(cookie[key])!=0:
                    mes.append(key)
        if len(mes)!=0:
            if mes[0]=="MPS-DefaultAdmin" or mes[0]=="MPS-Admin":
                if mes[0]=="MPS-Admin":
                    staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Admin-Id"].value)
                    message0=staffDtl.message
                elif mes[0]=="MPS-DefaultAdmin":
                    message0=["MPS-DefaultAdmin"]
                tmpl = env.get_template('pageNotFoundHumanResource.html')
                return tmpl.render(title="page not found",message0=message0)
            elif mes[0]=="MPS-BackDoor" or mes[0]=="MPS-HumanR":
                if mes[0]=="MPS-BackDoor":
                    message0=["MPS-BackDoor",cookie["MPS-BackDoor"].value]
                elif mes[0]=="MPS-HumanR":
                    staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-HumanR-Id"].value)
                    message0=staffDtl.message
                availableLaboratorists=humanResourceHelper.RetrieveAvailableHospitalLaboratorists()
                tmpl = env.get_template('availableLaboratorists.html')
                return tmpl.render(message=availableLaboratorists.message,hospitalDetails=hosp.hospitalDetails,title="Add Doctor Results",message0=message0)
            else:
                tmpl = env.get_template('login.html')
                return tmpl.render(title="login")
        else:
            tmpl = env.get_template('login.html')
            return tmpl.render(title="login")
    @cherrypy.expose
    def recruitPharmacist(self):
        hosp=accountManagementHelper.RetreiveExistingHopitalDetails()
        cookie = cherrypy.request.cookie
        mes=[]
        for key in cookie.keys():
            if key=="MPS-DefaultAdmin":
                if len(cookie[key])!=0:
                    mes.append(key)
            elif key=="MPS-Admin":
                if len(cookie[key])!=0:
                    mes.append(key)
            elif key=="MPS-BackDoor":
                if len(cookie[key])!=0:
                    mes.append(key)
            elif key=="MPS-HumanR":
                if len(cookie[key])!=0:
                    mes.append(key)
        if len(mes)!=0:
            if mes[0]=="MPS-DefaultAdmin" or mes[0]=="MPS-Admin":
                if mes[0]=="MPS-Admin":
                    staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Admin-Id"].value)
                    message0=staffDtl.message
                elif mes[0]=="MPS-DefaultAdmin":
                    message0=["MPS-DefaultAdmin"]
                tmpl = env.get_template('pageNotFoundHumanResource.html')
                return tmpl.render(title="page not found",message0=message0)
            elif mes[0]=="MPS-BackDoor" or mes[0]=="MPS-HumanR":
                if mes[0]=="MPS-BackDoor":
                    message0=["MPS-BackDoor",cookie["MPS-BackDoor"].value]
                elif mes[0]=="MPS-HumanR":
                    staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-HumanR-Id"].value)
                    message0=staffDtl.message
                tmpl = env.get_template('recruitPharmacist.html')
                return tmpl.render(hospitalDetails=hosp.hospitalDetails,title="recruit Clinician",message0=message0)
            else:
                tmpl = env.get_template('login.html')
                return tmpl.render(title="login")
        else:
            tmpl = env.get_template('login.html')
            return tmpl.render(title="login")
    @cherrypy.expose
    def addPharmacistResult(self,**kwags):
        try:
            hosp=accountManagementHelper.RetreiveExistingHopitalDetails()
            cookie = cherrypy.request.cookie
            mes=[]
            for key in cookie.keys():
                if key=="MPS-DefaultAdmin":
                    if len(cookie[key])!=0:
                        mes.append(key)
                elif key=="MPS-Admin":
                    if len(cookie[key])!=0:
                        mes.append(key)
                elif key=="MPS-BackDoor":
                    if len(cookie[key])!=0:
                        mes.append(key)
                elif key=="MPS-HumanR":
                    if len(cookie[key])!=0:
                        mes.append(key)
            if len(mes)!=0:
                if mes[0]=="MPS-DefaultAdmin" or mes[0]=="MPS-Admin":
                    if mes[0]=="MPS-Admin":
                        staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Admin-Id"].value)
                        message0=staffDtl.message
                    elif mes[0]=="MPS-DefaultAdmin":
                        message0=["MPS-DefaultAdmin"]
                    tmpl = env.get_template('pageNotFoundHumanResource.html')
                    return tmpl.render(title="page not found",message0=message0)
                elif mes[0]=="MPS-BackDoor" or mes[0]=="MPS-HumanR":
                    if mes[0]=="MPS-BackDoor":
                        message0=["MPS-BackDoor",cookie["MPS-BackDoor"].value]
                    elif mes[0]=="MPS-HumanR":
                        staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-HumanR-Id"].value)
                        message0=staffDtl.message
                    addNewPharmacist=humanResourceHelper.AddHospitalPharmacist(**kwags)
                    tmpl = env.get_template('staffAddResult.html')
                    return tmpl.render(message=addNewPharmacist.message,hospitalDetails=hosp.hospitalDetails,title="Add Doctor Results",message0=message0)
                else:
                    tmpl = env.get_template('login.html')
                    return tmpl.render(title="login")
            else:
                tmpl = env.get_template('login.html')
                return tmpl.render(title="login")
        except:
            hosp=accountManagementHelper.RetreiveExistingHopitalDetails()
            cookie = cherrypy.request.cookie
            mes=[]
            for key in cookie.keys():
                if key=="MPS-DefaultAdmin":
                    if len(cookie[key])!=0:
                        mes.append(key)
                elif key=="MPS-Admin":
                    if len(cookie[key])!=0:
                        mes.append(key)
                elif key=="MPS-BackDoor":
                    if len(cookie[key])!=0:
                        mes.append(key)
                elif key=="MPS-HumanR":
                    if len(cookie[key])!=0:
                        mes.append(key)
            if len(mes)!=0:
                if mes[0]=="MPS-DefaultAdmin" or mes[0]=="MPS-Admin":
                    if mes[0]=="MPS-Admin":
                        staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Admin-Id"].value)
                        message0=staffDtl.message
                    elif mes[0]=="MPS-DefaultAdmin":
                        message0=["MPS-DefaultAdmin"]
                    tmpl = env.get_template('pageNotFoundHumanResource.html')
                    return tmpl.render(title="page not found",message0=message0)
                elif mes[0]=="MPS-BackDoor" or mes[0]=="MPS-HumanR":
                    if mes[0]=="MPS-BackDoor":
                        message0=["MPS-BackDoor",cookie["MPS-BackDoor"].value]
                    elif mes[0]=="MPS-HumanR":
                        staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-HumanR-Id"].value)
                        message0=staffDtl.message
                    tmpl = env.get_template('index.html')
                    return tmpl.render(hospitalDetails=hosp.hospitalDetails,title="Home ",message0=message0)
                else:
                    tmpl = env.get_template('login.html')
                    return tmpl.render(title="login")
            else:
                tmpl = env.get_template('login.html')
                return tmpl.render(title="login")
    @cherrypy.expose
    def viewAvailablePharmacists(self):
        hosp=accountManagementHelper.RetreiveExistingHopitalDetails()
        cookie = cherrypy.request.cookie
        mes=[]
        for key in cookie.keys():
            if key=="MPS-DefaultAdmin":
                if len(cookie[key])!=0:
                    mes.append(key)
            elif key=="MPS-Admin":
                if len(cookie[key])!=0:
                    mes.append(key)
            elif key=="MPS-BackDoor":
                if len(cookie[key])!=0:
                    mes.append(key)
            elif key=="MPS-HumanR":
                if len(cookie[key])!=0:
                    mes.append(key)
        if len(mes)!=0:
            if mes[0]=="MPS-DefaultAdmin" or mes[0]=="MPS-Admin":
                if mes[0]=="MPS-Admin":
                    staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Admin-Id"].value)
                    message0=staffDtl.message
                elif mes[0]=="MPS-DefaultAdmin":
                    message0=["MPS-DefaultAdmin"]
                tmpl = env.get_template('pageNotFoundHumanResource.html')
                return tmpl.render(title="page not found",message0=message0)
            elif mes[0]=="MPS-BackDoor" or mes[0]=="MPS-HumanR":
                if mes[0]=="MPS-BackDoor":
                    message0=["MPS-BackDoor",cookie["MPS-BackDoor"].value]
                elif mes[0]=="MPS-HumanR":
                    staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-HumanR-Id"].value)
                    message0=staffDtl.message
                availablePharmacists=humanResourceHelper.RetrieveAvailableHospitalPharmacists()
                tmpl = env.get_template('availablePharmacists.html')
                return tmpl.render(message=availablePharmacists.message,hospitalDetails=hosp.hospitalDetails,title="Add Doctor Results",message0=message0)
            else:
                tmpl = env.get_template('login.html')
                return tmpl.render(title="login")
        else:
            tmpl = env.get_template('login.html')
            return tmpl.render(title="login")
    @cherrypy.expose
    def recruitStorePersonnel(self):
        hosp=accountManagementHelper.RetreiveExistingHopitalDetails()
        cookie = cherrypy.request.cookie
        mes=[]
        for key in cookie.keys():
            if key=="MPS-DefaultAdmin":
                if len(cookie[key])!=0:
                    mes.append(key)
            elif key=="MPS-Admin":
                if len(cookie[key])!=0:
                    mes.append(key)
            elif key=="MPS-BackDoor":
                if len(cookie[key])!=0:
                    mes.append(key)
            elif key=="MPS-HumanR":
                if len(cookie[key])!=0:
                    mes.append(key)
        if len(mes)!=0:
            if mes[0]=="MPS-DefaultAdmin" or mes[0]=="MPS-Admin":
                if mes[0]=="MPS-Admin":
                    staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Admin-Id"].value)
                    message0=staffDtl.message
                elif mes[0]=="MPS-DefaultAdmin":
                    message0=["MPS-DefaultAdmin"]
                tmpl = env.get_template('pageNotFoundHumanResource.html')
                return tmpl.render(title="page not found",message0=message0)
            elif mes[0]=="MPS-BackDoor" or mes[0]=="MPS-HumanR":
                if mes[0]=="MPS-BackDoor":
                    message0=["MPS-BackDoor",cookie["MPS-BackDoor"].value]
                elif mes[0]=="MPS-HumanR":
                    staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-HumanR-Id"].value)
                    message0=staffDtl.message
                tmpl = env.get_template('recruitStorePersonnel.html')
                return tmpl.render(hospitalDetails=hosp.hospitalDetails,title="recruit Store Personnel",message0=message0)
            else:
                tmpl = env.get_template('login.html')
                return tmpl.render(title="login")
        else:
            tmpl = env.get_template('login.html')
            return tmpl.render(title="login")
    @cherrypy.expose
    def addStorePersonnelResult(self,**kwags):
        try:
            hosp=accountManagementHelper.RetreiveExistingHopitalDetails()
            cookie = cherrypy.request.cookie
            mes=[]
            for key in cookie.keys():
                if key=="MPS-DefaultAdmin":
                    if len(cookie[key])!=0:
                        mes.append(key)
                elif key=="MPS-Admin":
                    if len(cookie[key])!=0:
                        mes.append(key)
                elif key=="MPS-BackDoor":
                    if len(cookie[key])!=0:
                        mes.append(key)
                elif key=="MPS-HumanR":
                    if len(cookie[key])!=0:
                        mes.append(key)
            if len(mes)!=0:
                if mes[0]=="MPS-DefaultAdmin" or mes[0]=="MPS-Admin":
                    if mes[0]=="MPS-Admin":
                        staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Admin-Id"].value)
                        message0=staffDtl.message
                    elif mes[0]=="MPS-DefaultAdmin":
                        message0=["MPS-DefaultAdmin"]
                    tmpl = env.get_template('pageNotFoundHumanResource.html')
                    return tmpl.render(title="page not found",message0=message0)
                elif mes[0]=="MPS-BackDoor" or mes[0]=="MPS-HumanR":
                    if mes[0]=="MPS-BackDoor":
                        message0=["MPS-BackDoor",cookie["MPS-BackDoor"].value]
                    elif mes[0]=="MPS-HumanR":
                        staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-HumanR-Id"].value)
                        message0=staffDtl.message
                    addNewStorePersonnel=humanResourceHelper.AddHospitalStorePersonnel(**kwags)
                    tmpl = env.get_template('staffAddResult.html')
                    return tmpl.render(message=addNewStorePersonnel.message,hospitalDetails=hosp.hospitalDetails,title="Add Doctor Results",message0=message0)
                else:
                    tmpl = env.get_template('login.html')
                    return tmpl.render(title="login")
            else:
                tmpl = env.get_template('login.html')
                return tmpl.render(title="login")
        except:
            hosp=accountManagementHelper.RetreiveExistingHopitalDetails()
            cookie = cherrypy.request.cookie
            mes=[]
            for key in cookie.keys():
                if key=="MPS-DefaultAdmin":
                    if len(cookie[key])!=0:
                        mes.append(key)
                elif key=="MPS-Admin":
                    if len(cookie[key])!=0:
                        mes.append(key)
                elif key=="MPS-BackDoor":
                    if len(cookie[key])!=0:
                        mes.append(key)
                elif key=="MPS-HumanR":
                    if len(cookie[key])!=0:
                        mes.append(key)
            if len(mes)!=0:
                if mes[0]=="MPS-DefaultAdmin" or mes[0]=="MPS-Admin":
                    if mes[0]=="MPS-Admin":
                        staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Admin-Id"].value)
                        message0=staffDtl.message
                    elif mes[0]=="MPS-DefaultAdmin":
                        message0=["MPS-DefaultAdmin"]
                    tmpl = env.get_template('pageNotFoundHumanResource.html')
                    return tmpl.render(title="page not found",message0=message0)
                elif mes[0]=="MPS-BackDoor" or mes[0]=="MPS-HumanR":
                    if mes[0]=="MPS-BackDoor":
                        message0=["MPS-BackDoor",cookie["MPS-BackDoor"].value]
                    elif mes[0]=="MPS-HumanR":
                        staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-HumanR-Id"].value)
                        message0=staffDtl.message
                    tmpl = env.get_template('index.html')
                    return tmpl.render(hospitalDetails=hosp.hospitalDetails,title="Home ",message0=message0)
                else:
                    tmpl = env.get_template('login.html')
                    return tmpl.render(title="login")
            else:
                tmpl = env.get_template('login.html')
                return tmpl.render(title="login")
    @cherrypy.expose
    def viewAvailableStorePersonnels(self):
        hosp=accountManagementHelper.RetreiveExistingHopitalDetails()
        cookie = cherrypy.request.cookie
        mes=[]
        for key in cookie.keys():
            if key=="MPS-DefaultAdmin":
                if len(cookie[key])!=0:
                    mes.append(key)
            elif key=="MPS-Admin":
                if len(cookie[key])!=0:
                    mes.append(key)
            elif key=="MPS-BackDoor":
                if len(cookie[key])!=0:
                    mes.append(key)
            elif key=="MPS-HumanR":
                if len(cookie[key])!=0:
                    mes.append(key)
        if len(mes)!=0:
            if mes[0]=="MPS-DefaultAdmin" or mes[0]=="MPS-Admin":
                if mes[0]=="MPS-Admin":
                    staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Admin-Id"].value)
                    message0=staffDtl.message
                elif mes[0]=="MPS-DefaultAdmin":
                    message0=["MPS-DefaultAdmin"]
                tmpl = env.get_template('pageNotFoundHumanResource.html')
                return tmpl.render(title="page not found",message0=message0)
            elif mes[0]=="MPS-BackDoor" or mes[0]=="MPS-HumanR":
                if mes[0]=="MPS-BackDoor":
                    message0=["MPS-BackDoor",cookie["MPS-BackDoor"].value]
                elif mes[0]=="MPS-HumanR":
                    staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-HumanR-Id"].value)
                    message0=staffDtl.message
                availableStorePersonnels=humanResourceHelper.RetrieveAvailableHospitalStorePersonnel()
                tmpl = env.get_template('availableStorePersonnels.html')
                return tmpl.render(message=availableStorePersonnels.message,hospitalDetails=hosp.hospitalDetails,title="Add Doctor Results",message0=message0)
            else:
                tmpl = env.get_template('login.html')
                return tmpl.render(title="login")
        else:
            tmpl = env.get_template('login.html')
            return tmpl.render(title="login")
