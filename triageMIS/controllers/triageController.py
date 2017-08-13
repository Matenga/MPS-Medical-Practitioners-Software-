import cherrypy
from systemAdminMIS.helpers import accountManagementHelper
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('triageMIS/templates'))
class TRMIS(object):
    #def __init__(self):
        #self.humanResource = humanRM.HumanResource()
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
            elif key=="MPS-PrincipleNO":
                if len(cookie[key])!=0:
                    mes.append(key)
            elif key=="MPS-Nurse":
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
            elif mes[0]=="MPS-BackDoor" or mes[0]=="MPS-Nurse":
                if mes[0]=="MPS-BackDoor":
                    message0=["MPS-BackDoor",cookie["MPS-BackDoor"].value]
                    tmpl = env.get_template('index.html')
                    return tmpl.render(oneTwo=2,hospitalDetails=hosp.hospitalDetails,title="Duo Account Access",message0=message0)
                elif mes[0]=="MPS-Nurse":
                    if int(cookie['MPS-Nurse-1-2'].value)==2 or int(cookie['MPS-nurse-1-2'].value)==1:
                        if cookie['MPS-Nurse-D'].value=="D001":
                            staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Nurse-Id"].value)
                            message0=staffDtl.message
                            tmpl = env.get_template('index.html')
                            return tmpl.render(oneTwo=int(cookie['MPS-Nurse-1-2'].value),hospitalDetails=hosp.hospitalDetails,title="home Front Desk",message0=message0)
                        elif cookie['MPS-Nurse-D'].value=="D000":
                            if int(cookie['MPS-Nurse-1-2'].value)==1:
                                staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Nurse-Id"].value)
                                message0=staffDtl.message
                                tmpl = env.get_template('pageNotFoundSingletonFrontDesk.html')
                                return tmpl.render(title="page not found",message0=message0)
                            if int(cookie['MPS-Nurse-1-2'].value)==2:
                                staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Nurse-Id"].value)
                                message0=staffDtl.message
                                tmpl = env.get_template('duoNurseTriageAccountSwitcher.html')
                                return tmpl.render(title="Duo Account Switcher",message0=message0)
                            else:
                                tmpl = env.get_template('login.html')
                                return tmpl.render(title="login")
                        else:
                            tmpl = env.get_template('login.html')
                            return tmpl.render(title="login")
                    else:
                        tmpl = env.get_template('login.html')
                        return tmpl.render(title="login")
            elif mes[0]=="MPS-PrincipleNO":
                staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-PrincipleNO-Id"].value)
                message0=staffDtl.message
                tmpl = env.get_template('pageNotFoundPrincipleNurseOfficer.html')
                return tmpl.render(title="page not found",message0=message0)
            elif mes[0]=="MPS-HumanR":
                staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-HumanR-Id"].value)
                message0=staffDtl.message
                tmpl = env.get_template('pageNotFoundHumanResource.html')
                return tmpl.render(title="page not found",message0=message0)
            else:
                tmpl = env.get_template('login.html')
                return tmpl.render(title="login")
        else:
            tmpl = env.get_template('login.html')
            return tmpl.render(title="login")
    @cherrypy.expose
    def registerNewPatientGET(self):
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
            elif key=="MPS-PrincipleNO":
                if len(cookie[key])!=0:
                    mes.append(key)
            elif key=="MPS-Nurse":
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
            elif mes[0]=="MPS-BackDoor" or mes[0]=="MPS-Nurse":
                if mes[0]=="MPS-BackDoor":
                    message0=["MPS-BackDoor",cookie["MPS-BackDoor"].value]
                    tmpl = env.get_template('registerNewPatient.html')
                    return tmpl.render(oneTwo=2,hospitalDetails=hosp.hospitalDetails,title="Duo Account Access",message0=message0)
                elif mes[0]=="MPS-Nurse":
                    if int(cookie['MPS-Nurse-1-2'].value)==2 or int(cookie['MPS-nurse-1-2'].value)==1:
                        if cookie['MPS-Nurse-D'].value=="D001":
                            staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Nurse-Id"].value)
                            message0=staffDtl.message
                            tmpl = env.get_template('registerNewPatient.html')
                            return tmpl.render(oneTwo=int(cookie['MPS-Nurse-1-2'].value),hospitalDetails=hosp.hospitalDetails,title="home Front Desk",message0=message0)
                        elif cookie['MPS-Nurse-D'].value=="D000":
                            if int(cookie['MPS-Nurse-1-2'].value)==1:
                                staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Nurse-Id"].value)
                                message0=staffDtl.message
                                tmpl = env.get_template('pageNotFoundSingletonFrontDesk.html')
                                return tmpl.render(title="page not found",message0=message0)
                            if int(cookie['MPS-Nurse-1-2'].value)==2:
                                staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Nurse-Id"].value)
                                message0=staffDtl.message
                                tmpl = env.get_template('duoNurseTriageAccountSwitcher.html')
                                return tmpl.render(title="Duo Account Switcher",message0=message0)
                            else:
                                tmpl = env.get_template('login.html')
                                return tmpl.render(title="login")
                        else:
                            tmpl = env.get_template('login.html')
                            return tmpl.render(title="login")
                    else:
                        tmpl = env.get_template('login.html')
                        return tmpl.render(title="login")
            elif mes[0]=="MPS-PrincipleNO":
                staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-PrincipleNO-Id"].value)
                message0=staffDtl.message
                tmpl = env.get_template('pageNotFoundPrincipleNurseOfficer.html')
                return tmpl.render(title="page not found",message0=message0)
            elif mes[0]=="MPS-HumanR":
                staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-HumanR-Id"].value)
                message0=staffDtl.message
                tmpl = env.get_template('pageNotFoundHumanResource.html')
                return tmpl.render(title="page not found",message0=message0)
            else:
                tmpl = env.get_template('login.html')
                return tmpl.render(title="login")
        else:
            tmpl = env.get_template('login.html')
            return tmpl.render(title="login")
