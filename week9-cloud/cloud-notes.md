# Cloud Fundamentals Notes

Notes from Microsoft's Azure Fundamentals material, related to what I built
in this repo.

## Core building blocks mapped to my projects
| Cloud idea | Azure example | What I used locally |
|---|---|---|
| Compute | Virtual machines, App Service, Functions | Docker containers (weeks 5, 6, 11) |
| Storage | Blob storage, managed disks | Docker volume for Postgres data |
| Networking | Virtual networks, network security groups | Docker network, unpublished database port |
| Identity and access | Microsoft Entra ID, role-based access control | GitHub token with no extra permissions, CI `permissions: contents: read` |
| Infrastructure as code | Bicep, Terraform | Terraform in weeks 10 and 11 |
| Monitoring | Azure Monitor | n8n execution history, container logs |
| Pipelines | Azure DevOps, GitHub Actions | GitHub Actions CI |

## Questions I can answer in my own words
1. What is the difference between IaaS, PaaS, and SaaS?
2. What is the shared responsibility model?
3. What are regions and availability zones, and why do they matter?
4. What is least privilege, and where did I apply it?
5. What would change if I ran the week 11 project on a cloud VM?
6. Why does Terraform state matter, and why is it sensitive?

## Labs and modules completed
- (date) module or lab name: one thing I learned

## Still unclear
- 
