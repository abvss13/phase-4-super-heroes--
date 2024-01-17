import sys
from subprocess import run

if __name__ == "__main__":
    name = ''
    with open('bin/config') as config_file:
        name = config_file.read().strip()

    if name:
        run(["cd", "code-challenge", "&&", "git", "add", ".", "&&", "git", "commit", "--allow-empty", "-m", "Final commit"])
        run(["cd", "code-challenge", "&&", f"git", "bundle", "create", f"../{name}.bundle", "HEAD", f"{name}"])
