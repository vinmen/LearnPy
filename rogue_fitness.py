import requests
import time

"""
url_list = ['https://www.roguefitness.com/miscellaneous-barbells-used',
            'https://www.roguefitness.com/rogue-28-5-mm-boneyard-bars',
            'https://www.roguefitness.com/rogue-29mm-boneyard-bars',
            'https://www.roguefitness.com/rogue-25mm-boneyard-bars',
            'https://www.roguefitness.com/rogue-28mm-boneyard-bars',
            'https://www.roguefitness.com/rogue-us-mil-sprc-bumper-plates',
            'https://www.roguefitness.com/rogue-hi-temp-bumper-plates',
            'https://www.roguefitness.com/rogue-hg-2-0-bumper-plates',
            'https://www.roguefitness.com/rogue-echo-bumper-plates-with-white-text',
            'https://www.roguefitness.com/rogue-color-echo-bumper-plate',
            'https://www.roguefitness.com/rogue-fleck-plates',
            'https://www.roguefitness.com/rogue-mil-echo-bumper-plates-black',
            'https://www.roguefitness.com/rogue-echo-bar',
            'https://www.roguefitness.com/the-rogue-bar-2-0',
            'https://www.roguefitness.com/rogue-45lb-ohio-power-bar-bare-steel',
            'https://www.roguefitness.com/rogue-45lb-ohio-power-bar-black-zinc',  
            'https://www.roguefitness.com/rogue-ohio-power-bar-e-coat'                    
            'https://www.roguefitness.com/rogue-ohio-bar-black-oxide',
             'https://www.roguefitness.com/the-ohio-bar-2-0-e-coat',
            'https://www.roguefitness.com/the-ohio-bar-black-zinc',  
            'https://www.roguefitness.com/the-rogue-c-70-bar',              
            'https://www.roguefitness.com/the-bella-bar-2-0-e-coat',
            'https://www.roguefitness.com/rogue-bella-bar-2-0-black-zinc']

"""

url_list = ['https://www.roguefitness.com/miscellaneous-barbells-used',
            'https://www.roguefitness.com/rogue-28-5-mm-boneyard-bars',
            'https://www.roguefitness.com/rogue-29mm-boneyard-bars',
            'https://www.roguefitness.com/rogue-25mm-boneyard-bars',
            'https://www.roguefitness.com/rogue-28mm-boneyard-bars',
            'https://www.roguefitness.com/rogue-us-mil-sprc-bumper-plates',
            'https://www.roguefitness.com/rogue-hi-temp-bumper-plates',
            'https://www.roguefitness.com/rogue-hg-2-0-bumper-plates',
            'https://www.roguefitness.com/rogue-echo-bumper-plates-with-white-text',
            'https://www.roguefitness.com/rogue-color-echo-bumper-plate',
            'https://www.roguefitness.com/rogue-fleck-plates',
            'https://www.roguefitness.com/rogue-mil-echo-bumper-plates-black']

for url in url_list:   
    try:
        r = requests.get(url)
        data = r.content  
        text_file = open("data.txt", "w")
        text_file.write(str(data))

        if 'type="tel"' in str(data):
            print(url)
        time.sleep(5)
    except: 
        print("Error - " + url)
