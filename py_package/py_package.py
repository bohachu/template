#!/usr/bin/env python3
import json
import sys

if __name__ == '__main__':
    data = json.load(sys.stdin)
    param1 = data.get('param1')
    param2 = data.get('param2')
    print(f'param1={param1}, param2={param2}')
