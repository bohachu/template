#!/usr/bin/env python3
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Description of your script')
    parser.add_argument('--package_name', default='default_package_name', help='Name of the package')
    args = parser.parse_args()

    print(f'Hi! The package name is {args.package_name}.')