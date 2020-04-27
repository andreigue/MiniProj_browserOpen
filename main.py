import webbrowser
import time
import random

start_time = time.time()    #save current time
while (time.time()-start_time)<15:      #run for 15 seconds
    visit = random.choice(['google.com', 'youtube.com'])
    site = "http://{}".format(visit)
    webbrowser.open(site)
    
#    breaktime = random.randrange(5,40)
    time.sleep(5)   #sleep for 5 seconds, can be replaced with 'breaktime' to make it random