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

channel = grpc.insecure_channel('{}:50051'.format(host))
stub = final_pb2_grpc.projectStub(channel)

if cmd == 'doConvert':
    text = open('sample_text.txt', 'r').read()
    req = final_pb2.convertRequest(file=text)
    rep = stub.doconvert(req)
elif cmd == 'doQueue':
    req = final_pb2.queueRequest()
    rep = stub.queue(req)
else:
    print("Unknown option", cmd)
