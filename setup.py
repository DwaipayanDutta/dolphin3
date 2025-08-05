from setuptools import setup, find_packages

setup(
    name='dolphin3',
    version='0.1.0',
    description='Offline Dolphin 3 question-answering client via Ollama',
    author='Dwaipayan',
    author='dwdutta@gmail.com',
    packages=find_packages(),
    install_requires=[
        'requests',
	'streamlit'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
