FROM python:3.8-slim
MAINTAINER nathan.pezzotti@datadoghq.com
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY app.py .
ENV FLASK_ENV=production
ENV FLASK_APP=app.py
ENV DD_AGENT_HOST=datadog-agent
ENV DD_TRACE_AGENT_PORT=8126
CMD ["ddtrace-run","flask","run"]
