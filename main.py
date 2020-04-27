import webbrowser
import time
import random

while True:
    visit = random.choice(['google.com', 'youtube.com'])
    site = "http://{}".format(visit)
    webbrowser.open(site)
    
    breaktime = random.randrange(5,10)
    time.sleep(breaktime)