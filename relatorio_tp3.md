# Relatorio
Este documento, como parte do desenvolvimento do TP3, visa indicar as etapas de desenvolvimento do projeto e responder as questões cujo código não é capaz de responder por sí proprio, isto é, que nescessitem de argumentação por extenso.


> **TODOS OS PRINTS REFERENCIADOS NESTE RELATÓRIO PODEM SER ENCONTRADOS DENTRO DA PASTA `/recursos_relatorio/tp2`**

# Exercício 1
### Item 1.1
Evidencia da extração de informações privadas de usuarios (incluindo hash da senha) utilizando SQL Injection :

![evidencia_q1_1.jpg](/recursos_relatorio/tp3/evidencia_q1_1.png)

[Clique aqui para acessar o arquivo da imagem evidencia_q1_1.png](/recursos_relatorio/tp3/evidencia_q1.png)

### Item 1.3
Evidencia da correção da vulnerabilidade:
![evidencia_q1_2.jpg](/recursos_relatorio/tp3/evidencia_q1_2.png)

[Clique aqui para acessar o arquivo da imagem evidencia_q1_2.png](/recursos_relatorio/tp3/evidencia_q2.png)


---

# Exercício 2
### Item 2.1
Vulnerabilidades '*OWASP Top Ten*' identificadas no endpoint `/auth/login`:

###### A07:2025 Authentication Failures 
Ausencia de *rate-limiting* ou de acompanhamento de numero de tentativas no endpoint de login pode permitir a descoberta de uma senha por combinações exaustivas e automatizadas.
*referencia: [https://top10.owasp.org/2025/A07_2025-Authentication_Failures/](https://top10.owasp.org/2025/A07_2025-Authentication_Failures/)*

###### A09:2025 Security Logging & Alerting Failures:
O endpoint de login não possui logs de auditoria 
*referencia: [https://top10.owasp.org/2025/A09_2025-Security_Logging_and_Alerting_Failures/](https://top10.owasp.org/2025/A09_2025-Security_Logging_and_Alerting_Failures/)*

###### A10:2025 Mishandling of Exceptional Conditions:
Apesar do endpoint considerar o caso de usuario e/ou senha incorretos, não há tratamento de exeções no endpoint, o que pode causar *crashes*. 
*referencia: [https://top10.owasp.org/2025/A10_2025-Mishandling_of_Exceptional_Conditions/](https://top10.owasp.org/2025/A10_2025-Mishandling_of_Exceptional_Conditions/)*

### Item 2.2
Em todos os casos apontados, a falha não se da por um trecho de código em específico, mas sim pela falta de código que lida com os erros em questão.

### Item 2.3
Segue aqui, para os casos identificados, a categoria OWASP e risco associado:
- **Authentication Failures**: Pode permitir que um usuario ilegitimo acesse o sistema.
- **Security Logging & Alerting Failures**: Invisibiliza ataques ao endpoint, ou seja, dificulta que a equipe de TI identifique um ataque e, no caso de um ataque bem sucedido, impede a auditoria do ocorrido.
- **Mishandling of Exceptional Conditions**: Pode gerar crashes inesperados e falha na disponibilidade do sistema.


---

# Exercício 3
### Item 3.1
Evidencia da leitura dos dados do usuario de `id=1` por um usuario não logado:
![evidencia_q3_1.jpg](/recursos_relatorio/tp3/evidencia_q3_1.png)

[Clique aqui para acessar o arquivo da imagem evidencia_q3_1.png](/recursos_relatorio/tp3/evidencia_q3_1.png)

### Item 3.2
A verificação de *ownership* poderia ser feita tanto na camada de API quanto na camada de abstração do acesso a dados (DAL).

**Na API**, poderiamos garantir que o usuário está logado e verificar se o id que ele requisita é o dele mesmo (ou se ele é admin e tem o poder de acessar as informações de outros usuarios)

**Na DAL**, poderiamos implantar uma verificação simples de leitura para garantir que somente o dono do recurso tem o direito de le-lo.


### Item 3.3
Deveriamos verificar se o `ID` do usuario logado é o mesmo que argumento fornescido no URL. Caso o usuario não esteja logado, podemos retornar `401 UNALTHORIZED`, caso o usuario logado esteja requisitando as informações de um `id` que não seja o dele, podemos retornar `403 FORBIDDEN`