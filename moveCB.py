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

#year offset based on grade level
YEAROFFSET = 9

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

for gamCommand in dataFrame['gamCommand']:
    if isinstance(gamCommand,str):
        #print(gamCommand) #uncomment this line to see the gam command
                           #comment out line below to run as test
        os.system(gamCommand)
  