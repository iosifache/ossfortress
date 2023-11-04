---
sidebar_position: 2
slug: flawfinder
---

import Documentation from '@site/src/components/Documentation';
import VulnsTBD from '@site/src/components/VulnsTBD';

<VulnsTBD>

- `UBUSEC-RECOVERY-OOB`

</VulnsTBD>

<Documentation software="flawfinder" link="https://github.com/david-a-wheeler/flawfinder#readme"/>

## Steps

### Scanning

1. Scan all files in the `portrait/c_modules` folder, generating a SARIF file as output, `/root/analysis/flawfinder.sarif`.
2. Validate each warning produced by flawfinder by manually inspecting the code.
