<h1>Aplicação Web em Python consumindo dados obtidos da API da Marvel </h1>
Este projeto contém uma lista com os três personagens favoritos e a partir de cada um, é possivel exibir as cinco primeiras histórias aos quais cada um conste.<br/>
<br/>
Documentação API Marvel:<br/>
https://developer.marvel.com/docs#

<h2>Ambiente de desenvolvimento</h2>
<div>
    <ul>
        <li>Python 3.6</li>
        <li>Pycharm 2018.2.4 (Community Edition)</li>
        <li>Ubuntu 18.04</li>
    </ul>
<div>

<h2>Guia de instalação</h2>
<div>
    <strong>Clonar o repositório</strong><br/><br/>
    $ git clone https://gitlab.com/marciafc.info/marvel-py.git <br/>
    $ cd marvel-py <br/><br/>
</div>    

<strong>Instalar dependências</strong><br/>
<div>    
    $ pip3 install  -r requirements.txt<br/><br/>
</div>

<strong>Rodar a aplicação</strong><br/>
<div>
    $ python3 run_app.py<br/><br/>
    Aguarde alguns segundos e acesse a aplicação no navegador (no terminal o cursor ficará piscando)<br/><br/>
 </div>   
 
<strong>Acessar a aplicação no navegador</strong><br/>
<div>
   http://127.0.0.1:5000/<br/>
 </div>  

<h2>Testes</h2>
<div>
    $ python3 -m unittest <br/>
</div>    