from tools.run import run_nmap

def runner_tool(tool: str, target: str, tags: dict):
    match(tool):
        case "nmap":
            run_nmap(target, tags)
    