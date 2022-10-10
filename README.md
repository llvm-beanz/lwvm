# Lightweight Virtual Machine

This project seeks to build a lightweight virtual machine implementation for
educational purposes. The implementation prioritizes clear understandable code
with helpful debugging features. Documentation and testing are high priorities
to make it easier for newcomers to understand the code and make changes with
confidence.

## Building LWVM

### Cloning

LWVM depends on LLVM for project infrastructure as well as base data structures.
You will need to clone LLVM and LWVM in order to build LWVM. LWVM does not
support building against a pre-installed LLVM.

```shell
git clone git@github.com:llvm/llvm-project.git
git clone git@github.com:llvm-beanz/lwvm.git
```

### Building

LWVM builds using CMake through LLVM's build system. To configure LWVM as part
of LLVM set `LLVM_EXTERNAL_PROJECTS=lwvm` and
`LLVM_EXTERNAL_LWVM_SOURCE_DIR=<path to lwvm>` when you invoke CMake for LLVM:

```shell
cmake -G Ninja -DLLVM_ENABLE_PROJECTS=clang -DLLVM_EXTERNAL_PROJECTS=lwvm -DLLVM_EXTERNAL_LWVM_SOURCE_DIR=<path to lwvm> <path to llvm>
```

After CMake configures you can build lwvm by running:

```shell
ninja lwvm-test-depends # Builds all lwvm components
ninja check-lwvm        # Runs lwvm's test suite using LIT
```
