#!/usr/bin/python3


import time
import requests
import concurrent.futures
import os


URLS = [
    'https://jsonplaceholder.typicode.com/posts',
    'https://jsonplaceholder.typicode.com/comments',
    'https://jsonplaceholder.typicode.com/albums',
    'https://jsonplaceholder.typicode.com/photos',
    'https://jsonplaceholder.typicode.com/todos',
    'https://jsonplaceholder.typicode.com/users'
]


def fetch_single(url: str) -> None:
    
    print("Fetching url: {}".format(url))
    
    requests.get(url)
    time.sleep(0.05)
    print(os.getpid())
    print("Fetched url: {}".format(url))

if __name__ == "__main__":
    time_start = time.time()
    
    with concurrent.futures.ProcessPoolExecutor() as ppe:
        for url in URLS:
            ppe.submit(fetch_single, url)
    

    time_end = time.time()
    
    print("All done! Took {}".format(round(time_end - time_start, 2)))
