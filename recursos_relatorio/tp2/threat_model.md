# Sobre este documento
Este documento apresenta a modelagem de ameaças para a eventos-api, uma aplicação desenvolvida em Python/FastAPI voltada ao gerenciamento e exibição de eventos feita para o cumprimento dos testes de performance da disciplina de Desenvolvimento Seguro de Aplicações Web (2026.3T), Por João Ramos.

Este documento em específico tem o objetivo de cumprir o exercício 3 do Teste de performance 2 da disciplina.

# 1. Ativos principais 
**Dados de Eventos:** Informações armazenadas sobre os eventos (título, descrição, ID e organizador).
**Dados de Usuários:** Credenciais, informações pessoais e dados de sessão.
**Credenciais e Segredos** *(Ainda não implementado)*: Tokens de autenticação (JWT), senhas e variaveis de ambiente.
**Disponibilidade e Recursos do Servidor:** Memória, Disco, processamento (CPU) e largura de banda da maquina e rede onde a API é executada.

# 2. Superficies de ataque
#### Endpoints:
> Todos os endpoints a seguir são, por hora, **publicos**. 
- `POST /eventos`,
- `GET /eventos/`,
- `GET /eventos/{id}`
- `GET /eventos/html`
- `POST /users/signup` *(Ainda não implementado)*
- `POST /users/login`  *(Ainda não implementado)*

#### Repositorio 
*(Ainda não implementado)*

A interface de acesso ao repositório possui o modulo `src.DAL` como camada de abstração. A atual implementação do repositório guarda os dados em memoria não persistente.

Com a futura implantação de um banco de dados como repositório da aplicação, o acesso ao banco se torna mais uma superfície de ataque.

#### Ameaças identificadas (STRIDE)
Categoria STRIDE        |Componente                                                      |Ameaça Identificada|Proposta de mitigação 
| --- | --- | --- | --- |
Spoofing                |Rota de Criação de Evento                                       |"Forja de identidade ao preencher o campo `organizador` com dados de outro usuario."|"Implementar autenticação e preencher automaticamente os dados do organizador com as informações do usuário"
Denial of Service (DoS) |Rota de Criação de Evento                                       |"Realizar um volume massivo de chamadas a endpoints sem restrição de taxa (*rate limiting*) ou autenticação."|"Implementar *rate limiting* e limite de tamanho para os campos textuais do evento"
Tampering               |Armazenamento                                                   |"Corrupção da integridade por conta de inconsistencia nos IDs de eventos se aproveitando da variavel global `latest_used_id`."|"Implantar uma integração com banco de dados na DAL do sistema."
Repudiation             |Armazenamento                                                   |"Impossibilidade de rastrear ou auditar quem inseriu determinado evento malicioso devido à ausência de logs no repositório."|"Implementar serviço de logs no sistema. Garantir que os logs do serviço sejam persistentes"
Information Disclosure  |View de Listagem HTML                                           |"Exposição de dados de sessão e cookies devido à injeção de JS via tag `<script>`."|"Sanitizar entrada de dados na criação de eventos|Sanitizar exibição de dados na leitura html de eventos"
Elevation of Privilege  |Camada de Autenticação e Autorização (*Ainda não implementado*) |"Possibilidade de edição de eventos de terceiros caso o controle de acesso e validação de identidade não seja adequadamente implementado."|"Implementar sistema de controle de acesso|definir normas de permição de vizualização e edição|garantir em cada endpoint que o usuario possui as devidas permições."



> ![Clique aqui para ver o arquivo ANALIZE_STRIDE_COM_MITIGACAO.csv](/recursos_relatorio/tp2/ANALIZE_STRIDE_COM_MITIGACAO.csv)







