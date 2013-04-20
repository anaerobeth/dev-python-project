import flask, flask.views
import utils

class Flashcard(flask.views.MethodView):
    @utils.login_required
    def get(self):
        return flask.render_template('flashcard.html')

