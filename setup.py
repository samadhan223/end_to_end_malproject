from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT="-e ."
def get_requirements(file_path:str)-> List[str]:
    '''
    this is the function return the list of requirements
    '''
    requierements=[]
    with open(file_path) as file_obj:
        requierements=file_obj.readlines()
        requierements=[req.replace("\n","") for req in requierements]

        if HYPEN_E_DOT in requierements:
            requierements.remove(HYPEN_E_DOT)
    return requierements

setup(
    name='end_to_to_mlproject',
    version='0.0.1',
    author='Samadhan',
    author_email='samasurvase@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)