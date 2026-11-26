import shutil
import typer


def validate_tool(tool):
    if shutil.which(f"{tool}") is None:
        typer.secho(f"{tool} is not installed or not in PATH", fg=typer.colors.RED, err=True)
        raise typer.Exit(code=1)