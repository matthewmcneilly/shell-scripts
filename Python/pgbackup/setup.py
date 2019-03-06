from setuptools import setup, find_packages

with open('README.rst', 'r') as f:
    readme = f.read()

setup(
    name='pgbackup',
    version='0.1.0',
    description='Database backups locally or to AWS S3.',
    long_description=readme,
    author='Matthew McNeilly',
    author_email='matthewmcneilly@protonmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'}, # Looks for packages within the src directory e.g. __init__.py
    install_requires=['boto3'],# Additional packages to install
    entry_points={ # mapping pgbackup command use to use pgbackup package, cli module and call main function
        'console_scripts': [
            'pgbackup=pgbackup.cli:main',
        ]
    }
)
