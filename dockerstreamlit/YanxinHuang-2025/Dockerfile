# app/Dockerfile

FROM python:3.8

WORKDIR /app

RUN apt-get update && apt-get install -y && apt-get install libgl1 -y && apt-get install ffmpeg -y

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8504

#HEALTHCHECK CMD curl --fail http://localhost:11000/_stcore/health

ENTRYPOINT ["streamlit", "run", "new_by_me.py", "--server.port=8504", "--server.address=0.0.0.0"]
