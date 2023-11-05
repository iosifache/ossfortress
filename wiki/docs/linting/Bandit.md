---
sidebar_position: 1
slug: bandit
---

import Documentation from '@site/src/components/Documentation';
import VulnsTBD from '@site/src/components/VulnsTBD';
import {DefaultSolution} from '@site/src/components/Solution';
import {CLISetup, WebSetup} from '@site/src/components/Setup';

<VulnsTBD>

- `UBUSEC-FIND-CMD`
- `UBUSEC-FLASK-DEBUG`
- `UBUSEC-LOGGING-PERMS`
- `UBUSEC-TAR-SLIP`

</VulnsTBD>

<CLISetup software="Bandit" profile="static-analysis" container="static-analysers"/>

<WebSetup software="Coder" profile="static-analysis" link="http://127.0.0.1:8002" credentials="oss-fortress"/>

<Documentation software="Bandit" link="https://bandit.readthedocs.io/en/latest/index.html"/>

## Steps

### Scanning

1. Scan all files in the `/root/codebase/portrait/portrait` folder, generating an output SARIF file, `/root/analysis/bandit.sarif`.
2. Using `bandit-config-generator`, generate the default configuration for Bandit in `/root/analysis/bandit.conf`.
3. Remove `portrait/c_modules` from the folders to be scanned. Test the created configuration by running Bandit again.
4. Validate each warning produced by Bandit by manually inspecting the code. Use the Coder instance in the Docker infrastructure to review the results.

<DefaultSolution>

1. `bandit --recursive /root/codebase/portrait/portrait --format sarif --o /root/analysis/bandit.sarif`
2. `bandit-config-generator --out /root/analysis/bandit.conf`
3. Add the below configuration to the `/root/analysis/bandit.conf` file and run `bandit --recursive /root/codebase/portrait/portrait --format sarif --o /root/analysis/bandit.sarif --config /root/analysis/bandit.conf`.

```yaml
exclude_dirs:
- portrait/c_modules
```

4. Manual validation

</DefaultSolution>

### Creating a baseline

1. Adapt the command created in the first section to output in the JSON file in `/root/analysis/bandit.baseline.json`.
2. Find the Bandit configuration to use the created JSON file as a baseline. The newly created JSON output file, `/root/analysis/bandit.diff.json`, shouldn't contain any warnings. SARIF is not supported yet in the baselining process.
3. Include a new vulnerability in the code and run the previous command again. Was the secret found?

<DefaultSolution>

1. `bandit --recursive /root/codebase/portrait/portrait/ --format json --o /root/analysis/bandit.baseline.json --config /root/analysis/bandit.conf`
2. `bandit-config-generator --out /root/analysis/bandit.conf`
3. Manual validation

</DefaultSolution>