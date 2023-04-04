# Set base image (host OS)
FROM python:3.9-slim

# By default, listen on port 5000
EXPOSE 5000/tcp

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY . .

# Install any dependencies
RUN pip install -r requirements.txt

# app.py -> app 
CMD gunicorn --bind 0.0.0.0:5000 app:app

# Copy the content of the local src directory to the working directory
# COPY app.py .

# docker build -t flask-container ./flask
# flask run --host 0.0.0.0
# docker run -p 5000:5000 flask-container flask run --host 0.0.0.0
# docker run -it flask-container /bin/sh  
# docker exec flask-container /bin/sh
#  curl 127.0.0.1:5000

#CMD ["python", "./app.py"]