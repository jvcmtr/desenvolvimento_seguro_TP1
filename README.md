# Desenvolvimento Seguro de Aplicações Web
*Repositorio utilizado para o cumprimento dos testes de performance da disciplina de Desenvolvimento Seguro de Aplicações Web (2026.3T). Por João Ramos*

Para acessar a aplicação e documentação no estagio de entrega de cada teste de performance, acesse o branch relevante (Exemplo: branch `tp1` diz respeito as questões do TP1)

---
# Modulos

## **API** *(routes)*
`/src/API`

Application Program Interface - Camada de alto nivel destinada a definir a interface do serviço. Contém as rotas e os endpoints fornescidos pelo programa.


## **Models**
`/src/models`

Modulo que contem as classes especificas da camada de dominio, isto é, as classes que correspondem às entidades e recursos do sistema. 


## **DAL** *(database)*
`/src/DAL`

Data Access Layer - Camada de destinada a abstrair a comunicação do sistema com um repositorio generico. Atualmente 
esta camada é somente um mock, ou seja, nenhuma função foi implementada para abstrair a funcionalidade e o codigo acessa diretamente um array.


---

# Executando o projeto
Para executar o projeto, siga o passo a passo disponível em `setup.py` e execute o seguinte comando:
```
python3 run 
``` 
