---
sidebar_position: 19
slug: cheatsheet
---

# Cheat sheet for getting started

import {BeginnerPage} from '@site/src/components/BeginnerContent';

<BeginnerPage>

## OWASP Threat Dragon for threat modelling

1. Install and run the Docker image

    ```bash
    docker run
        --interactive
        --tty
        --rm
        --port 8080:3000
        --volume $(pwd)/.env:/app/.env
        threatdragon/owasp-threat-dragon:stable
    ```

2. Access the OWASP Threat Dragon user interface at `http://localhost:8080`
3. Use the interface to create models, diagrams, assets, trust boundaries, and threats.

## Bandit for linting Python

1. Install bandit: `pip install bandit bandit_sarif_formatter`
2. Generate a configuration: `bandit-config-generator --out <config_path>`
3. Edit the configuration file stored at `<config_path>` according to your codebase.
4. Scan your codebase: `bandit --recursive <codebase_path> --format sarif --output <report_path> --config <config_path>`
5. Validate the resulting warnings using a SARIF explorer (for example, [the SARIF Viewer extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=MS-SarifVSCode.sarif-viewer)).

## flawfinder for linting C

1. Install flawfinder: `pip install flawfinder`
2. Recursively scan your codebase: `flawfinder --sarif <codebase_path> > <report_path>`
3. Validate the resulting warnings using a SARIF explorer (for example, [the SARIF Viewer extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=MS-SarifVSCode.sarif-viewer)).

## Semgrep for linting [any supported languages](https://semgrep.dev/docs/supported-languages/)

1. Install Semgrep: `pip install semgrep`
2. Scan your codebase: `semgrep scan --sarif --config auto --output <report_path> <codebase_path>`
3. Validate the resulting warnings using a SARIF explorer (for example, [the SARIF Viewer extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=MS-SarifVSCode.sarif-viewer)).

## OSV-Scanner for scanning dependencies in [any supported language](https://google.github.io/osv-scanner/supported-languages-and-lockfiles/)

1. Download any release of OSV-Scanner from [its GitHub page](https://github.com/google/osv-scanner/releases).
2. Scan your lock file: `osv-scanner --lockfile <lockfile_path>`
3. Validate the resulting warnings.

## Gitleaks for scanning secrets in Git repositories and codebases

1. Download any release of OSV-Scanner from [its GitHub releases](https://github.com/gitleaks/gitleaks/releases).
2. Scan: `gitleaks --no-banner detect --report-format sarif --source <codebase_path> --report-path <report_path> --redact`
3. Validate the resulting warnings using a SARIF explorer (for example, [the SARIF Viewer extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=MS-SarifVSCode.sarif-viewer)).

</BeginnerPage>
