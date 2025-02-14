#Importação

from flask import Flask

app = Flask(__name__) #instancia o caminho do flask

#Definir uma rota raiz(página inicial da api) e a função que será executada ao requisitar

@app.route('/')
def hello_world():
   return 'Hello World'

#rodar a api e o debug usado para desenvolvimento, nao produção(disponibilizado para usuário)
if __name__ == "__main__":
   app.run(debug=True) 

