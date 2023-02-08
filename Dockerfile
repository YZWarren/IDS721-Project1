FROM python:3.8
LABEL maintainer="yuzhou.zhao1022@gmail.com"

EXPOSE 8080

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["app.py"]
