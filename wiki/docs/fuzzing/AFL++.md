---
sidebar_position: 2
slug: aflplusplus
---

import Documentation from '@site/src/components/Documentation';
import VulnsTBD from '@site/src/components/VulnsTBD';
import {CLISetup} from '@site/src/components/Setup';
import {DefaultSolution} from '@site/src/components/Solution';
import {SolutionsNote} from '@site/src/components/BeginnerContent';

<VulnsTBD>

- `VULN-RECOVERY-OOB`

</VulnsTBD>

<CLISetup software="AFL++" profile="dynamic-analysis" container="aflplusplus"/>

<Documentation software="AFL++" link="https://aflplus.plus/docs/"/>

<SolutionsNote/>

## Steps

### Changing the input stream of the C library

1. At the moment, the files from `sandcastle/c_modules` are used to compile a shared object using `Makefile`. To increase the speed of the future fuzzing process, copy the folder with C sources in `/root/analysis/afl++/c_modules` and modify `test.c` to read the parameters for the `generate_recovery_token` call from `stdin` or a file. You should establish a convention for how the parameters are sent. For example, a 4-byte integer can be the first, followed by the bytes representing the string.
2. Use `afl-cc` to compile the source code you adapted. You can also leverage the already existing `Makefile`. The resulting executable file should be stored in `/root/analysis/afl++/c_modules/test`. Also make the required modifications to use Address Sanitizer and debugger symbols.
3. Create the directories `/root/analysis/afl++/c_modules/inputs` and `/root/analysis/afl++/c_modules/output`.
4. Using the convention that you established, create the file `/root/analysis/afl++/c_modules/inputs/example` that contains a valid input for the program you compiled.
5. Ensure the environment respects the expected state and that the program runs correctly by using `cat /analysis/afl++/c_modules/inputs/example | /analysis/afl++/c_modules/test`.

<DefaultSolution>

1. After copying the sources in `/root/analysis/afl++/c_modules`, replace the `test.c` content with:

    ```c
    int main(int argc, char *argv[]) {
        FILE *f;
        int length, read_length;
        char *buffer, *filename;

        if (argc != 2){
        return 1;
        }

        filename = argv[1];
        f = fopen (filename, "rb");

        fseek (f, 0, SEEK_END);
        length = ftell (f);
        fseek (f, 0, SEEK_SET);
        buffer = malloc (length);
        fread (buffer, 1, length, f);
        fclose (f);

        generate_recovery_token(buffer + 4, buffer);

        return 0;
    }
    ```

2. `AFL_USE_ASAN=1 /AFLplusplus/afl-cc -g -o /root/analysis/afl++/c_modules/test /root/analysis/afl++/c_module/*.c`
3. `mkdir /root/analysis/afl++/c_modules/inputs /root/analysis/afl++/c_modules/outputs`
4. `echo -ne "\x01\x00\x00\x00a" > /root/analysis/afl++/c_modules/inputs/example`
5. `export SANDCASTLE_RECOVERY_PASSPHRASE="secret"`

</DefaultSolution>

### Fuzzing the program

1. Create an `afl-fuzz` command that takes the demo inputs from `/root/analysis/afl++/c_modules/inputs` and writes the analysis to `/root/analysis/afl++/c_modules/output`. Let the program fuzz for a minute.

<DefaultSolution>

1. `afl-fuzz -i /root/analysis/afl++/c_modules/inputs/ -o /root/analysis/afl++/c_modules/outputs/ -- /root/analysis/afl++/c_modules/test  @@`

</DefaultSolution>

### Validating the crashes

1. For each crash, find the generated example input in `/root/analysis/afl++/c_modules/outputs` and run to validate the crash.
2. Use `gdb` to run the program with the generated example input and see where the program is crashing.

<DefaultSolution>

1. `/root/analysis/afl++/c_modules/test <crashy_input_filename>`, where `<crashy_input_filename>` is the file found in `/root/analysis/afl++/c_modules/outputs/crashes`
2. Verification with `gdb`

</DefaultSolution>
