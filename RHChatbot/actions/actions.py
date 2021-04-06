# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

class ActionHelloWorld(Action):
#
    def name(self) -> Text:
        return "action_hello_world"
#
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Hello World bla bla! " + tracker.get_slot("colaborador"))
#
        return[]

class ActionTempoEmpresa(Action):
#
    def name(self) -> Text:
        return "action_tempo_empresa"
#
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        r = requests.post('http://localhost:5000/tempoempresa', json={"data": tracker.get_slot("id_colaborador")})
        dispatcher.utter_message(text='Você está trabalhando na empresa fazem ' + r.json()["v"] + ' dias.')
#
        return[]

class ActionValorSalario(Action):
#
    def name(self) -> Text:
        return "action_valor_salario"
#
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        r = requests.post('http://localhost:5000/valorsalario', json={"data": tracker.get_slot("id_colaborador")})
        dispatcher.utter_message(text='O seu sálario é de R$ ' + r.json()["v"] + '.')
#
        return[]

class ActionSaldoVR(Action):
#
    def name(self) -> Text:
        return "action_saldo_VR"
#
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        r = requests.post('http://localhost:5000/saldoVR', json={"data": tracker.get_slot("id_colaborador")})
        dispatcher.utter_message(text='O saldo do seu vale é de R$ ' + r.json()["v"] + '.')
#
        return[]

class ActionBancoHoras(Action):
#
    def name(self) -> Text:
        return "action_banco_horas"
#
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        r = requests.post('http://localhost:5000/bancohoras', json={"data": tracker.get_slot("id_colaborador")})
        dispatcher.utter_message(text='O saldo do seu banco de horas é de ' + r.json()["v"] + '.')
#
        return[]

class ActionSaldoFerias(Action):
#
    def name(self) -> Text:
        return "action_saldo_ferias"
#
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        r = requests.post('http://localhost:5000/saldoferias', json={"data": tracker.get_slot("id_colaborador")})
        dispatcher.utter_message(text='Você possui ' + r.json()["v"] + '.')
#
        return[]

class ActionRelatorioColaborador(Action):
#
    def name(self) -> Text:
        return "action_relatorio_colaborador"
#
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        r = requests.post('http://localhost:5000/informacoescolaborador', json={"data": tracker.get_slot("id_colaborador")})
        dispatcher.utter_message(text=r.json()["v"])
#
        return[]

class ActionRelatorioGestor(Action):
#
    def name(self) -> Text:
        return "action_relatorio_gestor"
#
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if tracker.get_slot("id_colaborador") == "1":
                r = requests.post('http://localhost:5000/bancohorascolaboradores', json={"data": tracker.get_slot("id_colaborador")})
                dispatcher.utter_message(text=r.json()["v"])
        else:
              dispatcher.utter_message(text="Estou sem respostas para a sua pergunta")  
#
        return[]

class ActionRelatorios(Action):
#
    def name(self) -> Text:
        return "action_relatorios"
#
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        buttons = [{"title": "Informações colaborador", "payload": "/relatorio_colaborador"}]
        if (tracker.get_slot("id_colaborador") == "1"): # só para exemplo de gestor
                buttons.append({"title": "Banco de horas colaboradores", "payload": "/relatorio_gestor"})

        dispatcher.utter_button_message("Relatórios disponíveis:", buttons)
        return[]


