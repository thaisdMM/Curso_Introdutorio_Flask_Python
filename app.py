#Importação

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) #instancia o caminho do flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'

db = SQLAlchemy(app)

#Modelagem > Linha: registro - Coluna: informações
#Produto(id, name, price, description)

class Product(db.Model):
   id = db.Column(db.Integer, primary_key=True) #modelando a coluna, primary_key é única pois id é o identificado do produto
   name = db.Column(db.String(120), nullable=False) # nullable=False > não quer que esse parâmetro seja nulo/opcional
   price = db.Column(db.Float, nullable=False) # nullable=False > não quer que esse parâmetro seja nulo/opcional
   description = db.Column(db.Text, nullable=True) #Text para nao ter limite de caractere como na String; nullable=True pode ser opcional

#Definir rota para adicionar produtos- pegar o que está na documentação swagger.yaml
#Definiu também o método que irá aceitar "POST"

@app.route('/api/poducts/add', methods=["POST"])
def add_product():
   data = request.json 
   #criar o produto > pega o que o cliente escrever; no description pode retornar o que o cliente escreveu ou vazio
   product = Product(name=data["name"], price=data["price"], description=data.get("description", "")) 
  
   # adicionar o produto no banco de dados
   db.session.add(product)
   db.session.commit()
   return "Produto cadastrado com sucesso!"

#Definir uma rota raiz(página inicial da api) e a função que será executada ao requisitar

@app.route('/')
def hello_world():
   return 'Hello World'

#rodar a api e o debug usado para desenvolvimento, nao produção(disponibilizado para usuário)
if __name__ == "__main__":
   app.run(debug=True) 