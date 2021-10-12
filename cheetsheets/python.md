# PYTHON

dir(time)

help(time.sleep)

type(time)

    #!/usr/bin/python3

    #!/usr/bin/env python3



    if __name__ == "main":
        main()
    
list []

dict {key:value}

tuple ()
    

try:

except:

else:

finally:

--- lambda

sqaure = lambda num:num **2

square(7)

list(map(lambda num:num **2.mynums))


# list comprehensions

new_list = [expression for member in iterable (if conditional)]

mylist = [x for x in 'word']

mylist

mylist = [x for x in range(0,1)]

mylist

    sentence = 'the rocket came back from mars'
    vowels = [i for i in sentence if i in 'aeiou']
    vowels
    ['e', 'o', 'e', 'a', 'e', 'a', 'o', 'a']


for item in list:

if:

elif:

else:


while

#---------------


functional concepts(map, reduce, filter, etc)


REPL

    #!/usr/bin/env python3


    pip3 list
    pip3 install
    pip3 uninstall
    pip3 freeze
    pip3 freeze > requirements.txt
    pip3 install --user -r requirements.txt
    pip3 uninstall -y -r requirements.txt 

    pip install --upgrade boto3

_this is file that has a list all the modules needed to execute your python source_

requirements.txt 

# this one i knew about kind of but now blows my mind. you create a source env with what
# whate ever version of python you are using. so if you are using 2.7 or 3.9 you can 
# make it kind of exclusive and with just the packages you installed with pip so it keeps
# your system a bit cleaner and pin point what packages are needed. 

virtualenv

# create 

python3 -m venv venvs/experiment

# source it

source venvs/experiement/bin/activate

# check source

pip3 list

# to return back to og commadline

deactivate

# verify

which python3

python --version

