peer to peer authentication for certifychain

file structure (proposed) : 

```
p2p-auth/
|-- src/
|   |-- main.c
|   |-- pauth.c
|   |-- networking.c
|   |-- cryptography.c
|   |-- utils.c
|
|-- tests/
|   |-- test-main.c
|   |-- test-pauth.c
|   |-- test-networking.c
|   |-- test-cryptography.c
|   |-- test-utils.c
|
|-- include/
|   |-- pauth.h
|   |-- networking.h
|   |-- cryptography.h
|   |-- utils.h
|
|-- .gitignore
|-- CMakeLists.txt
|-- readme.md

```