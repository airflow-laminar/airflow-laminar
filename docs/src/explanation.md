---
myst:
  heading_anchors: 3
---

# How the packages fit together

## Configuration and execution

`airflow-pydantic` describes DAGs, tasks, hosts, and runtime configuration as models. `airflow-config` composes those models from YAML and can generate Python DAG files or instantiate DAGs while Airflow parses configuration.

The execution boundary depends on the integration. A generated Bash/Cron task executes a command on the Airflow worker. Supervisor manages processes on a local or SSH host. Nomad schedules workloads through its own client agents, while Airflow submits jobs and monitors their allocations.

This distinction determines setup and failure ownership. Generating a Nomad DAG can validate its configuration without a Nomad service; executing it requires a reachable agent and a usable task driver. Cron conversion needs no independent cron daemon because the generated schedule belongs to Airflow.

## Host choice and lifecycle

Balancer selects among configured candidates and gives tasks SSH hooks and pool identifiers. Its pool-manager task reconciles declared concurrency limits. HA adds repeated execution and stop conditions. Neither host labels nor a declared port establish live resource availability; a workload's runtime owns actual processes and sockets.

The meta-package groups compatible dependency ranges so these pieces can be installed together. Nomad and Cron extras add their integrations when selected. External service installation remains a deployment decision.

## Task events and DAG-run alerts

A task callback observes one task instance's success or failure. Priority listens to the enclosing DAG run's running, success, and failure events. A failed task attempt that later succeeds does not necessarily produce a failed DAG run.

The distinction matters for HA and watchdogs: retries or planned restarts can be part of normal lifecycle behavior. The operator and DAG failure policy determine whether the enclosing run fails. Configure task callbacks when the individual event matters, and Priority when the DAG-run outcome is the alerting boundary.

## Logs and validation

Cron commands use Airflow's Bash task logging. Supervisor and Nomad integrations forward configured workload output through their task loggers. An Airflow task log and a backend's full historical output can differ because forwarding has a scope, interval, and lifecycle.

Model, generation, and mocked receiver tests establish the configuration and API contracts. Live validation checks whether a failed workload produces the intended task state, output, callback, and DAG-run event through the running scheduler and task processes. Cron can be checked without an external service; Supervisor and Nomad need their respective runtimes.

The component guides provide the details for log-forwarding settings, watchdog failure handling, and alert delivery.
