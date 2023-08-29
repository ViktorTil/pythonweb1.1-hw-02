FROM python:3.9

WORKDIR /APP_HOME

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["python", "main.py"]