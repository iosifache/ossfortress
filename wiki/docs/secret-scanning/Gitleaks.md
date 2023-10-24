---
sidebar_position: 1
slug: exercise
---

:::info

The Gitleaks configuration is available [here](https://github.com/gitleaks/gitleaks#readme).

:::

## Scanning for leaked secrets

1. Create a Gitleaks command to check the repository for leaked secrets and dump the warnings in a SARIF file, `/analysis/gitleaks.sarif`.
2. Find a way to redact the secrets in the Gitleaks output.

## Validating the warnings

1. For each warning produced by Gitleaks, check if it is valid by using `git`.`

## Defining custom formats for secrets

1. For all unidentified secrets from the codebase, create a custom Regex rule in a Gitleak configuration file.
2. Find the configuration aspect that should be set to also keep the previously detected results.

## Creating a baseline

1. Adapt the command created in the first section to output in the JSON file in `/analysis/gitleaks.baseline.json`.
2. Find the Gitleaks configuration to use the created JSON file as a baseline. The newly created SARIF output, `/analysis/gitleaks.diff.sarif`, file shouldn't contain any warnings.
3. Include a new secret in the code and run the previous command again. Was the secret found?
