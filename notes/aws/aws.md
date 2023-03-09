## <ins>AWS-CLI</ins>

**Install**

[AWS CLI version 2](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)

**Configure Creds**
```
aws configure
```
**Get user info**
```
aws iam get-user
```
**Get configuration info**
```
aws configure list
```
**List profiles**
```
aws configure list-profiles
```
**Examlpe of .aws/credentials**
```
[default]
aws_access_key_id=
aws_secret_access_key=
aws_session_token=
```
**Example of config**
```
[profile default]
output = yaml
color = on
cli_pager=
```
