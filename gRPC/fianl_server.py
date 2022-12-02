import base64
import io, os, sys
from concurrent import futures
import grpc
import final_pb2
import final_pb2_grpc
from flask import Flask, request, Response,send_file
import jsonpickle, pickle
import platform
import redis
import hashlib, requests
import base64
from minio import Minio
from  minio.deleteobjects import DeleteObject
import hashlib

redisHost =  os.getenv("REDIS_HOST") or "localhost"
redisPort =  os.getenv("REDIS_PORT") or "6379"


minioHost = os.getenv("MINIO_HOST") or "localhost:9000"
minioUser = os.getenv("MINIO_USER") or "rootuser"
minioPasswd = os.getenv("MINIO_PASSWD") or "rootpass123"

queueBucketName = "queue"
outpuutBucketName = "output"

workQueue = "toWorker"

redisClient = redis.StrictRedis(host = redisHost,port= redisPort,db=0)
minioClient = Minio(minioHost,
               secure=False,
               access_key=minioUser,
               secret_key=minioPasswd )





# Initialize the Flask application
app = Flask(__name__)


class RouteGuideServicer(final_pb2_grpc.projectServicer):
     def __init__(self) -> None:
        pass

     def doconvert(self,request,context):
        pass
     def queue(self,request,context):
        pass
     def delete(self,request,context):
        pass

def serve():    
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    final_pb2_grpc.add_projectServicer_to_server(RouteGuideServicer(), server)
    
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
   
if __name__ == '__main__':
    serve()