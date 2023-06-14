# app/Dockerfile
#mainpage dockerfile

FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8503

HEALTHCHECK CMD curl --fail http://localhost:8502/_stcore/health

ENTRYPOINT ["streamlit", "run", "main_page.py", "--server.port=8503", "--server.address=0.0.0.0"]
