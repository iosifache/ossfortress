---
sidebar_position: 2
slug: gitleaks
---

import Documentation from '@site/src/components/Documentation';
import VulnsTBD from '@site/src/components/VulnsTBD';
import {CLISetup, WebSetup} from '@site/src/components/Setup';
import {DefaultSolution} from '@site/src/components/Solution';
import {SolutionsNote} from '@site/src/components/BeginnerContent';

<VulnsTBD>

- `VULN-FLASK-SECRETS`

</VulnsTBD>

<CLISetup software="Gitleaks" profile="static-analysis" container="static-analysers"/>

<WebSetup software="Coder" profile="static-analysis" link="http://127.0.0.1:8002" credentials="oss-fortress"/>

<Documentation software="Gitleaks" link="https://github.com/gitleaks/gitleaks#readme"/>

<SolutionsNote/>

## Steps

### Scanning for leaked secrets

1. Create a Gitleaks command to check the repository for leaked secrets and dump the warnings in a SARIF file, `/root/analysis/gitleaks.sarif`.
2. Find a way to redact the secrets in the Gitleaks output.
3. For each warning produced by Gitleaks, check if it is valid by using `git`. Use the Coder instance in the Docker infrastructure to review the results.

<DefaultSolution>

1. `gitleaks --no-banner detect --report-format sarif --source /root/codebase --report-path /root/analysis/gitleaks.sarif`
2. `--redact`
3. Manual validation

</DefaultSolution>

### Defining custom formats for secrets

1. For all unidentified secrets from the codebase, create a custom Regex rule in a Gitleak configuration file, `/root/analysis/gitleaks.toml`.
2. Find the configuration aspect that should be set to also keep the previously detected results.

<DefaultSolution>

1. Run the command `gitleaks --no-banner detect --report-format sarif --source /root/codebase --report-path /root/analysis/gitleaks.sarif --redact --config /root/analysis/gitleaks.toml` after creating the following configuration file in `/root/analysis/gitleaks.toml`:

    ```toml
        title = "Gitleaks configuration for Sand Castle"

        [[rules]]
        description = "hardcoded Flask key"
        file = '''^(.*?)\.py$'''
        regex = '''^[^\W0-9]\w*\.secret_key = '''
        tags = ["secret", "hardcoded", "python"]

        [[rules.Entropies]]
        Min = "3"
        Max = "7"
        Group = "1"
    ```

2. Append a new section in the previosly created file:

    ```toml
        [extend]
        useDefault = true
    ```

</DefaultSolution>

### Creating a baseline

1. Adapt the command created in the first section to output in the JSON file in `/root/analysis/gitleaks.baseline.json`.
2. Find the Gitleaks configuration to use the created JSON file as a baseline. The newly created SARIF output, `/root/analysis/gitleaks.diff.sarif`, file shouldn't contain any warnings.
3. Include a new secret in the code and run the previous command again. Was the secret found?

<DefaultSolution>

1. `gitleaks --no-banner detect --report-format json --source /root/codebase --report-path /root/analysis/gitleaks.baseline.json --redact --config /root/analysis/gitleaks.toml`
2. `gitleaks --no-banner detect --report-format sarif --source /root/codebase --report-path /root/analysis/gitleaks.sarif --redact --config /root/analysis/gitleaks.toml --baseline-path /root/analysis/gitleaks.baseline.json`
3. Manual validation

</DefaultSolution>
