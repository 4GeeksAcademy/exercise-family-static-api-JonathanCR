import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_get_all_menbers():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    return jsonify(members), 200

@app.route ('/members/<int:member_id>', methods=['GET'] )
def handle_get_single_member(member_id):
    members = jackson_family.get_member(member_id)
    return jsonify(members), 200

@app.route('/members', methods=['POST'])
def handle_post_member():
    members = request.json
    added_member = jackson_family.add_member(members)
    return jsonify(added_member), 200

@app.route('/members/<int:member_id>', methods=['DELETE'])
def handle_delete_single_member(member_id):
    jackson_family.delete_member(member_id)
    return jsonify({"done": True}), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
