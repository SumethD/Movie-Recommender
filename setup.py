from setuptools import setup

with open("Readme.md","r",encoding="utf-8") as  fh:
    long_desc =fh.read()

AUTHOR_NAME ='SUMETH_DL'
SRC_REPO ='src'
LIST_OF_REQUIREMENTS =['streamlit']

setup(
    name = SRC_REPO,
    version ='0.0.1',
    author= AUTHOR_NAME,
    author_email='reigekrypt@gmail.com',
    description='package for movie recommendations',
    long_description= long_desc,
    long_description_content_type='text/markdown',
    package =[SRC_REPO],
    python_requires = '>3.11.5',
    install_requires =LIST_OF_REQUIREMENTS,
)