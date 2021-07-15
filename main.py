#!/usr/bin/python3


"""
The most commonly bottlenecks for short, are bottlenecks where your
computer spends more time wainting on various inputs and outpus that it
does on processing the information.
"""

from urllib.request import urlopen
import time

def main():
    time_0 = time.time()
    req = urlopen("http://example.com/")
    page_html = req.read()
    time_1 = time.time()
    print("Total time to fetch page: {} seconds".format(time_1 - time_0))

if __name__ == "__main__":
    main()
