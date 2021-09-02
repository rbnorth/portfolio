install awscli


update awscli 
    
    sudo pip install --upgrade awscli && hash -r

install kubectl

    sudo curl --silent --location -o /usr/local/bin/kubectl \
    https://amazon-eks.s3.us-west-2.amazonaws.com/1.19.6/2021-01-05/bin/linux/amd64/kubectl

    sudo chmod +x /usr/local/bin/kubectl

Enable kubectl bash_completion

    kubectl completion bash >>  ~/.bash_completion
    . /etc/profile.d/bash_completion.sh
    . ~/.bash_completion

eksctl install
    
    curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp

    sudo mv -v /tmp/eksctl /usr/local/bin

verify eksctl
    
    eksctl version

enable bash-completion

    eksctl completion bash >> ~/.bash_completion
    . /etc/profile.d/bash_completion.sh
    . ~/.bash_completion

Install jq, envsubst (from GNU gettext utilities) and bash-completion

    sudo yum -y install jq gettext bash-completion moreutils

Install yq for yaml processing

    echo 'yq() {
    docker run --rm -i -v "${PWD}":/workdir mikefarah/yq "$@"
    }' | tee -a ~/.bashrc && source ~/.bashrc


kubectl commands

    kubectl get svc,po,deploy

    kubectl get svc ecsdemo-frontend -o jsonpath="{.status.loadBalancer.ingress[*].hostname}"; echo


# aws

_create user_
    aws iam create-user --user-name rbac-user
    aws iam create-access-key --user-name rbac-user | tee /tmp/create_output.json

_create user and add them to groups_
    
    aws iam create-user --user-name PaulAdmin
    aws iam create-user --user-name JeanDev
    aws iam create-user --user-name PierreInteg

    aws iam add-user-to-group --group-name k8sAdmin --user-name PaulAdmin
    aws iam add-user-to-group --group-name k8sDev --user-name JeanDev
    aws iam add-user-to-group --group-name k8sInteg --user-name PierreInteg

    aws iam get-group --group-name k8sAdmin
    aws iam get-group --group-name k8sDev
    aws iam get-group --group-name k8sInteg






