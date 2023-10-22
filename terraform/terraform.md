---
key: value
---

<header class="site-header">
  <a href="https://blog.hungovercoders.com"><img alt="hungovercoders" src="../assets/logo3.ico"
    width=50px align="left"></a>
</header>

# Terraform


```bash
terraform init                      # Initialize a Terraform working directory
terraform fmt                       # Formats files correctly
terraform validate                  # Validate the configuration files
terraform plan                      # Generate and show an execution plan
terraform apply                     # Apply the changes to reach the desired state
terraform apply -auto-approve       # Apply changes without prompting for confirmation
terraform destroy                   # Destroy the Terraform-managed infrastructure
terraform destroy -auto-approve     # Destroy infrastructure without prompting for confirmation
terraform state list                # List resources within the state
terraform state mv [SOURCE_ADDRESS] [DESTINATION_ADDRESS]   # Move an item in the state
terraform import [ADDRESS] [ID]                             # Import existing infrastructure into your Terraform state
terraform output                                            # Print the outputs from the state
```
