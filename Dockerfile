FROM python:3.8-slim
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
ENV FLASK_APP=flask-dogstatsd
ENV FLASK_RUN_HOST=0.0.0.0
CMD ["ddtrace-run","flask","run"]
