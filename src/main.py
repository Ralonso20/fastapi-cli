import typer
from src.commands.new_command import new as new_command
from src.commands.hello_command import app as hello

cli = typer.Typer()


@cli.command(
    help="Crea una nueva aplicación FastAPI con la estructura de directorios y archivos necesarios",
    name="new",
)
def new(app_name: str = typer.Argument(..., help="Nombre de la aplicación")):
    new_command(app_name)


cli.add_typer(hello, name="hello")


if __name__ == "__main__":
    cli()
