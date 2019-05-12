#!/usr/bin/env python

# SteamID To BattleEye GUID
# Author: AlFaMoDz | Twitter: @AlFaMoDzZ | GitHub: /alfamodz

import sys
from hashlib import md5


def uid2guid(steam_id):
    temp = ['BE']
    for x in xrange(8):
        temp.append(chr(steam_id & 0xFF))
        steam_id >>= 8
    return md5(''.join(temp)).hexdigest()

def main(argc, argv):
    if argc < 2:
        print('Usage: %s SteamID or .txt with IDs' % argv[0])
        return 1

    SteamID = argv[1]
    print('|--------------------------------------------------|')
    print('|       ~  SteamID to GUID by AlFaMoDz ~           |')
    print('| ~ github.com/alfamodz - twitter.com/alfamodzz ~  |')
    print('|--------------------------------------------------|\n')
    
    if (argv[1].isdigit()):
        print(' %s - %s' % (SteamID, uid2guid(int(SteamID))))
    else: 
        with open(argv[1]) as f:
            array = []
            for line in f:
                array.append(line)
        array = [x.strip() for x in array] 
        
        for x in range (0, (len(array))):
            print(' %s - %s \n' % (array[x],uid2guid(int(array[x]))))

if __name__ == '__main__':
    sys.exit(main(len(sys.argv), sys.argv))
