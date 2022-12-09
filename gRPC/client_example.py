#!/usr/bin/env python3
from __future__ import print_function
import requests
import json
import time
import sys
import base64
import jsonpickle
import random
import final_pb2, final_pb2_grpc
from concurrent import futures
import grpc


host = sys.argv[1]
cmd = sys.argv[2]
addr = f"http://{host}:5000"

if len(sys.argv) >3:
        hashcode = sys.argv[3]

channel = grpc.insecure_channel('{}:50051'.format(host))
stub = final_pb2_grpc.projectStub(channel)

if cmd == 'doConvert':
    with open('sample_text.txt', 'r') as file:
        data = file.read().replace('\n', '')
    req = final_pb2.convertRequest(file=data)
    rep = stub.doconvert(req)
    print(rep.hash)
elif cmd == 'doQueue':
    req = final_pb2.queueRequest()
    rep = stub.queue(req)
elif cmd == 'delete':
    req = final_pb2.deleteRequest(hash = hashcode)
    rep = stub.delete(req)
    print(f"delete {rep}" )
elif cmd =="download":
    req = final_pb2.downloadRequest(hash = hashcode)
    rep = stub.doDownload(req)
    if str(rep.file) == "fail":
        print("fail")
    else:
        with open (f"{hashcode}.mp3","wb") as file:
            file.write(rep.file)
else:
    print("Unknown option", cmd)
