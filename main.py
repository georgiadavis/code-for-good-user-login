import jinja2
import os
import webapp2
from google.appengine.api import users

env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class MainHandler(webapp2.RequestHandler):#this handles the default url and render index.html
    def get(self):
        template = env.get_template('index.html')
        self.response.write(template.render())

class AccountHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('account.html')
        self.response.write(template.render())
        user = users.get_current_user()
        if user:
            greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' %
                        (user.nickname(), users.create_logout_url('/')))
        else:
            greeting= self.redirect(users.create_login_url(self.request.uri))

        self.response.out.write('<html><body>%s</body></html>' % greeting)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/account.html', AccountHandler)
], debug=True)
