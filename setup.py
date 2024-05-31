from setuptools import find_packages, setup

setup(
    name="fastcli",
    version="0.2",
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
        "uv",
    ],
    entry_points={"console_scripts": ["fastcli = src.main:cli"]},
)
