FROM jenkins/jenkins:lts
ENV PYTHON_VERSION="3.6.10"
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt
COPY casc.yaml /var/jenkins_home/casc.yaml
ENV CASC_JENKINS_CONFIG=/var/jenkins_home/casc.yaml
ARG JENKINS_ADMIN_ID
ARG JENKINS_ADMIN_PASSWORD
ENV JAVA_OPTS -Djenkins.install.runSetupWizard=false
USER root
RUN apt-get update && apt-get install -y lsb-release
USER root
RUN apt-get update
RUN apt-get install -y build-essential software-properties-common llvm cmake wget git nano nasm yasm zip unzip pkg-config \
    libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
RUN wget https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tar.xz \
    && tar xvf Python-${PYTHON_VERSION}.tar.xz \
    && rm Python-${PYTHON_VERSION}.tar.xz \
    && cd Python-${PYTHON_VERSION} \
    && ./configure \
    && make altinstall \
    && cd / \
    && rm -rf Python-${PYTHON_VERSION}
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip \
    && ./aws/install \
    && which aws 
RUN apt install python3-pip -y
RUN apt-get update && apt-get install make
RUN apt-get install jq -y
RUN pip install boto3
RUN wget "https://raw.githubusercontent.com/silinternational/ecs-deploy/develop/ecs-deploy" -O /usr/local/bin/ecs-deploy 
RUN chmod +x /usr/local/bin/ecs-deploy 
