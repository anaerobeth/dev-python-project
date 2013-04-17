import flask, flask.views
import utils

class Videos(flask.views.MethodView):
    @utils.login_required
    def get(self):
        return flask.render_template('videos.html')
