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

minioClient = Minio(minioHost,
               secure=False,
               access_key=minioUser,
               secret_key=minioPasswd )


# Initialize the Flask application
app = Flask(__name__)


class RouteGuideServicer(final_pb2_grpc.projectServicer):
     def __init__(self) -> None:
        pass
    
     def to_worker(self, data, hash):
        try:
            r = redis.Redis(host=redisHost, port=redisPort)
            to_json = {
                'hash': hash,
                'data': data
            }
            worker_string = jsonpickle.encode(to_json)
            r.lpush('toWorker', worker_string) 
            return True 
        except:
            return False
            
     def doconvert(self,request,context):
        content = request.file
                
        hash = hashlib.sha256(content.encode('utf-8')).hexdigest()
            
        operation = self.to_worker(content, hash) 
            
        if operation: 
            return_hash = {
                'hash': hash,
                'reason': "File enqueued"
            }
        else:
            return_hash = {
                'hash': 0
            }
            
        response_pickled = jsonpickle.encode(return_hash)
        return final_pb2.convertReply(hash=response_pickled)                
            
        
     def queue(self,request,context):
        queue = []
        
        try:
            r = redis.Redis(host=redisHost, port=redisPort)
            
            for e in r.lrange('toWorker', 0, -1):
                tmp_dic = jsonpickle.decode(e)
                queue.append(tmp_dic['hash'])

            
            return_dic = {
                'queue': queue
            }
            
        except:
            return_dic = {
                'queue': queue,
                'error': "There has been an error when getting the queued files"
            }
        response_pickled = jsonpickle.encode(return_dic)
        return final_pb2.queueReply(file=response_pickled) 
        
    #def delete(self,request,context):
        
        
    #def doDownload(self, request, context):
        

    
def serve():    
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    final_pb2_grpc.add_projectServicer_to_server(RouteGuideServicer(), server)
    
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
   

if __name__ == '__main__':
    serve()