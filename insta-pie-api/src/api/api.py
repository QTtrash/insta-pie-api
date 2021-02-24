import flask
import json
from User import User
from User import Images
from User import Followers
from User import Following
from User import UserGroups

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<p>Insta-pie-api home dir</p>"


@app.route('/api/v1/users/<username>', methods=['GET'])
def api_user(username):
    response = app.response_class(
    json.dumps(User.get_user(username), sort_keys=False, indent=4),
    mimetype=app.config['JSONIFY_MIMETYPE'])
    return response


@app.route('/api/v1/users/grouptest', methods=['GET'])
def api_user_group():
    usernames = UserGroups.group()
    return User.get_user_group(usernames)


@app.route('/api/v1/users/images/<username>', methods=['GET'])
def api_image(username):
    response = app.response_class(
    json.dumps(Images.get_images(username), sort_keys=False, indent=4),
    mimetype=app.config['JSONIFY_MIMETYPE'])
    return response


@app.route('/api/v1/users/followers/<login>/<password>/<username>', methods=['GET'])
def api_followers(username, login, password):
    response = app.response_class(
    json.dumps(Followers.get_followers(username, login, password), sort_keys=False, indent=4),
    mimetype=app.config['JSONIFY_MIMETYPE'])
    return response


@app.route('/api/v1/users/following/<login>/<password>/<username>', methods=['GET'])
def api_following(username, login, password):
    response = app.response_class(
    json.dumps(Following.get_following(username, login, password), sort_keys=False, indent=4),
    mimetype=app.config['JSONIFY_MIMETYPE'])
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

app.run()
