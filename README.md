# Avaliação Sprint 3 - Programa de Bolsas Compass.uol e universidades de Rio Grande e Pelotas

## Grupo
- Everton Feijó
- Suélen Peres
- Tatieli Silveira

## Objetivo
O grupo definiu o uso de um dataset com dados de um conjunto de pacientes, que será usado como base, para ver a probabilidade de doença cardiaca. A partir desses dados, será treinada uma rede neural para a previsão, onde uma pessoa poderá ver a porcentagem de risco de ter uma doença cardiaca.

## Desenvolvimento
#### Bibliotecas usadas
- Tensorflow
- Tensorflow - Keras
- Tensorflow - Keras - Layers
- Numpy
- Pandas
- Matplotlip.pyplot
- Pymongo

#### Deploy no okteto
Dockerfile
```
FROM jupyter/tensorflow-notebook:latest

RUN pip install requests feature_engine \
    pip install -q tfds-nightly tensorflow matplotlib\
    pip install tensorflow-datasets\
    pip install tfds-nightly

USER root
# apt-utils is missing and needed to avoid warning about skipping debconf
RUN apt-get update && apt-get --yes install apt-utils
# install whatever else you want on this line
RUN apt-get --yes install curl
```

dockerfile-compose.yml
```
version: "3"

services: 
  jupyter_lab:
    container_name: jupyter_lab
    build: .
    depends_on:
      - mongodb
    ports:
      - "8888:8888"
    networks:
     - prod
    environment:
      JUPYTER_ENABLE_LAB: "yes"
      JUPYTER_TOKEN: "okteto"
      GRANT_SUDO: "yes"
    volumes: 
      - .:/home/jovyan/work

  mongodb:
      image: mongo
      container_name: db
      ports: 
        - 27017:27017
      networks:
        - prod
      environment:
        MONGO_INITDB_ROOT_USERNAME: root
        MONGO_INITDB_ROOT_PASSWORD: root
        MONGO_INITDB_DATABASE: sprint3

networks: 
    prod:
        driver: bridge
```

#### Dataset
O dataset escolhido foi o um conjunto de dados estruturados, a partir de um arquivo CSV bruto. O conjunto de dados é fornecido pela Cleveland Clinic Foundation For Heart Disease. É um arquivo com 303 linhas e cada linha contém informações sobre um paciente.

Link do dataset: https://archive.ics.uci.edu/ml/datasets/heart+Disease
![Captura de tel![Captura de tela de 2022-06-18 16-49-09](https://user-images.githubusercontent.com/29054252/174455171-65b4bce6-4465-4d23-ac58-4f0db6f703e5.png)
a de 2022-06-18 16-42-55](https://user-images.githubusercontent.com/29054252/174454947-4b6f9c26-49ff-4404-9c49-c83936dae311.png)

#### Modelo 

![Captura de tela de 2022-06-18 16-49-09](https://user-images.githubusercontent.com/29054252/174455191-1c3d74eb-9578-4315-b58f-a620d9997451.png)

#### Grafico de conectividade

![download (1)](https://user-images.githubusercontent.com/29054252/174455280-58ac115d-d6e5-4c30-81c2-b3d27b4cc605.png)

#### Resultados

![Captura de tela de 2022-06-17 22-50-26](https://user-images.githubusercontent.com/29054252/174455307-51b67828-af36-4b63-8e53-8f5299d94027.png)


![Captura de tela de 2022-06-17 22-47-37](https://user-images.githubusercontent.com/29054252/174455309-230bd800-8571-406a-9741-875817e42b16.png)

## Acesso ao app no Okteto
https://jupyter-lab-evertonlwf.cloud.okteto.net/

## Aplicação Cats vs Dogs

## Rede Neural Convolucional

Reconhecimento e distinção de imagens de gatos ou cachorros através do dataset cats_vs_dogs

## Desenvolvimento - Bibliotecas e tecnologias 

Geral:
* Tensorflow/Keras
* TFlearn
* Python
* Numpy
* matplotlib

Conexão com MongoDB:
* Pymongo

Tecnologias:
* Okteto 
* Docker
* Jupyter Notebook

## Carregando os dados
Foi feito o download dos dados brutos por meio de um arquivo zip.

Temos uma pasta chamada PetImages com duas subpastas chamadas Cat e Dog

## Preparação das imagens

Imagens corrompidas foram filtradas

## Preapração das imagens

Labels: As imagens foram classificadas com labels [1,0], sendo 0 para cat e 1 para dog

## Aumento de dados de imagens

Introduzimos artificialmente a diversidade de amostras aplicando transformações aleatórias, mas realistas, nas imagens de treinamento, como inversão horizontal aleatória ou pequenas rotações aleatórias

## Pré- processamento das imagens

As imagens foram redimensionadas em 48x48px

Os dados foram configurados para desempenho - arquivos de treino e validação

## Construção do modelo

* Iniciamos o modelo com o pré-processador, seguido de uma camada.data_augmentationRescaling
* Incluímos uma camada antes da camada de classificação final.Dropout

## Rede Neural 

O modelo criado foi feito baseando, primeiramente, nas predefinições da dataset que definem imagens coloridas 

* layers.Rescaling --> Uma camada de pré-processamento que redimensiona os valores de entrada para uma nova faixa. Esta camada redimensiona cada valor de uma entrada (muitas vezes uma imagem) multiplicando-se e adicionando.

* layers.Conv2D --> define o número de feautures a serem aprendidas pela rede

* layers.BatchNormalization --> Camada que normaliza as entradas. A normalização do lote aplica uma transformação que mantém a saída média próxima de 0 e o desvio padrão de saída próximo a 1.

* layers.SeparableConv2D --> Convolução 2D separável em profundidade. As convoluções separáveis consistem em primeiro executar uma convolução espacial em profundidade (que age em cada canal de entrada separadamente) seguida de uma convolução pontiacída que mistura os canais de saída resultantes. O argumento controla quantos canais de saída são gerados por canal de entrada na etapa de profundidade.


O ReLU aplicará a ativação da função;

Por fim será gerado a saída.

A rede foi treinada com um dataset de 781 imagens, em 10 épocas.

## Saída

Após ter sido treinado, o modelo possui uma acurácia de 85% (aproximadamente), sendo capaz de identificar, diferenciar e rotular imagens de cachorros e gatos.

No MongoDB é possível observar o modelo do projeto salvo e previamente treinado.

## Dificuldades encontradas
Problema encontrado para executar o treinamento do dataset no okteto. 
![performace-critical-operation](https://github.com/Compass-pb-rasa-2022-RG-Pel/sprint-3-pb-rg-pel/blob/grupo-1/assets/img/dificuldades.png)
Problema encontado ao baixar o dataset de imagens no okteto (velocidade muito baixa para download).
![performace-network-speed](https://raw.githubusercontent.com/Compass-pb-rasa-2022-RG-Pel/sprint-3-pb-rg-pel/grupo-1/assets/img/dificuldades-1.png)

Para contornar estes problemas optamos por execuar o notebook no ambiente do [colab](https://colab.research.google.com/), e subir o dataset pronto.

## Link para acessar o projeto no okteto

[Okteto](https://jupyter-lab-evertonlwf.cloud.okteto.net/)
