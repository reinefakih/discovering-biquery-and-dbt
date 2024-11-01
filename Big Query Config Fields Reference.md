# Big Query Config Fields Reference:

## Main Parameters: 

| Field                                                        | Type   | Property Name    |
| ------------------------------------------------------------ | ------ | ---------------- |
| Project ID                                                   | String | project_id       |
| Dataset Location                                             | String | dataset_location |
| Default Dataset ID                                           | String | dataset_id       |
| Loading Method                                               | Object | loading_method   |
| Service Account Key JSON (Required for cloud, optional for open-source) | Object | credentials      |

### Loading Method Object:

#### If method is Batched Standard Inserts:

| Property Name | Type   | Input      |
| ------------- | ------ | ---------- |
| method        | String | "Standard" |

#### If method is GCS Staging:

| Property Name                       | Type     | Input                                                        |
| ----------------------------------- | -------- | ------------------------------------------------------------ |
| method                              | String   | "GCS Staging"                                                |
| gcs_bucket_name                     | String   | name of the Google Cloud Storage (GCS) bucket                |
| gcs_bucket_path                     | String   | path within the specified GCS bucket where temporary data files will be stored |
| credential                          | Object   | HMAC key                                                     |
| keep_files_in_gcs-bucket (optional) | "String" | `"Delete all tmp files from GCS"` (default)<br>`"Keep all tmp files in GCS"` |

### Service Account Key Object:

| Property Name        | Type   | Input                                  |
| -------------------- | ------ | -------------------------------------- |
| auth_type            | String | "Service"                              |
| service_account_info | String | JSON object containing the credentials |

## Advanced Parameters:

| Field                                                   | Type    | Property Name                   | Defaults         |
| ------------------------------------------------------- | ------- | ------------------------------- | ---------------- |
| Transformation Query Run Type                           | String  | transformation_priority         | interactive      |
| Google BigQuery Client Chunk Size <br>(MIN=1, MAX = 15) | Integer | big_query_client_buffer_size_mb | 15               |
| Raw Table Dataset Name                                  | String  | raw_data_dataset                | airbyte_internal |
| Disable Final Tables                                    | Boolean | disable_type_dedupe             | False            |

