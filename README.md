# CBouPlace

**Place chromebooks in an OU based on student's grade level.**

This script reads a csv created by the student information system that is placed 
on a network share which includes the grade level and chromebook serial number that the student is assigned.


What you need in place before using script:

  A csv file from your student information system with at least the following columns for each student.
  
    **_CBSerialNumber, SchoolYear, GradeLevel_**
    
    The file must have at least these columns using those headers. Other columns will be ignored.
    
  GAM installed on your system
  
The chromeooks are put into an ou based on school and graduating year.


