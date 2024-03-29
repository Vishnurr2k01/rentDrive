from cli_utils.logger.logger import setup_logger
import argparse , sys
from cli_utils import process
p= setup_logger()

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="RentDrive Application")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    add_parser = subparsers.add_parser("add", help="Add files")
    add_parser.add_argument("path", nargs="+", help="Paths to add")
    # add_parser.add_argument("token",help="authentication token" )
    subparsers.add_parser("status", help="Check status")
    subparsers.add_parser("pull", help="Pull files")
    commit_parser = subparsers.add_parser("push",help="Ready to push")
    commit_parser.add_argument("token",help="Auth token")

    args = parser.parse_args()

    if args.command == "add":
        if not args.path:
            p.error("please pass arguments path")
            sys.exit(1)
        p.info("rentdrive add %s"%args.path)
        process.add(args.path)
    elif args.command == "pull":
        process.pull()
    elif args.command == "push":
        if not args.token:
            p.error("Invalid token")
            sys.exit(1)
        process.push()
        
        
     
