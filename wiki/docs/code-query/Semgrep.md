---
sidebar_position: 1
slug: semgrep
---

import Documentation from '@site/src/components/Documentation';
import VulnsTBD from '@site/src/components/VulnsTBD';
import {CLISetup, WebSetup} from '@site/src/components/Setup';

<VulnsTBD>

- `UBUSEC-FLASK-DEBUG`
- `UBUSEC-TAR-SLIP`
- `UBUSEC-LOGGING-PERMS`
- `UBUSEC-SECRET-LOG`
- `UBUSEC-UID-IDOR`
- `UBUSEC-ARCHIVE-WRITE`
- `UBUSEC-HASH-LEN`

</VulnsTBD>

<CLISetup software="Semgrep" profile="static-analysis" container="static-analysers"/>

<WebSetup software="Coder" profile="static-analysis" link="http://127.0.0.1:8002"/>

<Documentation software="Semgrep" link="https://semgrep.dev/docs"/>

## Steps

### Scanning

1. Create a Semgrep command that scans the entire codebase with the default configuration (`auto`) and creates a SARIF output file, `/root/analysis/semgrep.sarif`.
2. Validate each warning produced by Semgrep by manually inspecting the code. Use the Coder instance in the Docker infrastructure to review the results.

### Writing rules

:::info

For live testing your rules, you an also use [the Playground](https://semgrep.dev/playground/new).

:::

1. The vulnerabilityies listed below were not detected by any technique that we've seen so far. Inspect [the Semgrep documentation](/ubuntu-portrait/vulnerabilities) and write rules to catch them. The rules should have as many metadata fields filled as possible.

| Vulnerability ID       | Hints on how to catch it with Semgrep                                             |
| ---------------------- | --------------------------------------------------------------------------------- |
| `UBUSEC-SECRET-LOG`    | Calls to functions from `logging` where the parameters have sensitive names       |
| `UBUSEC-UID-IDOR`      | `execute_string_command` calls with dynamic arguments                             |
| `UBUSEC-ARCHIVE-WRITE` | `os.path.join` calls where the arguments came from the parameters of the function |
| `UBUSEC-HASH-LEN`      | `sha256_update` calls where the parameter is created by concatenation             |

2. Place the rules that you created in `/root/analysis/semgrep-rules` and modify the command from the first section to use them and to save the resulting SARIF file in `/root/analysis/semgrep.custom.sarif`.
