---
sidebar_position: 2
slug: osv-scanner
---

import Documentation from '@site/src/components/Documentation';
import VulnsTBD from '@site/src/components/VulnsTBD';
import {CLISetup, WebSetup} from '@site/src/components/Setup';
import {DefaultSolution} from '@site/src/components/Solution';
import {SolutionsNote} from '@site/src/components/BeginnerContent';

<VulnsTBD>

- `UBUSEC-PILLOW-OOB`

</VulnsTBD>

<CLISetup software="OSV-Scanner" profile="static-analysis" container="static-analysers"/>

<WebSetup software="Coder" profile="static-analysis" link="http://127.0.0.1:8002" credentials="oss-fortress"/>

<Documentation software="OSV-Scanner" link="https://google.github.io/osv-scanner/"/>

<SolutionsNote/>

## Steps

### Scanning for vulnerabilities

1. Based on your knowledge about Sand Castle, find out all files listing the dependencies of the application.
2. For each of them, create an OSV-Scanner command to scan it and to output the results in a SARIF file, `/root/analysis/<listing_id>.sarif`.

<DefaultSolution>

1. `/root/codebase/sandcastle/poetry.lock`
2. `osv-scanner --lockfile /root/codebase/sandcastle/poetry.lock --format sarif --output /root/analysis/pip.sarif`

</DefaultSolution>

### Validating the reported warnings

1. Validate in the code that functions related to the reported vulnerabilities are called. Use the Coder instance in the Docker infrastructure to review the results.

<DefaultSolution>

1. Manual validation

</DefaultSolution>

### Ignoring the false positives with a configuration file

1. Create an OSV-Scanner configuration file in `/root/analysis/osv-scanner.conf`
2. Specify the configuration file to the previously constructed OSV-Scanner command.
3. Using the configuration file, ignore all vulnerabilities that don't apply for the codebase of Sand Castle. For each of them, specify the reason.

<DefaultSolution>

1. `touch /root/analysis/osv-scanner.conf`
2. `osv-scanner --lockfile /root/codebase/sandcastle/poetry.lock --format sarif --output /root/analysis/pip.sarif`
3. Use the next configuration:

    ```ini
    [[IgnoredVulns]]
    id = "GHSA-j7hp-h8jx-5ppr"
    reason = "The backend is not processing HTML file with Pillow."

    [[IgnoredVulns]]
    id = "PYSEC-2023-175"
    reason = "Duplicate of GHSA-56pw-mpj4-fxww"
    ```

</DefaultSolution>
