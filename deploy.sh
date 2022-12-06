kubectl apply -f redis/redis-deployment.yaml
kubectl apply -f redis/redis-service.yaml

kubectl port-forward --address 0.0.0.0 service/redis 6379:6379
