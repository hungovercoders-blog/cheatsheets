---
key: value
---

<header class="site-header">
  <a href="https://blog.hungovercoders.com"><img alt="hungovercoders" src="../assets/logo3.ico"
    width=50px align="left"></a>
</header>

# Configuration

- [Configuration](#configuration)
  - [Variables](#variables)
    - [Rules](#rules)
    - [Values](#values)
    - [Dynamic Values](#dynamic-values)
  - [Conventions](#conventions)
  - [Variables Implementation](#variables-implementation)
    - [Local](#local)
    - [Gitpod](#gitpod)
    - [Github](#github)
      - [Codespaces](#codespaces)
      - [Actions](#actions)
    - [Terraform](#terraform)
  - [Events](#events)
    - [Topic Naming](#topic-naming)
      - [Rough Examples](#rough-examples)
    - [Event format](#event-format)


## Variables

### Rules

Variables are consistently used as environment variables as a developer and in all platforms.
The names of the variables should be **UPPER_CASE** with underscores denoting spaces.
The values of the variables should be **lowercase**.
The values should contain **no spaces**.

### Values

|  Name | Category | Scope | Description | Examples |
|---|---|---|---|---|
| ORGANISATION  | General  | Organisation | The name of the organisation.  | ['datagriff', 'hungovercoders', 'dogadopt', 'starwalks'] |
| UNIQUE_NAMESPACE  | General  | Organisation| The unique four character namespace of the organisation. This is used in resources to make them more likely to be globally unique. | ['dgrf', 'hngc', 'dgad', 'stwa'] |
| ENVIRONMENT  | General  | Environment | The name of the environment that the resource exists.  | ['development', 'uat', 'production'] |
| TEAM  | General  | Team | The name of the team. | ['whiskey', 'dogwalk', 'dogrescue'] |
| DOMAIN  | General  | Domain | The name of the domain that the resource belongs to. | ['platform', 'whiskeyreviews', 'dogwalkscheduling'] |
| ARM_TENANT_ID  | Azure  | Organisation | The tenant id of the Azure account  | |
| ARM_REGION  | Azure  | Organisation | The region that resources are deployed to.  | ['northeurope', 'westeurope'] |
| ARM_SUBSCRIPTION_ID  | Azure  | Environment and team or organisation | The id of the Azure subscription  | |
| ARM_SUBSCRIPTION_NAME  | Azure  | Environment and team or organisation  | The name id of the Azure subscription  | |
| ARM_CLIENT_ID  | Azure  | Environment and team or organisation  | The client id of an application registration in Azure  | |
| ARM_CLIENT_SECRET  | Azure  | Environment and team or organisation  | The client secret of an application registration in Azure  | |

### Dynamic Values

|  Name | Category | Scope | Description | Examples |
|---|---|---|---|---|
| ENVIRONMENT_SHORTCODE  | General  | Environment  | The shortcode of the environment that the resource exists. This is derived from the ENVIRONMENT variable.  | ['dev', 'uat', 'prd'] |
| ARM_REGION_SHORTCODE  | Azure |  Organisation | The shortcode of the region the resource belongs to.  | ['eun', 'euw'] |
| ARM_RESOURCE_TYPE_SHORTCODE  | Azure | Resource  | The shortcode of the resource type in Azure. This is derived from the Azure resource type.  | [Link](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-abbreviations) |

## Conventions

Below are how resources should be implemented and tagged.

|  Description | Category | Format | Example |
|---|---|---|---|
| Resource Tagging  | GENERAL  | environment={ENVIRONMENT_SHORTCODE};domain={DOMAIN};team={TEAM};organisation={ORGANISATION}; | ```tags = {environment = var.environment organisation = var.organisation team = var.team domain = var.domain}``` |
| Azure resource groups  | AZURE  | {ENVIRONMENT_SHORTCODE}-{DOMAIN}-{UNIQUE_NAMESPACE} | dev-whiskeyreviews-hngc |
| Resources that allow hyphens  | CLOUD | {ENVIRONMENT_SHORTCODE}-{DOMAIN}-{REGION_SHORTCODE}-{UNIQUE_NAMESPACE} | dev-whiskeyreviews-eun-hngc |
| Resources that don't allow hyphens  | CLOUD | {ENVIRONMENT_SHORTCODE}-{DOMAIN}-{REGION_SHORTCODE}-{UNIQUE_NAMESPACE} | devwhiskeyreviewseunhngc |

## Variables Implementation

### Local

### Gitpod

### Github

#### Codespaces

#### Actions

### Terraform

|  Name | Category | Description | Construction | Examples |
|---|---|---|---|---|
| TF_VAR_team | General | This is the name of the team that owns the terraform resource | export TF_VAR_team=$TEAM | ["hungovercoders","datagriff","dogadopt"] |
| TF_VAR_domain | General | This is the name of the domain the terraform resource belongs to | export TF_VAR_domain=$DOMAIN | ['platform', 'whiskeyreviews', 'dogwalkscheduling'] |
| TF_BACKEND_RESOURCE_GROUP | Azure | This is the name of the resource group that contains the storage account that holds the state of resources | TF_BACKEND_RESOURCE_GROUP="state-rg-$UNIQUE_NAMESPACE" | ["state-hngc","state-dgrf","state-dgad"] |
| TF_BACKEND_STORAGE_ACCOUNT | Azure | This is the name of the storage account that holds the state of resources | TF_BACKEND_STORAGE_ACCOUNT="statesa$UNIQUE_NAMESPACE" | ["statehngc","statedgrf","statedgad"] |
| TF_BACKEND_CONTAINER | Azure | This is the name of the storage account container that holds the state of resources in the correct environment | TF_BACKEND_CONTAINER=$ENVIRONMENT | ["development","uat","production"] |
| TF_VAR_environment | Azure | This is the name of the environment that the terraform resource is going to be deployed to | export TF_VAR_environment=$ENVIRONMENT | ["development","uat","production"] |
| TF_VAR_unique_namespace | Azure | This is the name of the unique organisational namespace that the terraform resource will belong to and act as a postfix to resources | export TF_VAR_unique_namespace=$UNIQUE_NAMESPACE | ["hngc","dgrf","dgad"] |
| TF_VAR_organisation | Azure | This is the name of the organisation that owns the terraform resource | export TF_VAR_organisation=$ORGANISATION | ["hungovercoders","datagriff","dogadopt"] |
| TF_VAR_region | Azure | This is the name of the Azure region that the terraform resource will deploy to| export TF_VAR_region=$ARM_REGION | ["northeurope","westeurope"] |

## Events

### Topic Naming

- Adopted {domain}.{eventtype}.{eventname}.{version} as adopted from [here](https://medium.com/inavitas/kafka-topic-naming-be16a51ef2c0).

#### Rough Examples

- booze.fct.whiskeyreviewed.v1
- booze.cdc.pub.v1
- dogrescue.fct.adoptionlead.v1
- dogwalkscheduling.cdc.dogwalk.v1

### Event format

- [Cloud Events](https://cloudevents.io/)