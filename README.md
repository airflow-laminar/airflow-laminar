# airflow-laminar

A compatible set of packages for configuring Airflow DAGs, selecting workers, supervising workloads, and routing DAG-run alerts. Import models and operators from their owning packages: `airflow_config`, `airflow_pydantic`, `airflow_supervisor`, and the other integrations.

[![Build Status](https://github.com/airflow-laminar/airflow-laminar/actions/workflows/build.yaml/badge.svg?branch=main&event=push)](https://github.com/airflow-laminar/airflow-laminar/actions/workflows/build.yaml)
[![codecov](https://codecov.io/gh/airflow-laminar/airflow-laminar/branch/main/graph/badge.svg)](https://codecov.io/gh/airflow-laminar/airflow-laminar)
[![License](https://img.shields.io/github/license/airflow-laminar/airflow-laminar)](https://github.com/airflow-laminar/airflow-laminar)
[![PyPI](https://img.shields.io/pypi/v/airflow-laminar.svg)](https://pypi.python.org/pypi/airflow-laminar)

```bash
pip install airflow-laminar
```

The base package installs the shared models, configuration loader, common tasks, Balancer, HA, Priority, Supervisor, Nomad, and Cron integration.

```bash

Install the appropriate Airflow/provider extra from a component package when creating an Airflow environment. See [installation and compatibility](docs/src/reference.md).

- [Tutorial: generate a DAG from YAML](docs/src/tutorial.md)
- [How-to guides: install, generate DAGs, and convert cron jobs](docs/src/how-to.md)
- [Reference: package roles, dependency bounds, and runtime requirements](docs/src/reference.md)
- [Explanation: configuration, execution, logs, and alerts](docs/src/explanation.md)

[Documentation](https://airflow-laminar.github.io/airflow-laminar/) · [Source](https://github.com/airflow-laminar/airflow-laminar) · [Issues](https://github.com/airflow-laminar/airflow-laminar/issues)
```
