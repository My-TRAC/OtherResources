There are two folders:

    app: it contains a folder 'src', with the sourcecode, and a folder 'docker-build' with the required information to build the docker.
    deployments: with the files to deploy the docker with docker-compose.

app/src/pythonTest.py:

    It creates a table called 'employees'.
    It reads a table called 'ratings'.

app/docker-build:

    Dockerfile: The file that describes the creation of the docker. It uses as base "python:3", install several required packages, and copies the required files that will be run when the docker is being deployed (i.e. sourcecode src/pythonTest.py and run.sh)
    run.sh: Is the file that the docker runs when is deployed. Is the flow of instruction that will be run at deployment time:

        It downloads from git a set of Configurations Scripts: git clone https://github.com/My-TRAC/ConfigurationScripts.git
        run.sh is written to use 5 of theses scripts:

            Scripts to guarantee that My-TRAC Platform is running and ready:

                waitForSchemaRegistry.sh in SCHEMA_REGISTRY_HOST_NAME
                waitForKakfkaConenct.sh in KAFKA_CONNECT_HOST

            Script to guarantee that the local MySQL in MYSQL_HOST is ready
            Kafka Connectors:

                setJDBCConnector.sh: This will set a source connector that will guarantee that the table 'employees' created by pythonTest.py creates a topic 'employees' within My-TRAC Platform, and that for each tuple within the table, a message of the topic 'employees' is created, and thus, it can be used by other modules.

                setJDBCSinkConnector.sh: This will set a sink connector that reads the messages within the topic SINK_TOPICS in My-TRAC Platform and creates a table in MYSQL_HOST with the corresponding information.

o        Calls pythonTest.py

         

    publish_docker_image.sh: Builds the docker and now is ready to be deployed. If docker-machine is required (OSX systems) it has to be built within the docker-machine environment.

deployments/docker-compose/docker-compose.yml:

    It deploys 2 dockers:

        mysql_python: the local mysql docker that the pythonTest.py is communicating with.
        python_test: the docker that runs pythonTest.py we have previously built. The deployment of this docker set previously mentioned variables:

            SCHEMA_REGISTRY_HOST_NAME: schema-registry (is the name taken when deploying My-Trac Platform; see here)
            KAFKA_CONNECT_HOST: kafka-connect (idem)
            MYSQL_HOST: mysql_python (name that we have given to the local mysql)
            SINK_TOPICS: "ratings" (in this way we are subscribing to ratings messages within My-TRAC Platform. So whenever a message within the ratings topic is created in My-TRAC Platform, it will be automatically inserted in a table called ratings within the local mysql.
