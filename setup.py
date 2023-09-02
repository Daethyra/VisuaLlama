from setuptools import setup, find_packages

# Read the content of README file
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='VisuaLlama',
    version='0.1',
    description='A Visual Assistance Project',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Daethyra (Daemon Carino)',
    packages=find_packages(),
    install_requires=[
        'fastapi',
        'torch',
        'transformers',
        'requests', 
        'Pillow'
    ],
    classifiers=[
        'Development Status :: v.1',
        'Intended Audience :: Non-technical Users, Developers',
        'License :: OSI Approved :: Affero GNU GPL v3.0',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.10',
)
