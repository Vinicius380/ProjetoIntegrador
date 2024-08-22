from flask import Flask

#Importa o banco de dados
from bd import Carros

#Instanciar o modulo Flask na nossa variavel app
app = Flask('carros')

#PRIMEIRO METODO - VISUALIZAR OS DADOS (GET)
#app.route -> Definir que essa funcao e uma rota para que o Flask entenda que aquilo e um metodo que deve ser executado
@app.route('/carros', methods=['GET'])

def get_carros():
    return Carros

#PRIMEIRO METODO PARTE 2 - VISUALIZAR DADOS POR ID (GET / ID)

#SEGUNDO METODO - CRIAR NOVOS DADOS (POST)

#TERCEIRO METODO - EDITAR DADOS (PUT)

#QUARTO METODO - DELETAR DADOS (DELETE)