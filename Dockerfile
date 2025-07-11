FROM python:3.11.2-slim
WORKDIR /app

#Install Dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#Expose port
COPY ./app /app
EXPOSE 8080

#Run the program and host the server
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "main:app"]