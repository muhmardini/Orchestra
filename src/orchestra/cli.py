from typing import Annotated
import typer
import re
from validators.validate_ports import validate_ports, validate_input
from validators.validate_tools import validate_tool
from validators.validate_target import validate_target



app = typer.Typer(chain=True)

@app.command()
def nmap(
    target: Annotated[str, typer.Argument(help="Nmap target you want to scan (IP, Domain, CIDR) 'example.com")],
    ports: Annotated[str | None, typer.Option("--ports", "-p", callback=validate_ports)] = None,
    fast: Annotated[bool, typer.option("-fast", "-F")] = True,
    service: Annotated[bool, typer.Option("--version-scan", "-sV", help="Version Detection")] = False,
):
    validate_input(ports, fast)
    validate_tool("nmap")
    validate_target(target)
    