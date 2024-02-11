# AWS Contact List Project

This repository contains the CloudFormation template and associated resources for setting up an AWS infrastructure to host a contact list application.

## Description

The CloudFormation template in this repository provisions various AWS resources required for the contact list application, including:

- VPC with public subnets
- Internet Gateway for internet access
- Security groups for EC2 instances, RDS instance, and Elastic Load Balancer
- Elastic Load Balancer for distributing incoming traffic
- Auto Scaling Group for maintaining desired EC2 instance capacity
- RDS MySQL instance for storing contact data
- Route 53 Record Set for associating a domain name with the Elastic Load Balancer

## Prerequisites

Before deploying this CloudFormation template, ensure you have the following:

- An AWS account with appropriate permissions to create the resources defined in the template.
- AWS CLI installed and configured on your local machine.
- Basic understanding of AWS services and CloudFormation.

## Deployment Instructions

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/ziyaasici/ContactListProject.git