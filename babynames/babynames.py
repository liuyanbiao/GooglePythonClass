#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def readFile(filename):
  f = open(filename, 'r')
  dic = f.read()
  f.close()

  year = re.search(r'Popularity\sin\s\d\d\d\d', dic).group().split()
  
  info = re.findall(r'<td>\d+</td><td>\w+</td><td>\w+</td>', dic)
  newlist = [] 
  for i in info:
    i=i.replace("<td>", " ")
    i=i.replace("</td>"," ")
    newlist.append(i)

  dic_names = {}
  for i in newlist:
    names = i.split()
    dic_names[names[1]+" "+names[2]] = int(names[0])

  return dic_names


def get_key(tuple):
  return tuple[-1]

def write_file(filename, dic):
  f = open(filename, 'w')

  list=sorted(dic.items(),key=get_key,reverse=True)
  
  for i in list:
    f.write(str(i[1])+":"+i[0]+"\n")

  f.close() 

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  nameinfo = readFile(filename)


  write_file(filename+".summary",nameinfo)


  return 


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
  #  del args[0]
    for i in range(1,len(args)):
      extract_names(args[i])     
  
  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
 # extract_names(args[1])
if __name__ == '__main__':
  main()
