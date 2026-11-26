from typing import Annotated
import typer

app = typer.Typer()

@app.command()
def nmap(
    target: Annotated[str, typer.Argument(help="Nmap target you want to scan 'example.com")],
    ports: Annotated[str | None, typer.Option("--ports", "-p", callback=validate_ports)]
    service: Annotated[bool, typer.Option("--version-scan", "-sV", help="Version Detection")] = False,
):
    scanned_ports = str(starting_port) + "-" + str(ending_port)