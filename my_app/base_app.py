# Individual web app
# Name: Beth

import flask
import settings

#Views
from login import Login
from main import Main
from flashcard import Flashcard

app = flask.Flask(__name__)
app.secret_key = settings.secret_key


#Routes
app.add_url_rule('/',
                view_func=Main.as_view('main'),
                methods=['GET'])
app.add_url_rule('/<page>/',
                view_func=Main.as_view('main'),
                methods=['GET'])
app.add_url_rule('/flashback/',
                view_func=Flashcard.as_view('flashback'),
                methods=['GET'])
app.add_url_rule('/login/',
                view_func=Login.as_view('login'),
                methods=['GET', 'POST'])


@app.errorhandler(404)
def page_not_found(error):
     return flask.render_template('404.html'), 404

app.debug = True
app.run()
