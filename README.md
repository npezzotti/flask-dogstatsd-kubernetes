# Flask-Dogsatsd-Kubernetes

## Getting started

1. Start minikube with `minikube start --driver virtualbox`
2. Configure your envronment to use the Docker daemon in the Minikube instance with `eval $(minikube docker-env)`

## Datadog Deployment

1. From the root directory, run `docker build -t flask-dogstatsd:1.0.0 .` to build the application image
2. In `/kubernetes/secrets/secrets.yaml`, replace the placeholders in each secret with your base64 encoded credentials, i.e `echo -n <API_KEY> | base64`
3. From the `kubernetes` directory, run the following commands:
  ```
  kubectl apply -f secrets
  kubectl apply -f agent
  kubectl apply -f cluster-agent
  kubectl apply -f custom-metric-server.yaml
  kubectl apply -f rbac-hpa.yaml
  ```
## HPA

1. From `kubernetes`, run the following commands:
  ```
  kubectl apply -f hpa.yaml
  ```
## DatadogMetric CRD

1. Install the DatadogMetric CRD in your cluster: `kubectl apply -f "https://raw.githubusercontent.com/DataDog/helm-charts/master/crds/datadoghq.com_datadogmetrics.yaml"`
2. In `kubernetes/cluster-agent/cluster-agent-deployment.yaml`, set `DD_EXTERNAL_METRICS_PROVIDER_USE_DATADOGMETRIC_CRD` to `"true"`
3. From `kubernetes`, run the following commands:
  ```
  kubectl apply -f datadog-metric.yaml 
  kubectl apply -f datadog-metric-hpa.yaml
  ```
## Flask Application
1. From `kubernetes`, run `kubectl apply -f flask-dogstatsd`
2. Make requests to the server: `curl $(minikube ip):30002`

### Testing HPA

Decrease the frequency of requests by editing the `sleep` duration in curl container command: `["-c", "while [ true ]; do sleep 2; curl http://127.0.0.1:80; done"]`. After reapplying the `flask-dogstatsd-deployment.yaml`, the HPA should scale the deployment to three replicas.
