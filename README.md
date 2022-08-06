<h1>Passo a passo das instalações</h1>

Instalando o Virtual Environment 

````sh
python3 -m pip install virtualenv
````

````sh
mkdir mytest
cd mytest
````

criando o ambiente virtual
````sh
python3 -m venv env
````

ativando o ambiente virtual
````sh
source env/bin/activate
````

instalando as bibliotecas que vamos precisar
````sh
python3 -m pip install flask
````

preparando o ambiente para versionamento no git
````sh
git init
````

removendo o ambiente virtual do versionamento
````sh
echo 'env' > .gitignore
````

criando o arquivo de requirements com as bibliotecas
````sh
pip freeze > requirements.txt
````

Instalando MySQLServer

[Tutorial Ubuntu 20.04](https://phoenixnap.com/kb/install-mysql-ubuntu-20-04)

[Tutorial Windows 10](https://www.lifewire.com/how-to-install-mysql-windows-10-4584021)

[Tutorial Windows Server](https://phoenixnap.com/kb/install-mysql-on-windows)


Linux - Rodando o código Flask
````sh
export FLASK_APP=bbb
flask run
````

Windows - Rodando o código Flask
````sh
set FLASK_APP=bbb
python -m flask run
````

Iniciando um projeto no GitHub
[Tutorial Githun](https://docs.github.com/pt/get-started/quickstart/hello-world)

[Comandos básicos do Git](https://comandosgit.github.io)