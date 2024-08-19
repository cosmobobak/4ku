# TREE-SITTER MINIFIER VERSION 1.0.0
# This script is used to perform a symbol-minification pass on a given C++ file.
# It uses the tree-sitter library to parse the file and then performs a
# symbol-minification pass on the tree.

import argparse
import os
import tree_sitter as ts
import tree_sitter_cpp as cpp
from tree_sitter import Language, Parser

FOURKU_PATH = "src/main.cpp"
CPP_LANGUAGE = Language(cpp.language())

def test():
    parser = Parser(language = CPP_LANGUAGE)
    with open(FOURKU_PATH, mode = "rb") as f:
        data = f.read()
    tree = parser.parse(data)
    
    new_tree = minify(tree)

    # get the source code from the new tree
    source_code = new_tree.root_node.to_sexp()

    # print the source code
    print(source_code)

def get_args():
    parser = argparse.ArgumentParser(description="C++ minifier")
    parser.add_argument("path", help="Path to source file")
    parser.add_argument("--tokens", action="store_true", help="Print tokens")
    parser.add_argument("--output", action="store_true", help="Print minified")
    parser.add_argument("--types", action="store_true", help="Print types")
    parser.add_argument("--names", action="store_true", help="Print names")
    return parser.parse_args()

def get_source(path: str) -> str:
    with open(path, "r") as f:
        return f.read()

def main():
    args = get_args()

    if not args.path:
        print("Path is required")
        return

    if not os.path.exists(args.path):
        print("File doesn't exist")
        return

    src: str = get_source(args.path)

    if args.output:
        res = minify(src)
        # write to file
        with open(args.output, "w") as f:
            f.write(res)
    else:
        print(minify(src))


if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()