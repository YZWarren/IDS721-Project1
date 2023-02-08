# IDS721-Projects
[![Python application test with Github Actions](https://github.com/YZWarren/IDS721-Projects/actions/workflows/main.yml/badge.svg)](https://github.com/YZWarren/IDS721-Projects/actions/workflows/main.yml)
This repo records all projects and progress did in IDS721 at Duke.
All code run and tested in codespace

## Deploy with Elastic Beanstalk CLI
0. need to include `awsebcli` in requirements.txt 

1. build environment with python 3.8

```conda create -n proj1 python=3.8```

2. Initialize your EB CLI repository with the eb init command:

```eb init -p python-3.8 flaskGANplayground --region us-east-1```

3. Create an environment and deploy your application to it with eb create:

```eb create flaskGan-env```


## Goals checklist
- [x] build flask framework
- [x] have Makefile, requirements.txt, and makefile.yml for github Actions CI
- [x] Create a Microservice in Flask API to generate images with ACGAN
- [ ] Optimize page rendering
- [ ] Configure Build System to Deploy changes
- [ ] Deploy on AWS App Runner


## examples
![](assets/example_chatgpt.png)

## Reference
https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html
