FROM aflplusplus/aflplusplus:latest

WORKDIR /AFLplusplus

RUN make source-only afl-fuzz

ENTRYPOINT ["tail", "-f", "/dev/null"]
