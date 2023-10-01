from setuptools import setup, find_packages

setup(
    name='NVB',
    version="0.1.0",
    # install_requires=[],
    packages=find_packages(),
    package_data={
        'NVB': ['static/img/*', 'static/*', 'templates/*'],
    },
)
