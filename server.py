import cherrypy
import os,os.path
from humanResourceMIS.controllers import humanResourceController
from frontDeskMIS.controllers import frontDeskController
from systemAdminMIS.controllers import systemAdminController
from nurseMIS.controllers import principleNurseOfficerController
from triageMIS.controllers import triageController
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('systemAdminMIS/templates'))
#----Server config imports ------------
import serverConfiguration

def error_page_404(status, message, traceback, version):
    tmpl = env.get_template('generalNotFound.html')
    return tmpl.render(title="page not found")

def start_server():
    serverConfig=serverConfiguration.serverConfig()
    cherrypy.tree.mount(humanResourceController.HRMIS(),'/humanResource',serverConfig.configHumanResourceMIS)
    cherrypy.tree.mount(systemAdminController.SAMIS(),'/',serverConfig.systemAdminMIS)
    cherrypy.tree.mount(frontDeskController.FDMIS(),'/frontDesk',serverConfig.configFrontDeskMIS)
    cherrypy.tree.mount(triageController.TRMIS(),'/triage',serverConfig.triageController)
    cherrypy.tree.mount(principleNurseOfficerController.PNOMIS(),'/pMO',serverConfig.principleNurseOfficerController)
    cherrypy.config.update(serverConfig.server_config0)
    cherrypy.config.update(serverConfig.server_config1)
    cherrypy.config.update({'error_page.404': error_page_404})
    cherrypy.engine.start()

if __name__ == '__main__':
    start_server()
