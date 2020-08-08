#!/usr/bin/env python

import subprocess


#### For windows ####
def shutdown():
    instruction = "shutdown/s"
    try:
        output_response = subprocess.run(instruction, shell=True, capture_output=True)
        print(output_response)
    except Exception as e:
        print(e)

def restart():
    instruction = "shutdown/r"
    try:
        output_response = subprocess.run(instruction, shell=True, capture_output=True)
        print(output_response)
    except Exception as e:
        print(e)

"""
###### For Linux ######
def shutdown():
    instruction = "sudo shutdown -r now"
    try:
        output_response = subprocess.run(instruction, shell=True, capture_output=True)
        print(output_response)
    except Exception as e:
        print(e)

def restart():
    instruction = "shudo reboot"
    try:
        output_response = subprocess.run(instruction, shell=True, capture_output=True)
        print(output_response)
    except Exception as e:
        print(e)

"""
if __name__=='__main__':
    option = input("Do you want to shutdown or restart [s/r]:")
    if option == 's':
        shutdown()
    elif option == 'r':
        restart()
    else:
        print("You want to continue using your pc! enjoy!")
