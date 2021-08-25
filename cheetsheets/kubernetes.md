# kubernetes 

# contents


# minikube
    minikube start
    minikube status
    minikube stop
    minikube dashboard

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
_pod-definition.yml_
    
    apiVersion:
    
    kind:
    
    metadata:
    
    spec:

_commands_
    
    kubectl create -f pod-definition.yml
    kubectl get pods
    kubectl get pods -o wide
    kubectl describe pod myapp-pod
    kubectl delete -f pod-definition.yml

### replicasets

info on both replicaioncontorller and replicasets

* replicationcontroller begining to be depricated

_rc-definition.yml_

_commands_

_replicationcontroller_
    
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

__kubectl run__

    - pod
    kubectl run nginx --image=nginx
    * to create yaml file
    kubctl run nginx --image=nginx --dry-run=client -o yaml

    - deployment
    kubectl create deployment --image=nginx nginx
    * to create deployment yaml file
    kubectl create deployment --image=nginx nginx --dry-run=client -o yaml






# Referneces
1. The Kunbernetes Book - book
2. Certified Kubernetes Administrator (CKA) - udemy class
3. https://kubernetes.io/docs/reference/kubectl/cheatsheet/  
