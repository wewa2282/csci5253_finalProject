kubectl apply -f redis/redis-deployment.yaml
kubectl apply -f redis/redis-service.yaml

kubectl port-forward --address 0.0.0.0 service/redis 6379:6379 &
kubectl port-forward -n minio-ns --address 0.0.0.0 service/minio-proj 9000:9000 &
