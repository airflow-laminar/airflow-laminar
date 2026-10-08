# Generate a DAG from YAML

Create a configuration file, generate an Airflow 3 DAG, and inspect its task. This exercise needs Python 3.11 or later. It does not run a scheduler or require Supervisor or Nomad services.

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

Place `generated/hello.py` in the DAG directory of an initialized Airflow deployment when you are ready to schedule or trigger it. Continue with the [how-to guides](how-to.md) for Airflow 2 generation, direct Python DAGs, and cron conversion.
