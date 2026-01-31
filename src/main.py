import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def gethomepage():
  html = """
  <!DOCTYPE html>
  <html>
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wallace Camargo - API</title>
    <style>
      body {
        font-family: Arial, sans-serif;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        margin: 0;
        padding: 20px;
        min-height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
      }
      .container {
        max-width: 600px;
        background: white;
        border-radius: 20px;
        padding: 40px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.2);
      }
      h1 {
        color: #333;
        text-align: center;
        margin-bottom: 10px;
      }
      .subtitle {
        color: #666;
        text-align: center;
        margin-bottom: 30px;
        line-height: 1.6;
      }
      h2 {
        color: #667eea;
        font-size: 20px;
        margin-bottom: 20px;
      }
      .link-container {
        display: flex;
        flex-direction: column;
        gap: 15px;
      }
      .link-item {
        background: #f8f9fa;
        border: 2px solid #e9ecef;
        border-radius: 10px;
        padding: 15px 20px;
        text-decoration: none;
        color: #333;
        transition: all 0.3s ease;
        display: block;
      }
      .link-item:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.3);
        border-color: #667eea;
      }
      .link-title {
        font-weight: bold;
        color: #667eea;
        margin-bottom: 5px;
      }
      .link-url {
        font-size: 14px;
        color: #666;
        word-break: break-all;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <h1>🚀 Wallace Camargo</h1>
      <p class="subtitle">
        Welcome to Wallace Camargo's API developed for data engineering tests and studies
      </p>
      
      <h2>Links:</h2>
      
      <div class="link-container">
        <a href="/dadospessoais" class="link-item">
          <div class="link-title">👤 My Personal Data</div>
          <div class="link-url">/dadospessoais</div>
        </a>
        
        <a href="https://wlcamargo.github.io/" target="_blank" class="link-item">
          <div class="link-title">💼 My Portfolio</div>
          <div class="link-url">https://wlcamargo.github.io/</div>
        </a>
        
        <a href="https://www.linkedin.com/in/wallace-camargo-35b615171/" target="_blank" class="link-item">
          <div class="link-title">💼 My Linkedin</div>
          <div class="link-url">https://www.linkedin.com/in/wallace-camargo-35b615171/</div>
        </a>
        
        <a href="https://www.youtube.com/channel/UCK0B4IoF57JoiVVVeEcN8-A/videos" target="_blank" class="link-item">
          <div class="link-title">▶️ My Youtube</div>
          <div class="link-url">https://www.youtube.com/channel/UCK0B4IoF57JoiVVVeEcN8-A/videos</div>
        </a>
        
        <a href="https://github.com/wlcamargo" target="_blank" class="link-item">
          <div class="link-title">🐙 My Github</div>
          <div class="link-url">https://github.com/wlcamargo</div>
        </a>
      </div>
    </div>
  </body>
  </html>
  """
  return html

@app.route('/dadospessoais')

def getdados():

  x = (
        {
        'id' : 1,
        'name': 'wallace camargo', 
        'nationality': 'brazilian',
        'birth_date': '07/11/1988',
        'residence': 'portugal',
        'education': 'mba in business intelligence',
        'profession': 'data engineer',
        'technologies': 'python, spark, sql, cloud, fabric, airflow, dbt, docker',
        'portfolio': 'https://wlcamargo.github.io/',
        'github': 'https://github.com/wlcamargo',
        'youtube':'https://www.youtube.com/channel/UCK0B4IoF57JoiVVVeEcN8-A/videos',
        'linkedin': 'https://www.linkedin.com/in/wallace-camargo-35b615171/'
      
        }
      )
  return jsonify(x)

app.run(host='0.0.0.0')
