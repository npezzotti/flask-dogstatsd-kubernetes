# Flask-Dogsatsd-Kubernetes

## Getting started

1. Start minikube with `minikube start --driver virtualbox`
2. Configure your envronment to use the Docker daemon in the Minikube instance with `eval $(minikube docker-env)`

## Deployment steps

1. Install the DatadogMetric CRD in your cluster:
`kubectl apply -f "https://raw.githubusercontent.com/DataDog/helm-charts/master/crds/datadoghq.com_datadogmetrics.yaml"`
2. cd kubernetes 
3. `kubectl apply -f secrets`
4. `kubectl apply -f agent`
5. `kubectl apply -f cluster-agent`
6. `kubectl apply -f external-metrics`
7. `kubectl apply -f flask-dogstatsd`

Make requests to the server with the followin `curl $(minikube ip):30002`
