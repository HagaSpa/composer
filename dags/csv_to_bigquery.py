from airflow import DAG
from airflow.contrib.operators.dataflow_operator import DataflowTemplateOperator
from datetime import datetime, timedelta
from airflow import models

PROJECT_ID = models.Variable.get('project_id')
BUCKET_NAME = models.Variable.get('gcs_bucket_name')
DAG_NAME = 'csv_to_bigquery'

yesterday = datetime.combine(
    datetime.today() - timedelta(days=1) + timedelta(hours=9),
    datetime.min.time()
)

default_dag_args = {
    'owner': 'HagaSpa',
    'start_date': yesterday,
    'project_id': PROJECT_ID,
    'dataflow_default_options': {
        'project': PROJECT_ID,
    }
}

with models.DAG(
    dag_id=DAG_NAME,
    schedule_interval="@once",
    default_args=default_dag_args) as dag:
    
        t1 = DataflowTemplateOperator(
            task_id='task1',
            template='gs://dataflow-templates/latest/GCS_Text_to_BigQuery',
            parameters={
                'javascriptTextTransformFunctionName': 'transform',                                    # udf.jsファイルにある呼び出したいメソッド名
                'JSONPath': 'gs://{}/composer/schema/schema.json'.format(BUCKET_NAME),                 # bqのスキーマ定義ファイルのgcsパス
                'javascriptTextTransformGcsPath': 'gs://{}/composer/udf/udf.js'.format(BUCKET_NAME),   # udf.jsファイルのgcsパス
                'inputFilePattern': 'gs://{}/composer/csv/sample.csv'.format(BUCKET_NAME),             # bqへ投入するcsvファイルのgcsパス
                'outputTable': '{}:my_dataset.sample'.format(PROJECT_ID),                              # 保存するbqのプロジェクトid:データセット名.テーブル名
                'bigQueryLoadingTemporaryDirectory': 'gs://{}/composer/temp'.format(BUCKET_NAME),      # bqへのロード中のtempディレクトリ
            },
        )
    
    