# Frogbot Race Condition Reproduction

Test project to reproduce the Contextual Analysis race condition in Frogbot scan-pull-request.

## Setup
- Watch: `piyushkgitwatch` with policy `skipapplicablecves` (`applicable_cves_only: true`)
- Dependencies: pyyaml 5.3.1, jinja2 3.0.0, werkzeug 1.0.0, flask 1.0
- Source code uses safe patterns (yaml.safe_load, autoescape=True)
