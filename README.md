# Grupo 3
- Ana Flávia Moraes
- Juan Carlos Quevedo Weimar
- Rodrigo Valadao

# Link para aplicação:

 - https://jupyter-lab-anamasflaviamoraes.cloud.okteto.net
 - Senha Jupyter: okteto

# Bibliotecas importadas:
 - numpy
 - tensorflow 
 - keras
 -  matplotlib
 - pymongo
 - io
 - bson
 - IPython

<img src="https://user-images.githubusercontent.com/105460289/174438498-fee8928e-23c4-40e1-a2c3-fa5d43012f51.jpg">

# Dataset utilizada:
<h3 > cifar10 </h3>

<p>Descrição:

O conjunto de dados CIFAR-10 consiste em 60.000 imagens coloridas 32x32 em 10 classes, com 6.000 imagens por classe. Existem 50.000 imagens de treinamento e 10.000 imagens de teste.

Classes da dataset:
 - Avião 
 - Automóvel 
 - Cachorro 
 - Caminhão 
 - Cavalo 
 - Cervo 
 - Gato 
 - Navio 
 - Pássaro 
 - Sapo 

Página inicial : https://www.cs.toronto.edu/~kriz/cifar.html

Código fonte : tfds.image_classification.Cifar10

<img src="https://user-images.githubusercontent.com/105460289/174439267-95daaaa2-c9ac-4110-80ac-811e0facf54e.jpg">

</p>

# Modelo de Rede criado:
O modelo criado foi feito baseando, primeiramente, nas predefinições da dataset que definem imagens coloridas de de dimensionalidade 32x32. 
- layers.Conv2D --> define o número de feautures a serem aprendidas pela rede
- layers.MaxPooling2D  --> realiza o agrupamento das camadas
- layers.Flatten --> realiza o achatamento das camadas
- layers.Dense --> classificação dos dados

A partir desses recursos conseguimos criar nosso modelo, para posteriormente o compilarmos. Com os dados encontrados, montamos um gráfico que demonstrassem a aprendizagem da nossa rede neural. 
A linha laranja que representa a variável val_acurracy informa o ínide de aprendizagem da mesma. Após alguns testes podemos confirmar que o número de epochs, número de imagens base e as camadas, influenciam diretamente nos valores obtidos. 

<img src="https://user-images.githubusercontent.com/105460289/174439311-dbb6918b-4f15-437c-8524-5ec1058c64c3.jpg">

# Gráfico de aprendizado

<img src="https://user-images.githubusercontent.com/105460289/174439309-2b6e2f56-91ea-4e3b-9ae2-5a3bb38fc0b6.jpg">

# Treinamento da Rede:

Para treinar a rede criamos uma pasta "dataset" com imagens retiradas da internet que se encaixavam dentro das 10 classes oferecidas pelo cifar10. Através da nossa rede e fazendo uma consulta no vetor de classes definidos ele indicará a que classe a imagem representa. 

No treinamento, utilizamos um pré-processamento da imagem enviada para que ao utilizarmos o numpy, tivessemos já um vetor com a representação dos pixels de cada imagem. Após isso, ele conseguia comparar a informação da imagem enviada com os valores aprendidos na rede e indicar a que classe a imagem testada se referia.

<img src="https://user-images.githubusercontent.com/105460289/174439312-a59c82b1-8494-42d5-9e0d-4917f7106bc0.jpg">

<img src="https://user-images.githubusercontent.com/105460289/174439313-ffcb78b7-8e52-432d-b102-8da83bbe2e6d.jpg">

<img src="https://user-images.githubusercontent.com/105460289/174439314-648d43f0-7e94-4c42-bbaf-904a6cefabb5.jpg">

<img src="https://user-images.githubusercontent.com/105460289/174439315-a27c2871-fcc5-45ea-9e14-c34aa95cf628.jpg">
<img src="https://user-images.githubusercontent.com/105460289/174439316-bda4c848-dcc9-4f2c-8616-1e94ae609694.jpg">
<img src="https://user-images.githubusercontent.com/105460289/174439317-dc20d606-568a-4ffb-8be5-95d021678c49.jpg">
<img src="https://user-images.githubusercontent.com/105460289/174439302-e119f5bf-01f0-47db-b881-dfd0e0b20068.jpg">
<img src="https://user-images.githubusercontent.com/105460289/174439304-e3294fdc-a44f-4484-b7c1-587fc5d909ad.jpg">
<img src="https://user-images.githubusercontent.com/105460289/174439306-cf0d8521-15d0-44d2-9cd8-dea0995391b7.jpg">

