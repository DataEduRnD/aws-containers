# Set base image (host OS)
FROM python:3.8-alpine

# By default, listen on port 5000
EXPOSE 5000/tcp

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY . .

# Install any dependencies
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
# COPY app.py .

# docker build -t flask-container ./flask
# docker run -p 5000:5000 flask-container flask run --host 0.0.0.0
# docker run -it flask-container /bin/sh  
# docker exec flask-container /bin/sh
#  curl 127.0.0.1:5000

CMD ["python", "./app.py"]