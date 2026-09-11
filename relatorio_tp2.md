# Relatorio
Este documento, como parte do desenvolvimento do TP2, visa indicar as etapas de desenvolvimento do projeto e responder as questões cujo código não é capaz de responder por sí proprio, isto é, que nescessitem de argumentação por extenso.


> **TODOS OS PRINTS REFERENCIADOS NESTE RELATÓRIO PODEM SER ENCONTRADOS DENTRO DA PASTA `/recursos_relatorio/tp2`**

## Exercício 1
### Item 1.1
Lista de misuse cases:
---
#### INJEÇÃO DE JS ARBITRÁRIO
- **Ator Malicioso:** Atacante externo

- **Ação Indesejada:** Injetar código JS dentro de uma tag `<script>` afim de fazer este código ser executado no navegador de outro usuario via `nome` ou `descrição` de um evento malicioso cadastrado pelo atacante.

- **Impacto Potencial:** O script pode ser executado no navegador de outro usuario ao ele acessar a rota `GET /eventos/html`, gerando possivel roubo de cookies, sessão, dados pessoais, dentre outros.

---
#### NEGAÇÃO DE SERVIÇO
- **Ator Malicioso:** Bot ou script gerado por atacante externo.

- **Ação Indesejada:** Realizar um volume massivo de chamadas a endpoints sem restrição de taxa (rate limiting) ou autenticação.

- **Impacto Potencial:** Queda de serviço por limite de memoria.

---
#### INCONSISTÊNCIA DE DADOS
- **Ator Malicioso:** Bot ou script gerado por atacante externo.

- **Ação Indesejada:** Disparo de requisições paralelas em `POST /eventos`

- **Impacto Potencial:** Gera inconsistencia nos IDs de eventos se aproveitando da variavel global `latest_used_id` podendo causar bugs e falhas em outros endpoints.

---
#### SOBRECARGA DE REDE
- **Ator Malicioso:** Atacante malicioso.

- **Ação Indesejada:** Realização de chamadas repetidas ao endpoint `GET /eventos/`.

- **Impacto Potencial:** Por falta de paginação ou rate-limiting no endpoint, ele é vulneravel a sobrecarga conforme a base de dados cresce. O tamanho da resposta do endpoint passa a ficar cada vez maior gerando sobrecarga na rede, tornando a API lenta.

---


### Item 1.2
Vetores de ataque para cada misuse case:

#### Injeção de HTML ou JS arbitrário :
- Ausencia de autenticação em `POST eventos/`.
- Falta de sanitização dos dados recebidos em `POST eventos/`.
- Falta de sanitização dos dados retornados em `GET /eventos/html`.

#### Negação de serviço :
- Ausencia de autenticação em `POST eventos/`.
- Falta de mecanismo de *rate-liiting* nos endpoints.

#### Inconsistencia de dados :
- Falta de banco de dados ou outro mecanismo capaz de realizar transações atômicas
- Falta de banco de dados ou outro mecanismo capaz de identificar IDs duplicados

#### Sobrecarga de rede :
- Ausencia de autenticação em `GET /eventos/`.
- Falta de paginação, filtragem e outras otimizações em `GET /eventos/`. 
- Falta de mecanismo de *rate-liiting* em `GET /eventos/`.
- Falta de mecanismo de *cache* em `GET /eventos/`.

### Item 1.3
Ranking de priorização por impacto e justificativa.

- **1° Injeção de HTML ou JS arbitrário** : Possui o maior impacto na segurança final, pois viola diretamente a Confidencialidade e a Integridade dos usuários.

- **2° Negação de serviço** : Possui o maior na disponibilidade do sistema já que impede completamente o seu funcionamento.  

- **3° Inconsistencia de dados** : Possui impacto menor *Negação de serviço* que viola a integridade do sistema, mas não o impede de funcionar. 

- **4° Sobrecarga de rede :** Possui menor impacto no sistema do que *Negação de serviço* e *Inconsistencia de dados* já que degrada o serviço mas não o impede de funcionar nem prejudica sua integridade, é mais proximo de uma falha de otimização.
