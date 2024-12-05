import argparse
import subprocess

def main():
  # Define script options
  parser = argparse.ArgumentParser(description="Run either EnvCheck.py or EnvDump.py")
  parser.add_argument("script", choices=["envcheck", "envdump"], help="Script to run (envcheck or envdump)")

  # Parse arguments
  args = parser.parse_args()

  # Run the selected script
  if args.script == "envcheck":
    subprocess.run(["python", "EnvCheck.py"])
  elif args.script == "envdump":
    subprocess.run(["python", "EnvDump.py"])
  else:
    print(f"Invalid script: {args.script}")

if __name__ == "__main__":
  main()
  