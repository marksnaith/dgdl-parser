"""
Copyright (C) 2020  Centre for Argument Technology (http://arg.tech)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

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
	'antlr4-python3-runtime=4.8'
     ],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
         "Operating System :: OS Independent",
     ],
 )
