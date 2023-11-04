---
sidebar_position: 1
slug: klee
---

:::info

The KLEE documentation is available [here](https://klee.github.io/docs/).

:::

## Vulnerabilities to be discovered

- `UBUSEC-RECOVERY-OOB`

## Steps

### Obtaining the LLVM bytecode

1. At the moment, the files from `portrait/c_modules` are used to compile a shared object using `Makefile`. Copy the folder with C sources in `/root/analysis/klee/c_modules` and modify `test.c` to call `generate_recovery_token` with two variables, which are both marked as symbolic variables (with the `klee_make_symbolic` method)
2. Use `clang` to generate the LLVM bytyecode.

### Symbolically executing the LLVM bytecode

1. Use `klee` to run the generated file with the LLVM bytecode

### Validating the test cases

1. Compile again the program using the `-lkleeRuntest` flag.
2. For each test case, run the program and check if it is crashing.
3. Inspect the associated `test<n>.<type>.err` file to see where in the program the problem appears.
