pipeline {
    agent any
    parameters {
        string(name: 'region', defaultValue: 'us-west-2', description: 'Region in which Cluster is ')
        string(name: 'asg_name', defaultValue: 'ecsmoazzam-EcsInstanceAsg-RM43ZSY3MM6L', description: 'Auto Scaling Name')
        string(name: 'asg_minhealthy_percentage', defaultValue: '50', description: 'ASG Minimum health percentage')
        string(name: 'asg_instance_warmup', defaultValue: '10', description: 'ASG Minimum Instance Warm-up Time in sec')

    }
    stages {
        stage("Update ECS Service") {
            steps {
                sh "python3 ./update-ecs-service/update-ecs-service.py ${params.region} ${params.asg_name} ${params.asg_minhealthy_percentage} ${params.asg_instance_warmup}"
            }
        }

    }
}