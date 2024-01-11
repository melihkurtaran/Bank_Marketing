# Bank Marketing App Docker Instructions

These instructions will guide you through building and running the Bank Marketing App Docker container.

## Prerequisites

Before you begin, make sure you have Docker installed on your system. You can download and install Docker from the [official Docker website](https://www.docker.com/get-started).

## Building the Docker Image

To build the Docker image for the Bank Marketing App, use the following command:

```bash
docker build -t bank-marketing-app .
```

This command will build a Docker image with the name "bank-marketing-app" using the Dockerfile located in the current directory (`.`). Be sure to run this command in the same directory as your Dockerfile.

## Running the Docker Container

Once the Docker image is built, you can run the Bank Marketing App in a Docker container using the following command:

```bash
docker run -p 80:80 bank-marketing-app
```

This command starts a Docker container based on the "bank-marketing-app" image and maps port 80 from the container to port 80 on your host machine. You can access the Bank Marketing App by opening a web browser and navigating to `http://localhost`.

### Optional: Running on a Different Port

If port 80 is already in use on your host machine, you can choose a different available port by modifying the `-p` option. For example, to use port 8080 on your host, you can run:

```bash
docker run -p 8080:80 bank-marketing-app
```


## Accessing the Bank Marketing App

After running the Docker container, you can access the Bank Marketing App by opening a web browser and navigating to `http://localhost`. If you are using a different port (e.g., 8080), replace "localhost" with the appropriate hostname and port number.

That's it! You should now have the Bank Marketing App up and running in a Docker container on your machine.
