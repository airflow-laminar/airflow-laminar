---
myst:
  heading_anchors: 3
---

# Reference

## Components

| Package               | Role                                                          |
| --------------------- | ------------------------------------------------------------- |
| `airflow-pydantic`    | DAG/task models, rendering, and Airflow compatibility imports |
| `airflow-config`      | Hydra/YAML composition and DAG generation                     |
| `airflow-common`      | Shared operators and task helpers                             |
| `airflow-balancer`    | Host/port selection and configuration viewer                  |
| `airflow-ha`          | HA cycles, retries, and execution limits                      |
| `airflow-priority`    | DAG-run listener routing to alert backends                    |
| `airflow-supervisor`  | Supervisor workload integration                               |
| `airflow-nomad`       | Nomad jobs, watchdogs, and allocation logs                    |
| `airflow-cron`        | Cron configuration converted to Airflow DAGs                  |
| `supervisor-pydantic` | Supervisor configuration and RPC client                       |
| `nomad-pydantic`      | Nomad job models and client tools                             |
| `cron-pydantic`       | Cron configuration models                                     |

The `airflow_laminar` module exposes `__version__`. Import tasks and models from the component packages.

## Dependency bounds

| Dependency            | Bound            |
| --------------------- | ---------------- |
| `airflow-balancer`    | `>=0.7.11,<0.8`  |
| `airflow-common`      | `>=0.7.10,<0.8`  |
| `airflow-config`      | `>=1.12.5,<1.13` |
| `airflow-cron`        | `>=0.1.1,<0.2`   |
| `airflow-ha`          | `>=1.6.5,<1.7`   |
| `airflow-nomad`       | `>=0.2,<0.3`     |
| `airflow-priority`    | `>=1.6.1,<1.7`   |
| `airflow-pydantic`    | `>=1.7.0,<1.8`   |
| `airflow-supervisor`  | `>=1.10.5,<1.12` |
| `cron-pydantic`       | `>=0.1.0,<0.2`   |
| `nomad-pydantic`      | `>=0.2.0,<0.3`   |
| `supervisor-pydantic` | `>=1.4.3,<1.6`   |

## Compatibility

`airflow-laminar` requires Python >=3.11 and installs all components listed above. Install Apache Airflow through a component’s `airflow` or `airflow3` extra, or use an existing Airflow environment.

| Environment                                 | Installation path                                     | Verification                                                               |
| ------------------------------------------- | ----------------------------------------------------- | -------------------------------------------------------------------------- |
| Configuration loading and source generation | `airflow-laminar`                                     | Models support generation without a running scheduler or managed workload. |
| Airflow 2                                   | `airflow-laminar` plus a component's `airflow` extra  | Examples checked on Python 3.11 / Airflow 2.11.2.                          |
| Airflow 3                                   | `airflow-laminar` plus a component's `airflow3` extra | Examples checked on Python 3.11 / Airflow 3.3.2.                           |

The Balancer component extras select Airflow `>=2.8,<3` or `>=3,<3.4` and install SSH/standard providers. Component packages declare their provider requirements and supported versions. The checks above cover installation and DAG construction; running workloads requires the services listed below.

## Runtime requirements

| Integration                   | External runtime                                                                                                  |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| Configuration/model rendering | Python packages; a running Airflow scheduler is not needed.                                                       |
| Cron conversion               | Airflow executes commands on its task worker. No system cron daemon is needed for these generated DAGs.           |
| Local Supervisor              | Supervisor tools/processes on the managed host, with access to the configured working directory and RPC endpoint. |
| SSH Supervisor                | SSH access and Supervisor on the remote managed host.                                                             |
| Nomad                         | Nomad CLI and a reachable Nomad agent/cluster with an eligible client and the job's task driver.                  |
| Priority delivery             | The chosen backend SDK and receiver credentials.                                                                  |

A Nomad development agent runs client and server roles in one process. The [Nomad tutorial](https://airflow-laminar.github.io/airflow-nomad/docs/src/tutorial.html) includes that setup and the task driver used by its example.

## Entry points

The meta-package has no command-line entry points. Component commands include `airflow-config` and `airflow-balancer-viewer`; each SDK documents its own commands.
