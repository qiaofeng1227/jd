## rainbond 平台安装应用实现自动化

1. 操作系统升级内核
centos系统

2. 安装docker
```
curl sh.rainbond.com/install_docker | bash
```

3. 运行控制台
```
docker run -d -p 7070:7070 --name=rainbond-allinone --restart=always -v ~/.ssh:/root/.ssh -v ~/rainbonddata:/app/data registry.cn-beijing.aliyuncs.com/quyc/rainbond-allinone:v1.1
```

4. 安装k8s
上传rke文件到 /usr/bin/rke 
上传cluster.yml文件到 /root/cluster.yml
```
chmod +x /usr/bin/rke 
rke up
wget https://grstatic.oss-cn-shanghai.aliyuncs.com/binary/kubectl -O /usr/bin/kubectl
chmod +x /usr/bin/kubectl
mkdir /root/.kube && cp kube_config_cluster.yml /root/.kube/config
wget https://pkg.goodrain.com/pkg/helm && chmod +x helm && mv helm /usr/local/bin/
```

5. 进入控制台
![image](https://user-images.githubusercontent.com/43192516/192736943-031fac38-a633-4e6d-97a4-d4e2cc47c401.png)

![image](https://user-images.githubusercontent.com/43192516/192737221-ebb5f4e6-3dfc-4d8c-9540-ea74101c2ba4.png)

![image](https://user-images.githubusercontent.com/43192516/192737515-dd643c77-1ebd-4ac7-a0ef-54161752c4a2.png)
