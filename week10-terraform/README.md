# Week 10: Terraform

Terraform config that runs an nginx container through the Docker provider.

## Files
- `main.tf`: the provider, the image, and the container.
- `variables.tf`: inputs, including a validated `host_port`.
- `outputs.tf`: the URL and container ID after apply.

## How to run
```
terraform init
terraform plan
terraform apply
terraform output
terraform destroy
```
Override a value with `terraform apply -var host_port=8084`.

## What I learned
- `plan` previews changes before anything happens.
- Changing the port forces the container to be replaced.
- Variables and validation reject bad input early.
- State files can hold secrets, so they stay out of Git.
- `keep_locally` stops Terraform from deleting a shared image.
