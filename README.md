# Flask-Dogsatsd-Kubernetes

## Getting started

1. Start minikube with `minikube start --driver virtualbox`
2. Configure your envronment to use the Docker daemon in the Minikube instance with `eval $(minikube docker-env)`

## Deployment steps

1. From the root directory, run `docker build -t flask-dogstatsd:1.0.0 .` to build the application image
2. In `/kubernetes/secrets/secrets.yaml`, replace the placeholders in each secret with your base64 encoded credentials, i.e `echo -n <API_KEY> | base64`
3. Install the DatadogMetric CRD in your cluster:
`kubectl apply -f "https://raw.githubusercontent.com/DataDog/helm-charts/master/crds/datadoghq.com_datadogmetrics.yaml"`
4. From the `kubernetes/` directory, run the following commands:
```
 kubectl apply -f secrets
 kubectl apply -f cluster-agent
 kubectl apply -f agent
 kubectl apply -f external-metrics
 kubectl apply -f flask-dogstatsd
```
5. Make requests to the server: `curl $(minikube ip):30002`
