#!/usr/bin/env python3

import sys

def main():
    if len(sys.argv) < 3:
        print("No se han pasado parámetros, modo interactivo\n")
        url = input("Introduce la URL: ").strip()
        queue = input("Introduce el valor de queue: ").strip()
    else:
        url = sys.argv[1]
        queue = sys.argv[2]

    print(f"URL: {url}")
    print(f"Queue: {queue}")

if __name__ == "__main__":
    main()
