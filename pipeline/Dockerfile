# imagem base utilizada -modo da imagem (leve, slim, etc)
FROM python:3.13.11-slim

# bibliotecas que serão necessárias
RUN pip install pandas pyarrow

# definido o diretorio de trabalho 
WORKDIR /app
# copiando o arquivo de origem pro destino container
COPY pipeline.py pipeline.py

# definindo o que sera feito antes, ordem de execução
ENTRYPOINT ["python", "pipeline.py"]

# pra construir a imagem que está desse Dockerfile, 
# no terminal executar: 

    # nome da imagem será teste
    # tag da imagem será pandas, se não fosse especificada seria latest
    # . diz pasta em que será contruida a imagem e que estara o Dockerfile
    # docker build -t teste:pandas .
