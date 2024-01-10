import sys
import json

if len(sys.argv)!=2:
    print("Enter your name as argument.")
    exit()

data = {"output": f"Hello, {sys.argv[1]}"}
print(json.dumps(data))