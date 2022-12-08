import argparse
import logging
import os

import boto3

logging.basicConfig(level=logging.DEBUG)

parser = argparse.ArgumentParser(description="Configure")

parser.add_argument(
    "--Serial_number",
    type=str,
    metavar="Serial_number",
    help="Serial_number",
)
parser.add_argument(
    "--Token",
    type=str,
    metavar="Token",
    help="Token",
)
parser.add_argument(
    "--Region",
    type=str,
    metavar="Region",
    help="Region",
)


def get_services() -> None:
    """Retrieve all deployed AWS Services"""
    client = boto3.client("resourcegroupstaggingapi", region_name=args.Region)
    resources = client.get_resources()
    for resource in resources["ResourcetagMappingList"]:
        split_resource = resource["ResourceARN"].split(":")
    logging.DEBUG(split_resource)


def set_env_vars() -> None:
    """Authenticate to AWS and set Vars"""
    client = boto3.client("sts", region_name=args.Region)
    response = client.get_session_token(
        SerialNumber=args.Serial_number, TokenCode=args.Token
    )
    logging.debug(response)
    os.environ["AWS_ACCESS_KEY_ID"] = str(response["Credentials"]["AccessKeyId"])
    os.environ["AWS_SECRET_ACCESS_KEY"] = str(response["Credentials"]["SecretAccessKey"])
    os.environ["AWS_SESSION_TOKEN"] = str(response["Credentials"]["SessionToken"])


if __name__ == "__main__":
    args = parser.parse_args()
    set_env_vars()
    get_services()
