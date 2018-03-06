
# [radare](http://radare.org)

[Back to catalogue](../README.md#radare)

The radare project started in February of 2006 aiming to provide a free and simple command line interface for a hexadecimal editor supporting 64 bit offsets to search and recover data from hard-disks.

Since then, the project has grown, and its aim has changed to provide a complete framework for analyzing binaries with some basic *NIX concepts in mind, like everything is a file, small programs that interact with each other using stdin/out, and keep it simple.

Radare2 is a complete LGPL3 rewrite of the original project, which removes design issues of the first iteration, and makes it more modular and easier to script and maintain. It features a testsuite that aims to cover as many cases as possible in order to catch regressions.

Radare2 is composed of a hexadecimal editor at its core, with support for several architectures and binary formats. It features code analysis capabilities, scripting, data and code visualization through graphs and other means, a visual mode, easy unix integration, a binary diffing engine for code and data, a shellcode compiler, and much, much more!

# Application Instructions

* Twitter: It is a requirement that students who want to apply to the radare2 project for the Google Summer of Code 2018 should submit a small pull request accomplishing one of the [microtasks](http://radare.org/gsoc/2018/tasks.html) as part of their application. You can also choose any of the GitHub issues if they are big enough to be a qualification task, still small enough to be finished in no more than a couple of weeks.

Steps for the application process

  - Read Google's instructions for participating
  - Grab any project from the [list of ideas](http://radare.org/gsoc/2018/ideas.html) that you're interested in (or propose your own)
  - Write a first draft proposal using Google Docs and [our template](https://docs.google.com/document/d/1kDPGgr_D5tQuYLQi_gEGlkuQ-DlU8GH5kDBqZbVSC7I/edit?usp=sharing) and ask one of the mentors or administrators to review it with you
  - Submit it using Google's web interface

How to fill in the application template

  - Keep it simple enough to fit on no more than a couple of pages. Despite the shortness of the sentences, try to preserve the clarity of the proposal.
  - Try to split the GSoC period into tasks, and each task into subtasks. It really helps us to understand how you want to accomplish your goals, but even more so, it'll help you too. 
 - Please note how much time per day/week you are going to spend on this project.
 - Specify your timezone, since so we can assign you a mentor in the same one. This helps ease communication.
 - Submit your proposal early, not at the last minute
 - You can also choose a “backup” idea (the second task you probably want to do), so that in case of some conflicts (two students for one task) it will be easier to solve.