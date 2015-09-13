import jinja2
import os
import webapp2
from google.appengine.api import users
from google.appengine.api import mail

env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class MainHandler(webapp2.RequestHandler):#this handles the default url and render index.html
    def get(self):
        template = env.get_template('index.html')
        self.response.write(template.render())

class AccountHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('account.html')
        user = users.get_current_user()
        if user:
            url = users.create_logout_url("/")
            url_linktext = 'Logout'
        else:
            url = self.redirect(users.create_login_url(self.request.uri))
            url_linktext = 'Login'

        template_values = {
            'url': url,
            'url_linktext': url_linktext,
        }
        self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/account.html', AccountHandler)
], debug=True)
