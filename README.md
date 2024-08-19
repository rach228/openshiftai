### Setup
1. Provisioned Red Hat OpenShift Service on AWS (ROSA)
2. Installed Standard OpenShift AI Cloud Service (RHOAI) and DataScienceCluster custom resource
3. Added a Machine Pool: g4dn.12xlarge worker node
4. Installed Node Feature Discovery operator and NodeFeatureDiscovery custom resource
5. Installed NVIDIA GPU operator and ClusterPolicy custom resource
6. Installed OpenShift Serverless operator and KnativeServing custom resource
7. Installed OpenShift Service Mesh operator and ServiceControlPlane custom resource
8. Installed OpenShift Pipelines operator

### Deploy MinIO to store training data and model files
1. Create a Data Science project in RHOAI, e.g. `demo`.
2. In ROSA, navigate to the `demo` project. Create a S3-compatible storage server, MinIO, using the `/yaml/minio.yaml` manifest file.
3. In ROSA, navigate to Networking > Routes. Login to MinIO console and create a bucket, e.g. `test`.
4. In RHOAI, under the `demo` project created earlier, and add a new data connection, e.g. `test-dc`.
5. In the same project, create a workbench, e.g. `test-wb`.
6. Open the `test-wb` workbench when the status is 'Running'.

### Create Elyra Pipeline to automate MLOps
1. In RHOAI, navigate to the `demo` project. Under the Pipelines tab, create a pipeline server. Click on the key icon to auto-fill in the fields based on the `test-dc`.
2. Open the `test-wb` workbench
3. On the Launcher view, click Elyra and rename pipeline, e.g. `test-pipeline`.
4. Open Panel and add Kubernetes Secrets (to use data connection) and choose appropriate Generic Node Defaults for Runtime Image. (Note: If you create the RHOAI data connection from the RHOAI dashboard, then the secret name is always preceded by aws-connection-)
5. Drag and drop files to the visual pipeline editor and connect them.
6. Right click the node to Open properties to configure output files.
7. Save `test-pipeline` pipeline.
8. Run `test-pipeline` pipeline.
9. In RHOAI, go to Experiments > Experiments and runs to check the status of the pipeline.
10. In the MinIO bucket, directory <pipeline-name-timestamp> is created and stores dependencies, log files, and output files of each node from each pipeline run.

### Deploy Model with vLLM runtime
1. 

### Deploy Milvus and MongoDB
1. 
