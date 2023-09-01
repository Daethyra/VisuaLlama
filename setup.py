from setuptools import setup, find_packages

setup(
    name='VisuaLlama',
    version='0.1',
    description='A Visual Assistance Project',
    author='Daethyra (Daemon Carino)',
    packages=find_packages(),
    install_requires=[
        'fastapi',
        'torch',
        'transformers'
    ]
)
