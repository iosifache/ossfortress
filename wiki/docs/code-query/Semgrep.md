---
sidebar_position: 2
slug: semgrep
---

:::info

The Semgrep documentation is available [here](https://semgrep.dev/docs).

:::

## Vulnerabilities to be discovered

- `UBUSEC-FLASK-DEBUG`
- `UBUSEC-TAR-SLIP`
- `UBUSEC-LOGGING-PERMS`
- `UBUSEC-SECRET-LOG`
- `UBUSEC-UID-IDOR`
- `UBUSEC-ARCHIVE-WRITE`
- `UBUSEC-HASH-LEN`

## Steps

### Scanning

1. Create a Semgrep command that scans the entire codebase with the default configuration (`auto`) and creates a SARIF output file, `/analysis/semgrep.sarif`.
2. Validate each warning produced by Semgrep by manually inspecting the code.

### Writing rules

:::info

For live testing your rules, you an also use [the Playground](https://semgrep.dev/playground/new).

:::

1. The vulnerabilityies listed below were not detected by any technique that we've seen so far. Inspect ![the Semgrep documentation](/ubuntu-portrait/vulnerabilities) and write rules to catch them. The rules should have as many metadata fields filled as possible.

| Vulnerability ID       | Hints on how to catch it with Semgrep                                             |
| ---------------------- | --------------------------------------------------------------------------------- |
| `UBUSEC-SECRET-LOG`    | Calls to functions from `logging` where the parameters have sensitive names       |
| `UBUSEC-UID-IDOR`      | `execute_string_command` calls with dynamic arguments                             |
| `UBUSEC-ARCHIVE-WRITE` | `os.path.join` calls where the arguments came from the parameters of the function |
| `UBUSEC-HASH-LEN`      | `sha256_update` calls where the parameter is created by concatenation             |
