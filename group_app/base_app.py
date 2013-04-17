# Group web app
# Name: Beth and Tracy

import flask
import settings

#Views
from login import Login
from main import Main
from gallery import Gallery
from videos import Videos

app = flask.Flask(__name__)
app.secret_key = settings.secret_key


#Routes
app.add_url_rule('/',
                view_func=Main.as_view('main'),
                methods=['GET'])
app.add_url_rule('/<page>/',
                view_func=Main.as_view('main'),
                methods=['GET'])
app.add_url_rule('/gallery/',
                view_func=Gallery.as_view('gallery'),
                methods=['GET'])
app.add_url_rule('/login/',
                view_func=Login.as_view('login'),
                methods=['GET', 'POST'])
app.add_url_rule('/videos/',
                view_func=Videos.as_view('videos'),
                methods=['GET'])


@app.errorhandler(404)
def page_not_found(error):
     return flask.render_template('404.html'), 404

app.debug = True
app.run()
