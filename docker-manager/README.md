这是一组用于操作Docker的函数，下面是每个函数的说明：

- `GetDockerClient(remote = '') -> docker.DockerClient`: 这个函数用于获取Docker客户端。如果提供了`remote`参数，它将连接到远程Docker服务器，否则它将连接到本地环境。

- `GetDockerVersion(client) -> dict`: 这个函数返回Docker服务器的版本信息。

- `GetDockerInfo(client) -> dict`: 这个函数返回Docker服务器的详细信息。

- `PullImage(client, image_name) -> dict`: 这个函数用于从Docker Hub拉取指定的镜像。

- `DeleteImage(client, image_name) -> dict`: 这个函数用于删除指定的镜像。

- `StartContainer(client, container_name) -> dict`: 这个函数用于启动指定的容器。

- `StopContainer(client, container_name) -> dict`: 这个函数用于停止指定的容器。

- `RestartContainer(client, container_name) -> dict`: 这个函数用于重启指定的容器。

- `DeleteContainer(client, container_name) -> dict`: 这个函数用于删除指定的容器。

- `ForceDeleteContainer(client, container_name) -> dict`: 这个函数用于强制删除指定的容器，即使它正在运行。

- `ShowAllContainers(client) -> dict`: 这个函数返回所有容器的列表，包括正在运行和已停止的容器。

- `ShowRunningContainers(client) -> dict`: 这个函数返回正在运行的容器列表。

- `ShowStoppedContainers(client) -> dict`: 这个函数返回已停止的容器列表。

- `ShowContainerInfo(client, container_name_or_id) -> dict`: 这个函数返回指定容器的详细信息，包括名称、ID、状态、使用的镜像和开放的端口等。

- `RunContainerByComposeFile(client, compose_file_dir) -> list`: 这个函数根据给定的docker-compose文件来运行容器。它只支持docker-compose.yml版本3，并且只支持'image', 'container_name', 'restart', 'environment', 'volumes', 'ports'这些键。

- `RunCommand(command: str, timeout=10) -> dict`: 这个函数在shell中运行指定的命令。注意，这可能会有风险。

- `GenerateUnusedPort() -> int`: 这个函数生成一个未被使用的端口号。它会不断地生成一个随机的端口号，直到找到一个未被使用的端口号为止。


以下是所有函数的详细信息：

| 函数名 | 必要参数 | 可选参数 | 调用示例 | 示例返回值 |
| --- | --- | --- | --- | --- |
| GetDockerClient | 无 | remote='' | GetDockerClient('tcp://192.168.1.100:2376') | docker.DockerClient 对象 |
| GetDockerVersion | client | 无 | GetDockerVersion(client) | {'status': 'success', 'version': '20.10.7'} |
| GetDockerInfo | client | 无 | GetDockerInfo(client) | {'status': 'success', 'info': {...}} |
| PullImage | client, image_name | 无 | PullImage(client, 'ubuntu:latest') | {'status': 'success'} |
| DeleteImage | client, image_name | 无 | DeleteImage(client, 'ubuntu:latest') | {'status': 'success'} |
| StartContainer | client, container_name | 无 | StartContainer(client, 'my_container') | {'status': 'success'} |
| StopContainer | client, container_name | 无 | StopContainer(client, 'my_container') | {'status': 'success'} |
| RestartContainer | client, container_name | 无 | RestartContainer(client, 'my_container') | {'status': 'success'} |
| DeleteContainer | client, container_name | 无 | DeleteContainer(client, 'my_container') | {'status': 'success'} |
| ForceDeleteContainer | client, container_name | 无 | ForceDeleteContainer(client, 'my_container') | {'status': 'success'} |
| ShowAllContainers | client | 无 | ShowAllContainers(client)  | {'status': 'success', 'containers': [{'name': 'xxx', 'id': 'abc', 'status': 'running'}, ...]} |
| ShowRunningContainers | client | 无 | ShowRunningContainers(client) | {'status': 'success', 'containers': [{'name': 'xxx', 'id': 'abc', 'status': 'running'}, ...]}|
| ShowStoppedContainers | client | 无 | ShowStoppedContainers(client) | {'status': 'success', 'containers': [{'name': 'xxx', 'id': 'abc', 'status': 'exited'}, ...]}|
| ShowContainerInfo | client, container_name_or_id | 无 | ShowContainerInfo(client, "my_container") | {'status': 'success', ...}|
| RunContainerByComposeFile | client, compose_file_dir | 无 | RunContainerByComposeFile(client, "/path/to/docker-compose.yml") | [{'status': 'success', ...}, ...]|
| RunCommand | command: str | timeout=10 | RunCommand("ls -l", timeout=5) | {'status': 'success', ...}|
| GenerateUnusedPort | 无 | 无 | GenerateUnusedPort() | 12345|

注意：以上示例返回值仅供参考，实际返回值可能会有所不同。另外，这些函数在执行过程中可能会抛出异常，需要在调用时进行适当的错误处理。如果函数执行成功，通常会返回一个包含'status'和'message'的字典，其中'status'为'success'，'message'包含了执行结果。如果函数执行失败，'status'将为'failed'，并且'message'将包含错误信息。对于一些函数，例如ShowAllContainers、ShowRunningContainers和ShowStoppedContainers，它们还会返回一个包含所有容器信息的列表。每个容器的信息是一个字典，包含'name'、'id'和'status'等键。对于ShowContainerInfo函数，它会返回一个包含指定容器详细信息的字典。

以上内容由AI辅助撰写，可能存在错误，以源代码为准