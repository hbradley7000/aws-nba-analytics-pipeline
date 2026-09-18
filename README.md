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
