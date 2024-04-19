import time
import sys

# Lista z ASCII arty
ascii_arts = [
    '''
    ___________   ._____.   .__    .___.__                                               
 /   _____/  | _|__\_ |__ |__| __| _/|__|                                              
 \_____  \|  |/ /  || __ \|  |/ __ | |  |                                              
 /        \    <|  || \_\ \  / /_/ | |  |                                              
/_______  /__|_ \__||___  /__\____ | |__|                                              
        \/     \/       \/        \/         
    ''',
    '''
 __         .__.__          __                                                        
_/  |_  ____ |__|  |   _____/  |_                                                      
\   __\/  _ \|  |  | _/ __ \   __\                                                     
 |  | (  <_> )  |  |_\  ___/|  |                                                       
 |__|  \____/|__|____/\___  >__|                                                       
                          \/    
    ''',
    '''
                         .__                                                              
   ____   ____   ____ |__|                                                             
  / ___\ /  _ \ /    \|  |                                                             
 / /_/  >  <_> )   |  \  |                                                             
 \___  / \____/|___|  /__|                                                             
/_____/             \/     
  '''
    ,
  '''

                 .__                                                                     
  _____   ____ |__| ____                                                               
 /     \ /    \|  |/ __ \                                                              
|  Y Y  \   |  \  \  ___/                                                              
|__|_|  /___|  /__|\___  >                                                             
      \/     \/        \/    
      '''
      ,
      '''
               .__                           __                                        
  ____________ |__| ______  _  _______      |__|____    ____                           
 /  ___/\____ \|  |/ __ \ \/ \/ /\__  \     |  \__  \ _/ ___\                          
 \___ \ |  |_> >  \  ___/\     /  / __ \_   |  |/ __ \\  \___                          
/____  >|   __/|__|\___  >\/\_/  (____  /\__|  (____  /\___  >                         
     \/ |__|           \/             \/\______| 
     '''
     ,
     '''
  __                                                                                   
_/  |_  ____                                                                           
\   __\/ __ \                                                                          
 |  | \  ___/                                                                          
 |__|  \___  >                                                                         
           \/      



''',
'''
       .__                            __                                               
______ |__| ____  ______ ____   ____ |  | __ ____                                      
\____ \|  |/  _ \/  ___// __ \ /    \|  |/ // __ \                                     
|  |_> >  (  <_> )___ \\  ___/|   |  \    <\  ___/                                     
|   __/|__|\____/____  >\___  >___|  /__|_ \\___  >                                    
|__|                 \/     \/     \/     \/    \/             


'''
,
'''




'''
]

colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m']  
# Kolor czerwony, kolor zielony, kolor żółty, kolor niebieski, kolor fioletowy, kolor cyjanowy

# Pętla wyświetlająca kolejne ASCII arty bez przerwy
while True:
    for i, art in enumerate(ascii_arts):
        print(colors[i % len(colors)] + art + '\033[0m', end='', flush=True)  # Wyświetl aktualny ASCII art z odpowiednim kolorem
        time.sleep(1)  # Poczekaj sekundę
        sys.stdout.write('\033[F')  # Przesuń kursor do góry o 1 linijkę