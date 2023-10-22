---
key: value
---

<header class="site-header">
  <a href="https://blog.hungovercoders.com"><img alt="hungovercoders" src="../assets/logo3.ico"
    width=50px align="left"></a>
</header>

# Configuration

## Variables

These variables are consistently used as environment variables as a developer and in all platforms.
The values of the variables should be **lowercase**.
The values should contain **no spaces**.

|  Name | Category  | Description | Examples |
|---|---|---|---|
| DOMAIN  | GENERAL  | The name of the domain that the resource belongs to. | ['platform', 'whiskeyreviews', 'dogwalkscheduling'] |
| ENVIRONMENT  | GENERAL  | The name of the environment that the resource exists.  | ['development', 'useracceptancetesting', 'production'] |
| ENVIRONMENT_SHORTCODE  | GENERAL  | The shortcode of the environment that the resource exists.  | ['dev', 'uat', 'prd'] |
| ORGANISATION  | GENERAL  | The name of the organisation.  | ['datagriff', 'hungovercoders', 'dogadopt', 'starwalks'] |
| UNIQUE_NAMESPACE  | GENERAL  | The unique four character namespace of the organisation. This is used in resources to make them more likely to be globally unique. | ['dgrf', 'hngc', 'dgad', 'stwa'] |
| TEAM  | GENERAL  | The name of the team. | ['whiskey', 'dogwalk', 'dogrescue'] |
| REGION  | GENERAL  | The region the resource belongs to.  | ['northeurope', 'westeurope'] |
| REGION_SHORTCODE  | GENERAL  | The shortcode of the region the resource belongs to.  | ['eun', 'euw'] |
| ARM_TENANT_ID  | AZURE  | The tenant id of the Azure account  | |
| ARM_SUBSCRIPTION_ID  | AZURE  | The id of the Azure subscription  | |
| ARM_SUBSCRIPTION_NAME  | AZURE  | The name id of the Azure subscription  | |
| ARM_CLIENT_ID  | AZURE  | The client id of an application registration in Azure  | |
| ARM_CLIENT_SECRET  | AZURE  | The client secret of an application registration in Azure  | |
| ARM_RESOURCE_TYPE_SHORTCODE  | AZURE  | The shortcode of the resource type in Azure  | [Link](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-abbreviations)|

## Conventions

Below are how resources should be implemented and tagged.

|  Description | Category | Format | Example |
|---|---|---|---|
| Resource Tagging  | GENERAL  | environment={ENVIRONMENT_SHORTCODE};domain={DOMAIN};team={TEAM};organisation={ORGANISATION}; | ```tags = {environment  = var.environment organisation = var.organisation team         = var.team domain       = var.domain}``` |
| Azure resource groups  | AZURE  | {ENVIRONMENT_SHORTCODE}-{DOMAIN} |dev-whiskeyreviews |
| Azure resources that allow hyphens  | AZURE     | {ENVIRONMENT_SHORTCODE}-{DOMAIN}-{REGION_SHORTCODE}-{UNIQUE_NAMESPACE} | dev-whiskeyreviews-eun-hngc |
