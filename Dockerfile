FROM python:3

COPY . /app
COPY /Ativos.csv /app/Ativo.csv
COPY requirements.txt /app

WORKDIR /app
RUN pip install -r requirements.txt

CMD [ "python", "/app/comparador.py" ]
