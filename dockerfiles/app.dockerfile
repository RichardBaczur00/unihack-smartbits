FROM python:3.10

WORKDIR /app

EXPOSE 80

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD [ "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload" ]