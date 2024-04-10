# python version to run the program
FROM python:3.11

# main code name and its directory
ADD main.py .

# the module to be installed so that the scritps works: create a requirement.txt
RUN pip install prettytable numpy

# how to run the program
CMD [ "python","./main.py" ]
