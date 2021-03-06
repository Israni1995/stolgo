from setuptools import setup,find_packages

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='stolgo',
   version='0.1',
   description='Utilities for the analysis of financial data',
   license="MIT",
   long_description=long_description,
   author='stolgo Developers',
   author_email='stockalgos@gmail.com',
   project_urls={
          "Organization":"http://www.stolgo.com",
          "Source":"https://github.com/stockalgo/stolgo",
          "Tracker":"https://github.com/stockalgo/stolgo/issues"
          },
   packages=find_packages(include=['stolgo','stolgo.*']),
   package_dir = {'':'lib'},
   include_package_data=True,
   install_requires=[
            'requests', 
            'pandas',
            'datetime'],
    classifiers=[
    'Development Status :: 3 - Alpha ',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.8',
  ],
)