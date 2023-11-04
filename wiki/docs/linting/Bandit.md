---
sidebar_position: 1
slug: bandit
---

import Documentation from '@site/src/components/Documentation';
import VulnsTBD from '@site/src/components/VulnsTBD';
import {CLISetup, WebSetup} from '@site/src/components/Setup';

<VulnsTBD>

- `UBUSEC-FIND-CMD`
- `UBUSEC-FLASK-DEBUG`
- `UBUSEC-LOGGING-PERMS`
- `UBUSEC-TAR-SLIP`

</VulnsTBD>

<CLISetup software="Bandit" profile="static-analysis" container="static-analysers"/>

<WebSetup software="Coder" profile="static-analysis" link="http://127.0.0.1:8002"/>

<Documentation software="Bandit" link="https://bandit.readthedocs.io/en/latest/index.html"/>

## Steps

### Scanning

1. Scan all files in the `portrait` folder, generating a SARIF file, `/root/analysis/bandit.sarif`, as output.
2. Using `bandit-config-generator`, generate the default configuration for Bandit in `/root/analysis/bandit.conf`.
3. Remove `portrait/c_modules` from the folders to be scanned. Test the created configuration by running Bandit again.
4. Validate each warning produced by Bandit by manually inspecting the code. Use the Coder instance in the Docker infrastructure to review the results.

### Creating a baseline

1. Adapt the command created in the first section to output in the JSON file in `/root/analysis/bandit.baseline.json`.
2. Find the Bandit configuration to use the created JSON file as a baseline. The newly created SARIF output, `/root/analysis/bandit.diff.sarif`, file shouldn't contain any warnings.
3. Include a new vulnerability in the code and run the previous command again. Was the secret found?
