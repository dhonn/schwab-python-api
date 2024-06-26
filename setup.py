from setuptools import setup
from setuptools import find_packages

# load the README file.
with open(file="README.md", mode="r") as fh:
    long_description = fh.read()

setup(
    # this will be my Library name.
    name='schwab-python-api',

    # Want to make sure people know who made it.
    author='Dhonn Lushine',

    # also an email they can use to reach out.
    author_email='dhonn@yahoo.com',

    # Set the version.
    version='0.0.2',

    # here is a simple description of the library, this will appear when
    # someone searches for the library on https://pypi.org/search
    description='A python client lirbary for the Schwab API.',

    # I have a long description but that will just be my README file, note the
    # variable up above where I read the file.
    long_description=long_description,

    # want to make sure that I specify the long description as MARKDOWN.
    long_description_content_type="text/markdown",

    # here is the URL you can find the code, this is just the GitHub URL.
    url='https://github.com/dhonn/schwab-python-api',

    # there are some dependencies to use the library, so let's list them out.
    install_requires=[
        'websockets',
        'requests',
        'flask',
        'requests-oauthlib',
        'pyopenssl',
        'portalocker',
        'python-dotenv'
    ],

    # some keywords for my library.
    keywords='finance, schwab, api',

    # here are the packages I want "build."
    packages=find_packages(
        include=['td', 'samples', 'td.app', 'td.templates']
    ),

    # here we specify any package data.
    package_data={
        # And include any files found subdirectory of the "td" package.
        "td": ["app/*", "templates/*"],
    },

    # I also have some package data, like photos and JSON files, so I want to
    # include those too.
    include_package_data=True,

    # additional classifiers that give some characteristics about the package.
    classifiers=[

        # I want people to know it's still early stages.
        'Development Status :: 3 - Alpha',

        # My Intended audience is mostly those who understand finance.
        'Intended Audience :: Financial and Insurance Industry',

        # My License is MIT.
        'License :: OSI Approved :: MIT License',

        # I wrote the client in English
        'Natural Language :: English',

        # The client should work on all OS.
        'Operating System :: OS Independent',

        # The client is intendend for PYTHON 3
        'Programming Language :: Python :: 3'
    ],

    # you will need python 3.7 to use this libary.
    python_requires='>=3.7'
)
