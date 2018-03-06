
# [Software and Computational Systems Lab at LMU Munich](https://www.sosy-lab.org/)

[Back to catalogue](../README.md#sosy-lab)

# Info
The following list contains our projects with the ideas that are (in our opinion) suitable for Google Summer of Code.
Feel free to suggest your own ideas.
A more detailed list of ideas (with descriptions) can be found at <https://www.sosy-lab.org/gsoc/gsoc2018.php#ideas> .

# CPAchecker ( [website](https://cpachecker.sosy-lab.org) )

CPAchecker is an [award-winning](https://cpachecker.sosy-lab.org/achieve.php) open-source framework
for the verification of software.
It is written in Java and based on a highly modular architecture
that allows to develop and combine a wide range of different analyses.
CPAchecker is used for [verification of the Linux kernel](http://linuxtesting.org/ldv)
and has helped to find [more than 50 bugs in the kernel](http://linuxtesting.org/results/ldv-cpachecker).

## Ideas
- Eclipse plugin
- Angular and automated tests for verification report
- Integrating SymPy into CPAchecker for Invariant Generation
- DART-like Test-case Generation in CPAchecker
- Checking Equivalence of Program Semantics Automatically

# JavaSMT ( [website](https://github.com/sosy-lab/java-smt) )

JavaSMT is a common API layer for accessing various SMT solvers.
It was created out of our experience integrating and using different SMT solvers in the CPAchecker project.
JavaSMT can express formulas in the theory of
integers, rationals, bitvectors, floating-points, and uninterpreted-functions,
and supports model generation, interpolation, formula inspection and transformation.

## Ideas
- Integrate more SMT solvers
- SMT in the Cloud

# BenchExec ( [website](https://github.com/sosy-lab/benchexec) )

BenchExec is a benchmarking framework for Linux (written in Python)
that is aimed at a high reliability of the results.
It can measure the CPU-time and peak memory usage of whole groups of processes.
To do so, it makes use of modern Linux features such as cgroups and namespaces,
effectively creating a benchmarking container whose resource usage is measured.

## Ideas
- Make use of the Intel Cache Allocation Technology
- Modern architecture and tests for HTML tables

# Application Instructions

* Twitter: Students wishing to participate in Summer of Code must realise that this is an important professional opportunity.
You will be required to produce code for an award-winning tool chain or parts of its infra structure.
Therefore, we seek students who are committed to helping our tools long-term and 
are willing to both do quality work, and be proactive in communication with their mentors.

You don't have to be a proven developer - in fact, this whole program is meant to facilitate joining our group and take a look at open source communities.
However, experience in coding is welcome and should be mentioned in your proposal.

You should take a look at the tools that you plan to work on before the start date.
The timeline from Google reserves a lot of time for bonding periods; use that time wisely.
Good communication is important. The group members are available via mail (or in person, if needed).
You should communicate with your mentor, and formally report progress and plans weekly.

## Recommended steps
- Join the mailing list of a project of your choice, introduce yourself, and meet your fellow developers
- Read Google's instructions for participating and the GSoC Student Manual
- Take a look at the list of ideas
- Come up with project that you're interested in
- Write a first draft proposal and get someone to review it
- Submit your proposal using Google's web interface ahead of the deadline

Further instructions are avaliable [on our website](https://www.sosy-lab.org/gsoc/gsoc2018.php#students "further instructions").