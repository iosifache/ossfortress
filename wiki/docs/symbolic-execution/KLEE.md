---
sidebar_position: 1
slug: klee
---

import Documentation from '@site/src/components/Documentation';
import VulnsTBD from '@site/src/components/VulnsTBD';
import {CLISetup} from '@site/src/components/Setup';
import {DefaultSolution} from '@site/src/components/Solution';
import {SolutionsNote} from '@site/src/components/BeginnerContent';

<VulnsTBD>

- `UBUSEC-RECOVERY-OOB`

</VulnsTBD>

<CLISetup software="AFL++" profile="dynamic-analysis" container="klee"/>

<Documentation software="KLEE" link="https://klee.github.io/docs/"/>

<SolutionsNote/>

## Steps

### Obtaining the LLVM bytecode

1. At the moment, the files from `sandcastle/c_modules` are used to compile a shared object using `Makefile`. Copy the folder with C sources in `/root/analysis/klee/c_modules` and modify `test.c` to call `generate_recovery_token` with two variables, which are both marked as symbolic variables (with the `klee_make_symbolic` method)
2. Use `clang` to generate the LLVM bytecode.

<DefaultSolution>

1. After copying the files, modify the `test.c` to contain the following definition:

    ```c
    int main() {
        char buffer[10];
        int count;

        // Make the input symbolic. 
        klee_make_symbolic(buffer, sizeof buffer, "buffer");
        buffer[10 - 1] = '\0';

        klee_make_symbolic(&count, sizeof(int), "count");

        generate_recovery_token(re, count);

        return 0;
    }
    ```

2. `clang -emit-llvm -c -g -O0 -Xclang -disable-O0-optnone -I . source.c -o source.bc`

</DefaultSolution>


### Symbolically executing the LLVM bytecode

1. Use `klee` to run the generated file with the LLVM bytecode

<DefaultSolution>

1. `klee source.bc`

</DefaultSolution>


### Validating the test cases

1. Compile again the program using the `-lkleeRuntest` flag.
2. For each test case, run the program and check if it is crashing.
3. Inspect the associated `test<n>.<type>.err` file to see where in the program the problem appears.

<DefaultSolution>

1. `clang -emit-llvm -c -g -O0 -Xclang -disable-O0-optnone -lkleeRuntest -I . source.c -o source.bc`
2. Compile the program with `gcc` with `gcc -L /home/klee/klee_build source.c -lkleeRuntest` and run it with `KTEST_FILE=k/root/analysis/lee-last/<ktest_file>./a.out`.
3. Manual validation

</DefaultSolution>
