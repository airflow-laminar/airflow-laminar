---
myst:
  heading_anchors: 3
---

# How the packages fit together

## Configuration and execution

`airflow-pydantic` describes DAGs, tasks, hosts, and runtime configuration as models. `airflow-config` composes those models from YAML and can generate Python DAG files or instantiate DAGs while Airflow parses configuration.

Bash and Cron commands run on Airflow workers. Supervisor manages processes on a local or SSH host. Nomad schedules workloads through its own client agents, while Airflow submits jobs and monitors their allocations.

## Host choice and lifecycle

Balancer selects configured hosts and supplies SSH hooks and pool names. Its pool-manager task reconciles declared concurrency limits. HA adds repeated execution and stop conditions. Host labels and port declarations describe configuration. The workload runtime controls the processes and sockets.

`pip install airflow-laminar` installs the component packages with compatible dependency bounds. Set up the external services needed by the workloads you choose to run.

## Task events and DAG-run alerts

A task callback observes one task instance's success or failure. Priority listens to the enclosing DAG run's running, success, and failure events. A failed task attempt that later succeeds does not necessarily produce a failed DAG run.

With HA and watchdogs, retries or planned restarts can be normal. The operator and DAG failure policy determine whether the run fails. Use task callbacks for individual task events and Priority for DAG-run outcomes.

## Logs and validation

Cron commands use Airflow's Bash task logging. Supervisor and Nomad integrations forward configured workload output through their task loggers. Forwarded logs cover the output selected by the integration during the task’s lifetime. The backend may retain additional history.

Model and generation tests check configuration and generated DAGs. Mocked receiver tests check alert routing. Live validation checks whether a failed workload produces the intended task state, output, callback, and DAG-run event through the running scheduler and task processes.
