import datetime

from requests.models import Response
from dateutil import relativedelta as rdelta
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app)
colaboradores = dict()

class Nivel:
    NORMAL = 1
    GESTOR = 2

class Colaborador:
  def __init__(self, id: int, nome: str, cargo: str, setor: str, data_admissao: datetime, nv_colaborador: Nivel, vr_disponivel: float, 
                qtd_dias_ferias_dispoveis: int, data_maxima_ferias: str, saldo_banco_horas: str, salario: float):
    self.id = id
    self.nome = nome
    self.cargo = cargo
    self.setor = setor
    self.data_admissao = data_admissao
    self.nv_colaborador = nv_colaborador
    self.vr_disponivel = vr_disponivel
    self.qtd_dias_ferias_dispoveis = qtd_dias_ferias_dispoveis
    self.data_maxima_ferias = data_maxima_ferias
    self.saldo_banco_horas = saldo_banco_horas
    self.salario = salario
    self.tempo_empresa = rdelta.relativedelta(datetime.date.today(), self.data_admissao.date())

def base() -> dict:
    cols = dict()
    cols[1] = Colaborador(1, 'Bernardete Silva ', 'CEO', 'Diretoria', datetime.datetime(2018, 1, 1), Nivel.GESTOR, 120.00, 30, '01/12/2021', '00:00', 8000.00)
    cols[2] = Colaborador(2, 'Flavia Franco', 'Analista de suporte do cliente', 'Suporte', datetime.datetime(2019, 3, 1), Nivel.NORMAL, 320.07, 15, '01/02/2022', '04:30', 2500.00)
    cols[3] = Colaborador(3, 'Michelle Barbosa', 'Analista administrativo', 'Administrativo/RH/Marketing/Financeiro', datetime.datetime(2019, 2, 1), Nivel.NORMAL, '250.90', 10, '01/01/2022', '00:00', 5000.00)
    cols[4] = Colaborador(4, 'Pedro Germano', 'Assistente comercial', 'Comercial', datetime.datetime(2019, 2, 1), Nivel.NORMAL, 200.00, 10, '01/01/2022', '10:00', 2000.00)
    cols[5] = Colaborador(5, 'Henrique Chaves', 'Programador', 'Desenvolvimento', datetime.datetime(2018, 5, 1), Nivel.NORMAL, 15.10, 30, '01/04/2022', '-01:00', 3100.00)

    return cols

@app.route('/colaboradores', methods=['OPTIONS'])
def get_colaboradores():
    response = jsonify(     [
            {'ID': colaboradores[1].id, 'Nome': colaboradores[1].nome, 'Cargo': colaboradores[1].cargo},
            {'ID': colaboradores[2].id, 'Nome': colaboradores[2].nome, 'Cargo': colaboradores[2].cargo},
            {'ID': colaboradores[3].id, 'Nome': colaboradores[3].nome, 'Cargo': colaboradores[3].cargo},
            {'ID': colaboradores[4].id, 'Nome': colaboradores[4].nome, 'Cargo': colaboradores[4].cargo},
            {'ID': colaboradores[5].id, 'Nome': colaboradores[5].nome, 'Cargo': colaboradores[5].cargo}
           ])
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    return response


@app.route('/bancohorascolaboradores', methods=['POST'])
@cross_origin()
def get_banco_horas_colaboradores():
    msg = ""
    for col in colaboradores:
        msg += "Colaborador: " + colaboradores[col].nome + " - Banco horas: " + colaboradores[col].saldo_banco_horas + "<br>"

    response = jsonify({'v': msg })
    return response

@app.route('/feriascolaboradores', methods=['POST'])
@cross_origin()
def get_ferias_colaboradores():
    msg = ""
    for col in colaboradores:
        msg += "Colaborador: " + colaboradores[col].nome + " - " + str(colaboradores[col].qtd_dias_ferias_dispoveis) + " dias para pegar até a data de " + str(colaboradores[col].data_maxima_ferias) + "<br>"

    response = jsonify({'v': msg })
    return response

@app.route('/informacoescolaborador', methods=['POST'])
@cross_origin()
def get_informacoes_colaborador():
    content = request.json
    colab = colaboradores[int(content['data'])]
    response = jsonify({'v': "Setor: " + colab.setor + "<br>" + "Cargo: " + colab.cargo })
    return response

@app.route('/tempoempresa', methods=['POST'])
@cross_origin()
def get_tempo_empresa():
    content = request.json
    
    response = jsonify({'v': "{0.years} ano(s) e {0.months} mes(es)".format(colaboradores[int(content['data'])].tempo_empresa) })
    return response

@app.route('/valorsalario', methods=['POST'])
@cross_origin()
def get_salario():
    content = request.json
    response = jsonify({'v': str(colaboradores[int(content['data'])].salario) })
    return response

@app.route('/saldoVR', methods=['POST'])
@cross_origin()
def get_saldo_VR():
    content = request.json
    response = jsonify({'v': str(colaboradores[int(content['data'])].vr_disponivel) })
    return response

@app.route('/bancohoras', methods=['POST'])
@cross_origin()
def get_banco_horas():
    content = request.json
    response = jsonify({'v': str(colaboradores[int(content['data'])].saldo_banco_horas) })
    return response

@app.route('/saldoferias', methods=['POST'])
@cross_origin()
def get_saldo_ferias():
    content = request.json
    colab = colaboradores[int(content['data'])]
    response = jsonify({'v': str(colab.qtd_dias_ferias_dispoveis) + " dias para pegar até a data de " + str(colab.data_maxima_ferias) })
    return response

if __name__ == '__main__':
    colaboradores = base()
    app.run(host='0.0.0.0', port=5000, debug=True)