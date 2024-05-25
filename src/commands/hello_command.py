import typer
from rich.console import Console

console = Console()
app = typer.Typer()


@app.command()
def hello(name: str):
    console.print(f"Hello, {name}!")
