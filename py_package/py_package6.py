#!/usr/bin/env python3
import argparse
from os import system as s

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Description of your script')
    parser.add_argument('--package_name', default='default_package_name', help='Name of the package')
    args = parser.parse_args()
    url_prefix = "https://raw.githubusercontent.com/bohachu/template/master/py_package/clone_files/"
    files = [
        "go.py", "package.yml", "requirements.txt", "setup.py", "upload_pip.py"
    ]
    for filename in files:
        s(f"curl -O {url_prefix + filename}")
    open('package.yml', 'w').write(f'''package_name: {args.package_name}\n''')
    print(f'Hi! The package name is {args.package_name}.')

'''
current_folder=$(basename "$PWD")
curl -sS https://raw.githubusercontent.com/bohachu/template/master/py_package/py_package6.py | python - --package_name $current_folder
'''