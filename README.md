![logoSmarttBot](https://user-images.githubusercontent.com/76957963/167670905-17547d0c-c046-415d-bbd6-adb4c84afbb8.png)

<h1 align="center"> Desafio Back-End Junior SmarttBot - Gerador de Trade </h1>
<h2> Descrição do projeto </h2>

Desenvolver um gerador de Trades, com alguns parâmetros definidos como entrada pelo usuário e os demais parâmetros gerados aleatoriamente.

Os parâmetros que devem ser definidos na entrada são os ativos (stock codes), para os quais os Trades serão gerados, e também a quantidade de Trades que deve ser gerada.
Trade: representa um negócio executado no mercado, contendo as seguintes informações:

Ativo negociado: PETR4, VALE3, WDOZ21, etc. (mais no link acima);
Data e horário de execução da negociação;
Preço de execução do negócio;
Identificador único para cada Trade.

Os requisitos desse gerador são:

  - O gerador precisa receber como parâmetro quais os ativos das Trades geradas. Por exemplo, "WINZ21", "ALUP11";
  
  - O gerador também precisa receber como parâmetro a quantidade de Trades que deve ser gerada;
  
  - Cada Trade deve conter os seguintes campos e valores:

    1. Código do ativo negociado: escolher aleatoriamente entre os ativos passados como parâmetro;
    
    2. Data e horário de execução da negociação: data e horário atual;
    
    3. Preço de execução do negócio: valor aleatório no intervalo de 1.0 a 100.0;
    
    4. Identificador único para cada Trade.


Com os Trades gerados, deve ser possível realizar algumas consultas nos mesmos. As consultas que devem ser implementadas são:

- Listar todos os Trades:

  1. De um determinado ativo;

  2. Com um preço de execução maior que algum valor passado como entrada;

  3. Com um preço de execução maior que algum valor passado como entrada de um ativo específico;

  4. Com um preço de execução menor que algum valor passado como entrada;

  5. Com um preço de execução menor que algum valor passado como entrada de um ativo específico;

- Listar o Trade mais recente de um ativo específico;

- Listar o Trade mais recente entre todos os Trades gerados. 

<h2> Tecnologias e Ferramentas </h2>

- Python 3

- Banco de dados mongodb

- Git & Github

<h2> Exemplificação do programa </h2>

Segue abaixo algumas imagens demonstrando o funcionamento do programa
<h2></h2>
<h2>1. Pedindo ao usuário a lista de ativos e a quantidade de trades</h2>

![listaDeAtivosEQuantTrades](https://user-images.githubusercontent.com/76957963/167684011-4af443d2-cf6e-450e-b68c-bd9f17286786.png)
<h2></h2>

<h2>2. Pedindo ao usuário qual saída de dados ele deseja obter</h2>

![saidaDeDados](https://user-images.githubusercontent.com/76957963/167684495-a99f12d8-2340-4df0-ae32-55643cbe65aa.png)
<h2></h2>

<h2>3. Informando todos os trades de um determinado ativo</h2>

![todasAsOperaçõesDeUmAtivo](https://user-images.githubusercontent.com/76957963/167685048-6c97ee22-3fe1-42a9-a083-4ce7ab1ce4d5.png)
<h2></h2>

<h2>4. Informando todos os trades com um preço de execução maior que algum valor passado</h2>

![todosOsAtivosComPrecoMaior](https://user-images.githubusercontent.com/76957963/167685456-fca5615a-8197-43af-828c-8d74b647710a.png)
<h2></h2>

<h2>5. Informando todos os trades de um determinado ativo com um preço de execução maior que algum valor passado</h2>

![AtivoComValorMaiorQuePassado](https://user-images.githubusercontent.com/76957963/167685950-f8bdea01-afb3-4fee-8129-121c17510379.png)
<h2></h2>

<h2>6. Informando todos os trades com um preço de execução menor que algum valor passado</h2>

![MenorQueValorPassado](https://user-images.githubusercontent.com/76957963/167686340-a1ebe988-d274-4b0d-94e8-f9cc912c3060.png)
<h2></h2>

<h2>7. Informando todos os trades de um determinado ativo com um preço de execução menor que algum valor passado</h2>

![MenorValorDeUmaAtivo](https://user-images.githubusercontent.com/76957963/167686901-37bc8776-a643-4f0c-b524-905ab296567f.png)
<h2></h2>

<h2>8. Informando o Trade mais recente de um ativo específico</h2>

![TradeMaisRecenteNoAtivo](https://user-images.githubusercontent.com/76957963/167687268-d5772da4-92b8-4a36-ab78-d6b3dedb1d77.png)
<h2></h2>

<h2>9. Informando o Trade mais recente entre todos os Trades gerados</h2>

![TradeMaisRecenteEntreTodos](https://user-images.githubusercontent.com/76957963/167687632-5c91061a-9e93-4d60-94fb-d50edc91247d.png)
<h2></h2>

<h2>10. Informando média de preços dos trades de um determinado ativo</h2>

![MediaPrecoTrade](https://user-images.githubusercontent.com/76957963/167687909-450f4a3f-6454-47d9-9e12-8b3f54ac050a.png)
<h2></h2>

<h2>11. Informando todas as operações realizadas</h2>

![TodasAsOperacoesRealizadas](https://user-images.githubusercontent.com/76957963/167688171-d1c87138-af35-4664-ad0e-e9bc72466635.png)
<h2></h2>
