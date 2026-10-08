---
myst:
  heading_anchors: 3
---

# Reference

## Components

| Package               | Role                                                          | Included      |
| --------------------- | ------------------------------------------------------------- | ------------- |
| `airflow-pydantic`    | DAG/task models, rendering, and Airflow compatibility imports | Base          |
| `airflow-config`      | Hydra/YAML composition and DAG generation                     | Base          |
| `airflow-common`      | Shared operators and task helpers                             | Base          |
| `airflow-balancer`    | Host/port selection and configuration viewer                  | Base          |
| `airflow-ha`          | HA cycles, retries, and execution limits                      | Base          |
| `airflow-priority`    | DAG-run listener routing to alert backends                    | Base          |
| `airflow-supervisor`  | Supervisor workload integration                               | Base          |
| `supervisor-pydantic` | Supervisor configuration and RPC client                       | Base          |
| `airflow-nomad`       | Nomad jobs, watchdogs, and allocation logs                    | `nomad` extra |
| `airflow-cron`        | Cron configuration converted to Airflow DAGs                  | `cron` extra  |

The `airflow_laminar` module exposes `__version__`. Public task/model imports come from the component packages.

## Dependency bounds

| Dependency                | Bound            |
| ------------------------- | ---------------- |
| `airflow-balancer`        | `>=0.7.11,<0.8`  |
| `airflow-common`          | `>=0.7.10,<0.8`  |
| `airflow-config`          | `>=1.12.5,<1.13` |
| `airflow-ha`              | `>=1.6.5,<1.7`   |
| `airflow-priority`        | `>=1.6.1,<1.7`   |
| `airflow-pydantic`        | `>=1.7.0,<1.8`   |
| `airflow-supervisor`      | `>=1.10.5,<1.12` |
| `supervisor-pydantic`     | `>=1.4.3,<1.6`   |
| `airflow-nomad` (`nomad`) | `>=0.2,<0.3`     |
| `airflow-cron` (`cron`)   | `>=0.1.1,<0.2`   |

The optional extras are pip dependency groups. Conda users install the available component packages explicitly; pip extras do not create equivalent conda packages.

## Compatibility

The meta-package requires Python >=3.11. It groups Python integrations and does not install Apache Airflow through its base dependencies or the Nomad/Cron extras.

| Environment                                 | Installation path                        | Verification                                                               |
| ------------------------------------------- | ---------------------------------------- | -------------------------------------------------------------------------- |
| Configuration loading and source generation | `airflow-laminar`                        | Models support generation without a running scheduler or managed workload. |
| Airflow 2                                   | Base plus a component's `airflow` extra  | Examples checked on Python 3.11 / Airflow 2.11.2.                          |
| Airflow 3                                   | Base plus a component's `airflow3` extra | Examples checked on Python 3.11 / Airflow 3.3.2.                           |

The Balancer component extras select Airflow `>=2.8,<3` or `>=3,<3.4` and install SSH/standard providers. Each component owns its complete dependency metadata and runtime requirements. Package-install compatibility and DAG construction checks do not establish live workload or scheduler behavior.

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

The meta-package has no command-line entry points. Component commands include `airflow-config`, `airflow-balancer-viewer`, and the SDK tools documented by each package.
