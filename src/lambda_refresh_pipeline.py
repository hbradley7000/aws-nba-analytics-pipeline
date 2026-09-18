import os
import time
from datetime import datetime

import boto3


# AWS service clients
glue = boto3.client("glue")
quicksight = boto3.client("quicksight")


def lambda_handler(event, context):

    # Configuration stored as Lambda environment variables
    game_info_crawler = os.environ["GAME_INFO_CRAWLER"]
    game_crawler = os.environ["GAME_CRAWLER"]
    dataset_id = os.environ["QUICKSIGHT_DATASET_ID"]
    account_id = os.environ["AWS_ACCOUNT_ID"]

    # Start AWS Glue crawlers
    glue.start_crawler(Name=game_info_crawler)
    glue.start_crawler(Name=game_crawler)

    # Allow time for crawler execution
    time.sleep(120)

    # Generate unique QuickSight ingestion ID
    current_time = datetime.now().strftime("%Y%m%d%H%M%S%f")
    ingestion_id = f"ingestion-{current_time}"

    # Refresh QuickSight dataset
    response = quicksight.create_ingestion(
        AwsAccountId=account_id,
        DataSetId=dataset_id,
        IngestionId=ingestion_id
    )

    print("QuickSight ingestion started:", response)

    return {
        "statusCode": 200,
        "body": "Files successfully sent to AWS Glue and QuickSight refresh started."
    }
