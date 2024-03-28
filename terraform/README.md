# IaC with Terraform

In this directory, you can find the terraform files used for deploy the infrastructure in Google Cloud Platform.

## Files

- main.tf
    - It contains the code for deploying the infrastructure required.
        - GCS, BigQuery
- variables.tf
    - This file contains the variables that are applied on `main.tf`

## Adittional

You have to create a file called `vars.tfvars` and provide the values for `credentials` & `project`. Also, you can change the default value of `bq_dataset_name` & `gcs_bucket_name`.

Example

```sh
credentials="personal-gcp.json"
project="capsule-corporation-19841995"
bq_dataset_name="bq_victims_cdmx"
gcs_bucket_name="victims-cdmx-bucket"
```

## Steps

1. Be sure you have installed [terraform](https://developer.hashicorp.com/terraform/install?product_intent=terraform).
2. Creates `vars.tfvars`
3. Runs `terraform init`.
4. Runs `terraform plan -var-file="var.tfvars"`.
4. Runs `terraform apply -var-file="var.tfvars"`

If you run well all steps, terraform will deploy all the infrastructure.
