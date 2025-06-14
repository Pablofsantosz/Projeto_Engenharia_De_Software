 <div align="left"> 
  <img src="https://github.com/user-attachments/assets/1671ae0c-2c24-40f4-bb2d-10f31841f12d" height="40" alt="Nome do Projeto"  />
  <img width="220" />
  <img src="https://portal.unicap.br/documents/475032/750674/Unicap_Icam_Tech-01.png/13922805-cdef-7e74-4d8c-e450b9e162f0?t=1605909509227" height="100" alt="UNICAP logo"  />
</div>

#

<p><h4>🛠️ Nossas Ferramentas:</h4> </p>

  <p align="left">
    <a href="https://www.figma.com/design/DNK3Ejy9Nl4oP6jBZP73Wz/Untitled?node-id=0-1&t=i4fZURRrA3fpa9fn-1"><img src="https://img.shields.io/badge/figma-%23F24E1E.svg?style=for-the-badge&logo=figma&logoColor=white" alt="Figma" /></a>
    <img width="4" />
    <a href="https://trello.com/b/3Qem3tDw/projeto-engenharia-de-software"><img src="https://img.shields.io/badge/Trello-%23026AA7.svg?style=for-the-badge&logo=Trello&logoColor=white" alt="Trello" target ="_blank" /></a>
    <img width="4" />
   
  </p>
<a href="Images/diagrama-3requisitos.png" target="_blank">
  <img src="https://img.shields.io/badge/Diagrama de%20Atividade-6A0DAD.svg?style=for-the-badge&logo=draw.io&logoColor=white" alt="Abrir Diagrama" />
</a>

---

  <h1 align="center">FastRx<p> </p></h1>
  <h1 align="center">🩺 Sistema de Receituário - UPA Emergência Pediátrica<p> </p></h1>

<div align="center">
  <img src="Images/Tela de login.png" width="400" />
  <img src="Images/Tela homepage.png" width="365" />
</div>

<br>

<p><h4>📌 Visão Geral</h4> Este projeto é um sistema web desenvolvido para gerar automaticamente receituários médicos durante atendimentos em emergências pediátricas da rede pública de saúde (UPA - PE). A iniciativa nasceu da necessidade de otimizar o tempo dos profissionais, reduzir erros e melhorar a qualidade do atendimento.</p><br>

---


<p><h4>🚨 Problema:</h4> Ana atua na linha de frente do atendimento em uma emergência pediátrica da rede pública de saúde do estado de Pernambuco. Durante a rotina, observou que dedicava uma parte significativa do tempo de consulta à elaboração manual de receituários. Atividade que embora essencial, revelou-se ineficiente diante da recorrência de casos clínicos semelhantes.</p>
  
<p><i>(Pacientes com sintomas e diagnósticos repetitivos ou de prognóstico equivalente).</i></p>

<p>Consequentemente, Ana escreve praticamente os mesmos receituários 12, 15 vezes ao dia, tornando as consultas cansativas e, por mais que pouco, suscetíveis a falha médica.</p>

---

<p><h4>✅ Solução: </h4>Diante dessa situação e após algumas reuniões com Ana para levantamento de informações, foi decidido criar um sistema WEB para geração automática de receituários em emergências pediátricas em UPAs - PE. <b>É importante ressaltar que o receituário é feito durante o tempo de consulta.</b></p>

---

<p><h4>📝 Os receituários: </h4></p> 

<b>(Antes de explicar como funciona, é necessário explicar como se constrói um receituário)</b>
<p>Refere-se à um documento que prescreve medicamentos, tratamentos e orientações para pacientes. O objetivo do sistema é preenchê-lo com as devidas informações: </p>

<ul>
  <li> <b>Medicamento(s);</b></li>
  <li> <b>Tratamentos(s);</b></li>
  <li> <b>Orientações</b>;</li>
</ul>

<p>Intuitivamente, os receituários mudam de acordo com o diagnóstico.</p>

---

<p><h4>✅ Como funciona: </h4>Durante a consulta, após o diagnóstico do paciente, o médico acessaria o site e, após cadastro/login, preencheria os campos:</p>

<ol>
  <li> <b>Ocorre a consulta;</b></li>
  <li> <b>Obtém-se o diagnóstico do paciente;</b></li>
  <li> <b>O médico acessa nossa aplicação;</b></li>
  <li> <b>Realiza o Login/Cadastro;</b></li>
  <li> <b>Preenche os campos: </b></li>
  <ul>
    <li> <b>CID-10;</b></li>
    <li> <b>Idade;</b></li>
    <li> <b>Peso (Kg)</b></li>
  </ul>
