'''
The setup.py file is an essential part of packaging and 
distributing Python projects. It is used by setuptools 
(or distutils in older Python versions) to define the configuration 
of your project, such as its metadata, dependencies, and more
'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This Function Will Return List Requirements
    
    """
    requirement_lst:list[str]=[]
    try:
        with open('requirements.txt','r') as file:
            ## Read lines from File
            lines=file.readlines()
            ## Proccess each lines
            for line in lines:
                requirement = line.strip()
                ## Ignore empty lines and -e.
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)

    except FileExistsError:
        print("requirements.txt not found")

    return requirement_lst  

print(get_requirements())       

setup(
      name="NetworkSecurity",
    version="0.0.1",
    author="Ashish Kumar",
    author_email="cseashishai@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)