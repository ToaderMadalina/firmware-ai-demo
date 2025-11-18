    .global _start

_start:
    bl main       // call main
1:  b 1b          // infinite loop if main returns
