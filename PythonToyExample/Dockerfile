FROM python:3

#INSTALL REQUIRED LIBRARIES
#RUN pip install time datetime


#COPY REQUIRED FILES
COPY src /opt/src
RUN chmod -R +x /opt/src
WORKDIR /opt/src


CMD ["python","/opt/src/printDate.py"]
