import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')

def gethomepage():
  return 'Olá, seja bem vindo ao site desenvolvido por Wallace Camargo'

@app.route('/dadospessoais')

def getdados():

  x = (
        {
        'id' : 1,
        'nome': 'wallace camargo', 
        'nacionalidade': 'brasileiro',
        'data_nascimento': '07/11/1988',
        'residencia': 'portugal',
        'formacao': 'bachareal em administracao',
        'profissao': 'consultor de business intelligence',
        'tecnologias': 'power bi, sql server, t-sql, python e pentaho',
        'portfolio': 'https://sites.google.com/view/wallacecamargo',
        'github': 'https://github.com/wlcamargo',
        'youtube':'https://www.youtube.com/channel/UCK0B4IoF57JoiVVVeEcN8-A/videos',
        'linkedin': 'https://www.linkedin.com/in/wallace-camargo-35b615171/'
      
        }
      )
  return jsonify(x)

app.run(host='0.0.0.0')
