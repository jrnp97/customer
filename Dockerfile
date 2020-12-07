FROM python:3.8.6

RUN apt-get update 

COPY pj_customer/ /src/

WORKDIR /src/

COPY requirements.txt /src/

RUN pip install -r requirements.txt

COPY entrypoint.sh /src/

RUN chmod +x entrypoint.sh
