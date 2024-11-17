SHELL:=bash

IMAGE_NAME=flask-docker-image

dbuild:
	docker build -t $(IMAGE_NAME) .
	docker rmi -f $(shell docker images --filter dangling=true -q)

drun:
	docker run -p 5000:5000 --mount src="$(shell realpath src)",target=/home/flaskuser/src,type=bind $(IMAGE_NAME):latest
