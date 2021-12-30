### Build the Docker Image
Now that all the files are in place, let's build the container image.

Go to the project directory
Build your FastAPI image:
docker build -t myimage .

### Start the Docker Container
Run a container based on your image:
docker run -d --name mycontainer -p 80:80 myimage

### Check it
You should be able to check it in your Docker container's URL, for example: http://192.168.99.100/predict/sample text info or http://127.0.0.1/predict/sample text info (or equivalent, using your Docker host).

You will see something like:
{"text": "sample text info"}

Interactive API docs¶
Now you can go to http://192.168.99.100/docs or http://127.0.0.1/docs (or equivalent, using your Docker host).

You will see the automatic interactive API documentation (provided by Swagger UI)

#### Note In Dockerfile:
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
This adjusts the Uvicorn command to use the new module main (instead of app.main as directory "app" is not added in docker container) to import the FastAPI object app.
