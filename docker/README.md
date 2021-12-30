### In order to build the image, we will run the docker build command:

docker build -t docker-model -f Dockerfile .

Or docker build -t docker-model .

### Viewing Model Artifacts

docker run docker-model cat /home/jovyan/model/metadata.json

### The command to perform inference is

docker run docker-model python3 inference.py

Or docker run -d --name mycontainer -p 80:80 docker-model python3 inference.py
