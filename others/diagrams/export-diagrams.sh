find projects/ -name "*.mmd" -exec sh -c 'mmdc -w 2000 -I container -H 2000 -i {} -o exports/$(basename {} .mmd).svg' \;
