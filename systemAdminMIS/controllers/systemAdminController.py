import cherrypy
from systemAdminMIS.helpers import accountManagementHelper
from jinja2 import Environment, FileSystemLoader
from passlib.hash import pbkdf2_sha256
env = Environment(loader=FileSystemLoader('systemAdminMIS/templates'))
class SAMIS(object):
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
            if mes[0]=="MPS-DefaultAdmin" or mes[0]=="MPS-Admin" or mes[0]=="MPS-BackDoor":
                if mes[0]=="MPS-Admin":
                    staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Admin-Id"].value)
                    message0=staffDtl.message
                elif mes[0]=="MPS-DefaultAdmin":
                    message0=["MPS-DefaultAdmin"]
                elif mes[0]=="MPS-BackDoor":
                    message0=["MPS-BackDoor",cookie["MPS-BackDoor"].value]
                tmpl = env.get_template('home.html')
                return tmpl.render(hospitalDetails=hosp.hospitalDetails,title="Admin home",message0=message0)
            elif mes[0]=="MPS-HumanR":
                staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-HumanR-Id"].value)
                message0=staffDtl.message
                tmpl = env.get_template('pageNotFoundHumanResource.html')
                return tmpl.render(title="page not found",message0=message0)
            elif mes[0]=="MPS-PrincipleNO":
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
                        tmpl = env.get_template('index.html')
                        return tmpl.render(title="login")
                else:
                    tmpl = env.get_template('index.html')
                    return tmpl.render(title="login")
            else:
                tmpl = env.get_template('index.html')
                return tmpl.render(title="login")
        else:
            tmpl = env.get_template('index.html')
            return tmpl.render(title="login")
    @cherrypy.expose
    def duoAccountDispatcherPOST(self,**kwags):
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
                elif mes[0]=="MPS-BackDoor" or mes[0]=="MPS-Nurse":
                    if mes[0]=="MPS-BackDoor":
                        message0=["MPS-BackDoor",cookie["MPS-BackDoor"].value]
                        try:
                            if int(cookie['MPS-BackDoor-1-2'])==2:
                                if kwags['accountId']=="D000":
                                    cookie0 = cherrypy.response.cookie
                                    cookie0['MPS-BackDoor-D'] = kwags['accountId']
                                    cookie0['MPS-BackDoor-D']['path'] = '/'
                                    cookie0['MPS-BackDoor-D']['max-age'] = 36000000
                                    cookie0['MPS-BackDoor-D']['version'] = 1
                                    hosp=accountManagementHelper.RetreiveExistingHopitalDetails()
                                    tmpl = env.get_template('duoFrontDeskDispatcher.html')
                                    return tmpl.render(hospitalDetails=hosp.hospitalDetails,title="Front Desk Account Switcher",message=message0)
                                elif kwags['accountId']=="D001":
                                    cookie0 = cherrypy.response.cookie
                                    cookie0['MPS-BackDoor-D'] = kwags['accountId']
                                    cookie0['MPS-BackDoor-D']['path'] = '/'
                                    cookie0['MPS-BackDoor-D']['max-age'] = 36000000
                                    cookie0['MPS-BackDoor-D']['version'] = 1
                                    hosp=accountManagementHelper.RetreiveExistingHopitalDetails()
                                    tmpl = env.get_template('duoTriageDispatcher.html')
                                    return tmpl.render(hospitalDetails=hosp.hospitalDetails,title="Triage Account Switcher",message=message0)
                                else:
                                    tmpl = env.get_template('index.html')
                                    return tmpl.render(title="login")
                            else:
                                tmpl = env.get_template('index.html')
                                return tmpl.render(title="login")
                        except:
                            cookie0 = cherrypy.response.cookie
                            cookie0['MPS-BackDoor-1-2'] = 2
                            cookie0['MPS-BackDoor-1-2']['path'] = '/'
                            cookie0['MPS-BackDoor-1-2']['max-age'] = 36000000
                            cookie0['MPS-BackDoor-1-2']['version'] = 1
                            hosp=accountManagementHelper.RetreiveExistingHopitalDetails()
                            tmpl = env.get_template('duoNurseAccountDispatcher.html')
                            return tmpl.render(hospitalDetails=hosp.hospitalDetails,title="Duo Account Access",message=message0)
                    elif mes[0]=="MPS-Nurse":
                        if int(cookie['MPS-Nurse-1-2'].value)==2:
                            if kwags['accountId']=="D000":
                                cookie0 = cherrypy.response.cookie
                                cookie0['MPS-Nurse-D'] = kwags['accountId']
                                cookie0['MPS-Nurse-D']['path'] = '/'
                                cookie0['MPS-Nurse-D']['max-age'] = 36000000
                                cookie0['MPS-Nurse-D']['version'] = 1
                                kwag={'staff_id':cookie['MPS-Nurse-Id'].value}
                                staffDtl=accountManagementHelper.RetrieveStaffDetails(**kwag)
                                message=staffDtl.message
                                hosp=accountManagementHelper.RetreiveExistingHopitalDetails()
                                tmpl = env.get_template('duoFrontDeskDispatcher.html')
                                return tmpl.render(hospitalDetails=hosp.hospitalDetails,title="Front Desk Account Switcher",message=message)
                            elif kwags['accountId']=="D001":
                                cookie0 = cherrypy.response.cookie
                                cookie0['MPS-Nurse-D'] = kwags['accountId']
                                cookie0['MPS-Nurse-D']['path'] = '/'
                                cookie0['MPS-Nurse-D']['max-age'] = 36000000
                                cookie0['MPS-Nurse-D']['version'] = 1
                                kwag={'staff_id':cookie['MPS-Nurse-Id'].value}
                                staffDtl=accountManagementHelper.RetrieveStaffDetails(**kwag)
                                message=staffDtl.message
                                hosp=accountManagementHelper.RetreiveExistingHopitalDetails()
                                tmpl = env.get_template('duoTriageDispatcher.html')
                                return tmpl.render(hospitalDetails=hosp.hospitalDetails,title="Triage Account Switcher",message=message)
                            else:
                                tmpl = env.get_template('index.html')
                                return tmpl.render(title="login")
                        elif int(cookie['MPS-Nurse-1-2'].value)==1:
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
                                tmpl = env.get_template('index.html')
                                return tmpl.render(title="login")
                        else:
                            tmpl = env.get_template('index.html')
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
                    tmpl = env.get_template('index.html')
                    return tmpl.render(title="login")
            else:
                tmpl = env.get_template('index.html')
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
                elif mes[0]=="MPS-BackDoor" or mes[0]=="MPS-Nurse":
                    if mes[0]=="MPS-BackDoor":
                        message0=["MPS-BackDoor",cookie["MPS-BackDoor"].value]
                        hosp=accountManagementHelper.RetreiveExistingHopitalDetails()
                        tmpl = env.get_template('duoNurseAccountDispatcher.html')
                        return tmpl.render(hospitalDetails=hosp.hospitalDetails,title="Duo Account Access",message=message0)
                    elif mes[0]=="MPS-Nurse":
                        if int(cookie['MPS-Nurse-1-2'].value)==2:
                            staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Nurse-Id"].value)
                            message0=staffDtl.message
                            tmpl = env.get_template('duoNurseAccountDispatcher.html')
                            return tmpl.render(hospitalDetails=hosp.hospitalDetails,title="Duo Account Access",message=message0)
                        elif int(cookie['MPS-Nurse-1-2'].value)==1:
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
                                tmpl = env.get_template('index.html')
                                return tmpl.render(title="login")
                        else:
                            tmpl = env.get_template('index.html')
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
                    tmpl = env.get_template('index.html')
                    return tmpl.render(title="login")
            else:
                tmpl = env.get_template('index.html')
                return tmpl.render(title="login")
    @cherrypy.expose
    def home(self,**kwags):
        hosp=accountManagementHelper.RetreiveExistingHopitalDetails()
        try:
            login=accountManagementHelper.LogIn(**kwags)
            if login.mes=='default' or login.mes=="System Administrator":
                if login.mes=='default':
                    cookie = cherrypy.response.cookie
                    cookie['MPS-DefaultAdmin'] = kwags['username']
                    cookie['MPS-DefaultAdmin']['path'] = '/'
                    cookie['MPS-DefaultAdmin']['max-age'] = 36000000
                    cookie['MPS-DefaultAdmin']['version'] = 1
                    mes="MPS-DefaultAdmin"
                    message0=["MPS-DefaultAdmin"]
                    # cherrypy.request.login=kwags['username']
                else:
                    cookie = cherrypy.response.cookie
                    cookie['MPS-Admin'] = kwags['username']
                    cookie['MPS-Admin']['path'] = '/'
                    cookie['MPS-Admin']['max-age'] = 36000000
                    cookie['MPS-Admin']['version'] = 1
                    cookie['MPS-Admin-Id'] = login.staff_id
                    cookie['MPS-Admin-Id']['path'] = '/'
                    cookie['MPS-Admin-Id']['max-age'] = 36000000
                    cookie['MPS-Admin-Id']['version'] = 1
                    mes="MPS-Admin"
                    kwag={'staff_id':login.staff_id}
                    staffDtl=accountManagementHelper.RetrieveStaffDetails(**kwag)
                    message=staffDtl.message
                tmpl = env.get_template('home.html')
                return tmpl.render(hospitalDetails=hosp.hospitalDetails,title="Admin Home",mes=mes,message=message)
            elif login.mes=="backdoor":
                puzzle=accountManagementHelper.FilteredPuzzle()
                print("bs")
                tmpl = env.get_template('backDoorPuzzle.html')
                return tmpl.render(puzzle=puzzle.puzzle,title="puzzle")
            elif login.mes=="Human Resource":
                cookie = cherrypy.response.cookie
                cookie['MPS-HumanR'] = kwags['username']
                cookie['MPS-HumanR']['path'] = '/'
                cookie['MPS-HumanR']['max-age'] = 36000000
                cookie['MPS-HumanR']['version'] = 1
                cookie['MPS-HumanR-Id'] = login.staff_id
                cookie['MPS-HumanR-Id']['path'] = '/'
                cookie['MPS-HumanR-Id']['max-age'] = 36000000
                cookie['MPS-HumanR-Id']['version'] = 1
                kwag={'staff_id':login.staff_id}
                staffDtl=accountManagementHelper.RetrieveStaffDetails(**kwag)
                message=staffDtl.message
                hosp=accountManagementHelper.RetreiveExistingHopitalDetails()
                tmpl = env.get_template('humanResourceAccountDispatcher.html')
                return tmpl.render(hospitalDetails=hosp.hospitalDetails,title="Human resource system",message=message)
            elif login.mes=="Principle Nurse Officer":
                cookie = cherrypy.response.cookie
                cookie['MPS-PrincipleNO'] = kwags['username']
                cookie['MPS-PrincipleNO']['path'] = '/'
                cookie['MPS-PrincipleNO']['max-age'] = 36000000
                cookie['MPS-PrincipleNO']['version'] = 1
                cookie['MPS-PrincipleNO-Id'] = login.staff_id
                cookie['MPS-PrincipleNO-Id']['path'] = '/'
                cookie['MPS-PrincipleNO-Id']['max-age'] = 36000000
                cookie['MPS-PrincipleNO-Id']['version'] = 1
                kwag={'staff_id':login.staff_id}
                staffDtl=accountManagementHelper.RetrieveStaffDetails(**kwag)
                message=staffDtl.message
                hosp=accountManagementHelper.RetreiveExistingHopitalDetails()
                tmpl = env.get_template('principleNurseOfficerAccountDispatcher.html')
                return tmpl.render(hospitalDetails=hosp.hospitalDetails,title="Principle Nurse Officer Module",message=message)
            elif login.mes=="Nurse":
                cookie = cherrypy.response.cookie
                cookie['MPS-Nurse'] = kwags['username']
                cookie['MPS-Nurse']['path'] = '/'
                cookie['MPS-Nurse']['max-age'] = 36000000
                cookie['MPS-Nurse']['version'] = 1
                cookie['MPS-Nurse-Id'] = login.staff_id
                cookie['MPS-Nurse-Id']['path'] = '/'
                cookie['MPS-Nurse-Id']['max-age'] = 36000000
                cookie['MPS-Nurse-Id']['version'] = 1
                if login.mes0==1:
                    cookie['MPS-Nurse-1-2'] = 1
                    cookie['MPS-Nurse-1-2']['path'] = '/'
                    cookie['MPS-Nurse-1-2']['max-age'] = 36000000
                    cookie['MPS-Nurse-1-2']['version'] = 1
                    cookie['MPS-Nurse-D'] = login.mes1
                    cookie['MPS-Nurse-D']['path'] = '/'
                    cookie['MPS-Nurse-D']['max-age'] = 36000000
                    cookie['MPS-Nurse-D']['version'] = 1
                    kwag={'staff_id':login.staff_id}
                    staffDtl=accountManagementHelper.RetrieveStaffDetails(**kwag)
                    message=staffDtl.message
                    hosp=accountManagementHelper.RetreiveExistingHopitalDetails()
                    if login.mes1=="D000":
                        tmpl = env.get_template('singletonFrontDeskNurseAccountDispatcher.html')
                    elif login.mes1=="D001":
                        tmpl = env.get_template('singletonTriageNurseAccountDispatcher.html')
                    return tmpl.render(hospitalDetails=hosp.hospitalDetails,title="Singleton Account Dispatcher",message=message)
                else:
                    cookie['MPS-Nurse-1-2'] = 2
                    cookie['MPS-Nurse-1-2']['path'] = '/'
                    cookie['MPS-Nurse-1-2']['max-age'] = 36000000
                    cookie['MPS-Nurse-1-2']['version'] = 1
                    kwag={'staff_id':login.staff_id}
                    staffDtl=accountManagementHelper.RetrieveStaffDetails(**kwag)
                    message=staffDtl.message
                    hosp=accountManagementHelper.RetreiveExistingHopitalDetails()
                    tmpl = env.get_template('duoNurseAccountDispatcher.html')
                    return tmpl.render(hospitalDetails=hosp.hospitalDetails,title="Duo Account Access",message=message)
            else:
                tmpl = env.get_template('index.html')
                return tmpl.render(title="login",unMatchedDetails="user name and password_ don't match")
        except:
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
                if mes[0]=="MPS-DefaultAdmin" or mes[0]=="MPS-Admin" or mes[0]=="MPS-BackDoor":
                    if mes[0]=="MPS-Admin":
                        staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Admin-Id"].value)
                        message0=staffDtl.message
                    elif mes[0]=="MPS-DefaultAdmin":
                        message0=["MPS-DefaultAdmin"]
                    elif mes[0]=="MPS-BackDoor":
                        message0=["MPS-BackDoor",cookie["MPS-BackDoor"].value]
                    tmpl = env.get_template('home.html')
                    return tmpl.render(hospitalDetails=hosp.hospitalDetails,title="Admin home",message0=message0)
                elif mes[0]=="MPS-HumanR":
                    staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-HumanR-Id"].value)
                    message0=staffDtl.message
                    tmpl = env.get_template('pageNotFoundHumanResource.html')
                    return tmpl.render(title="page not found",message0=message0)
                elif mes[0]=="MPS-PrincipleNO":
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
                            tmpl = env.get_template('index.html')
                            return tmpl.render(title="login")
                    else:
                        tmpl = env.get_template('index.html')
                        return tmpl.render(title="login")
                else:
                    tmpl = env.get_template('index.html')
                    return tmpl.render(title="login")
            else:
                tmpl = env.get_template('index.html')
                return tmpl.render(title="login")
    @cherrypy.expose
    def addAdmin(self):
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
            if mes[0]=="MPS-DefaultAdmin" or mes[0]=="MPS-Admin" or mes[0]=="MPS-BackDoor":
                if mes[0]=="MPS-Admin":
                    staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Admin-Id"].value)
                    message0=staffDtl.message
                elif mes[0]=="MPS-DefaultAdmin":
                    message0=["MPS-DefaultAdmin"]
                elif mes[0]=="MPS-BackDoor":
                    message0=["MPS-BackDoor",cookie["MPS-BackDoor"].value]
                tmpl = env.get_template('addAdmin.html')
                return tmpl.render(hospitalDetails=hosp.hospitalDetails,title="Add Admin",message0=message0)
            elif mes[0]=="MPS-HumanR":
                staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-HumanR-Id"].value)
                message0=staffDtl.message
                tmpl = env.get_template('pageNotFoundHumanResource.html')
                return tmpl.render(title="page not found",message0=message0)
            elif mes[0]=="MPS-PrincipleNO":
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
                        tmpl = env.get_template('index.html')
                        return tmpl.render(title="login")
                else:
                    tmpl = env.get_template('index.html')
                    return tmpl.render(title="login")
            else:
                tmpl = env.get_template('index.html')
                return tmpl.render(title="login")
        else:
            tmpl = env.get_template('index.html')
            return tmpl.render(title="login")
    @cherrypy.expose
    def hospitalDetails(self):
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
            if mes[0]=="MPS-DefaultAdmin" or mes[0]=="MPS-Admin" or mes[0]=="MPS-BackDoor":
                if mes[0]=="MPS-Admin":
                    staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Admin-Id"].value)
                    message0=staffDtl.message
                elif mes[0]=="MPS-DefaultAdmin":
                    message0=["MPS-DefaultAdmin"]
                elif mes[0]=="MPS-BackDoor":
                    message0=["MPS-BackDoor",cookie["MPS-BackDoor"].value]
                tmpl = env.get_template('hospitalDetails.html')
                return tmpl.render(hospitalDetails=hosp.hospitalDetails,title="hospitalDetails",message0=message0)
            elif mes[0]=="MPS-HumanR":
                staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-HumanR-Id"].value)
                message0=staffDtl.message
                tmpl = env.get_template('pageNotFoundHumanResource.html')
                return tmpl.render(title="page not found",message0=message0)
            elif mes[0]=="MPS-PrincipleNO":
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
                        tmpl = env.get_template('index.html')
                        return tmpl.render(title="login")
                else:
                    tmpl = env.get_template('index.html')
                    return tmpl.render(title="login")
            else:
                tmpl = env.get_template('index.html')
                return tmpl.render(title="login")
        else:
            tmpl = env.get_template('index.html')
            return tmpl.render(title="login")
    @cherrypy.expose
    def updateHospitalDetails(self,**kwags):
        try:
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
                if mes[0]=="MPS-DefaultAdmin" or mes[0]=="MPS-Admin" or mes[0]=="MPS-BackDoor":
                    if mes[0]=="MPS-Admin":
                        staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Admin-Id"].value)
                        message0=staffDtl.message
                    elif mes[0]=="MPS-DefaultAdmin":
                        message0=["MPS-DefaultAdmin"]
                    elif mes[0]=="MPS-BackDoor":
                        message0=["MPS-BackDoor",cookie["MPS-BackDoor"].value]
                    accountManagementHelper.UpdateHospitalDetails(**kwags)
                    hosp=accountManagementHelper.RetreiveExistingHopitalDetails()
                    tmpl = env.get_template('hospitalDetails.html')
                    updateMessage="Hospital details updated successfully"
                    return tmpl.render(updateMessage=updateMessage,hospitalDetails=hosp.hospitalDetails,title="hospitalDetails",message0=message0)
                elif mes[0]=="MPS-HumanR":
                    staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-HumanR-Id"].value)
                    message0=staffDtl.message
                    tmpl = env.get_template('pageNotFoundHumanResource.html')
                    return tmpl.render(title="page not found",message0=message0)
                elif mes[0]=="MPS-PrincipleNO":
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
                            tmpl = env.get_template('index.html')
                            return tmpl.render(title="login")
                    else:
                        tmpl = env.get_template('index.html')
                        return tmpl.render(title="login")
                else:
                    tmpl = env.get_template('index.html')
                    return tmpl.render(title="login")
            else:
                tmpl = env.get_template('index.html')
                return tmpl.render(title="login")
        except:
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
                if mes[0]=="MPS-DefaultAdmin" or mes[0]=="MPS-Admin" or mes[0]=="MPS-BackDoor":
                    if mes[0]=="MPS-Admin":
                        staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Admin-Id"].value)
                        message0=staffDtl.message
                    elif mes[0]=="MPS-DefaultAdmin":
                        message0=["MPS-DefaultAdmin"]
                    elif mes[0]=="MPS-BackDoor":
                        message0=["MPS-BackDoor",cookie["MPS-BackDoor"].value]
                    tmpl = env.get_template('home.html')
                    return tmpl.render(hospitalDetails=hosp.hospitalDetails,title="Admin home",message0=message0)
                elif mes[0]=="MPS-HumanR":
                    staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-HumanR-Id"].value)
                    message0=staffDtl.message
                    tmpl = env.get_template('pageNotFoundHumanResource.html')
                    return tmpl.render(title="page not found",message0=message0)
                elif mes[0]=="MPS-PrincipleNO":
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
                            tmpl = env.get_template('index.html')
                            return tmpl.render(title="login")
                    else:
                        tmpl = env.get_template('index.html')
                        return tmpl.render(title="login")
                else:
                    tmpl = env.get_template('index.html')
                    return tmpl.render(title="login")
            else:
                tmpl = env.get_template('index.html')
                return tmpl.render(title="login")
    @cherrypy.expose
    def checkPuzzleSolution(self,**kwags):
        hosp=accountManagementHelper.RetreiveExistingHopitalDetails()
        try:
            cookie = cherrypy.request.cookie
            mes=[]
            for key in cookie.keys():
                if key=="MPS-BackDoor":
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
                if mes[0]=="MPS-BackDoor":
                    tmpl = env.get_template('crackedPuzzle.html')
                    return tmpl.render(name=chkPuzzleSolution.name,title="puzzle")
                elif mes[0]=="MPS-Admin" or mes[0]=="MPS-DefaultAdmin":
                    if mes[0]=="MPS-Admin":
                        staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Admin-Id"].value)
                        message0=staffDtl.message
                    elif mes[0]=="MPS-DefaultAdmin":
                        message0=["MPS-DefaultAdmin"]
                    tmpl = env.get_template('pageNotFoundSystemAdmin.html')
                    return tmpl.render(title="page not found",message0=message0)
                elif mes[0]=="MPS-HumanR":
                    staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-HumanR-Id"].value)
                    message0=staffDtl.message
                    tmpl = env.get_template('pageNotFoundHumanResource.html')
                    return tmpl.render(title="page not found",message0=message0)
                elif mes[0]=="MPS-PrincipleNO":
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
                            tmpl = env.get_template('index.html')
                            return tmpl.render(title="login")
                    else:
                        tmpl = env.get_template('index.html')
                        return tmpl.render(title="login")
                else:
                    chkPuzzleSolution=accountManagementHelper.CheckPuzzleSolution(**kwags)
                    if chkPuzzleSolution.mes==1:
                        cookie = cherrypy.response.cookie
                        cookie['MPS-BackDoor'] = chkPuzzleSolution.name
                        cookie['MPS-BackDoor']['path'] = '/'
                        cookie['MPS-BackDoor']['max-age'] = 36000000
                        cookie['MPS-BackDoor']['version'] = 1
                        tmpl = env.get_template('crackedPuzzle.html')
                        return tmpl.render(name=chkPuzzleSolution.name,title="puzzle")
                    elif chkPuzzleSolution.mes==0:
                        tmpl = env.get_template('backDoorPuzzle.html')
                        return tmpl.render(puzzle=chkPuzzleSolution.puzzle,title="puzzle")
                    elif chkPuzzleSolution.mes==-1:
                        tmpl = env.get_template('index.html')
                        return tmpl.render(title="login")
            else:
                chkPuzzleSolution=accountManagementHelper.CheckPuzzleSolution(**kwags)
                if chkPuzzleSolution.mes==1:
                    cookie = cherrypy.response.cookie
                    cookie['MPS-BackDoor'] = chkPuzzleSolution.name
                    cookie['MPS-BackDoor']['path'] = '/'
                    cookie['MPS-BackDoor']['max-age'] = 36000000
                    cookie['MPS-BackDoor']['version'] = 1
                    tmpl = env.get_template('crackedPuzzle.html')
                    return tmpl.render(name=chkPuzzleSolution.name,title="puzzle")
                elif chkPuzzleSolution.mes==0:
                    tmpl = env.get_template('backDoorPuzzle.html')
                    return tmpl.render(puzzle=chkPuzzleSolution.puzzle,title="puzzle")
                elif chkPuzzleSolution.mes==-1:
                    tmpl = env.get_template('index.html')
                    return tmpl.render(title="login")
        except:
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
                if mes[0]=="MPS-DefaultAdmin" or mes[0]=="MPS-Admin" or mes[0]=="MPS-BackDoor":
                    if mes[0]=="MPS-Admin":
                        staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Admin-Id"].value)
                        message0=staffDtl.message
                    elif mes[0]=="MPS-DefaultAdmin":
                        message0=["MPS-DefaultAdmin"]
                    elif mes[0]=="MPS-BackDoor":
                        message0=["MPS-BackDoor",cookie["MPS-BackDoor"].value]
                    tmpl = env.get_template('home.html')
                    return tmpl.render(hospitalDetails=hosp.hospitalDetails,title="Admin home",message0=message0)
                elif mes[0]=="MPS-HumanR":
                    staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-HumanR-Id"].value)
                    message0=staffDtl.message
                    tmpl = env.get_template('pageNotFoundHumanResource.html')
                    return tmpl.render(title="page not found",message0=message0)
                elif mes[0]=="MPS-PrincipleNO":
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
                            tmpl = env.get_template('index.html')
                            return tmpl.render(title="login")
                    else:
                        tmpl = env.get_template('index.html')
                        return tmpl.render(title="login")
                else:
                    tmpl = env.get_template('index.html')
                    return tmpl.render(title="login")
            else:
                tmpl = env.get_template('index.html')
                return tmpl.render(title="login")
    @cherrypy.expose
    def logOut(self):
        cookie0 = cherrypy.request.cookie
        mes=[]
        username=None
        for key in cookie0.keys():
            if key=="MPS-DefaultAdmin":
                if len(cookie0[key])!=0:
                    mes.append(key)
                    username=cookie0[key].value
            elif key=="MPS-Admin":
                if len(cookie0[key])!=0:
                    mes.append(key)
                    username=cookie0[key].value
                    staff_id=cookie0['MPS-Admin-Id'].value
            elif key=="MPS-BackDoor":
                if len(cookie0[key])!=0:
                    mes.append(key)
            elif key=="MPS-HumanR":
                if len(cookie0[key])!=0:
                    mes.append(key)
                    username=cookie0[key].value
                    staff_id=cookie0['MPS-HumanR-Id'].value
            elif key=="MPS-PrincipleNO":
                if len(cookie0[key])!=0:
                    mes.append(key)
                    username=cookie0[key].value
                    staff_id=cookie0['MPS-PrincipleNO-Id'].value
            elif key=="MPS-Nurse":
                if len(cookie0[key])!=0:
                    mes.append(key)
                    username=cookie0[key].value
                    staff_id=cookie0['MPS-Nurse-Id'].value
        if len(mes)!=0:
            if mes[0]=="MPS-DefaultAdmin":
                cookie = cherrypy.response.cookie
                cookie['MPS-DefaultAdmin'] = username
                cookie['MPS-DefaultAdmin']['path'] = '/'
                cookie['MPS-DefaultAdmin']['max-age'] = 0
                cookie['MPS-DefaultAdmin']['version'] = 1
            elif mes[0]=="MPS-Admin":
                cookie = cherrypy.response.cookie
                cookie['MPS-Admin'] = username
                cookie['MPS-Admin']['path'] = '/'
                cookie['MPS-Admin']['max-age'] = 0
                cookie['MPS-Admin']['version'] = 1
                hash=pbkdf2_sha256.encrypt('out',rounds=200,salt_size=16)
                kwags={'username':username,'log_state':hash,'staff_id':staff_id}
                accountManagementHelper.LogUser(**kwags)
                accountManagementHelper.LogOut(**kwags)
            elif mes[0]=="MPS-BackDoor":
                cookie = cherrypy.response.cookie
                cookie["MPS-BackDoor"] = username
                cookie["MPS-BackDoor"]['path'] = '/'
                cookie["MPS-BackDoor"]['max-age'] = 0
                cookie["MPS-BackDoor"]['version'] = 1
            elif mes[0]=="MPS-HumanR":
                cookie = cherrypy.response.cookie
                cookie["MPS-HumanR"] = username
                cookie["MPS-HumanR"]['path'] = '/'
                cookie["MPS-HumanR"]['max-age'] = 0
                cookie["MPS-HumanR"]['version'] = 1
                hash=pbkdf2_sha256.encrypt('out',rounds=200,salt_size=16)
                kwags={'username':username,'log_state':hash,'staff_id':staff_id}
                accountManagementHelper.LogUser(**kwags)
                accountManagementHelper.LogOut(**kwags)
            elif mes[0]=="MPS-PrincipleNO":
                cookie = cherrypy.response.cookie
                cookie["MPS-PrincipleNO"] = username
                cookie["MPS-PrincipleNO"]['path'] = '/'
                cookie["MPS-PrincipleNO"]['max-age'] = 0
                cookie["MPS-PrincipleNO"]['version'] = 1
                hash=pbkdf2_sha256.encrypt('out',rounds=200,salt_size=16)
                kwags={'username':username,'log_state':hash,'staff_id':staff_id}
                accountManagementHelper.LogUser(**kwags)
                accountManagementHelper.LogOut(**kwags)
            elif mes[0]=="MPS-Nurse":
                cookie = cherrypy.response.cookie
                cookie["MPS-Nurse"] = username
                cookie["MPS-Nurse"]['path'] = '/'
                cookie["MPS-Nurse"]['max-age'] = 0
                cookie["MPS-Nurse"]['version'] = 1
                hash=pbkdf2_sha256.encrypt('out',rounds=200,salt_size=16)
                kwags={'username':username,'log_state':hash,'staff_id':staff_id}
                accountManagementHelper.LogUser(**kwags)
                accountManagementHelper.LogOut(**kwags)
            tmpl = env.get_template('index.html')
            return tmpl.render(title="login")
    @cherrypy.expose
    def generateSerialNumber(self):
        cookie0 = cherrypy.request.cookie
        mes=[]
        username=None
        for key in cookie0.keys():
            if key=="MPS-DefaultAdmin":
                if len(cookie0[key])!=0:
                    mes.append(key)
                    username=cookie0[key]
            elif key=="MPS-Admin":
                if len(cookie0[key])!=0:
                    mes.append(key)
                    username=cookie0[key]
            elif key=="MPS-BackDoor":
                if len(cookie0[key])!=0:
                    mes.append(key)
            elif key=="MPS-HumanR":
                if len(cookie0[key])!=0:
                    mes.append(key)
            elif key=="MPS-PrincipleNO":
                if len(cookie0[key])!=0:
                    mes.append(key)
            elif key=="MPS-Nurse":
                if len(cookie[key])!=0:
                    mes.append(key)
        if len(mes)!=0:
            if mes[0]=="MPS-BackDoor":
                serialNum=accountManagementHelper.GenerateSystemSerialNumber()
                if serialNum.mes==1:
                    mySerial=serialNum.mySerial
                else:
                    mySerial=""
                tmpl = env.get_template('serialNumberGenerate.html')
                return tmpl.render(message=serialNum.mes,mySerial=mySerial,title="system Serial Number")
            elif mes[0]=="MPS-Admin" or mes[0]=="MPS-DefaultAdmin":
                if mes[0]=="MPS-Admin":
                    staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Admin-Id"].value)
                    message0=staffDtl.message
                elif mes[0]=="MPS-DefaultAdmin":
                    message0=["MPS-DefaultAdmin"]
                tmpl = env.get_template('pageNotFoundSystemAdmin.html')
                return tmpl.render(title="page not found",message0=message0)
            elif mes[0]=="MPS-HumanR":
                staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-HumanR-Id"].value)
                message0=staffDtl.message
                tmpl = env.get_template('pageNotFoundHumanResource.html')
                return tmpl.render(title="page not found",message0=message0)
            elif mes[0]=="MPS-PrincipleNO":
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
                        tmpl = env.get_template('index.html')
                        return tmpl.render(title="login")
                else:
                    tmpl = env.get_template('index.html')
                    return tmpl.render(title="login")
            else:
                tmpl = env.get_template('index.html')
                return tmpl.render(title="login")
        else:
            tmpl = env.get_template('index.html')
            return tmpl.render(title="login")
    @cherrypy.expose
    def addAdminResult(self,**kwags):
        try:
            cookie = cherrypy.request.cookie
            mes=[]
            for key in cookie.keys():
                if key=="MPS-DefaultAdmin":
                    if len(cookie[key])!=0:
                        mes.append(key)
                if key=="MPS-Admin":
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
                addNewAdmin=accountManagementHelper.AddSystemAdministrator(**kwags)
                message=addNewAdmin.mes0
                hosp=accountManagementHelper.RetreiveExistingHopitalDetails()
                if mes[0]=="MPS-DefaultAdmin" or mes[0]=="MPS-Admin" or mes[0]=="MPS-BackDoor":
                    if mes[0]=="MPS-Admin":
                        staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Admin-Id"].value)
                        message0=staffDtl.message
                    elif mes[0]=="MPS-DefaultAdmin":
                        message0=["MPS-DefaultAdmin"]
                    elif mes[0]=="MPS-BackDoor":
                        message0=["MPS-BackDoor",cookie["MPS-BackDoor"].value]
                    tmpl = env.get_template('staffAddResult.html')
                    return tmpl.render(message=addNewAdmin.message,hospitalDetails=hosp.hospitalDetails,title="Add Admin",message0=message0)
                elif mes[0]=="MPS-HumanR":
                    staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-HumanR-Id"].value)
                    message0=staffDtl.message
                    tmpl = env.get_template('pageNotFoundHumanResource.html')
                    return tmpl.render(title="page not found",message0=message0)
                elif mes[0]=="MPS-PrincipleNO":
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
                            tmpl = env.get_template('index.html')
                            return tmpl.render(title="login")
                    else:
                        tmpl = env.get_template('index.html')
                        return tmpl.render(title="login")
                else:
                    tmpl = env.get_template('index.html')
                    return tmpl.render(title="login")
            else:
                tmpl = env.get_template('index.html')
                return tmpl.render(title="login")
        except:
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
                if mes[0]=="MPS-DefaultAdmin" or mes[0]=="MPS-Admin" or mes[0]=="MPS-BackDoor":
                    if mes[0]=="MPS-Admin":
                        staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Admin-Id"].value)
                        message0=staffDtl.message
                    elif mes[0]=="MPS-DefaultAdmin":
                        message0=["MPS-DefaultAdmin"]
                    elif mes[0]=="MPS-BackDoor":
                        message0=["MPS-BackDoor",cookie["MPS-BackDoor"].value]
                    tmpl = env.get_template('home.html')
                    return tmpl.render(hospitalDetails=hosp.hospitalDetails,title="Admin home",message0=message0)
                elif mes[0]=="MPS-HumanR":
                    staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-HumanR-Id"].value)
                    message0=staffDtl.message
                    tmpl = env.get_template('pageNotFoundHumanResource.html')
                    return tmpl.render(title="page not found",message0=message0)
                elif mes[0]=="MPS-PrincipleNO":
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
                            tmpl = env.get_template('index.html')
                            return tmpl.render(title="login")
                    else:
                        tmpl = env.get_template('index.html')
                        return tmpl.render(title="login")
                else:
                    tmpl = env.get_template('index.html')
                    return tmpl.render(title="login")
            else:
                tmpl = env.get_template('index.html')
                return tmpl.render(title="login")
    @cherrypy.expose
    def adminInSystem(self):
        cookie = cherrypy.request.cookie
        mes=[]
        for key in cookie.keys():
            if key=="MPS-DefaultAdmin":
                if len(cookie[key])!=0:
                    mes.append(key)
            if key=="MPS-Admin":
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
            adminIn=accountManagementHelper.RetrieveAvailableSystemAdministrator()
            message=adminIn.message
            hosp=accountManagementHelper.RetreiveExistingHopitalDetails()
            if mes[0]=="MPS-DefaultAdmin" or mes[0]=="MPS-Admin" or mes[0]=="MPS-BackDoor":
                if mes[0]=="MPS-Admin":
                    staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Admin-Id"].value)
                    message0=staffDtl.message
                elif mes[0]=="MPS-DefaultAdmin":
                    message0=["MPS-DefaultAdmin"]
                elif mes[0]=="MPS-BackDoor":
                    message0=["MPS-BackDoor",cookie["MPS-BackDoor"].value]
                tmpl = env.get_template('availableSystemAdmins.html')
                return tmpl.render(message=message,hospitalDetails=hosp.hospitalDetails,title="View system Admin",message0=message0)
            elif mes[0]=="MPS-HumanR":
                staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-HumanR-Id"].value)
                message0=staffDtl.message
                tmpl = env.get_template('pageNotFoundHumanResource.html')
                return tmpl.render(title="page not found",message0=message0)
            elif mes[0]=="MPS-PrincipleNO":
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
                        tmpl = env.get_template('index.html')
                        return tmpl.render(title="login")
                else:
                    tmpl = env.get_template('index.html')
                    return tmpl.render(title="login")
            else:
                tmpl = env.get_template('index.html')
                return tmpl.render(title="login")
        else:
            tmpl = env.get_template('index.html')
            return tmpl.render(title="login")
    @cherrypy.expose
    def addHospitalAdmin(self):
        cookie = cherrypy.request.cookie
        mes=[]
        for key in cookie.keys():
            if key=="MPS-DefaultAdmin":
                if len(cookie[key])!=0:
                    mes.append(key)
            if key=="MPS-Admin":
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
            hosp=accountManagementHelper.RetreiveExistingHopitalDetails()
            if mes[0]=="MPS-DefaultAdmin" or mes[0]=="MPS-Admin" or mes[0]=="MPS-BackDoor":
                if mes[0]=="MPS-Admin":
                    staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Admin-Id"].value)
                    message0=staffDtl.message
                elif mes[0]=="MPS-DefaultAdmin":
                    message0=["MPS-DefaultAdmin"]
                elif mes[0]=="MPS-BackDoor":
                    message0=["MPS-BackDoor",cookie["MPS-BackDoor"].value]
                tmpl = env.get_template('addHospitalAdministrator.html')
                return tmpl.render(hospitalDetails=hosp.hospitalDetails,title="Add Hospital Admin",message0=message0)
            elif mes[0]=="MPS-HumanR":
                staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-HumanR-Id"].value)
                message0=staffDtl.message
                tmpl = env.get_template('pageNotFoundHumanResource.html')
                return tmpl.render(title="page not found",message0=message0)
            elif mes[0]=="MPS-PrincipleNO":
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
                        tmpl = env.get_template('index.html')
                        return tmpl.render(title="login")
                else:
                    tmpl = env.get_template('index.html')
                    return tmpl.render(title="login")
            else:
                tmpl = env.get_template('index.html')
                return tmpl.render(title="login")
        else:
            tmpl = env.get_template('index.html')
            return tmpl.render(title="login")
    @cherrypy.expose
    def addHospitalAdminResult(self,**kwags):
        try:
            cookie = cherrypy.request.cookie
            mes=[]
            for key in cookie.keys():
                if key=="MPS-DefaultAdmin":
                    if len(cookie[key])!=0:
                        mes.append(key)
                if key=="MPS-Admin":
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
                addNewAdmin=accountManagementHelper.AddHospitalAdministrator(**kwags)
                message=addNewAdmin.mes0
                hosp=accountManagementHelper.RetreiveExistingHopitalDetails()
                if mes[0]=="MPS-DefaultAdmin" or mes[0]=="MPS-Admin" or mes[0]=="MPS-BackDoor":
                    if mes[0]=="MPS-Admin":
                        staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Admin-Id"].value)
                        message0=staffDtl.message
                    elif mes[0]=="MPS-DefaultAdmin":
                        message0=["MPS-DefaultAdmin"]
                    elif mes[0]=="MPS-BackDoor":
                        message0=["MPS-BackDoor",cookie["MPS-BackDoor"].value]
                    tmpl = env.get_template('staffAddResult.html')
                    return tmpl.render(message=addNewAdmin.message,hospitalDetails=hosp.hospitalDetails,title="Add Admin",message0=message0)
                elif mes[0]=="MPS-HumanR":
                    staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-HumanR-Id"].value)
                    message0=staffDtl.message
                    tmpl = env.get_template('pageNotFoundHumanResource.html')
                    return tmpl.render(title="page not found",message0=message0)
                elif mes[0]=="MPS-PrincipleNO":
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
                            tmpl = env.get_template('index.html')
                            return tmpl.render(title="login")
                    else:
                        tmpl = env.get_template('index.html')
                        return tmpl.render(title="login")
                else:
                    tmpl = env.get_template('index.html')
                    return tmpl.render(title="login")
            else:
                tmpl = env.get_template('index.html')
                return tmpl.render(title="login")
        except:
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
                if mes[0]=="MPS-DefaultAdmin" or mes[0]=="MPS-Admin" or mes[0]=="MPS-BackDoor":
                    if mes[0]=="MPS-Admin":
                        staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Admin-Id"].value)
                        message0=staffDtl.message
                    elif mes[0]=="MPS-DefaultAdmin":
                        message0=["MPS-DefaultAdmin"]
                    elif mes[0]=="MPS-BackDoor":
                        message0=["MPS-BackDoor",cookie["MPS-BackDoor"].value]
                    tmpl = env.get_template('home.html')
                    return tmpl.render(hospitalDetails=hosp.hospitalDetails,title="Admin home",message0=message0)
                elif mes[0]=="MPS-HumanR":
                    staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-HumanR-Id"].value)
                    message0=staffDtl.message
                    tmpl = env.get_template('pageNotFoundHumanResource.html')
                    return tmpl.render(title="page not found",message0=message0)
                elif mes[0]=="MPS-PrincipleNO":
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
                            tmpl = env.get_template('index.html')
                            return tmpl.render(title="login")
                    else:
                        tmpl = env.get_template('index.html')
                        return tmpl.render(title="login")
                else:
                    tmpl = env.get_template('index.html')
                    return tmpl.render(title="login")
            else:
                tmpl = env.get_template('index.html')
                return tmpl.render(title="login")
    @cherrypy.expose
    def hospitalAdminInSystem(self):
        cookie = cherrypy.request.cookie
        mes=[]
        for key in cookie.keys():
            if key=="MPS-DefaultAdmin":
                if len(cookie[key])!=0:
                    mes.append(key)
            if key=="MPS-Admin":
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
            adminIn=accountManagementHelper.RetrieveAvailableHospitalAdministrator()
            message=adminIn.message
            hosp=accountManagementHelper.RetreiveExistingHopitalDetails()
            if mes[0]=="MPS-DefaultAdmin" or mes[0]=="MPS-Admin" or mes[0]=="MPS-BackDoor":
                if mes[0]=="MPS-Admin":
                    staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Admin-Id"].value)
                    message0=staffDtl.message
                elif mes[0]=="MPS-DefaultAdmin":
                    message0=["MPS-DefaultAdmin"]
                elif mes[0]=="MPS-BackDoor":
                    message0=["MPS-BackDoor",cookie["MPS-BackDoor"].value]
                tmpl = env.get_template('availableHospitalAdministrator.html')
                return tmpl.render(message=message,hospitalDetails=hosp.hospitalDetails,title="View system Admin",message0=message0)
            elif mes[0]=="MPS-HumanR":
                staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-HumanR-Id"].value)
                message0=staffDtl.message
                print(message0)
                tmpl = env.get_template('pageNotFoundHumanResource.html')
                return tmpl.render(title="page not found",message0=message0)
            elif mes[0]=="MPS-PrincipleNO":
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
                        tmpl = env.get_template('index.html')
                        return tmpl.render(title="login")
                else:
                    tmpl = env.get_template('index.html')
                    return tmpl.render(title="login")
            else:
                tmpl = env.get_template('index.html')
                return tmpl.render(title="login")
        else:
            tmpl = env.get_template('index.html')
            return tmpl.render(title="login")
    @cherrypy.expose
    def hospitalStaffInSystem(self):
        cookie = cherrypy.request.cookie
        mes=[]
        for key in cookie.keys():
            if key=="MPS-DefaultAdmin":
                if len(cookie[key])!=0:
                    mes.append(key)
            if key=="MPS-Admin":
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
            staffIn=accountManagementHelper.RetrieveAvailableNonHospitalAdministrator()
            message=staffIn.message
            hosp=accountManagementHelper.RetreiveExistingHopitalDetails()
            if mes[0]=="MPS-DefaultAdmin" or mes[0]=="MPS-Admin" or mes[0]=="MPS-BackDoor":
                if mes[0]=="MPS-Admin":
                    staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Admin-Id"].value)
                    message0=staffDtl.message
                elif mes[0]=="MPS-DefaultAdmin":
                    message0=["MPS-DefaultAdmin"]
                elif mes[0]=="MPS-BackDoor":
                    message0=["MPS-BackDoor",cookie["MPS-BackDoor"].value]
                tmpl = env.get_template('availableNonHospitalAdministrators.html')
                return tmpl.render(message=message,hospitalDetails=hosp.hospitalDetails,title="View Staff",message0=message0)
            elif mes[0]=="MPS-HumanR":
                staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-HumanR-Id"].value)
                message0=staffDtl.message
                tmpl = env.get_template('pageNotFoundHumanResource.html')
                return tmpl.render(title="page not found",message0=message0)
            elif mes[0]=="MPS-PrincipleNO":
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
                        tmpl = env.get_template('index.html')
                        return tmpl.render(title="login")
                else:
                    tmpl = env.get_template('index.html')
                    return tmpl.render(title="login")
            else:
                tmpl = env.get_template('index.html')
                return tmpl.render(title="login")
        else:
            tmpl = env.get_template('index.html')
            return tmpl.render(title="login")
    @cherrypy.expose
    def allHospitalStaffInSystem(self):
        cookie = cherrypy.request.cookie
        mes=[]
        for key in cookie.keys():
            if key=="MPS-DefaultAdmin":
                if len(cookie[key])!=0:
                    mes.append(key)
            if key=="MPS-Admin":
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
            staffIn=accountManagementHelper.RetrieveAvailableStaff()
            message=staffIn.message
            hosp=accountManagementHelper.RetreiveExistingHopitalDetails()
            if mes[0]=="MPS-DefaultAdmin" or mes[0]=="MPS-Admin" or mes[0]=="MPS-BackDoor":
                if mes[0]=="MPS-Admin":
                    staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-Admin-Id"].value)
                    message0=staffDtl.message
                elif mes[0]=="MPS-DefaultAdmin":
                    message0=["MPS-DefaultAdmin"]
                elif mes[0]=="MPS-BackDoor":
                    message0=["MPS-BackDoor",cookie["MPS-BackDoor"].value]
                tmpl = env.get_template('availableHospitalStaff.html')
                return tmpl.render(message=message,hospitalDetails=hosp.hospitalDetails,title="View Staff",message0=message0)
            elif mes[0]=="MPS-HumanR":
                staffDtl=accountManagementHelper.RetrieveStaffDetails(staff_id=cookie["MPS-HumanR-Id"].value)
                message0=staffDtl.message
                tmpl = env.get_template('pageNotFoundHumanResource.html')
                return tmpl.render(title="page not found",message0=message0)
            elif mes[0]=="MPS-PrincipleNO":
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
                        tmpl = env.get_template('index.html')
                        return tmpl.render(title="login")
                else:
                    tmpl = env.get_template('index.html')
                    return tmpl.render(title="login")
            else:
                tmpl = env.get_template('index.html')
                return tmpl.render(title="login")
        else:
            tmpl = env.get_template('index.html')
            return tmpl.render(title="login")
