from flask import Flask, Response, request
import json

from EasySAV.Use_cases.Intervention_list_use_case import *
from EasySAV.Use_cases.Intervention_add_use_case import *
from EasySAV.Domain.Intervention import Intervention
from EasySAV.Repository.Memrepo import *
from EasySAV.Serializers.intervention_json_serializer import InterventionJsonEncoder


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
    repo = MemRepo([intervention1, intervention2, intervention3])
    use_case = InterventionListUseCase(repo)
    liste_interventions = use_case.execute()
    return Response(json.dumps(liste_interventions, cls=InterventionJsonEncoder),
                    mimetype='application/json', status=200)


@app.route('/add', methods=['POST'])
def add_intervention():
    print(request)
    dict_req = request.form.to_dict()
    print(dict_req)
    inter = Intervention(dict_req["code"], dict_req["ref_client"], dict_req["piece"], dict_req["probleme"])
    repo = MemRepo([intervention1, intervention2, intervention3])
    save_case = InterventionSaveUseCase(repo, inter)
    save_case.execute()
    use_case = InterventionListUseCase(repo)
    liste_interventions = use_case.execute()
    return Response(json.dumps(liste_interventions, cls=InterventionJsonEncoder),
                    mimetype='application/json', status=200)


if __name__ == '__main__':
    app.run()
