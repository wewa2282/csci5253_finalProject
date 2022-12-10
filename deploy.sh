kubectl apply -f redis/redis-deployment.yaml
kubectl apply -f redis/redis-service.yaml

kubectl apply -f gRPC/grpc-deployment.yaml
kubectl apply -f gRPC/gtts-grpc-service.yaml

kubectl apply -f worker/worker-deployment.yaml

kubectl apply -f minio/minio-external-service.yaml

kubectl port-forward --address 0.0.0.0 service/gtts-grpc-svc 5000:5000 &

kubectl port-forward --address 0.0.0.0 service/redis 6379:6379 &
kubectl port-forward -n minio-ns --address 0.0.0.0 service/minio-proj 9000:9000 &
kubectl port-forward -n minio-ns --address 0.0.0.0 service/minio-proj 9001:9001 &