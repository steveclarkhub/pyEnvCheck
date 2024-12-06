import argparse
import os
import sys

parser = argparse.ArgumentParser(description="Process hostname and port.")
parser.add_argument('--Dev', action='store_true', help='Is the CWD a virtual env?')
parser.add_argument('--DumpVars', action='store_true', help='Dump all the Environment Vars')
args = parser.parse_args()

if args.Dev:
    if sys.prefix != sys.base_prefix:
       print("Virtual environment detected at CWD ")
    else:
       print("NO venv at CWD")
    
    def git_exist(path):
        return os.path.exists(os.path.join(path, ".git"))
    if git_exist("."):
        print(".git exists at CWD")
    else:
        print("NO .git exists at CWD")

    def shell_name():
        shell = os.environ.get('SHELL', None)
        if shell:
            return shell.split('/')[-1]
        else:
            return "unknown"
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

