import docker
import time
import yaml
import subprocess
import sys
import socket
import random

def GetDockerClient(remote = '') -> docker.DockerClient:
    if remote:
        client = docker.DockerClient(base_url=remote)
    else:
        client = docker.from_env()
    return client

def GetDockerVersion(client) -> dict:
    return client.version()

def GetDockerInfo(client) -> dict:
    return client.info()

def PullImage(client, image_name) -> dict:
    try:
        client.images.pull(image_name)
    except docker.errors.APIError as e:
        print(e)
        return {'status': 'failed', 'message': e}
    return {'status': 'success'}

def DeleteImage(client, image_name) -> dict:
    try:
        client.images.remove(image_name)
    except docker.errors.APIError as e:
        print(e)
        return {'status': 'failed', 'message': e}
    return {'status': 'success'}

def StartContainer(client, container_name) -> dict:
    try:
        client.containers.get(container_name).start()
    except docker.errors.APIError as e:
        print(e)
        return {'status': 'failed', 'message': e}
    return {'status': 'success'}

def StopContainer(client, container_name) -> dict:
    try:
        client.containers.get(container_name).stop()
    except docker.errors.APIError as e:
        print(e)
        return {'status': 'failed', 'message': e}
    return {'status': 'success'}

def RestartContainer(client, container_name) -> dict:
    try:
        client.containers.get(container_name).restart()
    except docker.errors.APIError as e:
        print(e)
        return {'status': 'failed', 'message': e}
    return {'status': 'success'}

def DeleteContainer(client, container_name) -> dict:
    try:
        client.containers.get(container_name).remove()
    except docker.errors.APIError as e:
        print(e)
        return {'status': 'failed', 'message': e}
    return {'status': 'success'}

def ForceDeleteContainer(client, container_name) -> dict:
    try:
        client.containers.get(container_name).remove(force=True)
    except docker.errors.APIError as e:
        print(e)
        return {'status': 'failed', 'message': e}
    return {'status': 'success'}

def ShowAllContainers(client) -> dict:
    try:
        containers = client.containers.list(all=True)
    except docker.errors.APIError as e:
        print(e)
        return {'status': 'failed', 'message': e}
    return {'status': 'success', 'containers': containers}

def RunContainerByComposeFile(client, compose_file_dir) -> list:
    """
    Only support docker-compose.yml version 3
    Only support 'image', 'container_name', 'restart', 'environment', 'volumes', 'ports' keys
    """
    result = []
    with open(compose_file_dir, 'r') as f:
        container_info = yaml.load(f, Loader=yaml.FullLoader)
    container_info = container_info['services']
    # think about more than one container situation
    # use 'for' to run each single container
    for single_container in container_info.values():
        # image and pull
        if 'image' in single_container.keys():
            s = PullImage(client, single_container['image'])
            if s['status'] == 'failed':
                result.append({'status': 'failed', 'message': s['message']})
        else:
            result.append({'status': 'failed', 'message': 'No image assigned'})  # A MUST!
        # container_name
        if 'container_name' in single_container.keys():
            container_name = single_container['container_name']
        else:
            # use timestamp as container_name
            container_name = str(int(time.time()*100))
        # restart
        if 'restart' in single_container.keys():
            if single_container['restart'] == 'always':
                restart_policy = {"Name": "always"}
            else:
                restart_policy = {"Name": "on-failure", "MaximumRetryCount": 3}
        else:
            restart_policy = {"Name": "always"}
        # environment
        if 'environment' in single_container.keys():
            environment = single_container['environment']
        else:
            environment = None
        # volumes
        if 'volumes' in single_container.keys():
            volumes = single_container['volumes']
        else:
            volumes = None
        # ports
        host_ports = [] # use for log
        if 'ports' in single_container.keys():
            ports = dict()
            for mapping_rule in single_container['ports']:
                host_port, container_port = mapping_rule.split(':')
                host_port = GenerateUnusedPort()
                host_ports.append(host_port)
                ports[f'{container_port}/tcp'] = int(host_port)
        else:
            ports = None
        # run a container
        try:
            client.containers.run(single_container['image'], detach=True, name=container_name,
                                  restart_policy=restart_policy, environment=environment, volumes=volumes, ports=ports)
        except Exception as e:
            print(e)
            result.append({'status': 'failed', 'message': e})
        print('Run container {} success'.format(container_name))
        result.append({'status': 'success', 'ContainerName': container_name, 'Ports': host_ports})
    # 'for' end
    return result

def RunCommand(command: str) -> dict:
    """
    Run command in shell
    MAY BE DANGEROUS!
    """
    try:
        result = subprocess.Popen(command, shell=True)
        result.wait(10)

    except Exception as e:
        return {'status': 'failed', 'message': e}
    return {'status': 'success', 'result': result}

def GenerateUnusedPort() -> int:
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port = random.randint(10000, 65535)
        location = ('127.0.0.1', port)
        result = sock.connect_ex(location)
        if result != 0:
            # this port is not in use
            break
        sock.close()
    return port


# use for test
client = GetDockerClient()
print(GetDockerVersion(client))
print(GetDockerInfo(client))
print(RunContainerByComposeFile(client, './test/docker-compose.yml'))
#ForceDeleteContainer(client, '1697105828')
#print(ShowAllContainers(client))