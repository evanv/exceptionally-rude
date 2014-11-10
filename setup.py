from setuptools import setup

setup(
    name = 'exceptionally_rude',
    version = '0.0.0.0.1.0.1',
    author = 'Evan Volgas',
    author_email = 'evolgas@gmail.com',
    description = ("This Python module insults you when you screw something up."),
    license = 'MIT',
    keywords = 'exception handling, humor',
    url = 'https://github.com/evanv/exceptionally-rude',
    #long_description=open('README.md').read(),
    py_modules=['exceptionally_rude'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities'
    ]
)
