import boto3
import logging
import os
import argparse

logging.basicConfig(level=logging.DEBUG)

parser = argparse.ArgumentParser(description="Configure")

parser.add_argument(
    "--Region",
    type=str,
    metavar="Region",
    help="Region",
)
parser.add_argument(
    "--Serial_number",
    type=str,
    metavar="Serial_number",
    help="Serial_number",
)
def set_env_vars() -> None:
    """Authenticate to AWS and set Vars"""
    client =  boto3.client("sts", region_name=args.Region)
    response = client.get_session_token(
    SerialNumber=args.Serial_number,
    TokenCode=args.Token
)
    logging.debug(response)
    os.putenv("AccessKeyId" , response["Credentials"]["AccessKeyId"])
    os.putenv("SecretAccessKey" , response["Credentials"]["SecretAccessKey"])
    os.putenv("TokenCode" , response["Credentials"]["TokenCode"])


if __name__ == "__main__":
    args = parser.parse_args()