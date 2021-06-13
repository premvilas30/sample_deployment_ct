# Demo Devops application

This application demonstrates how to build, test & deploy a flask python app to Docker Hub then run a k8s deployement load balanced by k8s service on a k8s cluster.

## Prerequisites

We would need following :
  - K8s cluster where application can be deployed.

## Steps to deploy

In order to deploy the application logon to your cluster node and use deployment.yaml to deploy the application there.

Command to deploy the application: 
  
  `kubectl deploy -f deployment.yaml`
  
Once the application is deployed you can check the deployed service which acts a load balancer for the application using below command: 
  
  `Kubectl describe svc flask-service`

from the output look for IP and PORT entities and their values:
Now run below command to get response from application: 
  
  `curl http://<IP>:<PORT>` 
  
