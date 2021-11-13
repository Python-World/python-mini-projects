import speedtest
import os
import platform
import subprocess
import sys

USER = platform.system()

def clr_screen():
    if USER == 'Linux':
        subprocess.call('clear')
    elif USER == 'Windows':
        r = os.system('cls')

def speed_tester():
    clr_screen()
    
    try:
        test = speedtest.Speedtest()
    except speedtest.ConfigRetrievalError:
        print('Sorry, looks like you are not connected to any network!\nPlease make sure you are connected to the internet.')
        sys.exit()
    
    print('Loading server list...')
    test.get_servers()      # Get a list a servers available for speed test

    print('Choosing best server')
    best = test.get_best_server()       # Choose best server

    print('\n\n\nServer found!')
    print(f'Found : {best["host"]}\nServer location: {best["name"]}')

    print('\n\nPerforming download test...')
    downloadResult = test.download()
    print('Done!')
    print('\nPerforming upload test...')
    uploadResult = test.upload()
    print('Done\n\n')
    pingResult = test.results.ping

    print(f'Download Speed: {downloadResult/ 1024**2:.3f} mbps  {downloadResult}')        # Mega bits per seconds conversion
    print(f'Upload Speed: {uploadResult/ 1024**2:.3f} mbps')
    print(f'Ping Results: {pingResult}')

if __name__ == '__main__':
    speed_tester()
