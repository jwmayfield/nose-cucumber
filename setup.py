from setuptools import setup, find_packages

setup(
    name='nose-cucumber',
    version='0.0.1',
    description="A nose plugin for running cucumber tests.",
    long_description=open("README.rst",'r').read(),
    zip_safe=False,
    packages=find_packages(),
    include_package_data=True,
    install_requires=['nose'],
    entry_points="""
    [nose.plugins.0.10]
    cucumber = cucumber:Cucumber
    """
) 
