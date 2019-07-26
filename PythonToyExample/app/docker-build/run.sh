#!/bin/bash

git clone https://github.com/My-TRAC/ConfigurationScripts.git

chmod -R +x /opt/ConfigurationScripts/*.sh

#SYNCHRONIZING SCRIPTS
/opt/ConfigurationScripts/waitForSchemaRegistry.sh
/opt/ConfigurationScripts/waitForKafkaConenct.sh
/opt/ConfigurationScripts/waitForMySQL.sh

#CONNECTORS
/opt/ConfigurationScripts/setJDBCSourceConnector.sh\
    -c "cigo-jdbc-source_PythonTest"\
    -k $KAFKA_CONNECT_HOST\
    -n $SOURCE_TOPICS\
    -f "mytrac"\
    -m $MYSQL_HOST\
    -d $MYSQL_DATABASE\
    -u $MYSQL_USER\
    -p $MYSQL_PASSWORD\
    -i "mytrac_id"\
    -t "mytrac_last_modified" 

/opt/ConfigurationScripts/setJDBCSinkConnector.sh\
    -c "cigo-jdbc-sink_PythonTest"\
    -k $KAFKA_CONNECT_HOST\
    -s $SCHEMA_REGISTRY_HOST_NAME\
    -n $SINK_TOPICS\
    -m $MYSQL_HOST\
    -d $MYSQL_DATABASE\
    -u $MYSQL_USER\
    -p $MYSQL_PASSWORD\
    -pk "mytrac_id"\
    -ac "true"

#RUNNING OUR ALGORITHM
python3 /opt/src/pythonTest.py
