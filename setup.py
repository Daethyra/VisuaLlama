from setuptools import setup, find_packages

setup(
    name='VisuaLlama',
    version='0.1',
    description='A Visual Assistance Project',
    author='Your Name',
    packages=find_packages(),
    install_requires=[
        'fastapi',
        'torch',
        'transformers'
    ],
    dependency_links=[
        'git+https://github.com/facebookresearch/detectron2.git'
    ]
)
