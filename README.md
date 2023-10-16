# Ubuntu Portrait

## Setup

1. Set up an environment variable having the name `PORTRAIT_RECOVERY_PASSPHRASE` and the content a secret key that will be used in the password recovery mechanism.
2. Enter the `portrait/c_modules` folder and run `make`.
3. Run the application with `poetry run portrait`.

## Known vulnerabilities

1. Heap out-of-bound write in the `buf` buffer from the `generate_recovery_token` function from `portrait/c_modules/generate_recovery_token.c`
2. Zip splipping in `extract_archive` from `portrait/uploader.py`
3. Default (and exposed) secrets in `app.secret_key` from `portrait/app.py`
4. Logging credentials and tokens in the routes from `portrait/app.py`
5. Incorrect permissions for logging files in `check_log_file` from `portrait/app.py`
6. Hash length extension attack in the `generate_recovery_token` function from `portrait/c_modules/generate_recovery_token.c`, which leads to command injection as root
7. `find` for escaping the sandbox and injecting command as `$USER`, in `is_an_allowed_command` from `portrait/confinement.py`
8. IDOR by controlling the `uid` from the `translate_username_to_uid` route in `portrait/app.py`, which leads to user enumeration
9. Path traversal in `extract_archive_in_user_home` from `portrait/uploader.py`
