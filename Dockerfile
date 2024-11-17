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
COPY --chown=$USERNAME app/ ./app/
COPY --chown=$USERNAME migrations/ ./migrations/
COPY --chown=$USERNAME storage/ ./storage/
COPY --chown=$USERNAME config.py/ ./config/
COPY --chown=$USERNAME server.py/ ./server/
COPY --chown=$USERNAME .flaskenv/ ./.flaskenv/

# RUN pip install --upgrade pip setuptools && \
# 	pip install -r requirements.txt # --no-cache-dir

# RUN flask custom migrate_fresh_seed
# CMD ["flask", "run"]
