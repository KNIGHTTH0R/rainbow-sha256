#!/usr/bin/env python

import requests
import sys
import time

WORDS_FILE = "words/words.txt"
DELIMITER = "\n"
IP = "127.0.0.1"
URL = 'http://{}:9999/hash?str='.format(IP)


# Read the file and thrust word requests to the server to save
def main():
    with open(WORDS_FILE, 'r') as words_file:
        counter = 0
        time_start = time.time()
        for word in words_file.read().split('\n'):
            counter += 1
            formatted_url = URL + '{}'.format(word)
            requests.get(formatted_url)
            if counter == 1000:
                counter = 0
                speed = (time.time() - time_start)/1000
                print("Seconds per 1000 requests = {}".format(speed))
                time_start = time.time()


if __name__ == "__main__":
    IP = sys.argv[1]
    main()
