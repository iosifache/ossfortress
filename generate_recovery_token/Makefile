all: clean build build_test

build:
	gcc -fPIC -shared -o generate_recovery_token.so generate_recovery_token.c sha256.c

build_test:
	gcc -o test.elf generate_recovery_token.c test.c sha256.c

clean:
	rm -f generate_recovery_token.so test.elf
