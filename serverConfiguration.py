import os,os.path
import psycopg2
from cherrypy.lib import auth_basic
import cherrypy
class serverConfig(object):
    def __init__(self):
        self.configHumanResourceMIS={'/':{'tools.sessions.on':True,
                   'tools.staticdir.root':os.path.abspath(os.getcwd())},
              '/static':{'tools.staticdir.on':True,
                         'tools.staticdir.dir':'humanResourceMIS/assets',
                         'tools.sessions.storage_class':cherrypy.lib.sessions.FileSession,
                          'tools.sessions.storage_path':"sessions"
                         }}
        self.configFrontDeskMIS={'/':{'tools.sessions.on':True,
                   'tools.staticdir.root':os.path.abspath(os.getcwd())},
              '/static':{'tools.staticdir.on':True,
                         'tools.staticdir.dir':'frontDeskMIS/assets',
                         }}
        self.principleNurseOfficerController={'/':{'tools.sessions.on':True,
                   'tools.staticdir.root':os.path.abspath(os.getcwd())},
              '/static':{'tools.staticdir.on':True,
                         'tools.staticdir.dir':'nurseMIS/assets',
                         }}
        self.triageController={'/':{'tools.sessions.on':True,
                   'tools.staticdir.root':os.path.abspath(os.getcwd())},
              '/static':{'tools.staticdir.on':True,
                         'tools.staticdir.dir':'triageMIS/assets',
                         }}
        self.systemAdminMIS={'/':{'tools.sessions.on':True,
                   'tools.staticdir.root':os.path.abspath(os.getcwd())},
              '/static':{'tools.staticdir.on':True,
                         'tools.staticdir.dir':'{}/systemAdminMIS/assets'.format(os.path.abspath(os.getcwd())),
                         }
                    # '/': {
                    #     'tools.auth_basic.on': True,
                    #     'tools.auth_basic.realm': 'localhost',
                    #     'tools.auth_basic.checkpassword': validate_password,
                    #     'tools.sessions.storage_class':cherrypy.lib.sessions.FileSession,
                    #     'tools.sessions.storage_path':"sessions"}

                     }

        self.server_config0 = {
                             'server.socket_host': '127.0.0.1',
                              'server.socket_port': 60000
                              }
        self.server_config1 = {
           '/': {
               'tools.auth_basic.on': True,
               'tools.auth_basic.realm': 'localhost',
               'tools.auth_basic.checkpassword': validate_password
            }
        }
class databaseConfig(object):
    def __init__(self):
        self.db=psycopg2.connect("dbname=MPS user=postgres host=localhost port=5432 password='debo'")
USERS = {'joh': 'secret'}

def validate_password(realm, username, password):
    if username in USERS and USERS[username] == password:
       print(cherrypy.request.login)
       return True
    return False
def log_out(realm, username, password):
    if username in USERS and USERS[username] == password:
    #    cherrypy.request.login='Joel'
    #    print(cherrypy.request.login)
       cherrypy.lib.cptools.SessionAuth.do_login
       cherrypy.lib.cptools.SessionAuth.do_logout
       return False
    return True
