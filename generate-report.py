#!/usr/bin/env python3

native_log = open("native/results.out","r")
fexint_log = open("fexint/results.out","r")
fexjit_log = open("fexjit/results.out","r")

fexint_fails = 0
fexjit_fails = 0
while True:
    native_line = native_log.readline().strip("\n")

    if not native_line:
        break

    fexint_line = fexint_log.readline().strip("\n")
    fexjit_line = fexjit_log.readline().strip("\n")

    if native_line != fexint_line:
        print("Fexint failure:", native_line, "vs", fexint_line)
        fexint_fails = fexint_fails + 1;
    if native_line != fexjit_line:
        print("Fexjit failure:", native_line, "vs", fexjit_line)
        fexjit_fails = fexjit_fails + 1;

print(fexint_fails, "fexint failures");
print(fexjit_fails, "fexjit failures");
