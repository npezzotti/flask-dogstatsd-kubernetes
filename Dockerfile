FROM python:3.8-slim
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
CMD ["ddtrace-run",  "gunicorn", "--bind", "0.0.0.0:5000", "run:app"]
