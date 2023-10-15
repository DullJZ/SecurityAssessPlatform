from flask import Flask, request, jsonify
from main import *

app = Flask(__name__)
@app.route('/api', methods=['POST', 'GET'])
def api():
    return jsonify({'status': 'success'})

@app.route('/api/delete_image', methods=['POST'])
def delete_image():
    data = request.get_json()
    client = GetDockerClient(data['remote'])
    return DeleteImage(client, data['image_name'])

@app.route('/api/delete_container', methods=['POST'])
def delete_container():
    data = request.get_json()
    client = GetDockerClient(data['remote'])
    return DeleteContainer(client, data['container_name'])

@app.route('/api/pull_image', methods=['POST'])
def pull_image():
    data = request.get_json()
    client = GetDockerClient(data['remote'])
    return PullImage(client, data['image_name'])

@app.route('/api/restart_container', methods=['POST'])
def restart_container():
    data = request.get_json()
    client = GetDockerClient(data['remote'])
    return RestartContainer(client, data['container_name'])

@app.route('/api/start_container', methods=['POST'])
def start_container():
    data = request.get_json()
    client = GetDockerClient(data['remote'])
    return StartContainer(client, data['container_name'])

@app.route('/api/stop_container', methods=['POST'])
def stop_container():
    data = request.get_json()
    client = GetDockerClient(data['remote'])
    return StopContainer(client, data['container_name'])

@app.route('/api/get_docker_info', methods=['POST'])
def get_docker_info():
    data = request.get_json()
    client = GetDockerClient(data['remote'])
    return GetDockerInfo(client)

@app.route('/api/get_docker_version', methods=['POST'])
def get_docker_version():
    data = request.get_json()
    client = GetDockerClient(data['remote'])
    return GetDockerVersion(client)

@app.route('/api/show_running_containers', methods=['POST'])
def show_running_containers():
    data = request.get_json()
    client = GetDockerClient(data['remote'])
    return ShowRunningContainers(client)

@app.route('/api/show_all_containers', methods=['POST'])
def show_all_containers():
    data = request.get_json()
    client = GetDockerClient(data['remote'])
    return ShowAllContainers(client)

@app.route('/api/show_container_info', methods=['POST'])
def show_container_info():
    data = request.get_json()
    client = GetDockerClient(data['remote'])
    return ShowContainerInfo(client, data['container_name'])

@app.route('/api/run_container_by_compose_file', methods=['POST'])
def run_container_by_compose_file():
    data = request.get_json()
    client = GetDockerClient(data['remote'])
    return RunContainerByComposeFile(client, data['compose_file'])

if __name__ == '__main__':
    app.run(debug=False, port=15000)
