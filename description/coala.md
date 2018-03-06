
# [coala](https://coala.io/)

[Back to catalogue](../README.md#coala)

coala: Language Independent Code Analysis

coala provides a common command-line interface for linting and fixing all your code, regardless of the programming languages you use. It allows users to analyse projects containing multiple languages with just one tool, using just one configuration and seeing just one user interface.

# How does it work?

With coala, you create just one configuration file. It can be separated into sections that run independently to fit different scenarios. Using different bears (which are coala's modules) users can work with a wide range of existing tools, wrapped by bears, and native analysis routines. This enables users to check their python code for pep8 conformity, calculate complexity for their java code, find code duplicates in the C code and check the documentation for spelling errors, while making sure the commits follow the set guidelines. All controlled via one configuration file, run with one command and served in the same user interface.

# For Users

coala offers a unified static code analysis suite. It can be used as a simple standalone testing suite, pre-commit hook and CI tool. Besides the normal user interactive mode, there is a non interactive mode for CI, a html output mode, to view results in the browser, and JSON output if you want to integrate coala into your own system. If implemented, coala even offers to automatically fix problems.

# For Developers

You can easily write your own bears. coala is written with ease of extension in mind. That means: no big boilerplate, just write one small object with one routine, add the parameters you like and see how coala automates the organisation of settings, user interaction and execution parallelisation.

# For Newcomers

coala offers a great newcomer experience with an in depth step by step guide for your first contribution, extensive documentation of the whole workflow and fast and easy communication over the gitter channel.

# Application Instructions

* Twitter: Guidance for applying to coala can be found in our [FAQ](http://projects.coala.io/#/faq) and dedicated [gsoc](https://gitter.im/coala/coala/gsoc) gitter room.