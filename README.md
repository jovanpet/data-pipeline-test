# data-pipeline-apache-airflow
# Practice pipeline for AMS Dev Certification Exam - Using Apache Airflow

## Introduction

I've built data pipelines before using DataBricks for my previous job but never used AWS and Apache for this :D
I don't think I have a preference but I also don't have real use for pipelines in my mini projects.
Could defiantly see these kind of processes being important in large scale Data processing.

## Twitter ELT and DAG

I never used Twitter API, note, there are almost no useful free APIs available. I decided to track my profile data and just save it to a .csv file. Worked well :D
The DAG file is a basic copy of what says on Apache Airflow. There is definitely more complex things you can do.

## EC2 and S3 bucket

I decided to use AWS EC2 instance to run my code on. This was done by installing apache and copying the following code onto the instance when I SSHed into it. S3 bucket was there to store my .csv files. I have been preparing for AWS Dev exam and thought this would be a useful exercise for the actual exam.
