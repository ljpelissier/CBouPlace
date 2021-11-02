# CBouPlace

**Place chromebooks in an OU based on student's grade level.**

This script reads a csv created by the student information system that is placed 
on a network share which includes the grade level and chromebook serial number that the student is assigned.

The chromeooks are put into an OU in the Google admin panel based on school and graduating year.


What you need in place before using script:

  A csv file from your student information system with at least the following columns for each student.
  
    CBSerialNumber, SchoolYear, GradeLevel
    
    The file must have at least these columns using those headers. Other columns will be ignored.
    
  GAM installed on your system
  
  An OU structture that has a final OU ClassOfYYYY for each grade level
  

You will also need an config.ini file
There are two sections to this ini file.

The first section is unc path and filename for the csv with the data

The second lists the grade level as entered in the csv and the root of the ou where you would want the chromebooks stored.

The program will add ClassOfYYYY to the end of this root.

[hostpath]  
host = //hostIPaddres/path
file = filename.csv
[ouRoot]
04:/Chromebooks/StudentChromebooks/SchoolA/
05:/Chromebooks/StudentChromebooks/SchoolA/
06:/Chromebooks/StudentChromebooks/SchoolA/
07:/Chromebooks/StudentChromebooks/SchoolA/
08:/Chromebooks/StudentChromebooks/SchoolA/
01:/Chromebooks/StudentChromebooks/SchoolB/
02:/Chromebooks/StudentChromebooks/SchoolB/
03:/Chromebooks/StudentChromebooks/SchoolB/

For example the year 2020-21 the graduating class will have their chromebooks placed in the OU 

/Chromebooks/StudentChromebooks/SchoolA/ClassOf2021

If your school goes to 12th grade add lines to include those grades.

There is a YEAROFFSET constant in the python file that needs to be set for the upper grade level in the distrct.

Note: this has been writted for a small distrcit with one school per grade level. Additional data in the csv and logic in the script will be needed for use in districts with multiple schools at different levels.


