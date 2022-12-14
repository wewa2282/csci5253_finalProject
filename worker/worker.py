import io, os, sys
import jsonpickle, pickle
import redis
from minio import Minio
from  minio.deleteobjects import DeleteObject
from gtts import gTTS 
from io import BytesIO

redisHost =  os.getenv("REDIS_HOST") or "localhost"
redisPort =  os.getenv("REDIS_PORT") or "6379"
redisClient = redis.StrictRedis(host=redisHost, port=redisPort, db=0)


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



print(f"waitting for message")
while True:
    while redisClient.llen("toWorker") > 0:
        try: 
            work = redisClient.blpop("toWorker", timeout=0)
            text = jsonpickle.decode(work[1])

            try:
                hashcode = text["hash"]
                data = text["data"]
            except Exception as exp:
                print(exp)
                hashcode = 0
                data = ""

            #update to the input bucket
            if not minioClient.bucket_exists(queueBucketName):
                print(f"Create bucket {queueBucketName}")
                minioClient.make_bucket(queueBucketName)
            print("going to input bucket")
            data_as_bytes = data.encode('utf-8')
            data_as_a_stream = io.BytesIO(data_as_bytes)
            minioClient.put_object(queueBucketName, hashcode+".txt" , data_as_a_stream , length=len(data_as_bytes))



            tts = gTTS(data,lang='en',slow = False)
            save_file = f"{hashcode}.mp3"
            mp3_fp = BytesIO()
            tts.write_to_fp(mp3_fp)
            mp3_fp.seek(0)
         
            #update to the output bucket
            if not minioClient.bucket_exists(outpuutBucketName):
                print(f"Create bucket {outpuutBucketName}")
                minioClient.make_bucket(outpuutBucketName)
            print("going to output bucket")
            try:
                minioClient.put_object(outpuutBucketName, save_file , mp3_fp,mp3_fp.getbuffer().nbytes)
            except Exception as exp:
                print(exp)



        except Exception as exp:
            print(f"Exception raised in log loop: {str(exp)}")
    sys.stdout.flush()
    sys.stderr.flush()
