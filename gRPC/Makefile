VERSION=v1
DOCKERUSER=mariochg

build:
	docker build -f Dockerfile-grpc -t gtts-grpc .

push:
	sudo docker tag gtts-grpc $(DOCKERUSER)/gtts-grpc:$(VERSION)
	sudo docker push $(DOCKERUSER)/gtts-grpc:$(VERSION)
	sudo docker tag gtts-grpc $(DOCKERUSER)/gtts-grpc:latest
	sudo docker push $(DOCKERUSER)/gtts-grpc:latest