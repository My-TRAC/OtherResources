FROM python:3


RUN apt-get update && apt-get install -y mysql-client


#INSTALL REQUIRED LIBRARIES
RUN pip3 install mysql-connector-python
RUN pip3 install chmod


#COPY REQUIRED FILES
COPY run.sh /opt
RUN chmod -R +x /opt/run.sh

COPY src /opt/src
COPY scripts /opt/scripts
RUN chmod -R +x /opt/src


WORKDIR /opt


#CMD ["python","/opt/src/printDate.py"]
ENTRYPOINT ["/opt/run.sh"]
CMD [""]
