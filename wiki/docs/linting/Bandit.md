---
sidebar_position: 1
slug: bandit
---

import Documentation from '@site/src/components/Documentation';

<Documentation software="Bandit" link="https://bandit.readthedocs.io/en/latest/index.html"/>

## Vulnerabilities to be discovered

- `UBUSEC-FIND-CMD`
- `UBUSEC-FLASK-DEBUG`
- `UBUSEC-LOGGING-PERMS`
- `UBUSEC-TAR-SLIP`

## Steps

### Scanning

1. Scan all files in the `portrait` folder, generating a SARIF file, `/root/analysis/bandit.sarif`, as output.
2. Using `bandit-config-generator`, generate the default configuration for Bandit in `/root/analysis/bandit.conf`.
3. Remove `portrait/c_modules` from the folders to be scanned. Test the created configuration by running Bandit again.
4. Validate each warning produced by Bandit by manually inspecting the code.

### Creating a baseline

1. Adapt the command created in the first section to output in the JSON file in `/root/analysis/bandit.baseline.json`.
2. Find the Bandit configuration to use the created JSON file as a baseline. The newly created SARIF output, `/root/analysis/bandit.diff.sarif`, file shouldn't contain any warnings.
3. Include a new vulnerability in the code and run the previous command again. Was the secret found?
