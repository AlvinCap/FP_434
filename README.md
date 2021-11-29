# Final Project -- BE434 

# INTRODUCTION: 
# Create a python program called Seasons; that will allow the user to input a picture text file and make a judgement on whether the season is spring/summer, fall, winter based on color distrbutions. 

# Application Examples: 
# Weather Station building softawre to filter and feed the photo stream of user uploaded content by seasons. 
# Private Company running data anlysis on photo dumps to draw links and parallels between associated seasons and photo content. 

# Parameters for the program include: 
# -p: --picture: picture text file that the user must provide for the program to run; no default 
# -o: --output: output text file that contains the response to the season inqury, is optional and can be ommitted by user. Text then displays in command line terminal. 

# The usage the program should print for -h or --help:
<!-- 
$ ./seasons.py -h
usage: seasons.py [-h] [p] [-o file]

Seasons

optional arguments:
  -h, --help       show this help message and exit
  -o file, --output file  File (default: None) -->


# When run with no file argument, it should print an error :
# "No such file or directory:"
# The arguement parser is setup such that the program should error out for a bad file input.
# The program will on good input, scan and verify the color distribution levels in the file provided and display a mini summary statement for the findings that will ultimately power the prediction.
# The program will handle much of workload behind the user interface and will work to simply output a season as a preliminary anlaysis tool. 


# The program should pass all tests:
<!-- $ make test
pytest -xv test.py
============================= test session starts ==============================
...
collected 5 items

test.py::test_exists PASSED                                              [  25%]
test.py::test_usage PASSED                                               [ 50%]
test.py::test_no_input PASSED                                            [ 75%] -->
<!-- test.py::test_outputval PASSED                                           [ 100%] -->
# -------------------------------------------------
## Author 
# Alvin Onyango 