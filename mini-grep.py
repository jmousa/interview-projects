
"""
Sudo code

  read the user input and determine if he is passing a file or entering the text to be searched from standard input
    if he is passing a file
        then read and check the argument he is passing using argv*
            if he is not passing the right number and type of argument
                then through an error
                exception handling ( please enter -e [-q] PATTERN [file...]
            if he is not passing the -q argument then 
                  search for the pattern he is passing and pull the line number along with it
                  (this will require some code)
            else  search for the pattern he is passing without pulling the line number 
                    this could be a simple operation like the below code

       else he is not passing a file and he is entering the text to be searched on the standard input
            then read the input into a file and repeat the above
        
at a minimum you will need the following utilities 

import re
import sys
and maybe some something else like
import os                                
    
"""

import re
import os
import sys

with open(sys.argv[3], "r") as input_file:

    for line in input_file:

        if re.search(sys.argv[2], line):

            print(line)
