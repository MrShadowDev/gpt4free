import codecs
import os
from setuptools import find_packages, setup

# Get the directory where this script is located
here = os.path.abspath(os.path.dirname(__file__)

# Read the README file
with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = fh.read()

# Read the requirements from the requirements.txt file
with open("requirements.txt") as f:
    required = f.read().splitlines()

# Define project metadata
VERSION = "0.1.7.5"
DESCRIPTION = "The official gpt4free repository | various collection of powerful language models"

# Define setup parameters
setup(
    name="g4f",
    version=VERSION,
    author="Tekky",
    author_email="support@g4f.ai",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    package_data={
        "g4f": ["g4f/interference/*", "g4f/gui/client/*", "g4f/gui/server/*"]
    },
    include_package_data=True,
    install_requires=required,
    entry_points={
        "console_scripts": ["g4f=g4f.cli:main"],
    },
    url="https://github.com/xtekky/gpt4free",
    project_urls={
        "Source Code": "https://github.com/xtekky/gpt4free",
        "Bug Tracker": "https://github.com/xtekky/gpt4free/issues",
    },
    keywords=[
        "python", "chatbot", "reverse-engineering", "openai", "chatbots",
        "gpt", "language-model", "gpt-3", "gpt3", "openai-api", "gpt-4",
        "gpt4", "chatgpt", "chatgpt-api", "openai-chatgpt", "chatgpt-free",
        "chatgpt-4", "chatgpt4", "chatgpt4-api", "free", "free-gpt", "gpt4free", "g4f",
    ],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
