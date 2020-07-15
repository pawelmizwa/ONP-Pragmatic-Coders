from flask import Flask, jsonify, make_response, request
from flask_restful import Resource, Api
from werkzeug.exceptions import BadRequestKeyError
from flask_basicauth import BasicAuth
from helpers.onp_handler import ONPHandler, ONP_PHRASE_ERROR
from config import prod
import logging

logger = logging.getLogger("example")
app = Flask(__name__)
api = Api(app)
app.config["BASIC_AUTH_USERNAME"] = prod.local_user
app.config["BASIC_AUTH_PASSWORD"] = prod.local_password
basic_auth = BasicAuth(app)
app.config["BASIC_AUTH_FORCE"] = True


class Nesting_level_error(Exception):
    pass


class Data(Resource):
    def __init__(self):
        self.onp = ONPHandler(
            digits=prod.digits,
            operations=prod.operations,
        )

    def post(self):
        try:
            phrase = request.args["phrase"]
            if self.onp.validate_onp(phrase):
                result = self.onp.onp(phrase)
                response = make_response(jsonify(result), 200)
        except BadRequestKeyError as e:
            response = make_response(
                {"message": "Please specify phrase in params"}, 400
            )
            logger.warning(msg=e)
        except ONP_PHRASE_ERROR as e:
            response = make_response(
                {"message": e}, 400
            )
        except Exception as e:
            logger.critical(msg=e)
            response = make_response({"message": "System issue"}, 500)
        return response


api.add_resource(Data, "/data")

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=4002)
