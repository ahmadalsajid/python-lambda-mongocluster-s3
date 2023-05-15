.PHONY: archive publish

include config.mk

clean:
	rm -rf lambda_function.zip

archive: clean
	zip -9 lambda_function.zip lambda_function.py
	#zip -9 lambda_function.zip lambda_function.py mongodump

deletefunction:
	aws lambda delete-function \
	--function-name ${FUNCTION_NAME}

pushfunction:
	aws lambda create-function \
	--region $(REGION) \
	--function-name $(FUNCTION_NAME) \
	--zip-file fileb://lambda_function.zip \
	--role $(ROLE_ARN) \
	--handler lambda_function.lambda_handler \
	--runtime python3.10 \
	--description "Python script with mongodump binary to backup MongoDB Atlas database to AWS S3 bucket using AWS Lambda python function." \
	--timeout $(TIMEOUT) \
	--memory-size $(MEMORY) \
	--environment "Variables={MONGODB_URI=$(MONGODB_URI),S3_BUCKET=$(S3_BUCKET)}"


publish: archive pushfunction