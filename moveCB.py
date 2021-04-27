"""
 author: Louis Pelssier
 python script will read year, grade and chromebook serial number from csv
 using the year and grade level will calculate graduation year and place
 the chromebook in the corresponding ou using GAM
 server location and school name will be contaned int config.ini
 see readme for details on config.ini
"""
import configparser
import os
import pandas as pd
import subprocess

#year offset based on grade level
#comment line 34 and uncomment line 32 to test
YEAROFFSET = 9  #9 for 8th grade 13 for High School

config = configparser.ConfigParser()
config.read('config.ini')

dataFrame =  pd.read_csv(config['hostpath']['hostPath'] + \
                        config['hostpath']['fileName'], index_col='StudentID')
dataFrame['CBSerialNumber'] = dataFrame['CBSerialNumber'].str.split(' ', expand=False).str[0]
dataFrame['GradeLevel'] = dataFrame['GradeLevel'].replace('KF','10')
dataFrame['GradYear'] = dataFrame['SchoolYear'].str[:4].astype('int') +\
                        YEAROFFSET - dataFrame['GradeLevel'].astype('int')
dataFrame['gamCommand'] = 'gam cros_sn ' + dataFrame['CBSerialNumber'] +\
                          ' update ou ' + dataFrame['GradeLevel'].map(config['ouRoot']) +\
                          'ClassOf' + dataFrame['GradYear'].astype('str')

#for gamCommand in dataFrame['gamCommand']:
#    if isinstance(gamCommand,str):
#        #print(gamCommand) #uncomment this line to see the gam command
#                           #comment out line below to run as test
#        os.system(gamCommand)

gamCommand = 'gam cros_ou "/Chromebooks/StudentChromebooks/Forrestdale/ClassOf2021" print cros fields serialnumber'
#chromebooksInOU = []
serialnumbersInOU = []
chromebooksInOU = subprocess.check_output(gamCommand)
print(type(chromebooksInOU))
print('printing ou data')
for cb in str(chromebooksInOU).split("\\r\\n"):
    serialnumbersInOU.append(cb.split(","))
for sn in serialnumbersInOU:
    print(sn[1])
