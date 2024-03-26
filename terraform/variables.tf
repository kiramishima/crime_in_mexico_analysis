variable "credentials" {
  description = "GCP Credentials"
  #ex: if you have a directory where this file is called keys with your service account json file
  # saved there as my-creds.json you could use default = "./keys/my-creds.json"
}


variable "project" {
  description = "Project ID"
  #ex: You can find you project id on you gcp account
}

variable "region" {
  description = "Region"
  #Update the below to your desired region
  default = "us-central1"
}

variable "location" {
  description = "Project Location"
  #Update the below to your desired location
  default = "US"
}

variable "bq_dataset_name" {
  description = "BigQuery Name"
  #Update the below to what you want your dataset to be called
  default = "bq_crimes_mexico_city"
}

variable "gcs_bucket_name" {
  description = "Storage Bucket Name"
  #Update the below to a unique bucket name
  default = "crimes-mexico-city-bucket"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}