#!/bin/bash

git clone https://github.com/My-TRAC/ConfigurationScripts.git

chmod -R +x /opt/ConfigurationScripts/*.sh


/opt/ConfigurationScripts/waitForSchemaRegistry.sh
/opt/ConfigurationScripts/waitForKafkaConenct.sh
/opt/ConfigurationScripts/waitForMySQL.sh
/opt/ConfigurationScripts/setJDBCSinkConnector.sh cigo-jdbc-sink_PythonTest
/opt/ConfigurationScripts/setJDBCConnector.sh cigo-jdbc-source_PythonTest mytrac ratings


python3 /opt/src/printDate.py
