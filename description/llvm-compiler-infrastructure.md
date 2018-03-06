
# [LLVM Compiler Infrastructure](http://llvm.org)

[Back to catalogue](../README.md#llvm-compiler-infrastructure)

The LLVM Project is a collection of modular and reusable compiler and toolchain technologies. Despite its name, LLVM has little to do with traditional virtual machines. LLVM began as a research project at the University of Illinois, with the goal of providing a modern, SSA-based compilation strategy capable of supporting both static and dynamic compilation of arbitrary programming languages. Since then, LLVM has grown to be an umbrella project consisting of a number of different subprojects, many of which are being used in production by a wide variety of commercial and open source projects as well as being widely used in academic research.

The primary sub-projects of LLVM are:
*  The LLVM Core libraries provide a modern source- and target-independent optimizer, along with code generation support for many popular CPUs. These libraries are built around a well specified code representation known as the LLVM intermediate representation ("LLVM IR").
*  Clang is an "LLVM native" C/C++/Objective-C compiler, which aims to deliver amazingly fast compiles, extremely useful error and warning messages and to provide a platform for building great source level tools. The Clang Static Analyzer is a clang-based tool that automatically finds bugs in your code.
*  The LLDB project builds on libraries provided by LLVM and Clang to provide a great native debugger on top of Clang and LLVM libraries.
*  The libc++ and libc++ ABI projects provide a standard conformant and high-performance implementation of the C++ Standard Library.
*  The polly project implements a suite of cache-locality optimizations as well as auto-parallelism and vectorization using a polyhedral model.
*  The lld project aims to be the built-in linker for clang/llvm. Currently, clang must invoke the system linker to produce executables.

In addition to official subprojects of LLVM, there are a broad variety of other projects that use components of LLVM for various tasks.

# Application Instructions

* Twitter: We strongly suggest each proposal to be discussed first at the corresponding sub-project mailing list (e.g. llvm-dev, cfe-dev, etc.) Prior patch submission to LLVM (or its subprojects) is recommended, but not strictly required. Please also indicate your prior knowledge with LLVM, whether you already contributed to it, etc.