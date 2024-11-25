# sd_1707372_2024-25

Cibersegurança
 
1707372

João Gaspar

Coca-Cola

SLB Benfica

# Trabalho

## 1. Descrição do Trabalho

Implementar uma função chamada tabuada(x) que foi utilizada para calcular a tabuada do número inteiro fornecido pelo utilizador, onde este, ao enviar um valor inteiro, irá receber pelo servidor a tabuada correspondente a esse valor, sendo esta função utilizada para gerar os resultados da multiplicação pelo número inserido pelo utilizador pelos números de 1 a 10 e apresentar essa informação de forma clara e organizada.	

## 2. Arquitectura do trabalho

![Fotografia da Arquitetura do Trabalho](/Trabalho/img/Arquitetura_Trabalho.png)

Como pode ser visualizado na imagem acima , o cliente irá enviar um número inteiro "x" para o servidor ,onde no servidor existe uma função chamada tabuada(x) que irá efetuar a tabuada do número enviado pelo utilizador e enviar a respetiva tabuada para o utilizador.

## 3. Descrição da implementação

O trabalho resume-se a desenvolver um sistema cliente-servidor na linguagem Python para calcular a tabuada de um número fornecido pelo utilizador. No código do servidor, existe uma função chamada “tabuada” onde esta função vai fazer a tabuada completa de um número recebido pelo utilizador, mostrando-a em linhas separadas para cada multiplicação. No lado do cliente, o sistema solicita ao utilizador que coloque um número inteiro, após enviar o número ao servidor, o cliente recebe a tabuada do número pedido. 

![Fotografia do Código do Trabalho](/Trabalho/img/Trabalho_Codigo.png)


## 4. Funcionamento do trabalho

![Fotografia do Trabalho a Funcionar](/Trabalho/img/Trabalho_Funcao.png)

Na fotografia acima  pode ser visualizada duas janelas, onde a janela da esquerda pertence à do servidor e a janela da direita pertence ao cliente. Na janela do Servidor pode ser observado o diretório que está a ser executado “SimpleXMLRPCServer.py” mostrando qual o endereço e qual a porta que está a ser utilizada. Na janela do Cliente pode ser observado o diretório que está a ser executado “cliente.py”, onde é pedido ao utilizador que “Insira um número inteiro:”, para finalizar o programa, o utilizador insere o número 5 e depois é mostrado a tabuada do número, está feita de 0 a 10.

## 5. Conclusão

O trabalho desenvolvido em python demonstra a criação de uma função onde o utilizador introduz um número inteiro e o programa devolve a tabuada desse número com o modelo de comunicação RPC.
 
## 6. Bibliografia

- Códigos fornecidos pelo Professor
- Apresentações no moodle fornecidos pelo Professor

