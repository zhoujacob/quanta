from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read().splitlines()

setup(
    name='quanta',
    version='0.0.1',
    author='Jacob Zhou',
    author_email='zhoujaco9220@gmail.com',
    license='MIT License',
    description='Quanta test',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/zhoujacob/quanta',
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'quanta=app.my_tool:cli', 
        ],
    },
)
