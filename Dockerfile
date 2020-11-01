FROM python:3.8-slim
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY app.py .
ENV FLASK_ENV=production
ENV FLASK_APP=app.py
CMD ["ddtrace-run","flask","run"]
