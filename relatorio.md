# Relatorio
Este documento, como parte do desenvolvimento deste trabalho, visa indicar as etapas de desenvolvimento do projeto e responder as questões cujo código não é capaz de responder por sí proprio, isto é, que nescessitem de argumentação por extenso.


> **TODOS OS PRINTS REFERENCIADOS NESTE RELATÓRIO PODEM SER ENCONTRADOS DENTRO DA PASTA `/recursos_relatorio`**


## Exercício 1
Um passo a passo para o setup do ambiente virtual e da instalação das dependencias pode ser encontrado no arquivo `setup.py`.

Para executar o programa, basta rodar o comando `python3 run` dentro do ambiente virtual e com as dependencias instaladas. As configurações do uvicorn podem ser encontradas no arquivo `run`

Evidencias da configuração do hot-reload incluem:
- `recursos_relatorio/q1_hot-reload.png` 
- `recursos_relatorio/q1_status.png` 


## Exercício 2.3
Separar os routers de uma API REST por recurso facilita a divisão da solução em modulos independentes. Mantendo os endpoints e seus modelos relacionados proximos ao mesmo tempo em que os isola dos demais recursos, mantendo a objetividade do codigo e a separação de responsabilidades.