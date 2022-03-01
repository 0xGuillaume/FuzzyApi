# Custom Image : Fuzzy API
FROM python:latest AS fuzzyapi

WORKDIR /code

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -q -r requirements.txt

COPY ./api /code/api

CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8000"]


