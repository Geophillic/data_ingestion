from setuptools import setup, find_packages


setup(
    name = "data_ingestion",
    version = "0.1",
    packages = find_packages(exclude=['tests*']),
    license='MIT',
    descrition ="data ingestion python packages",
    long_description=open('README.md').read(),
    install_requires=['pandas', 'logging', 'sqlalchemy'],
    url='https://github.com/Geophillic/data_ingestion',
    author='Oladipupo Ademola Ibrahim',
    author_email='oladipupoademola@gmail.com'
    )