#!/usr/bin/env python

from optparse import OptionParser
import os
import time
import re

start_time = time.clock()

regex = re.compile(("([a-z0-9!#$%&*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`"
                    "{|}~-]+)*(@|\sat\s)(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?(\.|"
                    "\sdot\s))+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)"))

def file_to_str(filename):
    with open(filename) as f:
        return f.read().lower() # Case is lowered to prevent regex mismatches.

def get_emails(s):
    return (email[0] for email in re.findall(regex, s) if not email[0].startswith('//'))

def writeFile(fileToWrite, listData):
    with open(fileToWrite, 'w') as f:
        for item in listData:
            f.write("%s\n" % item)

def unic_mails(mails, outfile):
    print len(mails), 'emails collected'
    uniqEmail = set(listEmail)
    print len(uniqEmail), 'uniq emails' 

    outfile = outfile + '/result.txt'
    print 'saving to ' , outfile
    writeFile(outfile, uniqEmail)
    return

listEmail = []

if __name__ == '__main__':
    parser = OptionParser(usage="Usage: python %prog [DIR]...")
    options, args = parser.parse_args()

    if not args:
        parser.print_usage()
        exit(1)

    for arg in args:
        if os.path.isdir(arg):
            # Get all files in dir
            for r, d, f in os.walk(arg):
                for file in f:
                    print(os.path.join(r, file))
                    for email in get_emails(file_to_str(os.path.join(r, file))):
                        listEmail.append (email)

            unic_mails(listEmail, arg)                 
        else:
            print ('"{}" is not a dir.'.format(arg))
    print 'done in ', time.clock() - start_time, "seconds"
else:
    parser.print_usage()

