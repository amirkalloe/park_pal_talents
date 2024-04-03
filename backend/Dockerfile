FROM python:3.12

ENV YOUR_ENV=${YOUR_ENV} \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.2.2

RUN apt-get update && \
  apt-get -y install sudo

ADD ./backend/app /backend/app
ADD ./backend/alembic /backend/alembic
COPY ./backend/poetry.lock /backend/poetry.lock
COPY ./backend/pyproject.toml /backend/pyproject.toml
COPY ./backend/start.sh /backend/start.sh

WORKDIR /backend

RUN sudo apt-get -y install gcc g++ && \
  pip install "poetry==$POETRY_VERSION" && \
  poetry config virtualenvs.create false && \
  poetry install --without dev --no-interaction --no-ansi && \
  apt-get remove --purge -y gcc g++ && \
  pip uninstall -y "poetry==$POETRY_VERSION" && \
  sudo apt-get clean

# # add non root user for security with home directory for test files
RUN groupadd -r nonroot &&\
  useradd -r -g nonroot nonroot
RUN chown -R nonroot:nonroot /backend

# make start.sh executable
RUN chmod 777 /backend/start.sh

USER nonroot
EXPOSE 8000:8000
EXPOSE 8501:8501
CMD ["./start.sh"]
