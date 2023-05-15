# python-lambda-mongocluster-s3
Python script with mongodump binary to back up MongoDB Atlas database to AWS S3 bucket using AWS Lambda python function.

# Back up MongoDB (Atlas) to S3 through Lambda

Back up a MongoDB database to AWS S3 through a simple AWS Lambda function by using the mongodump binary.
Result is a ZIP archive with .bson and .metadata.json files for each collection.

For a **MongoDB Atlas cluster database** backup, specify the URI command option like this:

`--uri "mongodb+srv://[user]:[pass]@[host]/[name]"`

Adapted from [llangit/lambda-mongocluster-s3](https://github.com/llangit/lambda-mongocluster-s3).

`mongodump` binary is version 100.7.0 (mongodb-database-tools-amazon2-x86_64-100.7.0)

___

## Setup instructions

1. Clone this repository. 
2. Create a configuration file with your options, i.e. 
   ```bash
   ACCOUNT_ID=AWS_ACCOUNT_ID
   REGION=PREFERRED_AWS_REGION
   ROLE_ARN=arn:aws:iam::AWS_ACCOUNT_ID:ROLE_NAME
   FUNCTION_NAME=FUNCTION_NAME
   MEMORY=512
   TIMEOUT=300
   ZIP_FILENAME=ZIP_FILE_NAME
   S3_BUCKET=S3_BUCKET
   MONGODB_URI=mongodb+srv://{USERNAME}:{PASSWORD}@HOST/{DATABASE}?retryWrites=true&w=majority
   ```
3. Create an AWS Lambda function using the [Makefile](Makefile), i.e.
   ```bash
   make publish
   ```
   
## Environment variables

| Variable     | Description                                                                                                                                                                                                                                                          | Required?                        |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|
| MONGODB_URI  | Your mongodb connection string, for instance `"mongodb+srv://[user]:[pass]@[host]/[name]"` Refer to the [mongodump docs](https://docs.mongodb.com/database-tools/mongodump/) for a list of available options. Important: do not include the `--out` or `-o` option.  | Yes                              |
| S3_BUCKET    | Name of the S3 bucket                                                                                                                                                                                                                                                | Yes                              |
| ZIP_FILENAME | Name of the ZIP archive                                                                                                                                                                                                                                              | No. Default is `mongodb_backup`  |
