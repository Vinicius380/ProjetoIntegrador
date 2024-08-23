from flask import Flask, jsonify, request, make_response

from bancoDados import DadosSensores

app = Flask('DadosSensores')

#GET
@app.route('/DadosSensores', methods=['GET'])
def get_dados_sensores():
    return DadosSensores

#GET_ID
@app.route('/DadosSensores/<int:id>', methods=['GET'])
def get_dados_sensores_id(id):
    for dados in DadosSensores:
        if dados.get('id') == id:
            return jsonify(dados)
        
#POST
@app.route('/DadosSensores', methods=['POST'])
def criar_dados():
    dados = request.json
    DadosSensores.append(dados)
    return make_response(
        jsonify(mensagem='Dados inseridos com sucesso',
                dados=dados)
    )

#PUT
@app.route('/DadosSensores/<int:id>', methods=['PUT'])
def editar_dados_id(id):
    dados_alterados = request.get_json()
    for indice, dados in enumerate(DadosSensores):
        if dados.get('id') == id:
            DadosSensores[indice].update(dados_alterados)
            return jsonify(DadosSensores[indice])
        
#DELETE
@app.route('/DadosSensores/<int:id>', methods=['DELETE'])
def deletar_dadoS(id):
    for indice,dados in enumerate(DadosSensores):
         if dados.get('id') == id:
             del DadosSensores[indice]
             return jsonify({'Mensagem:': 'Dados excluidos com sucesso'})

#Rodar API
app.run(port=5000, host='localhost')