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

ADD ./streamlit /backend/streamlit
COPY ./poetry.lock /backend/poetry.lock
COPY ./pyproject.toml /backend/pyproject.toml

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

USER nonroot
EXPOSE 8501
CMD ["streamlit", "run", "streamlit/Homepage.py"]
