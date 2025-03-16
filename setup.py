from setuptools import find_packages, setup

# Read dependencies from requirements.txt and ignore "-e ."
with open("requirements.txt") as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith("-e")]

setup(
    name='cellSegmentation',
    version='0.0.0',
    author='Mansoureh Aghabeig',
    author_email='mans.aghabeig@gmail.com',
    packages=find_packages(),
    install_requires=requirements  # Read dependencies from requirements.txt, excluding '-e .'
)
