---
sidebar_position: 2
slug: flawfinder
---

import Documentation from '@site/src/components/Documentation';
import VulnsTBD from '@site/src/components/VulnsTBD';
import {DefaultSolution} from '@site/src/components/Solution';
import {CLISetup, WebSetup} from '@site/src/components/Setup';

<VulnsTBD>

- `UBUSEC-RECOVERY-OOB`

</VulnsTBD>

<CLISetup software="flawfinder" profile="static-analysis" container="static-analysers"/>

<WebSetup software="Coder" profile="static-analysis" link="http://127.0.0.1:8002" credentials="ossfortress"/>

<Documentation software="flawfinder" link="https://github.com/david-a-wheeler/flawfinder#readme"/>

## Steps

### Scanning

1. Scan all files in the `portrait/c_modules` folder, generating a SARIF file as output, `/root/analysis/flawfinder.sarif`.
2. Validate each warning produced by flawfinder by manually inspecting the code. Use the Coder instance in the Docker infrastructure to review the results.

<DefaultSolution>

1. `flawfinder --sarif /root/codebase/portrait/portrait/c_modules/ > /root/analysis/flawfinder.sarif`
2. Manual validation

</DefaultSolution>