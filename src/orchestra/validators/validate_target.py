import typer


def validate_target(target: str):
    if target.startswith("-"):
        raise typer.BadParameter("Target can't start with '-'")