from setuptools import setup, find_packages

from typing import List

HYPEN_E_DOT = '-e .'
def get_req(file_path:str)->List[str]:

    req = []
    with open(file_path) as file_obj:
        req = file_obj.readlines()
        req = [i.replace('\n','') for i in req]

        if HYPEN_E_DOT in req:
            req.remove(HYPEN_E_DOT)

    return req



setup(
name = 'MLProject',
version = '0.0.1',
author = 'shivam',
author_email='shivam.gaur2011@gmail.com',
packages=find_packages(),
install_requires = get_req('requirements.txt')
)