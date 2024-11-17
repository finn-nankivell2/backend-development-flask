if [ ! -d venv ]; then
	echo "Creating venv"
	python3 -m venv venv
	. venv/bin/activate
	pip install -r requirements.txt
	pip install --upgrade pip
fi

. venv/bin/activate

systemctl is-active docker.socket --quiet || sudo systemctl start docker.socket
