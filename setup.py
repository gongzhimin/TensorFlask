from setuptools import find_packages, setup

setup(
    name='TensorFlask',
    author='JiminKong',
    description='An implementation of MLaaS to identify porn images.',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)


"""
To run `tensorflask` app in PowerShell:
1. $env:FLASK_APP="tensorflask"
2. $env:FLASK_ENV="development"
3. flask init-db
4. flask run --host=0.0.0.0

In Command Prompt:
1. set FLASK_APP=tensorflask
2. set FLASK_ENV=development
3. flask init-db
4. flask run --host=0.0.0.0
"""
