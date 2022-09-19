<h1 align="center"> SimplifiedBankingSystem </h1>
<p> 
  O trabalho consiste em desenvolver um sistema bancário simplificado para gerenciamento de
contas bancárias. O código fonte deve ser desenvolvido em Python 3, utilizar o conteúdo
trabalhado em aula, estar corretamente identado e comentado. O programa deve ser orientado a
objetos. Deve utilizar a biblioteca TkInter como interface gráfica, e para persistência de dados
deve ser usado um banco SQLite acessado a partir da biblioteca SQLAlchemy.
</p>
<h3>Diagrama de Classes:</h3>
<img src="/DiagramaDeClasses.png">
<p>O diagrama de classes abaixo representa o estado inicial para o desenvolvimento. É permitido
adicionar atributos e métodos de acordo com a necessidade.</p>
<h3>Funcionalidades:</h3>
<p>O programa deverá conter as seguintes funcionalidades:</p>
<ul>
<li>Cadastrar cliente: Realizar o cadastro de um cliente. Não deve permitir CPF duplicado.</li>
<li>Abrir conta: Criar a conta de um cliente previamente cadastrado, solicitando o CPF, tipo de
conta (1 - corrente, 2 - poupança, 3 – investimento) e saldo inicial. Um cliente não pode ter
mais de uma conta.</li>
<li>Realizar depósito: Localizar uma conta bancária. Solicitar ao usuário o valor a ser
depositado, obrigatoriamente numérico e maior que zero. Caso afirmativo, registrar uma
movimentação de depósito associada à conta bancária e mostrar o novo saldo. Caso negativo,
mostrar mensagem e não realizar a movimentação. Depósito é uma movimentação de tipo 1.
UNIVERSIDADE DO VALE DO RIO DOS SINOS Prof. Márcio Miguel Gomes - marciomg@unisinos.br</li>
<li>Realizar saque: Localizar uma conta bancária. Solicitar ao usuário o valor a ser sacado,
obrigatoriamente numérico e maior que zero. Caso o saldo da conta bancária seja insuficiente,
mostrar mensagem na tela e não realizar o saque. Caso tenha saldo suficiente, registrar uma
movimentação de saque associada à conta bancária, atualizar e mostrar na tela o novo saldo.
Do contrário, mostrar mensagem na tela e não realizar o saque. Operação disponível apenas
para conta-corrente e poupança. Saque é uma operação de tipo 2.</li>
<li>Aplicar juros: Localizar uma conta bancária. Solicitar uma taxa de juros, obrigatoriamente
numérica e maior que zero. Caso afirmativo, registrar uma movimentação de juros associada
à conta bancária, atualizar e mostrar na tela o novo saldo. Caso negativo, mostrar mensagem
e não aplicar os juros. Operação disponível apenas para poupança e investimento. Juros é uma
operação de tipo 3.</li>
<li>Extrato: Localizar uma conta bancária, informar data inicial e data final. Mostrar um extrato
em formato de listagem com as seguintes informações:
• Cabeçalho:
◦ Dados do cliente
◦ Dados da conta bancária
◦ Data inicial e final
• Listagem das movimentações:
◦ Data
◦ Tipo
◦ Valor
• Rodapé:
◦ Quantidade e valor dos depósitos realizados
◦ Quantidade e valor dos saques realizados
◦ Quantidade e valor das operações de juros aplicados</li>
<li>Sair: Encerra o programa.</li>
</ul> 


