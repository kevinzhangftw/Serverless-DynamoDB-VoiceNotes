# For VoiceNotes
DynamoDB store with serverless

# Endpoints
  POST - `https://ghjn9h71oj.execute-api.us-east-1.amazonaws.com/dev/voicenotes`
  
  GET - `https://ghjn9h71oj.execute-api.us-east-1.amazonaws.com/dev/voicenotes/{id}`
  
  
  GET - `https://ghjn9h71oj.execute-api.us-east-1.amazonaws.com/dev/voicenotes`
  
  DELETE - `https://ghjn9h71oj.execute-api.us-east-1.amazonaws.com/dev/voicenotes/{id}`
  
# functions
  ## create: voicenotes-dynamodb-dev-create
  ## list: voicenotes-dynamodb-dev-list
  ## get: voicenotes-dynamodb-dev-get
  ## delete: voicenotes-dynamodb-dev-delete
  
# Example
## To Write to VoiceNotes
```
curl -X POST https://ghjn9h71oj.execute-api.us-east-1.amazonaws.com/dev/voicenotes --data '{ "text": "getting demo ready for james and jon" }'
```
## To Read a Note given timestamp
```
curl https://ghjn9h71oj.execute-api.us-east-1.amazonaws.com/dev/voicenotes/1530566080974
```
## (DEBUG)To Read all The Notes from VoiceNotes
```
curl https://ghjn9h71oj.execute-api.us-east-1.amazonaws.com/dev/voicenotes
```
