import argparse
import pandas as pd
import sys, os

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", dest = "filename", action="store", help="the file to load the data from", required=True)

args = sys.argv[1:]

arguments = parser.parse_args(args)
print arguments.filename
dataFrame = pd.read_csv(arguments.filename)


privateTransportDF =  dataFrame[(dataFrame.g=="Cotxe") | (dataFrame.g=="Bicicleta") | (dataFrame.g=="Moto")]
publicTransportDF = dataFrame[~dataFrame.index.isin(privateTransportDF.index)]

HcountPrivate = len(privateTransportDF.loc[privateTransportDF['at']=="Home"].index)
DcountPrivate = len(privateTransportDF.loc[privateTransportDF['at']=="Dona"].index)



print "Private Transport Men " + str(HcountPrivate*1.0/(HcountPrivate+DcountPrivate) * 100)
print "Private Transport Women " + str(DcountPrivate*1.0/(HcountPrivate+DcountPrivate) * 100)


v18Private =  len(privateTransportDF.loc[privateTransportDF['au']==18].index)
v25Private =  len(privateTransportDF.loc[privateTransportDF['au']==25].index)
v35Private =  len(privateTransportDF.loc[privateTransportDF['au']==35].index)
v45Private =  len(privateTransportDF.loc[privateTransportDF['au']==45].index)
v55Private =  len(privateTransportDF.loc[privateTransportDF['au']==55].index)
v65Private =  len(privateTransportDF.loc[privateTransportDF['au']==65].index)

totalAgePrivate = (v18Private + v25Private + v35Private+ v45Private + v55Private + v65Private)*1.0

print "18-24 " + str(v18Private/totalAgePrivate*100) + "%" 
print "25-34 " + str(v25Private/totalAgePrivate*100) + "%" 
print "35-44 " + str(v35Private/totalAgePrivate*100) + "%" 
print "45-54 " + str(v45Private/totalAgePrivate*100) + "%" 
print "55-64 " + str(v55Private/totalAgePrivate*100) + "%" 
print ">65   " + str(v65Private/totalAgePrivate*100) + "%" 


HcountPublic = len(publicTransportDF.loc[publicTransportDF['at']=="Home"].index)
DcountPublic = len(publicTransportDF.loc[publicTransportDF['at']=="Dona"].index)

print "Public Transport Men " + str(HcountPublic*1.0/(HcountPublic+DcountPublic) * 100)
print "Public Transport Women " + str(DcountPublic*1.0/(HcountPublic+DcountPublic) * 100)


v18Public =  len(publicTransportDF.loc[publicTransportDF['au']==18].index)
v25Public =  len(publicTransportDF.loc[publicTransportDF['au']==25].index)
v35Public =  len(publicTransportDF.loc[publicTransportDF['au']==35].index)
v45Public =  len(publicTransportDF.loc[publicTransportDF['au']==45].index)
v55Public =  len(publicTransportDF.loc[publicTransportDF['au']==55].index)
v65Public =  len(publicTransportDF.loc[publicTransportDF['au']==65].index)

totalAgePublic = (v18Public + v25Public + v35Public+ v45Public + v55Public + v65Public)*1.0

print "18-24 " + str(v18Public/totalAgePublic*100) + "%" 
print "25-34 " + str(v25Public/totalAgePublic*100) + "%" 
print "35-44 " + str(v35Public/totalAgePublic*100) + "%" 
print "45-54 " + str(v45Public/totalAgePublic*100) + "%" 
print "55-64 " + str(v55Public/totalAgePublic*100) + "%" 
print ">65   " + str(v65Public/totalAgePublic*100) + "%" 



totalPrivate = HcountPrivate+DcountPrivate
totalPublic =  HcountPublic+DcountPublic
total= HcountPrivate+DcountPrivate+HcountPublic+DcountPublic

print "Total Private " + str((totalPrivate*1.0)/total*100) 
print "Total Public " + str((totalPublic*1.0)/total*100) 
