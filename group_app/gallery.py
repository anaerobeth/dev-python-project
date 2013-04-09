import flask, flask.views
import utils

class Gallery(flask.views.MethodView):
    @utils.login_required
    def get(self):
        return flask.render_template('gallery.html')

