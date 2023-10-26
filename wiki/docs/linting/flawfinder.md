---
sidebar_position: 2
slug: flawfinder
---

:::info

The flawfinder documentation is available [here](https://github.com/david-a-wheeler/flawfinder#readme).

:::

## Vulnerabilities to be discovered

- `UBUSEC-RECOVERY-OOB`

## Steps

### Scanning

1. Scan all files in the `portrait/c_modules` folder, generating a SARIF file as output.
2. Validate each warning produced by Fflawfinder by manually inspecting the code.