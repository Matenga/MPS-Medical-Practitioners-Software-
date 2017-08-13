import cherrypy
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('humanResourceMIS/templates'))
class HRMIS(object):
    #def __init__(self):
        #self.humanResource = humanRM.HumanResource()
    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('index.html')
        return tmpl.render(title='home')
    @cherrypy.expose
    def recruiteDoctor(self):
        tmpl = env.get_template('recruit.html')
        return tmpl.render(title='home')
