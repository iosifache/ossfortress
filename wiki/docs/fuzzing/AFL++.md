---
sidebar_position: 2
slug: aflplusplus
---

:::info

The AFL++ documentation is available [here](https://aflplus.plus/docs/).

:::

## Vulnerabilities to be discovered

- `UBUSEC-RECOVERY-OOB`

## Steps

### Changing the input stream of the C library

1. At the moment, the files from `portrait/c_modules` are used to compile a shared object using `Makefile`. To increase the speed of the future fuzzing process, copy the folder with C sources in `/root/analysis/afl++/c_modules` and modify `test.c` to read the parameters for the `generate_recovery_token` call from `stdin` or a file. You should establish a convention for how the parameters are sent. For example, a 4-byte integer can be the first, followed by the bytes representing the string.
2. Use `afl-cc` to compile the source code you adapted. You can also leverage the already existing `Makefile`. The resulting executable file should be stored in `/root/analysis/afl++/c_modules/test`. Also make the required modifications to use Address Sanitizer and debugger symbols.
3. Create the directories `/root/analysis/afl++/c_modules/inputs` and `/root/analysis/afl++/c_modules/output`.
4. Using the convention that you established, create the file `/root/analysis/afl++/c_modules/inputs/example` that contains a valid input for the program you compiled.
5. Ensure the environment respects the expected state and that the program runs correctly by using `cat /analysis/afl++/c_modules/inputs/example | /analysis/afl++/c_modules/test`.

### Fuzzing the program

1. Create an `afl-cc` command that takes the demo inputs from `/root/analysis/afl++/c_modules/inputs` and writes the analysis to `/root/analysis/afl++/c_modules/output`.
2. Let the program fuzz for a minute.

### Validating the crashes

1. For each crash, find the generated example input in `/root/analysis/afl++/c_modules/outputs` and run to validate the crash.
2. Use `gdb` to run the program with the generated example input and see where the program is crashing.
