import os
import platform

import typer
from rich.console import Console
import subprocess
from src.config.pre_commit_config import pre_commit_config
from src.config.pytest_config import pytest_ini_config
from src.config.ruff_config import ruff_config
from src.templates.main_app.main_app_template import main_app_template
from src.templates.main_app.main_controller_template import main_controller_template
from src.templates.main_app.main_service_template import main_service_template
from src.templates.main_app.main_test_template import main_test_template
from src.utils.create_file import create_file
from src.config.gitignore_config import git_ignore_config
from src.templates.main_app.requirements_template import (
    requirements_dev_content,
    requirements_prod_content,
)

console = Console()
# app = typer.Typer()


def create_venv(app_dir: str):
    console.print("Creating virtual environment")
    os.chdir(app_dir)
    subprocess.run(
        [
            "uv",
            "venv",
        ]
    )


def shell_source(script):
    """Emulate the action of "source" in bash, setting some environment variables."""
    pipe = subprocess.Popen(". %s; env" % script, stdout=subprocess.PIPE, shell=True)
    output = pipe.communicate()[0]
    output = output.decode()  # Decodificar la salida a una cadena de texto
    env = dict((line.split("=", 1) for line in output.splitlines()))
    os.environ.update(env)


def activate_venv():
    if platform.system() == "Windows":
        venv_activate = ".venv\\Scripts\\activate"
    else:
        venv_activate = ".venv/bin/activate"
        shell_source(venv_activate)
    console.print("Activating virtual environment")


def install_dependencies():
    console.print("Installing development dependencies", style="bold green", emoji="📦")
    subprocess.run(["uv", "pip", "install", "-r", "requirements-dev.txt"])
    console.print("Installing production dependencies", style="bold green", emoji="📦")
    subprocess.run(["uv", "pip", "install", "-r", "requirements.txt"])


def new(app_name: str):
    # Crear el directorio de la aplicación
    app_dir = os.path.join(os.getcwd(), app_name)
    if not os.path.exists(app_dir):
        os.makedirs(app_dir)
        console.print(f"Creating directory: {app_dir}", style="bold green", emoji="📁")
    else:
        console.print(
            f"¡Directory {app_name} already exits!", style="bold red", emoji="😅"
        )
        raise typer.Abort()

    create_repository = typer.confirm("Do you want to create a git repository?")
    if create_repository:
        gitignore_ini_file = os.path.join(app_dir, ".gitignore")
        create_file(gitignore_ini_file, git_ignore_config)
        console.print("Creating git repository", style="dark_orange", emoji="🚀")
        subprocess.run(["git", "init"], cwd=app_dir)

    # Crear la estructura de directorios
    dirs_to_create = [
        "src",
        "tests",
    ]
    for directory in dirs_to_create:
        dir_path = os.path.join(app_dir, directory)
        os.makedirs(dir_path)
        console.print(f"Creating directory: {dir_path}", style="bold green", emoji="📁")

    # Crear archivos básicos
    main_file = os.path.join(app_dir, "src", "main.py")
    create_file(main_file, main_app_template)

    app_controller_file = os.path.join(app_dir, "src", "app_controller.py")
    create_file(app_controller_file, main_controller_template)

    app_services_file = os.path.join(app_dir, "src", "app_services.py")
    create_file(app_services_file, main_service_template)

    # Crear archivos de configuración
    pre_commit_file = os.path.join(app_dir, ".pre-commit-config.yaml")
    create_file(pre_commit_file, pre_commit_config)

    ruff_file = os.path.join(app_dir, "ruff.toml")
    create_file(ruff_file, ruff_config)

    pytest_ini_file = os.path.join(app_dir, "pytest.ini")
    create_file(pytest_ini_file, pytest_ini_config)

    example_test_file = os.path.join(app_dir, "tests", "test_example.py")
    create_file(example_test_file, main_test_template)

    create_file(os.path.join(app_dir, "requirements-dev.txt"), requirements_dev_content)
    create_file(os.path.join(app_dir, "requirements.txt"), requirements_prod_content)

    console.print(
        "Configuration for pre-commit, Ruff y pytest created",
        style="bold green",
        emoji="🔧",
    )
    create_venv(app_dir)
    activate_venv()
    install_dependencies()
    console.print("¡App created and ready!", style="bold green", emoji="🚀 ")
