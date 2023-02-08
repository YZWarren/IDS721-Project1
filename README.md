# IDS721-Project1
[![Python application test with Github Actions](https://github.com/YZWarren/IDS721-Projects/actions/workflows/main.yml/badge.svg)](https://github.com/YZWarren/IDS721-Projects/actions/workflows/main.yml)

* [Link to my deployed version](https://k6kgjpm4zz.us-east-1.awsapprunner.com/)

This repo was originally aimed to deploy a GAN image generator via flask microservice, yet failed. Changed into a Calculator microservice.
All code run and tested both in codespace and Dockerfile

## Deploy with AWS app runner
1. In AWS App Runner console, click `Create Service`
2. Choose to deploy from `Source code repository`, fill in your github ID, repo name, and branch
3. Choose Deploy Settins as `Automatic` if you want Continuous Delivery on every push
4. Choose runtime as Python3, fill in `pip install -r requirements.txt` and `python app.py`
5. Fill in service name and change any other configurations if you want, create the service

## Deploy with Elastic Beanstalk
1. In EB console, go to `Applications`
2. Click `Create New Application`, complete the prompt for app name
3. Click `Create New Environment`, choose `Web Server Environment`
4. Choose `Docker` for `Platform specification`. Upload the zip file of your repo (Zip all files within the repo)
5. Create Environment with your Containerized code

## Goals checklist
- [x] build flask framework
- [x] have Makefile, requirements.txt, and makefile.yml for github Actions CI
- [x] Create a Microservice in Flask API to generate images with ACGAN
- [x] Configure Build System to Deploy changes
- [x] Deploy on AWS App Runner
- [x] Containerize app using docker


## Reference
https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html
