#!/bin/bash

# Create service account

oc login

oc project ${OPENSHIFT_PROJECT_NAME_DEV}
oc create sa pipeline
oc describe sa pipeline

oc project ${OPENSHIFT_PROJECT_NAME_PROD}
oc create sa pipeline
oc describe sa pipeline
