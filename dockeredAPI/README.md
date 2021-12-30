### Build the Docker Image¶
Now that all the files are in place, let's build the container image.

Go to the project directory
Build your FastAPI image:
docker build -t myimage .

### Start the Docker Container¶
Run a container based on your image:
docker run -d --name mycontainer -p 80:80 myimage
