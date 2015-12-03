from setuptools import setup, find_packages

setup(
    name='SantaSelector',
    author='DCRichards',
    url='https://github.com/DCRichards/santaSelector',
    version='0.1.0',
    long_description='A Secret Santa Selector',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask', 'flask-cors']
)