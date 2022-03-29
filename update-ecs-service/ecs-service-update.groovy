pipeline {
    agent any
    parameters {
        string(name: 'region', defaultValue: 'us-west-2', description: 'Region in which Cluster is ')
        string(name: 'cluster_name', defaultValue: 'demoCluster', description: 'ECS Cluster Name')
        string(name: 'service_name', defaultValue: 'ecsmoazzam-demoService-qb1Y0U16kEgL', description: 'ECS Cluster Name')
    }
    stages {
        stage("Update ECS Service") {
            steps {
                sh "python3 ./update-ecs-service/update-ecs-service.py ${params.region} ${params.cluster_name} ${params.service_name}"
            }
        }

    }
}