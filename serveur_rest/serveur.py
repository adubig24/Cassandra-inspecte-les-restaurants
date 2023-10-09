from flask import Flask, render_template, request, jsonify
from data import DataAccess as da

app = Flask(__name__)

@app.route("/api/restaurant/<int:id>", methods=['GET'])
def get_inforesto(id):
    da.connexion()
    info = da.inforesto(id)
    da.deconnexion()

    return jsonify(info), 200

@app.route("/api/type_cuisine/<string:type>", methods=['GET'])
def get_restos_par_type(type):
    da.connexion()
    department = da.noms_resto_par_type_de_cuisine(type)
    da.deconnexion()

    return jsonify(department), 200

@app.route("/api/inspection/<int:id>", methods=['GET'])
def get_nombre_inspection_pour_ce_resto(id):
    da.connexion()
    inspections=da.nombre_inspection_pour_ce_resto(id)
    da.deconnexion()

    return jsonify(inspections), 200

@app.route("/api/grade/<string:grade>", methods=['GET'])
def get_top_10(grade):
    da.connexion()
    top10=da.top_10(grade)
    da.deconnexion()

    return jsonify(top10), 200

@app.errorhandler(404)
def page_not_found(e):
    return "erreur", 404

if __name__ == "__main__" :
    app.run(debug=True, port=5001)