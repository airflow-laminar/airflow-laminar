# Generate a DAG from YAML

Generate an Airflow 3 DAG from a YAML file and inspect its task. Use Python 3.11 or later; the exercise runs locally without a scheduler or managed services.

## Install the packages

In an empty directory:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install airflow-laminar 'airflow-balancer[airflow3]'
```

The shell commands use Linux/macOS syntax.

## Describe the DAG

Create a `config` directory and save `config/hello.yaml`:

```yaml
# @package _global_
_target_: airflow_config.Configuration
default_dag_args:
  start_date: '2025-01-01T00:00:00+00:00'
  catchup: false
dags:
  hello:
    schedule: null
    tasks:
      greet:
        _target_: airflow_pydantic.BashTask
        bash_command: echo laminar-ready
```

## Generate a Python file

Save `generate_dags.py` beside the `config` directory:

```python
from airflow_config import load_config

config = load_config("config", "hello")
config.generate("generated", airflow_major_version=3)
```

Run it:

```bash
python generate_dags.py
```

The `generated` directory contains `hello.py`.

## Inspect the task

Save `inspect_dag.py` beside `generate_dags.py`:

```python
import runpy

namespace = runpy.run_path("generated/hello.py")
dag = namespace["dag"]
print(dag.dag_id)
print(dag.get_task("greet").bash_command)
```

Run it:

```bash
python inspect_dag.py
```

The script prints these lines, alongside any Airflow import messages:

```text
hello
echo laminar-ready
```

To run the DAG, place `generated/hello.py` in an initialized Airflow deployment’s DAG directory. Continue with the [how-to guides](how-to.md) for Airflow 2 generation, direct Python DAGs, and cron conversion.
