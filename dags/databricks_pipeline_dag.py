from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime

with DAG(
    dag_id="ecommerce_data_pipeline",
    start_date=datetime(2026, 7, 1),
    schedule="@daily",
    catchup=False,
    tags=["ecommerce", "databricks"],
) as dag:

    start = EmptyOperator(task_id="start")

    bronze = EmptyOperator(task_id="01_bronze_ingestion")

    silver = EmptyOperator(task_id="02_silver_transformation")

    gold = EmptyOperator(task_id="03_gold_transformation")

    quality = EmptyOperator(task_id="04_data_quality_checks")

    incremental = EmptyOperator(task_id="05_incremental_load")

    end = EmptyOperator(task_id="end")

    start >> bronze >> silver >> gold >> quality >> incremental >> end