import boto3
import logging
import argparse

logging.basicConfig(level=logging.DEBUG)

parser = argparse.ArgumentParser(description="Configure")

parser.add_argument(
    "--Region",
    type=str,
    metavar="Region",
    help="Region",
)
def get_services() -> None:
    """Retrieve all deployed AWS Services"""
    client =  boto3.client("resourcegroupstaggingapi", region_name=args.Region)
    resources = client.resources()
    for resource in resources["ResourcetagMappingList"]:
        split_resource = resource["ResourceARN"].split(":")
    logging.DEBUG(split_resource)

if __name__ == "__main__":
    args = parser.parse_args()