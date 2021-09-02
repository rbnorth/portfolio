# kubernetes 

# contents
1. minikube
2. commands
3. pods
4. deployments
5. services
6. service discovery

# minikube
    minikube start
    minikube status
    minikube ip
    minikube dashboard
    minikube stop
    minikube delete

# install kubectl

    sudo curl --silent --location -o /usr/local/bin/kubectl \
        https://amazon-eks.s3.us-west-2.amazonaws.com/1.19.6/2021-01-05/bin/linux/amd64/kubectl

    sudo chmod +x /usr/local/bin/kubectl


# commands

## version
    kubectl version
    kubectl version -o yaml

## cluster info
    kubectl cluster-info

## 
    kubectl get componetstatuses

## contexts
    kubectl config set-context my-context --namespace=mystuff
    kubectl config use-context my-context

## pods
_pod-definition.yml example_
    
    apiVersion: v1
    kind: Pod
    metadata:
    name: static-web
    labels:
        role: myrole
    spec:
    containers:
        - name: web
        image: nginx
        ports:
            - name: web
            containerPort: 80
            protocol: TCP

_commands_
    
    kubectl create -f pod-definition.yml
    kubectl get pods
    kubectl get pods -o wide
    kubectl describe pod myapp-pod
    kubectl delete -f pod-definition.yml

    *the kubernetes book
    kubectl get pods hello-pod -o yaml
    kubectl describe pods hello-pod
    kubectl exec hello-pod ps aux
    kubectl exec -it hello-pod sh
    (revised)
    kubectl exec hello-pod -- ps aux
    kubectl exec -it hello-pod -- sh
     
### replicasets

info on both replicaioncontorller and replicasets

* replicationcontroller begining to be depricated

_rc-definition.yml example_
    
    apiVersion: apps/v1
    kind: ReplicaSet
    metadata:
    name: web
    labels:
        env: dev
        role: web
    spec:
    replicas: 4
    selector:
        matchLabels:
        role: web
    template:
        metadata:
        labels:
                role: web
        spec:
        containers:
        - name: nginx
                image: nginx

_commands_

_replicationcontroller(deprecated)_
    
    kubectl create -f rc-definition.yml
    kubectl get replicationcontroller
    kubectl delete -f rc-definition.yml

_replicaset_
    
    kubectl create -f replicaset-definition.yml
    kubectl get replicaset 
    kubectl delete -f replicaset-definition.yml

__scaling__
    
    - edit replicateset-definition.yml
    kubectl replace -f replicaset-definition.yml

    kubectl scale --replicas=6 -f replicatset-definition.yml
    or
    kubect scale --replicas=6 relicaset myapp-replicaset
    
    kubectl delete replicaset myapp-replicaset

### deployments
_deployments-definition.yml_

_commands_

    kubectl create -f deployment-definition.yml
    kubeclt get deployments
    kubectl get replicasets
    kubectl get pods

__the kubernetes book__

    kubectl apply -f deploy.yml
    kubectl get deploy hello-deploy
    kubectl describe deploy hello-deploy
    kubectl get replicasets
    kubectl get rs      

    kubectl apply -f svc.yml

    kubectl apply -f deploy.yml --record
    kubectl rollout status deployment hello-deploy
    kubectl get deploy
    kubectl get deploy hello-deploy 

    # rollback 
    kubectl rollout history deployment hello-deploy
    kubectl get rs
    kubectl rollout undo deployment hello-deploy --to-revision=1
    kubectl get deploy hello-deploy
    kubectl rollout status deployment hello-deploy
    
    kubectl delete -f deploy.yml
    kubectl delete -f svc.yml

__kubectl run__

    - pod
    kubectl run nginx --image=nginx
    * to create yaml file
    kubctl run nginx --image=nginx --dry-run=client -o yaml

    - deployment
    kubectl create deployment --image=nginx nginx
    * to create deployment yaml file
    kubectl create deployment --image=nginx nginx --dry-run=client -o yaml

### services

__the kubernetes book__

    kubectl apply -f deploy.yml

_imperative way (you should avoid this, its dumb and can cause ibs)_
    
    kubectl expose deployment web-deploy --name=hello-svc --target-port=8080 --type=NodePort
    kubectl describe svc hello-svc
    kubectl delete svc hello-svc

_declarative way (this is the way you should do it, keeps track of changes and whats been done)_

    kubectl apply -f svc.yml
    kubectl get svc hello-svc
    kubectl describe svc hello-svc

    kubectl get endpoints hello-svc
    kubectl get ep hello-svc
    kubectl describe ep hello-svc

    kubectl delete -f deploy.yml
    kubectl delete -f svc.yml

### service discovery 


# Referneces
1. The Kunbernetes Book - book
2. Certified Kubernetes Administrator (CKA) - udemy class
3. https://kubernetes.io/docs/reference/kubectl/cheatsheet/  
