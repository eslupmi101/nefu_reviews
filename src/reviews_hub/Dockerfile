FROM python:3.10.12

WORKDIR /app

RUN pip install poetry

COPY . .

RUN [ ! -d "mediafiles" ] && mkdir mediafiles || true

RUN poetry install

EXPOSE 8000

CMD ["poetry", "run", "gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "reviews_hub.wsgi"]