# Relatorio
Este documento, como parte do desenvolvimento do TP2, visa indicar as etapas de desenvolvimento do projeto e responder as questões cujo código não é capaz de responder por sí proprio, isto é, que nescessitem de argumentação por extenso.


> **TODOS OS PRINTS REFERENCIADOS NESTE RELATÓRIO PODEM SER ENCONTRADOS DENTRO DA PASTA `/recursos_relatorio/tp2`**

# Exercício 1
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

---

# Exercício 2
![Clique aqui para ver o arquivo ANALIZE_STRIDE.csv](/recursos_relatorio/tp2/ANALIZE_STRIDE.csv)

Categoria STRIDE        | Componente                                                      | Ameaça Identificada
| --- | --- | --- |
Spoofing                | Rota de Criação de Evento                                       | "Forja de identidade ao preencher o campo `organizador` com dados de outro usuario."
Denial of Service (DoS) | Rota de Criação de Evento                                       | "Realizar um volume massivo de chamadas a endpoints sem restrição de taxa (*rate limiting*) ou autenticação."
Tampering               | Armazenamento                                                   | "Corrupção da integridade por conta de inconsistencia nos IDs de eventos se aproveitando da variavel global `latest_used_id`."
Repudiation             | Armazenamento                                                   | "Impossibilidade de rastrear ou auditar quem inseriu determinado evento malicioso devido à ausência de logs no repositório."
Information Disclosure  | View de Listagem HTML                                           | "Exposição de dados de sessão e cookies devido à injeção de JS via tag `<script>`."
Elevation of Privilege  | Camada de Autenticação e Autorização (*Ainda não implementado*) | "Possibilidade de edição de eventos de terceiros caso o controle de acesso e validação de identidade não seja adequadamente implementado."

---

# Exercício 3
> *O arquivo requerido pela questão pode ser encontrado em `/recursos_relatorio/tp2/threat_model.md` ou acessando o link abaixo*

![Clique aqui para acessar o arquivo threat_model.md](/recursos_relatorio/tp2/threat_model.md)

# Exercício 4
![EventosAPI_TrustBoundries.png](/recursos_relatorio/tp2/EventosAPI_TrustBoundries.png)
![Clique aqui para acessar o arquivo da imagem EventosAPI_TrustBoundries.png](/recursos_relatorio/tp2/EventosAPI_TrustBoundries.png)

O diagrama acima demostra de forma abstraida as partições do sistema bem como o trafego de dados e as fronteiras de confiança entre os componentes do sistema. Juntamente com o documento ![threat_model.md](/recursos_relatorio/tp2/threat_model.md) podemos veríficar que as ameaças de *Spoofing*, *Denial of Service*, *Information Disclosure* e *Elevation of Privilege* ocorrem no cruzamento entre EventosAPI e o Cliente, Já que se aproveitam da falta de validação de identidade, *rate-limiting* e sanitização dos dados trafegados. Ao mesmo tempo, podemos verificar que Tampering e Repudiation ocorrem na fronteira entre EventosAPI e a camada de persistencia de dados, já que se aproveitam de falhas de implementação do sistema como o modelo de geração dos IDs e a falta de logs persistentes.

**Vale a pena ressaltar que existe uma desconexão central nesta análize, isso porque o diagrama representa o sistema como ele *planeja* ser implementado (com autenticação, autorização e persistencia), enquanto a analize de modelagem de ameaças aponta as falhas que existem na implementação atual.**
