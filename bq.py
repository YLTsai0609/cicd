from google.cloud import bigquery
from typing import List

class BQ:
    def __init__(self):
        self.client = bigquery.Client(project='dbhandling')

    def query(
        self,
        sql: str,
        priority: bigquery.QueryPriority = bigquery.QueryPriority.BATCH,
    ) -> List[dict]:
        job_config = bigquery.QueryJobConfig(
            priority=priority,
        )
        query_job = self.client.query(
            query=sql,
            job_config=job_config,
        )
        result = [[row for row in rows] for rows in query_job]
        return result