import cherrypy
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('nurseMIS/templates'))
from systemAdminMIS.helpers import accountManagementHelper
from nurseMIS.helpers import principleNurseOfficerHelper
class PNOMIS(object):
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
            elif mes[0]=="MPS-BackDoor" or mes[0]=="MPS-PrincipleNO":
                if mes[0]=="MPS-BackDoor":
                    message0=["MPS-BackDoor",cookie["MPS-BackDoor"].value]
                elif mes[0]=="MPS-PrincipleNO":
                    staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-PrincipleNO-Id"].value)
                    message0=staffDtl.message
                tmpl = env.get_template('index.html')
                return tmpl.render(hospitalDetails=hosp.hospitalDetails,title="Home PNO",message0=message0)
            elif mes[0]=="MPS-HumanR":
                staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-PrincipleNO-Id"].value)
                message0=staffDtl.message
                tmpl = env.get_template('pageNotFoundPrincipleNurseOfficer.html')
                return tmpl.render(title="page not found",message0=message0)
            elif mes[0]=="MPS-Nurse":
                if int(cookie['MPS-Nurse-1-2'].value)==2 or int(cookie['MPS-Nurse-1-2'].value)==1:
                    if cookie['MPS-Nurse-D'].value=="D000":
                        staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Nurse-Id"].value)
                        message0=staffDtl.message
                        tmpl = env.get_template('pageNotFoundSingletonFrontDesk.html')
                        return tmpl.render(title="page not found",message0=message0)
                    elif cookie['MPS-Nurse-D'].value=="D001":
                        staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Nurse-Id"].value)
                        message0=staffDtl.message
                        tmpl = env.get_template('pageNotFoundSingletonTriage.html')
                        return tmpl.render(title="page not found",message0=message0)
                    else:
                        tmpl = env.get_template('login.html')
                        return tmpl.render(title="login")
                else:
                    tmpl = env.get_template('login.html')
                    return tmpl.render(title="login")
            else:
                tmpl = env.get_template('login.html')
                return tmpl.render(title="login")
        else:
            tmpl = env.get_template('login.html')
            return tmpl.render(title="login")
    @cherrypy.expose
    def unassignedNurses(self):
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
            elif mes[0]=="MPS-BackDoor" or mes[0]=="MPS-PrincipleNO":
                if mes[0]=="MPS-BackDoor":
                    message0=["MPS-BackDoor",cookie["MPS-BackDoor"].value]
                elif mes[0]=="MPS-PrincipleNO":
                    staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-PrincipleNO-Id"].value)
                    message0=staffDtl.message
                unassgnNrs=principleNurseOfficerHelper.RetrieveUnsignedHospitalNurses()
                tmpl = env.get_template('unassignedNurses.html')
                return tmpl.render(message=unassgnNrs.message,departments=unassgnNrs.departments,hospitalDetails=hosp.hospitalDetails,title="Home PNO",message0=message0)
            elif mes[0]=="MPS-HumanR":
                staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-PrincipleNO-Id"].value)
                message0=staffDtl.message
                tmpl = env.get_template('pageNotFoundPrincipleNurseOfficer.html')
                return tmpl.render(title="page not found",message0=message0)
            elif mes[0]=="MPS-Nurse":
                if int(cookie['MPS-Nurse-1-2'].value)==2 or int(cookie['MPS-Nurse-1-2'].value)==1:
                    if cookie['MPS-Nurse-D'].value=="D000":
                        staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Nurse-Id"].value)
                        message0=staffDtl.message
                        tmpl = env.get_template('pageNotFoundSingletonFrontDesk.html')
                        return tmpl.render(title="page not found",message0=message0)
                    elif cookie['MPS-Nurse-D'].value=="D001":
                        staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Nurse-Id"].value)
                        message0=staffDtl.message
                        tmpl = env.get_template('pageNotFoundSingletonTriage.html')
                        return tmpl.render(title="page not found",message0=message0)
                    else:
                        tmpl = env.get_template('login.html')
                        return tmpl.render(title="login")
                else:
                    tmpl = env.get_template('login.html')
                    return tmpl.render(title="login")
            else:
                tmpl = env.get_template('login.html')
                return tmpl.render(title="login")
        else:
            tmpl = env.get_template('login.html')
            return tmpl.render(title="login")
    @cherrypy.expose
    def AssignNurseToDepartmentPOST(self,**kwags):
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
                elif mes[0]=="MPS-BackDoor" or mes[0]=="MPS-PrincipleNO":
                    if mes[0]=="MPS-BackDoor":
                        message0=["MPS-BackDoor",cookie["MPS-BackDoor"].value]
                    elif mes[0]=="MPS-PrincipleNO":
                        staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-PrincipleNO-Id"].value)
                        message0=staffDtl.message
                    assgnNr=principleNurseOfficerHelper.AssignNurseToDepartment(**kwags)
                    unassgnNrs=principleNurseOfficerHelper.RetrieveUnsignedHospitalNurses()
                    tmpl = env.get_template('unassignedNurses.html')
                    return tmpl.render(message=unassgnNrs.message,departments=unassgnNrs.departments,hospitalDetails=hosp.hospitalDetails,title="Home PNO",message0=message0)
                elif mes[0]=="MPS-HumanR":
                    staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-PrincipleNO-Id"].value)
                    message0=staffDtl.message
                    tmpl = env.get_template('pageNotFoundPrincipleNurseOfficer.html')
                    return tmpl.render(title="page not found",message0=message0)
                elif mes[0]=="MPS-Nurse":
                    if int(cookie['MPS-Nurse-1-2'].value)==2 or int(cookie['MPS-Nurse-1-2'].value)==1:
                        if cookie['MPS-Nurse-D'].value=="D000":
                            staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Nurse-Id"].value)
                            message0=staffDtl.message
                            tmpl = env.get_template('pageNotFoundSingletonFrontDesk.html')
                            return tmpl.render(title="page not found",message0=message0)
                        elif cookie['MPS-Nurse-D'].value=="D001":
                            staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Nurse-Id"].value)
                            message0=staffDtl.message
                            tmpl = env.get_template('pageNotFoundSingletonTriage.html')
                            return tmpl.render(title="page not found",message0=message0)
                        else:
                            tmpl = env.get_template('login.html')
                            return tmpl.render(title="login")
                    else:
                        tmpl = env.get_template('login.html')
                        return tmpl.render(title="login")
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
                elif mes[0]=="MPS-BackDoor" or mes[0]=="MPS-PrincipleNO":
                    if mes[0]=="MPS-BackDoor":
                        message0=["MPS-BackDoor",cookie["MPS-BackDoor"].value]
                    elif mes[0]=="MPS-PrincipleNO":
                        staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-PrincipleNO-Id"].value)
                        message0=staffDtl.message
                    unassgnNrs=principleNurseOfficerHelper.RetrieveUnsignedHospitalNurses()
                    tmpl = env.get_template('unassignedNurses.html')
                    return tmpl.render(message=unassgnNrs.message,departments=unassgnNrs.departments,hospitalDetails=hosp.hospitalDetails,title="Home PNO",message0=message0)
                elif mes[0]=="MPS-HumanR":
                    staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-PrincipleNO-Id"].value)
                    message0=staffDtl.message
                    tmpl = env.get_template('pageNotFoundPrincipleNurseOfficer.html')
                    return tmpl.render(title="page not found",message0=message0)
                elif mes[0]=="MPS-Nurse":
                    if int(cookie['MPS-Nurse-1-2'].value)==2 or int(cookie['MPS-Nurse-1-2'].value)==1:
                        if cookie['MPS-Nurse-D'].value=="D000":
                            staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Nurse-Id"].value)
                            message0=staffDtl.message
                            tmpl = env.get_template('pageNotFoundSingletonFrontDesk.html')
                            return tmpl.render(title="page not found",message0=message0)
                        elif cookie['MPS-Nurse-D'].value=="D001":
                            staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Nurse-Id"].value)
                            message0=staffDtl.message
                            tmpl = env.get_template('pageNotFoundSingletonTriage.html')
                            return tmpl.render(title="page not found",message0=message0)
                        else:
                            tmpl = env.get_template('login.html')
                            return tmpl.render(title="login")
                    else:
                        tmpl = env.get_template('login.html')
                        return tmpl.render(title="login")
                else:
                    tmpl = env.get_template('login.html')
                    return tmpl.render(title="login")
            else:
                tmpl = env.get_template('login.html')
                return tmpl.render(title="login")
    @cherrypy.expose
    def assignedNurses(self):
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
            elif mes[0]=="MPS-BackDoor" or mes[0]=="MPS-PrincipleNO":
                if mes[0]=="MPS-BackDoor":
                    message0=["MPS-BackDoor",cookie["MPS-BackDoor"].value]
                elif mes[0]=="MPS-PrincipleNO":
                    staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-PrincipleNO-Id"].value)
                    message0=staffDtl.message
                unassgnNrs=principleNurseOfficerHelper.RetrieveAssignedHospitalNurses()
                tmpl = env.get_template('assignedNurses.html')
                return tmpl.render(message=unassgnNrs.message,departments=unassgnNrs.departments,hospitalDetails=hosp.hospitalDetails,title="Home PNO",message0=message0)
            elif mes[0]=="MPS-HumanR":
                staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-PrincipleNO-Id"].value)
                message0=staffDtl.message
                tmpl = env.get_template('pageNotFoundPrincipleNurseOfficer.html')
                return tmpl.render(title="page not found",message0=message0)
            elif mes[0]=="MPS-Nurse":
                if int(cookie['MPS-Nurse-1-2'].value)==2 or int(cookie['MPS-Nurse-1-2'].value)==1:
                    if cookie['MPS-Nurse-D'].value=="D000":
                        staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Nurse-Id"].value)
                        message0=staffDtl.message
                        tmpl = env.get_template('pageNotFoundSingletonFrontDesk.html')
                        return tmpl.render(title="page not found",message0=message0)
                    elif cookie['MPS-Nurse-D'].value=="D001":
                        staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Nurse-Id"].value)
                        message0=staffDtl.message
                        tmpl = env.get_template('pageNotFoundSingletonTriage.html')
                        return tmpl.render(title="page not found",message0=message0)
                    else:
                        tmpl = env.get_template('login.html')
                        return tmpl.render(title="login")
                else:
                    tmpl = env.get_template('login.html')
                    return tmpl.render(title="login")
            else:
                tmpl = env.get_template('login.html')
                return tmpl.render(title="login")
        else:
            tmpl = env.get_template('login.html')
            return tmpl.render(title="login")
    @cherrypy.expose
    def AssignNurseToOneMoreDepartmentPOST(self,**kwags):
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
                elif mes[0]=="MPS-BackDoor" or mes[0]=="MPS-PrincipleNO":
                    if mes[0]=="MPS-BackDoor":
                        message0=["MPS-BackDoor",cookie["MPS-BackDoor"].value]
                    elif mes[0]=="MPS-PrincipleNO":
                        staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-PrincipleNO-Id"].value)
                        message0=staffDtl.message
                    principleNurseOfficerHelper.AssignNurseToOneMoreDepartment(**kwags)
                    assgnNrs=principleNurseOfficerHelper.RetrieveAssignedHospitalNurses()
                    tmpl = env.get_template('assignedNurses.html')
                    return tmpl.render(message=assgnNrs.message,departments=assgnNrs.departments,hospitalDetails=hosp.hospitalDetails,title="Home PNO",message0=message0)
                elif mes[0]=="MPS-HumanR":
                    staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-PrincipleNO-Id"].value)
                    message0=staffDtl.message
                    tmpl = env.get_template('pageNotFoundPrincipleNurseOfficer.html')
                    return tmpl.render(title="page not found",message0=message0)
                elif mes[0]=="MPS-Nurse":
                    if int(cookie['MPS-Nurse-1-2'].value)==2 or int(cookie['MPS-Nurse-1-2'].value)==1:
                        if cookie['MPS-Nurse-D'].value=="D000":
                            staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Nurse-Id"].value)
                            message0=staffDtl.message
                            tmpl = env.get_template('pageNotFoundSingletonFrontDesk.html')
                            return tmpl.render(title="page not found",message0=message0)
                        elif cookie['MPS-Nurse-D'].value=="D001":
                            staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Nurse-Id"].value)
                            message0=staffDtl.message
                            tmpl = env.get_template('pageNotFoundSingletonTriage.html')
                            return tmpl.render(title="page not found",message0=message0)
                        else:
                            tmpl = env.get_template('login.html')
                            return tmpl.render(title="login")
                    else:
                        tmpl = env.get_template('login.html')
                        return tmpl.render(title="login")
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
                elif mes[0]=="MPS-BackDoor" or mes[0]=="MPS-PrincipleNO":
                    if mes[0]=="MPS-BackDoor":
                        message0=["MPS-BackDoor",cookie["MPS-BackDoor"].value]
                    elif mes[0]=="MPS-PrincipleNO":
                        staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-PrincipleNO-Id"].value)
                        message0=staffDtl.message
                    unassgnNrs=principleNurseOfficerHelper.RetrieveUnsignedHospitalNurses()
                    tmpl = env.get_template('unassignedNurses.html')
                    return tmpl.render(message=unassgnNrs.message,departments=unassgnNrs.departments,hospitalDetails=hosp.hospitalDetails,title="Home PNO",message0=message0)
                elif mes[0]=="MPS-HumanR":
                    staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-PrincipleNO-Id"].value)
                    message0=staffDtl.message
                    tmpl = env.get_template('pageNotFoundPrincipleNurseOfficer.html')
                    return tmpl.render(title="page not found",message0=message0)
                elif mes[0]=="MPS-Nurse":
                    if int(cookie['MPS-Nurse-1-2'].value)==2 or int(cookie['MPS-Nurse-1-2'].value)==1:
                        if cookie['MPS-Nurse-D'].value=="D000":
                            staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Nurse-Id"].value)
                            message0=staffDtl.message
                            tmpl = env.get_template('pageNotFoundSingletonFrontDesk.html')
                            return tmpl.render(title="page not found",message0=message0)
                        elif cookie['MPS-Nurse-D'].value=="D001":
                            staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Nurse-Id"].value)
                            message0=staffDtl.message
                            tmpl = env.get_template('pageNotFoundSingletonTriage.html')
                            return tmpl.render(title="page not found",message0=message0)
                        else:
                            tmpl = env.get_template('login.html')
                            return tmpl.render(title="login")
                    else:
                        tmpl = env.get_template('login.html')
                        return tmpl.render(title="login")
                else:
                    tmpl = env.get_template('login.html')
                    return tmpl.render(title="login")
            else:
                tmpl = env.get_template('login.html')
                return tmpl.render(title="login")
