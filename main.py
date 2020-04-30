import webbrowser
import time
import random

start_time = time.time()    #save current time
while (time.time()-start_time)<1.5:      #run for 1.5 seconds
    visit = random.choice(['google.com', 'youtube.com'])
    site = "http://{}".format(visit)
#    webbrowser.open(site)  #this works if already have google chrome opened, and it'll just open a new tab
    url = 'http://www.google.com/'
    # Windows
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

    # Linux
    # chrome_path = '/usr/bin/google-chrome %s'

    webbrowser.get(chrome_path).open(url)
#    breaktime = random.randrange(5,40)
    time.sleep(1)   #sleep for 5 seconds, can be replaced with 'breaktime' to make it random
    
    