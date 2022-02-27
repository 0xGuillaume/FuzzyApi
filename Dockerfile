# Custom Image : Run FuzzyAPI
FROM python:latest

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY api/ code/api/

EXPOSE 8000

CMD ["uvicorn", "api.app:app", "--host", "127.0.0.1", "--port", "8000"]
