#!/usr/bin/env bash
# Defining all varibales
APP_NAME="PAYTM"
APP_ENV="PRODUCTION"
CLUSTER_REGION="US-EAST-1"
INSTANCE_COUNT=5
DEPLOYMENT_ID="${APP_ENV}_${APP_NAME}_release"
echo "====================================="
echo "STARTING DEPLOYMENT"
echo "====================================="
echo "Application : $APP_NAME"
echo "Target Env  : $APP_ENV"
echo "Region      : $CLUSTER_REGION"
echo "Instances   : $INSTANCE_COUNT"
echo "Deployment ID  : $DEPLOYMENT_ID"

