---
sidebar_position: 1
slug: osv-scanner
---

:::info

The OSV-Scanner documentation is available [here](https://google.github.io/osv-scanner/).

:::


## Vulnerabilities to be discovered

- `UBUSEC-PILLOW-OOB`

## Steps

### Scanning for vulnerabilities

1. Based on your knowledge about Ubuntu Portrait, find out all files listing the dependencies of the application.
2. For each of them, create an OSV-Scanner command to scan it and to output the results in a SARIF file, `/analysis/<listing_id>.sarif`.

### Validating the reported warnings

3. Validate in the code that functions related to the reported vulnerabilities are called.

### Ignoring the false positives with a configuration file

1. Create an OSV-Scanner configuration file.
2. Specify the configuration file to the previously constructed OSV-Scanner command.
3. Using the configuration file, ignore all vulnerabilities that don't apply for the codebase of Ubuntu Portrait. For each of them, specify the reason.