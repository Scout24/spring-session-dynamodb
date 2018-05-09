from __future__ import print_function
from subprocess import ( check_call,
                         check_output )
from multiprocessing import Process
from time import sleep

run_server = lambda: check_call("java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -port 7777 -sharedDb", shell=True)
create_table = lambda: check_output("AWS_SECRET_ACCESS_KEY='' AWS_ACCESS_KEY_ID='' AWS_SECRET_KEY='' aws dynamodb create-table --region eu-west-1 --table-name Sessions --attribute-definitions AttributeName=SessionID,AttributeType=S --key-schema AttributeName=SessionID,KeyType=HASH --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1 --endpoint-url http://localhost:7777", shell=True)

if __name__ == '__main__':
    server = Process(target=run_server)
    server.start()
    sleep(3)
    print(create_table())
    sleep(3)
    server.terminate()
