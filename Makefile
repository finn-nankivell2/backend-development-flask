SHELL:=bash
.ONESHELL:

dbuild:
	docker build -t flask-docker-image .

drun:
	docker run -p 5000:5000 --mount src="$(realpath src)",target=/home/flaskuser/src,type=bind flask-docker-image:latest
	docker rmi $(docker images --filter dangling=true -q)
