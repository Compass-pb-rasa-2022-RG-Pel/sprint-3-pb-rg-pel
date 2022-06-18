# Avaliação Sprint 3 - Programa de Bolsas Compass.uol e universidades de Rio Grande e Pelotas

## Grupo
- Everton Feijó
- Suélen Peres
- Tatieli Silveira

## Objetivo
O grupo definiu o uso de um dataset com dados de um conjunto de pacientes, que será usado como base, para uma predição. A partir desses dados, será treinada uma rede neural para a previsão, onde uma pessoa poderá ver a porcentagem de risco de ter uma doença cardiaca.

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
[endereço do app no okteto]
- www.okteto.com/appp...