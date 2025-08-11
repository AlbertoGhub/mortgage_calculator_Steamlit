FROM python:3.11-slim

LABEL maintainer="This is just a test"

WORKDIR /app

COPY requirements.txt dependencies.txt

RUN pip install --no-cache-dir -r dependencies.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app/app.py", "--server.address=0.0.0.0"]