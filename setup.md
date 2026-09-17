# Setup

## 1. Inicialização do ambiente virtual
Crie e acesse o ambiente virtual
```
python3 -m venv .venv
source .venv/bin/activate
```

## 2. Instale as dependencias
Execute o pip nas dependencias listadas em `requirements.txt`
```
pip install -r requirements.txt
```

## 3. Crie o banco de dados
Execute o seguinte comando para gerar o arquivo de banco de dados:
``` python
python3 setup_db
```