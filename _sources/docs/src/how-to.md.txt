# How-to guides

## How to install the shared stack

For an existing Airflow environment:

```bash
pip install airflow-laminar
```

For a new Airflow 2 environment:

```bash
pip install airflow-laminar 'airflow-balancer[airflow]'
```

For a new Airflow 3 environment:

```bash
pip install airflow-laminar 'airflow-balancer[airflow3]'
```

The Balancer extras install Airflow and the SSH and standard providers. Install the packages in the environment used by the DAG parser and task processes. Configure the services and command-line tools required by your workloads; see the [runtime reference](reference.md#runtime-requirements).

## How to generate DAGs for an Airflow version

Use a configuration file with the structure in the [tutorial](tutorial.md), then specify the target Airflow version:

```python
from airflow_config import load_config

config = load_config("config", "hello")
config.generate("generated", airflow_major_version=2)
```

Set `airflow_major_version=3` for Airflow 3. Copy generated files into the deployment's configured DAG directory.

For generation during DAG parsing, put the following in a DAG file beside the configuration directory:

```python
from airflow_config import load_config

config = load_config("config", "hello")
config.generate_in_mem(placeholder_dag_id="laminar-generate-dags")
```

Use one generation method per configuration. See the [airflow-config guides](https://airflow-laminar.github.io/airflow-config/docs/src/how-to.html) for composing environments and extensions.

## How to write the same task directly in Python

The equivalent of the tutorial's YAML task is:

```python
from datetime import UTC, datetime

from airflow_pydantic.airflow import DAG, BashOperator

with DAG(
    dag_id="hello",
    start_date=datetime(2025, 1, 1, tzinfo=UTC),
    schedule=None,
    catchup=False,
) as dag:
    BashOperator(task_id="greet", bash_command="echo laminar-ready")
```

Import other operators and models from their component packages. The `airflow_pydantic.airflow` imports work with Airflow 2 and 3; see the [component reference](reference.md#components).

## How to convert a cron job into an Airflow-owned schedule

Save `cron.yaml`:

```yaml
job:
  heartbeat:
    schedule: '*/5 * * * *'
    command: echo cron-ready
```

Load it and generate the DAG:

```python
from airflow_config import Configuration
from airflow_cron import CronAirflowConfiguration, create_dags

cron = CronAirflowConfiguration.load("cron.yaml")
config = Configuration(
    default_dag_args={"start_date": "2025-01-01"},
    dags=create_dags(cron),
)
config.generate("generated", airflow_major_version=3)
```

The generated `heartbeat.py` has a `run` task. Airflow schedules it every five minutes and records its command output in the task log. See the [Cron guides](https://airflow-laminar.github.io/airflow-cron/docs/src/how-to.html) for environment settings, callbacks, and exit-code handling.

## How to choose an integration

| Goal                                                           | Guide                                                               |
| -------------------------------------------------------------- | ------------------------------------------------------------------- |
| Select a worker, build an SSH hook, or reconcile pools         | [Balancer](https://airflow-laminar.github.io/airflow-balancer/)     |
| Keep a DAG running within configured limits                    | [HA](https://airflow-laminar.github.io/airflow-ha/)                 |
| Manage a local or SSH Supervisor workload and forward its logs | [Supervisor](https://airflow-laminar.github.io/airflow-supervisor/) |
| Submit and monitor a Nomad workload                            | [Nomad](https://airflow-laminar.github.io/airflow-nomad/)           |
| Convert cron data to scheduled Airflow tasks                   | [Cron](https://airflow-laminar.github.io/airflow-cron/)             |
| Route DAG-run events to alerting backends                      | [Priority](https://airflow-laminar.github.io/airflow-priority/)     |

For task success and failure events, configure callbacks on the task models. For DAG-run alerts, configure Priority and tag the DAG. The [explanation](explanation.md#task-events-and-dag-run-alerts) describes the different event scopes.
