
install

    curl -sSL https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 | bash

verify version
    
    helm version --short

download stabe

    helm repo add stable https://charts.helm.sh/stable

chart list
    helm search repo stable


bash completion
  
    helm completion bash >> ~/.bash_completion
    . /etc/profile.d/bash_completion.sh
    . ~/.bash_completion
    source <(helm completion bash)

update the chart repository

    # first, add the default repository, then update
    helm repo add stable https://charts.helm.sh/stable
    helm repo update

search chart repos

    helm search repo
    helm search repo nginx


install bitnami/nginx
    
    helm install mywebserver bitnami/nginx

verify bitnami/nginx install
    
    kubectl get svc,po,deploy
    kubectl describe deployment mywebserver
    kubectl get pods -l app.kubernetes.io/name=nginx
    kubectl get service mywebserver-nginx -o wide

helm list

helm uninstall mywebserver


helm create eksdemo

helm install --debug --dry-run workshop ~/environment/eksdemo

helm install workshop ~/environment/eksdemo

helm upgrade workshop ~/environment/eksdemo

helm status workshop

helm history workshop

_rollback failed upgrade_

    helm history workshop

    # rollback to the 1st revision
    helm rollback workshop 1

    helm status workshop

    kubectl get pods

_clean up_

    helm uninstall workshop

    