import argparse
import os
import sys

parser = argparse.ArgumentParser(description="Info about the CWD prior to getting started.")
parser.add_argument('--Dev', action='store_true', help='Is the CWD a virtual env?')
parser.add_argument('--DumpVars', action='store_true', help='Dump all the Environment Vars')
args = parser.parse_args()

print("")

if args.Dev:
    if sys.prefix != sys.base_prefix:
       print("Venv: Virtual environment detected at CWD ")
    else:
       print("Venv: NO venv at CWD")
    
    def git_exist(path):
        return os.path.exists(os.path.join(path, ".git"))
    if git_exist("."):
        print("Git: .git exists at CWD")
    else:
        print("Git: NOT found at CWD")

    def shell_name():
        shell = os.environ.get('SHELL', None)
        if shell:
            return f"Shell: {shell.split('/')[-1]}"
        else:
            return "Shell can't be ID'd"
    shell = shell_name()
    print(shell)

if args.DumpVars:
   def print_env_vars():
       """Prints environment variables in a tabular format."""
       env_vars = os.environ.items()
       max_key_len = max(len(key) for key, _ in env_vars)
       for key, value in env_vars:
           print(f"{key:{max_key_len}} | {value}")
    
   print_env_vars()

