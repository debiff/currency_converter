FROM python:3.7

WORKDIR /app

RUN pip install pipenv

COPY Pipfile .
COPY Pipfile.lock .

RUN pipenv install --system --deploy --ignore-pipfile

COPY src ./src
COPY .ci/entrypoint.sh .

ENV PYTHONPATH /app

EXPOSE 5000

ENTRYPOINT ["sh","entrypoint.sh"]

