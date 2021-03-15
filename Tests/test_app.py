import unittest
import json
from UserInterfaces.app import app


class TestApp(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        app.config["DEBUG"] = True
        self.app = app.test_client()
        self.assertEqual(app.debug, True)

    def test_get_interventions(self):
        reponse = self.app.get('/interventions', follow_redirects=False)
        dico = json.loads(reponse.data)
        self.assertEqual(dico[0]["ref_client"], "CFGRRF")
        self.assertEqual(dico[0]["probleme"], "fuite")
        self.assertEqual(dico[0]["piece"], "lave linge")
        self.assertEqual(reponse.status_code, 200)

    def test_add_interventions(self):
        reponse = self.app.post('/add',
                                data=json.dumps(
                                    {"ref_client": "CTGSST", "probleme": "panne", "piece": "lave vaisselle"}),
                                content_type='application/json')
        self.assertEqual(reponse.status_code, 200)
        self.assertEqual(reponse.data, b"200")


if __name__ == '__main__':
    unittest.main()
