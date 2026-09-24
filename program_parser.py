import argparse

class ProgramParser:

    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.subparsers = self.parser.add_subparsers(dest="command")

        info = self.subparsers.add_parser("info")
        info.add_argument("file")

    def parse(self):
        return self.parser.parse_args()


