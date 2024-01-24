peer to peer authentication for certifychain

file structure (proposed) : 

```
p2p-auth/
|-- src/
|   |-- main.c
|   |-- pauth.c
|   |-- pauth.h
|   |-- networking.c
|   |-- networking.h
|   |-- cryptography.c
|   |-- cryptography.h
|   |-- utils.c
|   |-- utils.h
|
|-- tests/
|   |-- test-main.c
|   |-- test-pauth.c
|   |-- test-networking.c
|   |-- test-cryptography.c
|   |-- test-utils.c
|
|-- include/
|   |-- pauth-common.h
|
|-- .gitignore
|-- CMakeLists.txt
|-- readme.md

```