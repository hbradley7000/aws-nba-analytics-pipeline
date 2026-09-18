# aws-nba-analytics-pipeline
Serverless AWS data pipeline for NBA analytics using S3, Lambda, Glue, Athena, QuickSight, Python, and SQL.

## Architecture

The project used a serverless AWS analytics pipeline:

```text
External NBA Data
        ↓
     Amazon S3
        ↓
     AWS Lambda
        ↓
 AWS Glue Crawler
        ↓
AWS Glue Data Catalog
        ↓
   Amazon Athena
        ↓
 Amazon QuickSight
```

NBA game data was stored in Amazon S3, AWS Lambda triggered Glue crawlers to update the data catalog, Athena was used to query the data, and QuickSight provided the visualization layer.

## AWS Services Used

- **Amazon S3** — Stored the NBA game and team datasets used as the source layer for the analytics pipeline.
- **AWS Lambda** — Automated the workflow by triggering AWS Glue crawlers and initiating the QuickSight dataset refresh.
- **AWS Glue Crawler** — Scanned data stored in S3 and updated table metadata.
- **AWS Glue Data Catalog** — Maintained metadata and table definitions used by Athena.
- **Amazon Athena** — Queried and joined NBA datasets using SQL.
- **Amazon QuickSight** — Visualized NBA metrics and created the final analytics dashboard.
- **AWS IAM** — Managed permissions between services and users within the AWS environment.
- **Python / boto3** — Used inside Lambda to automate AWS service interactions.
- **SQL** — Used in Athena to query and combine the NBA datasets.

## Team Project & My Contributions

This project was completed collaboratively as part of a cloud engineering course at Saint Mary's College of California. The team designed and implemented a serverless AWS analytics pipeline for NBA data.

My primary contributions included:

- **AWS Lambda** — Configured and developed the Python/boto3 Lambda workflow used to trigger AWS Glue crawlers and initiate the QuickSight dataset refresh.
- **AWS IAM** — Configured IAM roles and permissions to support communication between Lambda, Glue, Athena, and S3.
- **AWS Glue Crawlers** — Configured crawlers to scan NBA data stored in S3 and update table metadata in the AWS Glue Data Catalog.
- **Amazon Athena** — Developed SQL queries to join and analyze NBA game and team-level datasets using the tables cataloged through AWS Glue.
