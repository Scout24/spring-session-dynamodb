FROM openjdk:8-jre

RUN /usr/bin/curl -L https://s3.eu-central-1.amazonaws.com/dynamodb-local-frankfurt/dynamodb_local_latest.tar.gz | /bin/tar xz

RUN apt-get update && apt-get install -y python3-pip python3 && pip3 install --upgrade awscli && apt-get clean all

ADD create_table.py .

RUN python3 create_table.py

ENTRYPOINT ["java", "-Djava.library.path=./DynamoDBLocal_lib", "-jar", "DynamoDBLocal.jar"]

CMD ["-help"]