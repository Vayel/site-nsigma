from setuptools import setup, find_packages


setup(
    name='site-nsigma',
    url='https://github.com/Vayel/site-nsigma',
    author='Vincent Lefoulon',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask',
        'Flask-WTF',
        'flask_httpauth',
    ],
)
