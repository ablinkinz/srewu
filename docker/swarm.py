import docker

client = docker.from_env()
container = client.containers.run("ubuntu:latest", "/bin/bash", detach=True)
container.logs()
