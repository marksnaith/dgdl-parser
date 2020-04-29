import setuptools

long_description = "DGDL"

setuptools.setup(
     name='dgdl',
     version='0.1',
     author="Mark Snaith",
     author_email="mark@arg.tech",
     description="A lightweight framework for constructing dialogue games",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="http://arg.tech",
     packages=setuptools.find_packages(),
     install_requires = [
	'dill'
     ],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: Creative Commons Attribution Share Alike 4.0",
         "Operating System :: OS Independent",
     ],
 )
