from setuptools import setup, find_packages

setup(
    name="fast",
    version="0.1",
    description="FastAPI CLI for initializing projects",
    packages=find_packages(),
    install_requires=[
        "typer",
        "rich",
        "fastapi",
        "uvicorn",
        "pre-commit",
        "pytest",
        "ruff",
    ],
    entry_points={"console_scripts": ["fast = src.main:cli"]},
)
