import os

def print_env_vars():
  """Prints environment variables in a tabular format."""
  env_vars = os.environ.items()
  max_key_len = max(len(key) for key, _ in env_vars)

  for key, value in env_vars:
    print(f"{key:{max_key_len}} | {value}")

if __name__ == "__main__":
  print_env_vars()
