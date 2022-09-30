## rainbond 平台安装应用实现自动化

1. 操作系统升级内核  
ubuntu20.04内核足够新，centos系统需要[升级](https://t.goodrain.com/d/9-centos)

2. 安装docker
```
curl sh.rainbond.com/install_docker | bash
```

3. 安装
```
yum -y install nfs-utils    # Cenots系统
apt-get install nfs-common  # ubuntu系统
```

3. 运行控制台
```
docker run -d -p 7070:7070 --name=rainbond-allinone --restart=always -v ~/.ssh:/root/.ssh -v ~/rainbonddata:/app/data registry.cn-beijing.aliyuncs.com/quyc/rainbond-allinone:v1.2
```

4. 安装k8s
准备：
```
1. ssh-keygen
2. cat ~/.ssh/id_rsa.pub
3. wget http://sh.rainbond.com/init_node && chmod +x init_node
4. export SSH_RSA="步骤2内容" && ./init_node
```
上传rke文件到 /usr/bin/rke 
上传cluster.yml文件到 /root/cluster.yml
```
chmod +x /usr/bin/rke 
rke up
wget https://grstatic.oss-cn-shanghai.aliyuncs.com/binary/kubectl -O /usr/bin/kubectl
chmod +x /usr/bin/kubectl
mkdir /root/.kube && cp kube_config_cluster.yml /root/.kube/config
wget https://pkg.goodrain.com/pkg/helm && chmod +x helm && mv helm /usr/local/bin/
kubectl get node
```

5. 进入控制台
![image](https://user-images.githubusercontent.com/43192516/192736943-031fac38-a633-4e6d-97a4-d4e2cc47c401.png)

![image](https://user-images.githubusercontent.com/43192516/192741901-424eadc7-2a5f-4f5f-8926-ca09d41d515b.png)

![image](https://user-images.githubusercontent.com/43192516/192737515-dd643c77-1ebd-4ac7-a0ef-54161752c4a2.png)


6. 手动创建tomcat应用，开放外部端口并挂载路径/usr/local/tomcat
7. 记录token和集群ID
![image](https://user-images.githubusercontent.com/43192516/192935429-d1b95488-a075-48d5-8fd0-607d6070c651.png)

![image](https://user-images.githubusercontent.com/43192516/192935451-f81ab112-a1dd-4486-b331-84395eecf4fc.png)

8. 安装grctl命令
```
docker run -it --rm -v /:/rootfs registry.cn-beijing.aliyuncs.com/quyc/rainbond-grctl:v1.2 copy && mv /usr/local/bin/rainbond-grctl /usr/local/bin/grctl && grctl install
```
9. init service
```
grctl replace ip --ip=$public_ip --domain=$public_ip:7070 --token=<token值> --n=< 集群id> --s=true
```
