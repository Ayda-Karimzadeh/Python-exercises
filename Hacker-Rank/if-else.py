#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if 1<=n<=100:
        if n%2!=0 :
            print("Weird")
        else:
            pass
        if n%2==0 and 2<=n<=5:
            print("Not Weird")
        else:
            pass
        if n%2==0 and 6<=n<=20:
            print("Weird")
        else:
            pass
        if n%2==0 and 20<n :
            print("Not Weird")
        else:
            pass