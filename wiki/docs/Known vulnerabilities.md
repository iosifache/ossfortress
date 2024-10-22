---
sidebar_position: 6
slug: vulnerabilities
---

import {BeginnerPage} from '@site/src/components/BeginnerContent';

<BeginnerPage>

## Vulnerabilities in Sand Castle

Each vulnerability described in [the next section](#all-vulnerabilities) has an easy-to-remember identifier. All are short and prefixed with `VULN-`. These IDs will be used to refer to a vulnerability in the workshop.

At this point, you may read the ID (which is the title of the subsections) and description of each vulnerability quickly. This will assist you in getting familiar with them, and don't worry, you'll learn more specifics (for example, the attack vector) when you discover each of the vulnerability using open source tools!

## All vulnerabilities

:::note

The list of vulnerabilities is not exhaustive. Please see the [contribution guide](https://github.com/iosifache/ossfortress/blob/main/CONTRIBUTING.md) to propose including new vulnerabilities of Sand Castle.

:::

### `VULN-HASH-LEN`

- **Description**: SHA256 hash length extension attack
- **CWEs**
  - CWE-1240: Use of a Cryptographic Primitive with a Risky Implementation
- **Affected component**: Recovery token module
- **Vulnerable code**: `generate_recovery_token()` in `sandcastle/c_modules/generate_recovery_token.c`
- **Attack vector**: Unauthenticated HTTP call to `/recovery_command`
- **Impact**: `root` account compromise and privilege escalation

### `VULN-FIND-CMD`

- **Description**: Command sandbox escape via `find`
- **CWEs**
  - CWE-78: Improper Neutralization of Special Elements used in an OS Command
- **Affected component**: Web API
- **Vulnerable code**: `is_an_allowed_command()` from `sandcastle/confinement.py`
- **Attack vector**: Authenticated HTTP call to `/command`
- **Impact**: Arbitrary command execution as `$USER`

### `VULN-FLASK-DEBUG`

- **Description**: Enabled Flask debugging
- **CWEs**
  - CWE-489: Active Debug Code
- **Affected component**: Web API
- **Vulnerable code**: `sandcastle/app.py`
- **Attack vector**: HTTP calls
- **Impact**: Information disclosure, and, eventually, code execution

### `VULN-RECOVERY-OOB`

- **Description**: Heap out-of-bound write when generating recovery tokens
- **CWEs**
  - CWE 787: Out-of-bounds Write
- **Affected component**: Recovery token module
- **Vulnerable code**: `buf[]` from `generate_recovery_token()` in `sandcastle/c_modules/generate_recovery_token.c`
- **Attack vector**: Unauthenticated HTTP call to `/recovery_command`
- **Impact**: Memory write and, eventually, code execution

### `VULN-PILLOW-OOB`

- **Description**: Heap out-of-bound write when converting image formats with Pillow
- **CWEs**
  - CWE 787: Out-of-bounds Write
- **Affected component**: Web API
- **Vulnerable code**: `convert_format` in `sandcastle/image_ops.py`
- **Attack vector**: Unauthenticated HTTP call to `/convert_image`
- **Impact**: Memory write and, eventually, code execution

### `VULN-TAR-SLIP`

- **Description**: Tar slipping when extracting user-submitted archives
- **CWEs**
  - CWE-23: Relative Path Traversal
- **Affected component**: Web API
- **Vulnerable code**: `extract_archive()` in `sandcastle/uploader.py`
- **Attack vector**: Authenticated HTTP call to `/upload`
- **Impact**: Arbitrary file write

### `VULN-ARCHIVE-WRITE`

- **Description**: Arbitrary file write when extracting user-submitted archives
- **CWEs**
  - CWE-23: Relative Path Traversal
- **Affected component**: Web API
- **Vulnerable code**: `extract_archive_in_user_home()` in `sandcastle/uploader.py`
- **Attack vector**: Authenticated HTTP call to `/upload`
- **Impact**: Arbitrary file write

### `VULN-UID-IDOR`

- **Description**: IDOR when translating usernames to UIDs
- **CWEs**
  - CWE-641: Improper Restriction of Names for Files and Other Resources
  - CWE-280: Improper Handling of Insufficient Permissions or Privileges 
- **Affected component**: Web API
- **Vulnerable code**: `translate_username_to_uid()` in `sandcastle/app.py`
- **Attack vector**: Authenticated HTTP call to `/username`
- **Impact**: User enumeration

### `VULN-XSS`

- **Description**: Two XSSes when validating if a JSON document respects a schema
- **CWEs**
  - CWE-79: Improper Neutralization of Input During Web Page Generation
- **Affected component**: Web UI
- **Vulnerable code**: Error handling in `sandcastle/app.py`'s `validate_json()`
- **Attack vector**: Tricking users into accessing a custom-built URL
- **Impact**: Code execution in client's browser

### `VULN-SSRF`

- **Description**: Arbitrary GET requests to attacker-controlled domains or addresses
- **CWEs**
  - CWE-918: Server-Side Request Forgery
- **Affected component**: Web API
- **Vulnerable code**: `validate_json()` in `sandcastle/app.py`
- **Attack vector**: Unauthenticated HTTP call to `/validate_json`
- **Impact**: Unauthorized resource access and proxying of malicious requests

### `VULN-CSRF`

- **Description**: When coupled with `VULN-XSS`, arbitrary requests made in the name of an authenticated user
- **CWEs**
  - CWE-352: Cross-Site Request Forgery
- **Affected component**: Web UI
- **Vulnerable code**: All routes in `sandcastle/app.py` (which lacks anti-CSRF tokens)
- **Attack vector**: Tricking users into accessing a custom-built URL
- **Impact**: Executing privileged operations in the name of the user, including code execution on the managed server

### `VULN-SECRET-LOG`

- **Description**: Credentials and tokens logging
- **CWEs**
  - CWE-215: Insertion of Sensitive Information Into Debugging Code
- **Affected component**: Web API
- **Vulnerable code**: Multiple routes from `sandcastle/app.py`
- **Attack vector**: Access to the filesystem of the web server
- **Impact**: Accounts' compromise and, eventually, privilege escalation

### `VULN-LOGGING-PERMS`

- **Description**: Insecure permissions for created logging file
- **CWEs**
  - CWE-279: Incorrect Execution-Assigned Permissions
- **Affected component**: Web API
- **Vulnerable code**: `check_log_file()` in `sandcastle/app.py`
- **Attack vector**: Access to the filesystem of the web server
- **Impact**: Accounts' compromise and, eventually, privilege escalation

### `VULN-FLASK-SECRETS`

- **Description**: Default (and exposed) Flask secrets
- **CWEs**
  - CWE-318: Cleartext Storage of Sensitive Information in Executable
- **Affected component**: Web API
- **Vulnerable code**: `app.secret_key` from `sandcastle/app.py`
- **Attack vector**: Codebase access
- **Impact**: Exposure of the Flask secret used by all Sand Castle instances

### `VULN-HTTP`

- **Description**: Lack of HTTPS
- **CWEs**
  - CWE-319: Cleartext Transmission of Sensitive Information
- **Affected component**: Web API, Web UI
- **Vulnerable code**: `app` from `sandcastle/app.py`
- **Attack vector**: adversary-in-the-middle attack 
- **Impact**: Exposed credentials, commands, and other sensitive information transferred between the web UI and web API

</BeginnerPage>