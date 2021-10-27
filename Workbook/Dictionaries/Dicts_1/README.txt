COPYRIGHT
=========
Copyright (C) 2019- Andrea Sterbini <sterbini@di.uniroma1.it>, 
                    Angelo Monti <monti@di.uniroma1.it>, 
                    Matteo Neri <matteo2794@outlook.com>

All programs and files contained in this archive / directory are released under the GPL v.3 license
(https://www.gnu.org/licenses/gpl-3.0.en.html)

INSTRUCTIONS
==========
To carry out the exercise, edit the program.py file using a text editor, better still an IDE.
Notepad ++, Atom, Spyder, PyCharm and other text editors are fine. 
DO NOT use Notepad, Word, Wordpad or other document editors.

TEST
====
This directory contains the files necessary to verify, on at least 3 input examples, that your program is correct. 
Before running the tests, if necessary, install Python and the necessary libraries (see below).

To check if your program works fine on the sample data: 
- open an Anaconda Prompt window and go to the exercise directory (using the cd command) 
- execute the command:
	python test.py
- otherwise
	pytest test.py

To obtain more detailed information on the execution (with an analysis of the time spent in the different parts of the program)
- run the command instead
	pytest -v -rA --profile test.py

SOLUTION
=========
A solution of our exercise is included in the directory. 
We advise you to examine it ONLY AFTER TRYING TO SOLVE THE EXERCISE BY YOURSELF.

INSTALLATION
=============
To be able to perform these tests or those of another exercise, install (must be done only once): 
- the Anaconda distribution in the version that contains Python 3.x (from https://www.anaconda.com/distribution/) 
- the following Python modules
   Open an Anaconda Prompt and execute the commands
	conda install -c conda-forge pytest
	conda install -c conda-forge ddt
	conda install -c conda-forge pytest-timeout
	conda install -c conda-forge pytest-profiling

