API文档：

1. `/api`
   -  方法 : `POST`, `GET`
   -  描述 : 返回一个状态为'success'的JSON对象。
   -  返回示例 ：`{"status":"success"}`

2. `/api/delete_image`
   -  方法 : `POST`
   -  描述 : 删除指定的Docker镜像。
   -  参数 :
     - `remote`: Docker服务器的地址 若为远程实验模式则填写空字符串。
     - `image_name`: 要删除的Docker镜像的名称。
   -  返回示例 ：`{"status":"success"}`

3. `/api/delete_container`
   -  方法 : `POST`
   -  描述 : 删除指定的Docker容器。
   -  参数 :
     - `remote`: Docker服务器的地址 若为远程实验模式则填写空字符串。
     - `container_name`: 要删除的Docker容器的名称。
   -  返回示例 ：`{"status":"success"}`

4. `/api/pull_image`
   -  方法 : `POST`
   -  描述 : 从Docker Hub拉取指定的镜像。
   -  参数 :
     - `remote`: Docker服务器的地址 若为远程实验模式则填写空字符串。
     - `image_name`: 要拉取的Docker镜像的名称。
   -  返回示例 ：`{"status":"success"}`

5. `/api/restart_container`
   -  方法 : `POST`
   -  描述 : 重启指定的Docker容器。
   -  参数 :
     - `remote`: Docker服务器的地址 若为远程实验模式则填写空字符串。
     - `container_name`: 要重启的Docker容器的名称。
   -  返回示例 ：`{"status":"success"}`

6. `/api/start_container`
   -  方法 : `POST`
   -  描述 : 启动指定的Docker容器。
   -  参数 :
     - `remote`: Docker服务器的地址 若为远程实验模式则填写空字符串。
     - `container_name`: 要启动的Docker容器的名称。
   -  返回示例 ：`{"status":"success"}`

7. `/api/stop_container`
   -  方法 : `POST`
   -  描述 : 停止指定的Docker容器。
   -  参数 :
     - `remote`: Docker服务器的地址 若为远程实验模式则填写空字符串。
     - `container_name`: 要停止的Docker容器的名称。
   -  返回示例 ：`{"status":"success"}`

8. `/api/get_docker_info`
   -  方法 : `POST`
   -  描述 : 获取Docker服务器信息。
   -  参数 :
     - `remote`: Docker服务器的地址 若为远程实验模式则填写空字符串。
   -  返回示例 ：`{"Architecture":"x86_64","BridgeNfIp6tables":true,"BridgeNfIptables":true,"CPUSet":true,"CPUShares":true,"CgroupDriver":"cgroupfs","CgroupVersion":"2","ContainerdCommit":{"Expected":"61f9fd88f79f081d64d6fa3bb1a0dc71ec870523","ID":"61f9fd88f79f081d64d6fa3bb1a0dc71ec870523"},"Containers":3,"ContainersPaused":0,"ContainersRunning":3,"ContainersStopped":0,"CpuCfsPeriod":true,"CpuCfsQuota":true,"Debug":false,"DefaultRuntime":"gitpod","DockerRootDir":"/workspace/.docker-root","Driver":"overlay2","DriverStatus":[["Backing Filesystem","xfs"],["Supports d_type","true"],["Using metacopy","false"],["Native Overlay Diff","false"],["userxattr","true"]],"ExperimentalBuild":false,"GenericResources":null,"HttpProxy":"","HttpsProxy":"","ID":"b2deeeba-b6cc-48e3-b47c-8d09d079c175","IPv4Forwarding":true,"Images":5,"IndexServerAddress":"https://index.docker.io/v1/","InitBinary":"docker-init","InitCommit":{"Expected":"de40ad0","ID":"de40ad0"},"Isolation":"","KernelVersion":"6.1.54-060154-generic","Labels":[],"LiveRestoreEnabled":false,"LoggingDriver":"json-file","MemTotal":67421282304,"MemoryLimit":true,"NCPU":16,"NEventsListener":0,"NFd":50,"NGoroutines":66,"Name":"dulljz-securityassesspl-snj15fqb6ua","NoProxy":"","OSType":"linux","OSVersion":"22.04","OomKillDisable":false,"OperatingSystem":"Ubuntu 22.04.3 LTS (containerized)","PidsLimit":true,"Plugins":{"Authorization":null,"Log":["awslogs","fluentd","gcplogs","gelf","journald","json-file","local","logentries","splunk","syslog"],"Network":["bridge","host","ipvlan","macvlan","null","overlay"],"Volume":["local"]},"RegistryConfig":{"AllowNondistributableArtifactsCIDRs":null,"AllowNondistributableArtifactsHostnames":null,"IndexConfigs":{"docker.io":{"Mirrors":[],"Name":"docker.io","Official":true,"Secure":true}},"InsecureRegistryCIDRs":["127.0.0.0/8"],"Mirrors":null},"RuncCommit":{"Expected":"v1.1.9-0-gccaecfcb","ID":"v1.1.9-0-gccaecfcb"},"Runtimes":{"gitpod":{"path":"/usr/bin/runc-facade"},"io.containerd.runc.v2":{"path":"runc"},"runc":{"path":"runc"}},"SecurityOptions":["name=seccomp,profile=builtin","name=cgroupns"],"ServerVersion":"24.0.6","SwapLimit":true,"Swarm":{"ControlAvailable":false,"Error":"","LocalNodeState":"inactive","NodeAddr":"","NodeID":"","RemoteManagers":null},"SystemTime":"2023-10-15T08:52:52.76065897Z","Warnings":null}
`

