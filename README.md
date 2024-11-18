# sd_1707372_2024-25

Cibersegurança
 
1707372

João Gaspar

Coca-Cola

SLB Benfica

1. Descrição do Trabalho

Implementar uma função chamada tabuada(x) que foi utilizada para calcular a tabuada do número inteiro fornecido pelo utilizado, onde este, ao enviar um valor inteiro, irá receber pelo servidor a tabuada correspondente a esse valor, sendo esta função utilizada para gerar os resultados da multiplicação pelo número inserido pelo utilizador pelos números de 1 a 10 e apresentar essa informação de forma clara e organizada.	

2. Arquitectura do trabalho

![Fotografia da Arquitetura do Trabalho](/Trabalho/Arquitetura_Trabalho.png)

3. Descrição da implementação

![Fotografia do Código do Trabalho](/Trabalho/Trabalho_Codigo.png)

O trabalho resume-se a desenvolver um sistema cliente-servidor na linguagem Python para calcular a tabuada de um número fornecido pelo utilizador. No código do servidor, existe uma função chamada “tabuada” onde esta função vai fazer a tabuada completa de um número recebido pelo utilizador, mostrando-a em linhas separadas para cada multiplicação. No lado do cliente, o sistema solicita ao utilizador que coloque um número inteiro, onde existe uma função onde esta irá validar se o número inserido é válido. Após enviar o número ao servidor, o cliente recebe a tabuada do número pedido. 

4. Funcionamento do trabalho

![Fotografia do Trabalho a Funcionar](/Trabalho/Trabalho_Funcao.png)

Na fotografia a cima  pode ser visualizada duas janelas, onde a janela da esquerda pertence á do servidor e a janela da direita pertence ao cliente. Na janela do Servidor pode ser observado o diretório que está a ser executado “SimpleXMLRPCServer.py” mostrando qual o endereço e qual a porta que está a ser utilizada. Na janela do Cliente pode ser observado o diretório que está a ser executado “cliente.py”, onde é pedido ao utilizador que “Insira um número inteiro:”, pode ser comprovado que se não for inserido um número inteiro, irá ser pedido novamente ao utilizador para inserir um número inteiro, para finalizar o programa, o utilizador insere o número 5 e depois é mostrado a tabuada do número, está feita de 0 a 10.

7. Conclusão
 
8. Bibliografia
