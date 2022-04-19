FROM python:3.8


RUN mkdir /app
WORKDIR /app
ADD . /app/

RUN pip install requests beautifulsoup4

CMD ["python","/app/main.py""]
