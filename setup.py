from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements from the provided file.
    It strips whitespace and removes empty lines and comments, 
    and ensures '-e .' is removed if present.
    '''
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # Clean up the lines: strip whitespace and remove empty lines or comments
        requirements = [req.strip() for req in requirements if req.strip() and not req.startswith("#")]

        # Remove '-e .' if present
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

# Setup function for the package installation
setup(
    name="mlproject",
    version="0.0.1",
    author="shivam_navik",
    author_email="shivamnavik03@hmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)


