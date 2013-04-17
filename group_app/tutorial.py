import flask, flask.views

class Tutorial(flask.views.MethodView):
    @utils.login_required
    def get(self):
        return flask.render_template('tutorial.html')

