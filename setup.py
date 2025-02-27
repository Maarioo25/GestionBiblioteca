from setuptools import setup, find_packages

setup(
    name="gestion_biblioteca_mario",
    version="1.0.0",
    author="Mario Bueno López",
    author_email="mariobueno060@gmail.com",
    description="Sistema de Gestión de Biblioteca en Python.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Maarioo25/GestionBiblioteca",
    packages=find_packages(),
    install_requires=[
        "sqlalchemy>=2.0.38",
        "pytest>=8.3.4"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    entry_points={
        "console_scripts": [
            "gestion_biblioteca_mario=main:main",
        ],
    },
)
