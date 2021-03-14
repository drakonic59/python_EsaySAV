from flask import Flask, request, jsonify

from EasySAV.Use_cases.Intervention_list_use_case import *
from EasySAV.Use_cases.Intervention_add_use_case import *
from EasySAV.Repository.DataBaseRepo import *

DBAccess = "D:/school/python_EsaySAV/UserInterfaces/Database.db"

app = Flask(__name__)

# Alimentation de la base de données en mémoire
intervention1 = {
            "code": "d753578e-tc0f-4e75-81b8-566c5dfda35b",
            "ref_client" : "CFGRRF",
            "piece" : "lave linge",
            "probleme" : "fuite"
 }

intervention2 = {
            "code": "e987578e-fc0v-5e75-82b8-566c5dfda66y",
            "ref_client": "REFTY",
            "piece": "TV",
            "probleme": "allumage"
}

intervention3 = {
            "code": "j953979d-uc4f-5e75-81b8-576G5dfda75p",
            "ref_client": "YGTGDR",
            "piece": "lave vaisselle",
            "probleme": "fuite"
}


@app.route('/interventions', methods=['GET'])
def interventions():
    repo = DataBaseRepo(DBAccess)
    use_case = InterventionListUseCase(repo)
    liste_interventions = use_case.execute()
    return jsonify(liste_interventions)


@app.route('/add', methods=['POST'])
def add_intervention():
    try :
        new_intervention = request.get_json(force=True)
        repo = DataBaseRepo(DBAccess)
        use_case = InterventionSaveUseCase(repo, new_intervention)
        response = use_case.execute()

        return ("{}".format(str(response)), {"Content-Type": "application/plaintext"})
    except Exception as exc:
        return str(exc)


if __name__ == '__main__':
    app.run()
