#!/bin/bash

echo "Build frontend image"
docker build -t frontend:latest frontend

echo "Push frontend image on local registry"
docker tag frontend lx-8-9:5000/frontend:latest
docker push lx-8-9:5000/frontend:latest

echo "Deploy frontend"
kubectl apply -f deployment-frontend.yaml
kubectl apply -f svc-frontend.yaml

echo "Frontend is now available on http://localhost:30001"
