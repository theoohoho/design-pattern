"""
Worker contain train, test, build, deploy, remove, register
SRP => split all of job component
OCP => 
LSP => 
ISP =>
DIP => 
"""
# DIP: High level module
# LSP: import WorkerBase can used Father class method
class Worker:
    def __init__(worker: WorkerBase):
        self.worker = worker

    def run():
        self.worker.run()

# Abstraction
class WorkerBase:

    def git_clone():

    def run():
        pass

# DIP: Detail
# SRP: single resposibility 
class Tester(WorkerBase):
    def test():
    def run():
        self.test()

class Builder(WorkerBase):
    import docker
    import os
    def docker_client(docker_login：DockerLogin):
        docker_client = docker_login.login(docker.DockerClient())
        return docker_client
        
    def build():
        if os.get['DOCKER_LOGIN_CONFIG'] == 'config':
            docker_login = new DockerLoginByConfig()
        else:
            docker_login = new DockerLoginByPassword()

        docker_client = docker_client(docker_login)
        docker_client.build()
        docker_client.push()

    def run():
        self.build()

# OCP: Abstract login method 
class DockerLogin:
    def login(client):
        pass
class DockerLoginByConfig(DockerLogin):
    def login(client):
        client.login(username='', dockercfg='path/to/docker/config')
        return client
class DockerLoginByPassword(DockerLogin):
    def login(client):
        client.login(username='', password='')
        return client

# trigger builder
mew Worker(new Buidler()).run()