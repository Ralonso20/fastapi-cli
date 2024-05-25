import os
import typer
from rich.console import Console
from src.config.pre_commit_config import pre_commit_config
from src.config.ruff_config import ruff_config
from src.config.pytest_config import pytest_ini_config

console = Console()
# app = typer.Typer()


def create_file(path: str, content: str):
    with open(path, "w") as f:
        f.write(content)
    console.print(f"Archivo creado en: [bold blue]{path}[/]")


# @app.command(
#     help="Crea una nueva aplicación FastAPI con la estructura de directorios y archivos necesarios",
#     name="new",
# )
def new(app_name: str):
    # Crear el directorio de la aplicación
    app_dir = os.path.join(os.getcwd(), app_name)
    if not os.path.exists(app_dir):
        os.makedirs(app_dir)
        console.print(
            f"Directorio de la aplicación creado en: [bold green]{app_dir}[/]"
        )
    else:
        console.print(
            f"¡El directorio de la aplicación {app_name} ya existe!", style="bold red"
        )
        raise typer.Abort()

    # Crear la estructura de directorios
    dirs_to_create = [
        "src",
        "src/controllers",
        "src/models",
        "src/services",
        "src/utils",
        "tests",
    ]
    for directory in dirs_to_create:
        dir_path = os.path.join(app_dir, directory)
        os.makedirs(dir_path)
        console.print(f"Directorio creado en: [bold blue]{dir_path}[/]")

    # Crear archivos básicos
    main_file = os.path.join(app_dir, "src", "main.py")
    with open(main_file, "w") as f:
        f.write(
            "from fastapi import FastAPI\n\n"
            "app = FastAPI()\n\n"
            "@app.get('/')\n"
            "async def read_root():\n"
            "    return {'message': 'Hello, World!'}\n"
        )
    console.print(f"Archivo principal de FastAPI creado en: [bold blue]{main_file}[/]")

    # Crear archivos de configuración
    pre_commit_file = os.path.join(app_dir, ".pre-commit-config.yaml")
    create_file(pre_commit_file, pre_commit_config)

    ruff_file = os.path.join(app_dir, "ruff.toml")
    create_file(ruff_file, ruff_config)

    pytest_ini_file = os.path.join(app_dir, "pytest.ini")
    create_file(pytest_ini_file, pytest_ini_config)

    example_test_file = os.path.join(app_dir, "tests", "test_example.py")
    with open(example_test_file, "w") as f:
        f.write("def test_example():\n" "    assert True\n")
    console.print(
        f"Ejemplo de archivo de prueba creado en: [bold blue]{example_test_file}[/]"
    )

    console.print(
        "Configuración de pre-commit, Ruff y pytest creada", style="bold green"
    )
    console.print("¡Aplicación creada exitosamente!", style="bold green")
