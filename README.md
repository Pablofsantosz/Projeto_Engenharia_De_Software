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
    <a href="https://youtu.be/uQzJRZK_C74?si=oOG6BtTm4aDfDp6o"><img src="https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white" alt="ScreenCast" /></a>
  </p>
<a href="https://drive.google.com/file/d/1KYlZ8NbpWH50f1MgVje8TT58aSciFUOs/view?usp=sharing" target="_blank">
  <img src="https://img.shields.io/badge/Diagrama de%20Atividade-6A0DAD.svg?style=for-the-badge&logo=draw.io&logoColor=white" alt="Abrir Diagrama" />
</a>

---

  <h1 align="center">FastRx<p> </p></h1>
  <h1 align="center">🩺 Sistema de Receituário - UPA Emergência Pediátrica<p> </p></h1>
  <img src="https://private-user-images.githubusercontent.com/134156256/437454003-efb351ed-f752-41a5-a114-8612326efc7f.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDc3NjU0MjcsIm5iZiI6MTc0Nzc2NTEyNywicGF0aCI6Ii8xMzQxNTYyNTYvNDM3NDU0MDAzLWVmYjM1MWVkLWY3NTItNDFhNS1hMTE0LTg2MTIzMjZlZmM3Zi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNTIwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDUyMFQxODE4NDdaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1kMTViZTVmOGU1MjA4OWVjNWZiZjNkMjcyYzM3YjBmMzQwNjdjYzM5MmY5NjEyYTc2ZDg0YTIwMDE1MjI4ZWMzJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.6D1qwEOFsXI_YMw42EJ_B68aiQ7c3BP_1uHr5ZV501A" height="300" align="center" alt="Nome do Projeto"  
  
  




<p><h4>📌 Visão Geral</h4> Este projeto é um sistema web desenvolvido para gerar automaticamente receituários médicos durante atendimentos em emergências pediátricas da rede pública de saúde (UPA - PE). A iniciativa nasceu da necessidade de otimizar o tempo dos profissionais, reduzir erros e melhorar a qualidade do atendimento.</p>

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

Durante o desenvolvimento do projeto, aplicamos a metodologia de Programação em Pares nas seguintes tarefas:

- Implementação do login , cadastro , excluir (Nunno e Pablo);
- Implementação da auteticação do login (Nunno e Pablo);

- Correções de bugs e testes de funcionalidade (Nunno e Pablo).
 </p></h1>
  <img src="https://github.com/malu-fnb/uparImagem/blob/main/Imagem%20do%20WhatsApp%20de%202025-05-20%20%C3%A0(s)%2010.40.55_6d770541.jpg" height="300" align="center" alt="programação em pares"  
<p> <h4>
Essa abordagem permitiu uma maior troca de conhecimento e agilidade na resolução de problemas



---

<h4>🎥 Screencast das Funcionalidades</h4>

O vídeo abaixo apresenta a demonstração das funcionalidades implementadas:

   <a href="https://youtu.be/uQzJRZK_C74?si=oOG6BtTm4aDfDp6o"><img src="https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white" alt="ScreenCast" /></a>
  </p>

Funcionalidades demonstradas:
<ul>
  <li>  <b> UH Cadastro na plataforma:</b>
 </p></h1>
  <img src="https://github.com/malu-fnb/uparImagem/blob/main/Captura%20de%20tela%202025-05-20%20132632.png" height="300" align="center" alt="programação em pares"  
<p> <h4>

  <li> <b>UH Login na plataforma: </b>
 </p></h1>
  <img src="https://github.com/malu-fnb/uparImagem/blob/main/Captura%20de%20tela%202025-05-20%20132357.png" height="300" align="center" alt="programação em pares"  
<p> <h4>
  <li> <b>UH Excluir Conta: </b>
 </p></h1>
  <img src="https://github.com/malu-fnb/uparImagem/blob/main/Captura%20de%20tela%202025-05-20%20132557.png" height="300" align="center" alt="programação em pares"  
<p> <h4>
</ul>

---
<h4>🐞 Bug Tracker</h4>

Durante o desenvolvimento do projeto, enfrentamos algumas dificuldades técnicas e bugs, que documentamos abaixo como parte do nosso processo de aprendizado e evolução do sistema:

<h3>🧠 Dificuldades </h3>

- **Aprendizado do framework Django**: Tivemos dificuldades iniciais no entendimento da estrutura do Django e na prática de suas convenções, especialmente na separação entre models, views e templates.
- **Manipulação do banco de dados**: Foi desafiador compreender como o Django ORM funciona e como realizar as migrações corretamente sem corromper os dados.


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



