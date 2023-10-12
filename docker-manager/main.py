import docker
import time
import yaml
import subprocess

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

def RunContainerByComposeFile(client, compose_file_dir) -> dict:
    """
    Only support docker-compose.yml version 3
    Only support 'image', 'container_name', 'restart', 'environment', 'volumes', 'ports' keys
    """
    with open(compose_file_dir, 'r') as f:
        container_info = yaml.load(f, Loader=yaml.FullLoader)
    container_info = container_info['services']
    for single_container in container_info.values():
        # image and pull
        if 'image' in single_container.keys():
            s = PullImage(client, single_container['image'])
            if s['status'] == 'failed':
                return {'status': 'failed', 'message': s['message']}
        else:
            return {'status': 'failed', 'message': 'No image assigned'}  # A MUST!
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
        if 'ports' in single_container.keys():
            ports = dict()
            for mapping_rule in single_container['ports']:
                host_port, container_port = mapping_rule.split(':')
                ports[f'{container_port}/tcp'] = int(host_port)
        else:
            ports = None

        # run container
        try:
            client.containers.run(single_container['image'], detach=True, name=container_name,
                                  restart_policy=restart_policy, environment=environment, volumes=volumes, ports=ports)
        except Exception as e:
            print(e)
            return {'status': 'failed', 'message': e}
        print('Run container {} success'.format(container_name))
        return {'status': 'success', 'ContainerName': container_name}

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
    pass


# use for test
client = GetDockerClient()
print(GetDockerVersion(client))
print(GetDockerInfo(client))
#print(RunContainerByComposeFile(client, './test/docker-compose.yml'))
#ForceDeleteContainer(client, '1697105828')
print(ShowAllContainers(client))