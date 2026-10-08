import ast

import pytest
from airflow_config import Configuration

cron = pytest.importorskip("airflow_cron")


def test_cron_configuration_generates_airflow_task(tmp_path):
    declaration = cron.CronAirflowConfiguration.model_validate({"job": {"heartbeat": {"schedule": "*/5 * * * *", "command": "echo cron-ready"}}})
    config = Configuration(default_dag_args={"start_date": "2025-01-01"}, dags=cron.create_dags(declaration))
    config.generate(tmp_path, airflow_major_version=3)

    source = ast.parse((tmp_path / "heartbeat.py").read_text())
    tasks = [node for node in ast.walk(source) if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "BashOperator"]
    assert len(tasks) == 1
    arguments = {keyword.arg: ast.literal_eval(keyword.value) for keyword in tasks[0].keywords if keyword.arg in ("task_id", "bash_command")}
    assert arguments["task_id"] == "run"
    assert arguments["bash_command"] == "echo cron-ready"
