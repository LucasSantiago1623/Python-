from flask import Flask


app = Flask(__name__) # inicio o flask

@app.route('/decorator') # Isso é o decorator, ele é usado para mapear a função abaixo para a rota '/'
def decorator():
    return 'Decorators em Python são funções especiais que modificam ou estendem o comportamento de outras funções ou métodos sem alterar seu código-fonte original. ' \
    'Eles funcionam "embrulhando" a função original com uma nova, adicionando funcionalidades antes ou depois da execução dela, sendo amplamente usados para logging, ' \
    'autenticação e cache.'' # Isso é o que será retornado quando a rota for acessada'

@app.route('/serve') # Isso é outro decorator, mapeando a função abaixo para a rota '/hello'
def Funcionalidade():
    return 'O Decorator lhe permite estruturar sua lógica de negócio em camadas, criar um decorador para cada camada, ' \
    'e compor objetos com várias combinações dessa lógica durante a execução.' # Isso é o que será retornado quando a rota '/hello' for acessada

@app.route('/Como_usa')
def utiliza():
    return ''

if __name__ == '__main__':
    app.run(debug=True) # Isso inicia o servidor Flask em modo de depuração, o que é útil para desenvolvimento