Repare que nas próximas imagens o modelo de rede indica a classe errada. Isso acontece devido a precisão alcançada no aprendizado do modelo!

<img src="https://user-images.githubusercontent.com/105460289/174439307-7664d0f5-2a17-4b73-bab4-daeddac670cd.jpg">
<img src="https://user-images.githubusercontent.com/105460289/174439319-3254b269-abd7-460f-9627-5cc77de4dbc8.jpg">

# Mongo DB:

Para enviarmos o modelo de rede criado utilizamos o Jupyter e o Mongo dentro do próprio Okteto.
Para salvar a rede criada, primeiro salvamos o modelo em um arquivo .h5, que logo em seguida é aberto para e convertido para um valor binário. Por fim, o arquivo era inserido no mongo utilizando o método insert_one()

Para carregar o modelo do banco, primeiro foi necessário localizar o arquivo .h5, previamente, criado.

Para testar se o modelo do mongo estava funcionando, reutilizamos o método de treinamento, porém substituindo o modelo de rede exigido pelo método para o que foi carregado pelo banco de dados.

<img src="https://user-images.githubusercontent.com/105460289/174444304-6de97918-0061-49a1-aa21-281db9b16530.jpg">
<img src="https://user-images.githubusercontent.com/105460289/174444308-cf41bd44-f188-4744-bdf5-7f8a9f13bfe3.jpg">
<img src="https://user-images.githubusercontent.com/105460289/174444310-350812a9-ecea-4526-b51d-3cdb0dc5baa6.jpg">
<img src="https://user-images.githubusercontent.com/105460289/174444311-42f156a9-bfe1-4374-b11c-6ab7555e47bd.jpg">
<img src="https://user-images.githubusercontent.com/105460289/174444300-abf9e50a-2f68-4a06-ac26-b04024cf178c.jpg">
<img src="https://user-images.githubusercontent.com/105460289/174444303-a5150d14-f97f-452e-b585-d7f34ad55050.jpg">

# Dificuldades encontradas:
<p>
<ul>
 <li>GPU do Jupyter: O processamento das funções no Jupyter dificultaram no andamento do projeto, pois cada modificação que realizássemos que necessitasse de um novo teste, demandava muito tempo de espera. A solução encontrada, foi criar o notebook no Colab e utilizar o Jupyter do Okteto para os testes do mongo.</li>
 <img src="https://user-images.githubusercontent.com/105460289/174440053-017150b1-c49a-40d7-835e-ea7cbd1ed820.jpg">
 <li> Precisão da rede: a rede neural indicava uma precisão no accuracy entre 0.69 e 0.71. Como a dataset trabalha obrigatoriamente com 10 classes ao testar a rede, conseguimos alcançar um acerto de 8/10. No entanto, quando testávamos novamente, esse valor de 8/10 variava de 7 ou 6 acertos. Concluímos que isso acontecia devido as fotos utilizadas na testagem e as imagens que a aplicação usava como base ao criar a rede, ou seja, se ao executarmos a aplicação as imagens base fossem diferentes a rede poderia confundir causando a variação nos acertos. </li>
 <li>Conexão com o MongoDB: iniciamos tentando realizar a conexão com o mongo através do Atlas, porém todo teste a aplicação indicava o erro: "ServerSelectionTimeoutError", ou seja, ele tentava encontrar a nossa database, mas não tinha sucesso. A solução foi utilizar o okteto para construir a ligação com o mongo. Através do docker-compose criamos uma imagem para o Jupyter e outra para o Mongo. Dessa forma, ao lançar a aplicação no Okteto, abríamos o Jupyter e fazíamos as conexão com o mongo. </li>
<li>Diretório não encontrado no Jupyter Okteto: ao lançarmos a aplicação no Okteto, ao abrir o Jupyter, não mostrava a pasta com nossos arquivos. Concluímos que o problema estava no arquivo okteto.yml. Ao excluirmos esse arquivo e testarmos novamente, todos os nossos arquivos estavam presentes no Jupyter do Okteto.</li>
<li>Salvar mudanças no Jupyter Okteto: ao fazermos modificações no notebook lançado, elas não poderiam ser salvas, pois o Jupyter indicava um problema de permissão. Isso dificultou nosso processo, pois a testagem do banco foi feita toda, dentro do ambiente do Okteto. Para contornar esse problema, tivemos que fazer o código em duas partes baixar o notebook e juntá-las novamente.</li>
</p>
