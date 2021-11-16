from setuptools import setup, find_packages

setup(
    name='Ranking',
    version='0.1.0',
    url='https://github.com/vemonet/biohackathon2021.git',
    author='Vincent Emonet',
    author_email='vincent.emonet@gmail.com',
    description='Ranking of datasets',
    packages=find_packages(),
    install_requires=open("requirements.txt", "r").readlines(),
)