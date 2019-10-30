# Currency Converter API

Currency converter API is a service to convert an amount from 
a currency to another in a given date based on European Central Bank rates.

## Dependecies

- Python 3.7

Use the package manager [pipenv](https://github.com/pypa/pipenv) to create 
the virtual environment and install the dependencies.

```bash
pip install pipenv
pipenv install
export PYTHONPATH=`pwd` 
```

## Usage

Run the server with:
```bash
pipenv run python src/app.py
```
## Tests

In the root directory, run the test with:
```bash
pipenv run pytest
```

## Docker

In the root directory, run the docker with:
```bash
docker-compose build
docker-compose up
```