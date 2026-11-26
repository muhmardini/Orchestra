from typing import Optional
import re
import typer


PORT_ITEM = re.compile(r"^(\d+)(?:-(\d+))?$")

def validate_ports (value: Optional[str]) -> Optional[str]:
    if value is None:
        return value
    if  value == "-":
        return value   
    
    for item in value.split(","):
        match = PORT_ITEM.match(item)
        if not match:
            raise typer.BadParameter(f"'{item}' is not valid. Use things like 80 22,443 1-1000 22,80,1-1000")
        start = int(match.group(1))
        end = int(match.group(2) or start)
        if not (1 <= start <= 65535 and 1 <= end <= 65535):
            raise typer.BadParameter(f"Ports must be between 1 and 65535 (got '{item}')")
        if start > end:
            raise typer.BadParameter(f"Range {item} starts higher than it ends")
    return value

def validate_input (ports, fast):
    if ports and fast:
        raise typer.BadParameter("User either --ports '-p' or --fast '-F', can't use both")
