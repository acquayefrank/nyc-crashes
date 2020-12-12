import sys
import logging

logging.basicConfig(level=logging.DEBUG)

def main(argv):
    logging.info("Hello world!")

if __name__ == "__main__":
    main(sys.argv[1:])
