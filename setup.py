from setuptools import find_packages,setup
from typing import List

# HYPEN_E_DOT = '-e .'

def get_requirement(file_path:str)-> List[str]:
    '''
    this function is return the list of requirement
    '''
    requirments = []
    with open(file_path) as file_obj:
        requirments=file_obj.readline()
        requirments= [i.replace("\n","") for i in requirments]

    # if HYPEN_E_DOT in requirments:
    #     requirments.remove(HYPEN_E_DOT)

    return requirments

setup(
    name= 'mlproject',
    version='1.0.0',
    author='vatsaly',
    author_email='vatsalyrajyaguru@gmail.com',
    packages=find_packages(),
    install_requires = get_requirement('requirments.txt')
)