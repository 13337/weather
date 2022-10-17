#!/usr/bin/python3
import subprocess

def main():
    process = subprocess.Popen(['weather'],stdout=subprocess.PIPE)
    out, err = process.communicate()
    out = out.decode()
    out = out.strip("\n")
    out = out.split("-")
    out = out[0]
    out = out.lstrip()
    out = out.rstrip()
    print(out)

if __name__ == "__main__":
    main()