</ol>

<br>

<p>Com os campos preenchidos, nosso sistema automaticamente gera receituários pré-prontos, fornecendo opções de escolha e, caso o médico em questão prefira/necessite, receituários limpos. </p>

---

<p><h4>🎯 Benefícios: </h4> Com o sistema funcionando, uma série de benefícios são alcançados:</p>

<ol>
  <li><b> Tempo de consulta reduzido;</b></li>
  <li><b> Falha médica improvável;</b></li>
  <li><b> Melhor prognóstico;</b></li>
  <li><b> Melhora na qualidade de trabalho;</b></li>
  <li><b> Maior atenção ao paciente;</b></li>
</ol>

---

<p><i>❓ O que é o CID-10?</i></p>
<p><i>(Classificação Internacional de Doenças, a décima revisão. Publicada pela Organização Mundial da Saúde (OMS), trata-se de um sistema de códigos alfanuméricos que permite identificar doenças, sintomas e outros problemas de saúde).</i></p>

---

<h4>🤝 Programação em Pares:</h4>

<br>

<div align="center">
  <img src="Images/Pair-programming1.png" width="360" alt="Pair programming 1"/>
  <img src="Images/Pair-programming2.png" width="360" alt="Pair programming 2"/>
  <img src="Images/programação em pares.jpg" width="500" alt="Pair programming 2"/>

</div>

<br>

<b>Durante o desenvolvimento do projeto, aplicamos a metodologia de Programação em Pares nas seguintes tarefas:</b>

- Implementação das histórias login , cadastro , excluir conta (Nunno e Pablo);
- Integração das histórias com o banco de dados sqlite3 (Nunno e Pablo);
- Implementação da auteticação do login (Nunno e Pablo);
- Correções de bugs e testes de funcionalidade (Nunno e Pablo).
- Implemetações: homepage, criar receituário, preencher com CPF, preencher com nome, preencher com peso, creiar modelo com preenchimento de modelo de receituário, editar informações, redefinir dados, gerar um receituário em branco, preencher com CID 10, logout da plataforma, imprimir receituário, gerar receituário preenchido. (Nunno, Pablo, Pedro, Malu)
- Atualização do README (Nunno, Pablo, Pedro, Malu)
- Tentativa de Deploy (Nunno, Pablo, Pedro, Malu, Lucas)

#

<b>Essa abordagem permitiu uma maior troca de conhecimento e agilidade na resolução de problemas</b>



---


<h4>🗃️ Diagramas de Atividade</h4>

<ul>
  <li>  <b>Diagrama Login, Cadastro e Excluir conta:</b><br><br>
  <img src="Images/diagrama-3requisitos.png" width="1000" align="center" style="margin-top: 50px; margin-bottom: 30px;" alt="Diagrama 1"/>
  </li>

  <br><br>

  <li>  <b>Diagrama Editar dados do usuário:</b><br><br>
  <img src="Images/Diagrama editar informações do usuário.jpg" width="300" align="center" style="margin-top: 50px; margin-bottom: 30px;" alt="Diagrama 2"/>
  </li>
  
  <br><br>

  <li>  <b>Diagrama Criar receituário carregando modelo ou em branco:</b><br><br>
  <img src="Images/Diagramas criar receituario carregando modelo ou em branco.jpg" width="800" align="center" style="margin-top: 50px; margin-bottom: 30px;" alt="Diagrama 3"/>
  </li>
  
  <br><br>  

  <li>  <b>Diagrama Inserir nome, CPF, idade, peso e OBS do paciente:</b><br><br>
  <img src="Images/Diagramas inserir dados do paciente.jpg" width="1000" align="center" style="margin-top: 50px; margin-bottom: 30px;" alt="Diagrama 4"/>
  </li>
  
  <br><br>
  
  <li>  <b>Diagrama Visualizar modelos de preenchimento de receituario ou Histórico de consulta:</b><br><br>
  <img src="Images/Diagramas visualizar modelos de preenchimentos de receituarios e historico de consultas.jpg" width="500" align="center" style="margin-top: 50px; margin-bottom: 30px;" alt="Diagrama 5"/>
  </li>
  
  <br><br>
</ul>

---

<h4>🎥 Screencast das Funcionalidades</h4>

1. O vídeo abaixo apresenta a demonstração do protótipo no figma:

   <a href="https://youtu.be/uQzJRZK_C74?si=oOG6BtTm4aDfDp6o"><img src="https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white" alt="ScreenCast" /></a>
    <img width="4" />

