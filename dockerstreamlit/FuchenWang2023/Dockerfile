# app/Dockerfile

FROM python:3.8

WORKDIR /app

RUN apt-get update && apt-get install -y && apt-get install libgl1 -y

COPY . .

RUN pip3 install -r requirements.txt

#EXPOSE 11000

HEALTHCHECK CMD curl --fail http://localhost:11000/_stcore/health

#ENTRYPOINT ["streamlit", "run", "src/Display.py", "--server.port=11000", "--server.address=0.0.0.0"]
