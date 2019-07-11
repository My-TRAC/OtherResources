#!/bin/bash

git clone https://github.com/My-TRAC/ConfigurationScripts.git

chmod -R +x /opt/ConfigurationScripts/*.sh


/opt/ConfigurationScripts/waitForSchemaRegistry.sh
/opt/ConfigurationScripts/waitForKafkaConenct.sh
/opt/ConfigurationScripts/waitForMySQL.sh
#/opt/ConfigurationScripts/setJDBCSinkConnector.sh cigo-jdbc-sink_PythonTest


/opt/ConfigurationScripts/setJDBCSourceConnector.sh   -c "cigo-jdbc-source_PythonTest" \ 
                                                -n "employees"
                                                -f "mytrac" \  
                                                -k $KAFKA_CONNECT_HOST \
                                                -m $MYSQL_HOST \
                                                -d $MYSQL_DATABASE \
                                                -u $MYSQL_USER \
                                                -p $MYSQL_PASSWORD \
                                                -i "id" \
                                                -t "timestamp" 

                                                
                                                
                                              


python3 /opt/src/pythonTest.py
