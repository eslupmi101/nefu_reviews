FROM python:3.10.12

WORKDIR /app

RUN pip install poetry

COPY . .

RUN poetry install

CMD ["poetry", "run", "python", "main.py"]
