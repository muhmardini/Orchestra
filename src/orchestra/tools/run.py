import typer
import subprocess

def run_nmap(target, tags):
    cmd = ["nmap"]
    if tags['ports']:
        cmd += ["-p", tags['ports']]
    elif tags['fast']:
        cmd += ["-F"]
    cmd.append(target)
    typer.echo(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd)
    raise typer.Exit(code=result.returncode)