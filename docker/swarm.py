import docker

client = docker.from_env()
client.containers.run("ubuntu:latest", "/bin/bash", detach=True)
container.logs()
