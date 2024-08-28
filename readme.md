# Arthromate
_backend for the main arthromate app_

## Requirements
[AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)

## Build
```bash
sam build
```

## Deploy
```bash
sam deploy
```

## Group members
- Varun Nair
- Gul Tandon

## example _(for developer reference)_
```
{
    version: 1
    action: create/update/read/delete
    log: {
        usr_id: ...
        time: ...
        location: ...
        intensity: ...
        notes: ...
    }
}
```
