from flask import Flask 

app = Flask(__name__)

@app.route('/') 
def curriculo(): 
    return '''
   <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
        <style> 
        body {
        font-family: font-family: "Gill Sans", sans-serif;
        color: #086B81;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 80vh; 
        background-color: #96C6FC;
        
              }

        .container{
        border: 1px solid;
        border-radius: 10%;
        background-color: white;
        padding: 20px;

           }   
        </style>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Currículo</title>
        </head>
        <body>
        <div class="container">
            <h1>Currículo</h1>

            <h2> 🧑🏾 Informações Pessoais</h2>
            <ul>
                <li><strong>Nome: </strong> Lucas Santiago</li>  
                <li><strong>Email: </strong> lucassantiagocostatarabal@gmail.com
                <li><strong>Telefone: </strong> (31) 971533461 </li>
                <li><strong>Endereço: </strong> Rua Úrsula Paulino 1321, Torre 1, Ap - 1607
            </ul>

            <h2> 👨🏾‍💻 Formação Técnica</h2>
            <ul>
                <li><strong>Escola:</strong> Cotemig Barroca</li>
                <li><strong>Curso: </strong> Cursando 3° Ano Ensino Médio Técnico </li>
                <li><strong>Ocupação: </strong> Estudante</li>
            </ul>
            </div>
        </body>
        </html>
'''
if __name__ == '__main__':
    app.run(debug=True)
