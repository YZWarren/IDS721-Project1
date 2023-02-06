FROM python:3.8
LABEL maintainer="yuzhou.zhao1022@gmail.com"

WORKDIR .
COPY .

EXPOSE 5000:8080

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]
