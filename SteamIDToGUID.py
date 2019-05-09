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

def main(argc, argv) :
    if argc < 2:
        print('Usage: %s SteamID' % argv[0])
        return 1

    SteamID = int(argv[1])
    print('|--------------------------------------------------|')
    print('|       ~  SteamID to GUID by AlFaMoDz ~           |')
    print('| ~ github.com/alfamodz - twitter.com/alfamodzz ~  |')
    print('|--------------------------------------------------|\n')
    print(' SteamID: %d \n GUID: %s' % (SteamID, uid2guid(SteamID)))

if __name__ == '__main__':
        sys.exit(main(len(sys.argv), sys.argv))
