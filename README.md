# Dataflow
# Installing Docker and Kubernetes (k8s) on Ubuntu

This is a step-by-step guide to installing Docker and Kubernetes (k8s) on Ubuntu.

## Prerequisites

Before you begin, make sure you have the following:

- A machine running Ubuntu
- sudo privileges

## Installing Docker

1. Update the apt package index:
```console
sudo apt-get update
```
2. Install Docker:
```console
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

3. Verify that Docker is installed correctly by running the hello-world image:
```console
sudo docker run hello-world
```

## Installing Kubernetes (k8s)

1. Add the Kubernetes signing key:
```console
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
```
2. Add the Kubernetes repository:
```console
sudo apt-add-repository "deb http://apt.kubernetes.io/ kubernetes-xenial main"
```
3. Update the apt package index:
```console
sudo apt-get update
```
4. Install Kubernetes:
```console
sudo apt-get install -y kubelet kubeadm kubectl
```
5. Initialize the master node:
```console
sudo kubeadm init
```
6. Copy the Kubernetes configuration file to your home directory:
```console
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
```
7. Verify that Kubernetes is installed correctly by running the following command:
```console
kubectl version
```

## Conclusion

Congratulations! You have successfully installed Docker and Kubernetes (k8s) on Ubuntu. Now you can start deploying your applications to a Kubernetes cluster.

For more information, see the [official Docker documentation](https://docs.docker.com/get-docker/) and the [official Kubernetes documentation](https://kubernetes.io/docs/setup/).






