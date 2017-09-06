'''
Created on Oct 17, 2013

@author: shu, Long
'''
import socket;
import time;
import datetime;
import threading;
import thread;
import bluetooth;
import ReadXML;
import os;
import signal;
import SaveRawFile;

def main():
    
    while (True):
        Nearby_address = bluetooth.discover_devices(duration = 3, lookup_names = True);
                
        MacData = '{0};{1};'.format(datetime.datetime.now(), Nearby_address);
        
        print(MacData);
        
        del Nearby_address;

if __name__ == "__main__":
    main();
