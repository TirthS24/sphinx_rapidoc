from setuptools import setup, find_packages

setup(
    name='sphinx_rapidoc',
    version='0.1',
    description='Custom Sphinx extension for embedding RapiDoc',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'sphinx',
    ],
    package_data={
        'sphinx_rapidoc': ['static/*'],
    },
    entry_points={
        'sphinx.extensions': [
            'sphinx_rapidoc = sphinx_rapidoc',
        ],
    },
)
