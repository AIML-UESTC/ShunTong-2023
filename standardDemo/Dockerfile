# app/Dockerfile
#mainpage dockerfile

FROM python:3.8-slim

WORKDIR /app

RUN apt-get update && apt-get install -y && apt-get install libgl1 -y && apt-get install libglib2.0-0 -y && apt-get install libgtk2.0-dev -y

COPY . .

RUN pip3 install -r dockerimage/requirements.txt

EXPOSE 8507

HEALTHCHECK CMD curl --fail http://localhost:8507/_stcore/health

ENTRYPOINT ["streamlit", "run", "webpage/home.py", "--server.port=8507", "--server.address=0.0.0.0"]
