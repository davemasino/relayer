# relayer

A lightweight workflow engine in AWS. Work is in progress.

## Setup

Install the [serverless](https://www.serverless.com) framework.

Set the environment variable for your AWS profile name.

bash:

```bash
export AWS_PROFILE=<your profile name>
```

fish:

```fish
set -x AWS_PROFILE <your profile name>
```

## Test

```bash
pytest
```

## Deploy

```bash
sls deploy
```
