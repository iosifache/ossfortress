---
sidebar_position: 2
slug: semgrep
---

import Documentation from '@site/src/components/Documentation';
import VulnsTBD from '@site/src/components/VulnsTBD';
import {DefaultSolution} from '@site/src/components/Solution';
import {CLISetup, WebSetup} from '@site/src/components/Setup';

<VulnsTBD>

- `UBUSEC-FLASK-DEBUG`
- `UBUSEC-TAR-SLIP`
- `UBUSEC-LOGGING-PERMS`
- `UBUSEC-SECRET-LOG`
- `UBUSEC-UID-IDOR`
- `UBUSEC-ARCHIVE-WRITE`
- `UBUSEC-HASH-LEN`

</VulnsTBD>

<CLISetup software="Semgrep" profile="static-analysis" container="static-analysers"/>

<WebSetup software="Coder" profile="static-analysis" link="http://127.0.0.1:8002" credentials="oss-fortress"/>

<Documentation software="Semgrep" link="https://semgrep.dev/docs"/>

## Steps

### Scanning

1. Create a Semgrep command that scans the entire codebase with the default configuration (`auto`) and creates a SARIF output file, `/root/analysis/semgrep.sarif`.
2. Validate each warning produced by Semgrep by manually inspecting the code. Use the Coder instance in the Docker infrastructure to review the results.

<DefaultSolution>

1. `semgrep scan --sarif --config auto --output /root/analysis/semgrep.sarif /root/codebase/portrait`
2. Manual validation

</DefaultSolution>

### Writing rules

:::info

For live testing of your rules, you can also use [the Playground](https://semgrep.dev/playground/new).

:::

1. The vulnerabilities listed below were not detected by any technique that we've seen so far. Inspect [the Semgrep documentation](/ubuntu-portrait/vulnerabilities) and write rules to catch them in the `/root/analysis/semgrep-rules` folder. The rules should have as many metadata fields filled as possible.

| Vulnerability ID       | Hints on how to catch it with Semgrep                                             |
| ---------------------- | --------------------------------------------------------------------------------- |
| `UBUSEC-SECRET-LOG`    | Calls to functions from `logging` where the parameters have sensitive names       |
| `UBUSEC-UID-IDOR`      | `execute_string_command` calls with dynamic arguments                             |
| `UBUSEC-ARCHIVE-WRITE` | `os.path.join` calls where the arguments came from the parameters of the function |
| `UBUSEC-HASH-LEN`      | `sha256_update` calls where the parameter is created by concatenation             |

2. Modify the command from the first section to use them and to save the resulting SARIF file in `/root/analysis/semgrep.custom.sarif`.

<DefaultSolution>

1. The following rules can be created in `/root/analysis/semgrep-rules`:

   -  `exec-arg-from-http-get.yaml`

        ```yaml
        rules:
        - id: exec-arg-from-http-get
            languages:
            - python
            message: A GET HTTP parameter was used in an execute_string_command() call.
            mode: taint
            pattern-sources:
            - pattern: request.args.get(...)
            pattern-sinks:
            - pattern: execute_string_command(...)
            severity: WARNING
            metadata:
            category: security
            subcategory:
                - vuln
            cwe:
                - "CWE 78: Improper Neutralization of Special Elements used in an OS
                Command ('OS Command Injection')"
            confidence: HIGH
            likelihood: HIGH
            impact: HIGH
            owasp:
                - A3:2021 Injection
        ```

   -  `hash-length-extention-attack.yaml`

        ```yaml
        rules:
        - id: hash-length-extension-attack
            patterns:
            - pattern: |
                strcpy($BUFFER, ...);
                ...
                sha256_update(..., $BUFFER, ...);
            message: A SHA256 hash length extension attack is possible.
            languages:
            - c
            severity: WARNING
            metadata:
            category: security
            subcategory:
                - vuln
            cwe:
                - "CWE 1240: Use of a Cryptographic Primitive with a Risky
                Implementation"
            confidence: HIGH
            likelihood: MEDIUM
            impact: HIGH
            owasp:
                - A2:2021 Cryptographic Failures
        ```

    - `htts-flask-server.yaml`

        ```yaml
        rules:
        - id: htts-flask-server
            patterns:
            - pattern: |
                $FLASK_APP = Flask(...)

                ...

                $FLASK_APP.run(...)
            - pattern-not: |
                $FLASK_APP = Flask(...)

                ...

                $FLASK_APP.run(..., ssl_context=$SSL_CONTEXT, ...)
            message: The Flask server is run without setting up HTTPS.
            languages:
            - python
            severity: WARNING
            metadata:
            category: security
            subcategory:
                - vuln
            cwe:
                - "CWE 319: Cleartext Transmission of Sensitive Information"
            confidence: HIGH
            likelihood: MEDIUM
            impact: HIGH
            owasp:
                - A5:2021 Security Misconfiguration
        ```

    - `secret-logging.yaml`

        ```yaml
        rules:
        - id: secret-logging
            patterns:
            - pattern-either:
                - pattern: $LOGGING_LIB.$METHOD(..., $MESSAGE, ...)
            - metavariable-pattern:
                metavariable: $LOGGING_LIB
                patterns:
                    - pattern-either:
                        - pattern: logging
                        - pattern: logger
            - metavariable-pattern:
                metavariable: $MESSAGE
                patterns:
                    - pattern-either:
                        - pattern: <... password ...>
                        - pattern: <... token ...>
                    - pattern-not: |
                        "..."
            message: Logging of sensitive information
            languages:
            - python
            severity: WARNING
            metadata:
            category: security
            subcategory:
                - vuln
            cwe:
                - "CWE 215: Insertion of Sensitive Information Into Debugging Code"
            confidence: MEDIUM
            likelihood: LOW
            impact: MEDIUM
            owasp:
                - A3:2017 Sensitive Data Exposure
        ```

2. `semgrep scan --sarif --config /root/analysis/semgrep-rules/ --output /root/analysis/semgrep.custom.sarif /root/codebase/portrait/portrait/`

</DefaultSolution>