2. O vídeo abaixo apresenta a demonstração das funcionalidades implementadas:

   <a href="https://www.youtube.com/watch?v=m5BIkN4cZ7Q"><img src="https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white" alt="ScreenCast" /></a>
  </p>

<h3>Funcionalidades demonstradas:</h3>

<ul>
  <li>  <b>UH Cadastro na plataforma:</b><br><br>
  <img src="Images/Tela de cadastro.png" width="450" align="center" style="margin-top: 50px; margin-bottom: 30px;" alt="Tela de cadastro"/>
  </li>

  <br><br>

  <li> <b>UH Login na plataforma:</b><br><br>
  <img src="Images/Tela de cadastro.png" width="450" align="center" style="margin-top: 50px; margin-bottom: 30px;" alt="Tela de login"/>
  </li>

  <br><br>
   
  <li> <b>UH Confirmar Senha Para Excluir Conta:</b><br><br>
  <img src="Images/Tela inserir senha para excluir conta.png" width="450" align="center" style="margin-top: 50px; margin-bottom: 30px;" alt="Tela de inputar senha para exclusão da conta"/>
  </li>

   <br><br>
   
  <li> <b>UH Home Page:</b><br><br>
  <img src="Images/Tela homepage.png" width="450" align="center" style="margin-top: 50px; margin-bottom: 30px;" alt="tela de home page"/>
  </li>

   <br><br>
   
  <li> <b>UH Histórico de Consulta:</b><br><br>
  <img src="Images/Visualizar historico de consultas.jpg" width="450" align="center" style="margin-top: 50px; margin-bottom: 30px;" alt="tela que vizualiza o histórico de consulta"/>
  </li>

  
   <br><br>
   
  <li> <b>UH Modelos receituário CID_10:</b><br><br>
  <img src="Images/Modelo receituário CID_10.jpg" width="450" align="center" style="margin-top: 50px; margin-bottom: 30px;" alt="Modelo pré preenchidos"/>
  </li>
  
  
   <br><br>
   
  <li> <b>UH Gerar novo receituário:</b><br><br>
  <img src="Images/Gerar Novo Receituário.jpg" width="450" align="center" style="margin-top: 50px; margin-bottom: 30px;" alt="Novo Receituário"/>
  </li>
    
  
   <br><br>
   
  <li> <b>UH Print do Receituário Criado:</b><br><br>
  <img src="Images/Visualização do receituario2.jpg" width="600" align="center" style="margin-top: 100px; margin-bottom: 60px;" alt="Novo Receituário"/>
  </li>
  
</ul>

---
<h4>🐞 Bug Tracker</h4>

Durante o desenvolvimento do projeto, enfrentamos algumas dificuldades técnicas e bugs, que documentamos abaixo como parte do nosso processo de aprendizado e evolução do sistema:

<h3>🧠 Dificuldades </h3>

- **Aprendizado do framework Django**: Tivemos dificuldades iniciais no entendimento da estrutura do Django e na prática de suas convenções, especialmente na separação entre models, views e templates.
- **Manipulação do banco de dados**: Foi desafiador compreender como o Django ORM funciona e como realizar as migrações corretamente sem corromper os dados.
- **Funcionalidade**: Toda vez que atualizamos o modelo do receituário, aparece uma mensagem em excluir conta
-**Deploy**: tivemos uma enorme dificuldade em fazer o deploy pelos seguintes fatos:
 - Trabalho muito extenso;
 - Uso do SQLite;
 - versão do python (python-3.12.1);
 - ***Servidores que testamos***
     - date space 
     - pythonanywhere
     - vercel
     - replit
     - fly
     - railaway
     - render
     - Github
   Utilizei todos esses caminhos para conseguir fazer o deploy,mas pelos motivos acima, não foi aceito.



### 🐛 Bug Encontrado - IDs não reutilizados

Durante os testes, identificamos um comportamento específico no banco de dados:

 **Cenário**: Ao cadastrar três usuários (1, 2, 3) e deletar o usuário de ID 2, a lista resultante fica como (1, 3).  
 **Problema**: O ID 2 não é reutilizado então sempre ficara um espaço vazios sendo ocupado por nada  (isso acontece por que o sqlite é um  banco de dados relacional com chave primária autoincremental)

---

<h4 align="left">👥 Integrantes:</h4>
<p>Malu de Faria Neves Bezerra</p>
<p>Nunno Wakiyama Diniz Carvalho</p>
<p>Pablo Felipe dos Santos</p>
<p>Pedro Alves dos Santos </p>



