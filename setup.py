from setuptools import setup, find_packages

# Optionally read README.md for long description
def read_long_description():
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "Offline Dolphin 3 question-answering client via Ollama"

setup(
    name='dolphin3',
    version='0.1.0',
    description='Offline Dolphin 3 question-answering client via Ollama',
    long_description=read_long_description(),
    long_description_content_type='text/markdown',
    author='Dwaipayan',
    author_email='dwdutta@gmail.com',
    url='https://github.com/yourusername/dolphin3',  # Update this if applicable
    license='MIT',  # Change if using a different license
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests',
        'streamlit',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.7',
)
