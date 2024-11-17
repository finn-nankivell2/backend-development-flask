FROM python:3.11.2-slim-bullseye

RUN apt-get update && apt-get upgrade --yes

ARG USERNAME=flaskuser
RUN useradd --create-home $USERNAME
USER $USERNAME
WORKDIR /home/$USERNAME

ENV VENVPATH=/home/$USERNAME/venv
RUN python3 -m venv $VENVPATH
ENV PATH="$VENVPATH/bin:$PATH"

COPY --chown=$USERNAME requirements.txt ./

RUN pip install --upgrade pip setuptools && \
	pip install -r requirements.txt --no-cache-dir

COPY --chown=$USERNAME src ./src/
WORKDIR /home/$USERNAME/src
RUN flask custom migrate_fresh_seed
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]
