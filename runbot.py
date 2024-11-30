import argparse
from dotenv import load_dotenv
import os
from hypebot import HypeSquad


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='HypeSquad')
    parser.add_argument(
        '--sync',
        action=argparse.BooleanOptionalAction,
        default=False,
        help='Sync the tree with the guild',
    )
    return parser.parse_args()


def get_token() -> str:
    load_dotenv()
    token = os.getenv('DISCORD_TOKEN')
    if token is None:
        raise ValueError(
            "DISCORD_TOKEN environment variable is not set. "
            "Please create a .env file with your Discord token or set the environment variable."
        )
    return token


if __name__ == '__main__':
    token = get_token()
    args = parse_args()

    client = HypeSquad(sync=args.sync)
    client.run(token)
