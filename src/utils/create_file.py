from rich.console import Console

console = Console()


def create_file(path: str, content: str):
    with open(path, "w") as f:
        f.write(content)
    console.print(f"File created at: [bold blue]{path}[/]")
