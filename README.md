# mc-server-config-validator

Starter policy checks for configuration files used in Paper and Velocity deployments. Syntax validation alone is insufficient: add version-aware schema rules and review effective configuration on the target server build.

## Run
Python 3.11+ and PyYAML are required. `python3 validate.py config/` parses YAML and reports policy violations. Extend rules only with keys valid for your declared server versions.

Secrets should be injected at deploy time, never committed. This tool does not prove the server will meet a TPS target. MIT licensed.
