# Knitting Patterns Web App (Work in progress!)

This is a web application for saving and retrieving knitting pattern information. It is desingned to be used for storing planned future knitting projects and easily retrieving them based on what kind of yarn is available for use. 

**NOTE: Currently only backend infrastructure code implemented!**

## Description

The application has a web user interface with login. The web page includes a form for adding new knitting patterns and also a form for retrieving patterns from the database. 
The data will is stored in a DynamoDB database apart from image files, which are stored in a S3 bucket and referenced in the database table.
The application has a backend implemented using AWS CDK and Python and a frontend implemented using React and Typescript.

## Getting Started
### Dependencies
- You will need an AWS account and have AWS CLI installed.
- AWS CDK CLI
- Node.js
- Python 3.7 or later including `pip` and `virtualenv`
- TypeScript 3.8 or later (`npm -g install typescript`)
- Each AWS environment that you plan to deploy resources to must be bootstrapped.

### Executing program
First, in the kp-app-backend folder run:

`pip install -r requirements.txt`

To deploy your CDK stack to AWS CloudFormation using the CDK CLI, run the following in the kp-app-backend folder:

`cdk deploy`

To deploy the frontend, run the following in the kp-app-frontend folder:

`npm run dev`