9. `/api/get_docker_version`
   -  方法 : `POST`
   -  描述 : 获取Docker版本信息。
   -  参数 :
     - `remote`: Docker服务器的地址 若为远程实验模式则填写空字符串。
   -  返回示例 ：`{"ApiVersion":"1.43","Arch":"amd64","BuildTime":"2023-09-04T12:31:44.000000000+00:00","Components":[{"Details":{"ApiVersion":"1.43","Arch":"amd64","BuildTime":"2023-09-04T12:31:44.000000000+00:00","Experimental":"false","GitCommit":"1a79695","GoVersion":"go1.20.7","KernelVersion":"6.1.54-060154-generic","MinAPIVersion":"1.12","Os":"linux"},"Name":"Engine","Version":"24.0.6"},{"Details":{"GitCommit":"61f9fd88f79f081d64d6fa3bb1a0dc71ec870523"},"Name":"containerd","Version":"1.6.24"},{"Details":{"GitCommit":"v1.1.9-0-gccaecfcb"},"Name":"gitpod","Version":"1.1.9"},{"Details":{"GitCommit":"de40ad0"},"Name":"docker-init","Version":"0.19.0"}],"GitCommit":"1a79695","GoVersion":"go1.20.7","KernelVersion":"6.1.54-060154-generic","MinAPIVersion":"1.12","Os":"linux","Platform":{"Name":"Docker Engine - Community"},"Version":"24.0.6"}
`

10. `/api/show_running_containers`
    -  方法 : `POST`
    -  描述 : 显示正在运行中的所有Docker容器。
    -  参数 :
      - `remote`: Docker服务器的地址 若为远程实验模式则填写空字符串。
    -  返回示例 ：`{"containers":[{"id":"c126a9625767e4e024072e9ba4ed506c287025fcb054fdef46ee0766fe1bc0b6","name":"169735854918","status":"running"},{"id":"3ca83f1374db3f2e685cfae0944b19db172600d376113c5a96372bda058f6b9b","name":"alist1","status":"running"},{"id":"ab1c51393188eca88734e7610ad08b5f072655ed0f222dad93ef487f04be8967","name":"portainer","status":"running"}],"status":"success"}
`

11. `/api/show_all_containers`
    -  方法 : `POST`
    -  描述 : 显示所有Docker容器，包括未运行中的。
    -  参数 :
      - `remote`: Docker服务器的地址 若为远程实验模式则填写空字符串。
    -  返回示例 ：`{"containers":[{"id":"c126a9625767e4e024072e9ba4ed506c287025fcb054fdef46ee0766fe1bc0b6","name":"169735854918","status":"running"},{"id":"3ca83f1374db3f2e685cfae0944b19db172600d376113c5a96372bda058f6b9b","name":"alist1","status":"running"},{"id":"ab1c51393188eca88734e7610ad08b5f072655ed0f222dad93ef487f04be8967","name":"portainer","status":"running"}],"status":"success"}
`

12. `/api/show_container_info`
    -  方法 : `POST`
    -  描述 : 显示指定Docker容器信息。
    -  参数 :
      - `remote`: Docker服务器的地址 若为远程实验模式则填写空字符串。
      - `container_name`: 要查询信息的Docker容器名称。
    -  返回示例 ：`{"container":{"id":"ab1c51393188eca88734e7610ad08b5f072655ed0f222dad93ef487f04be8967","image":"portainer/portainer-ce:latest","name":"portainer","ports":{"8000/tcp":[{"HostIp":"0.0.0.0","HostPort":"8000"},{"HostIp":"::","HostPort":"8000"}],"9000/tcp":[{"HostIp":"0.0.0.0","HostPort":"9000"},{"HostIp":"::","HostPort":"9000"}],"9443/tcp":null},"short_id":"ab1c51393188","status":"running"},"status":"success"}
`

13. 13.：`/api/run_container_by_compose_file` 
    - 方法：`POST` 
    - 描述：通过compose文件运行容器。 
    - 参数： 
        - remote：docker服务器地址。 
        - compose_file：compose文件路径。 
    -  返回示例 ：`{"info":[{"ContainerName":"alist1","Ports":["53596:5244"],"status":"success"}]}`
