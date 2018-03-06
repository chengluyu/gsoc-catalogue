
# [PMD](https://pmd.github.io/)

[Back to catalogue](../README.md#pmd)

PMD is a static code analyzer. It finds common programming flaws, sub-optimal code and code style issues in multiple languages. For example, it can highlight unused variables, empty catch blocks or too complex code, just to name a few.

# Programming Languages
Initially PMD started out to be a Java-only code analyzer. But nowadays, it fully supports 8 languages: Java, JavaScript, Salesforce.com Apex and Visualforce, PLSQL, Apache Velocity, XML and XSL. All languages provide many rules, that you can immediately use to check your source code.

# Copy-Paste-Detector
Additionally it includes CPD, the copy-paste-detector. CPD finds duplicated code in all the above languages and additionally in C, C++, C#, Groovy, PHP, Ruby, Fortran, Scala, Objective C, Matlab, Python, Go, and Swift.

# Usage
PMD has over 50000 monthly downloads and is actively used by many open source and closed source projects. It is integrated into most common build tools like Maven, Gradle and Ant, but it can also be used from the command line. Integrations into CI systems such as Jenkins can provide comparisons between builds to see quality improvements or degradation over time based on the issues found by PMD. When integrated into the build, PMD can serve as a quality gate.

# Extensibility
PMD comes out of the box with many rules in the area of code design, optimizations, naming and many more. It provides a flexible infrastructure to customize the existing rules via properties and to define completely new custom rules. The rules can be organized in rulesets, which can be shared within a software project, so that every developer is using the same PMD configuration.

An innovative approach allows to define PMD rules using a single XPath expression, allowing developers to do so without having to write code or deal with PMD internals. PMD ships with a designer tool to help build and test such expressions. More complex rules can be coded in Java using a visitor pattern over the analyzed code.

# Application Instructions

* Twitter: Although PMD is a mature project there are plenty of opportunities to improve and build upon existing features.
We've collected already many ideas in our [Wiki](https://github.com/pmd/pmd/wiki/%5BGSoC%5D-Google-Summer-of-Code).

We have two kinds of idea lists:

* [Project Ideas [Mature]](https://github.com/pmd/pmd/wiki/Project-Ideas-%5BMature%5D) are ready to use ideas that can be tackled immediately.
* [Project Ideas [Inception]](https://github.com/pmd/pmd/wiki/Project-Ideas-%5BInception%5D) are ideas, that need some additional effort to properly define goals. There is even the [Roadmap](https://github.com/pmd/pmd/wiki/Roadmap-and-future-directions) with more topics.

You may also suggest a project of your own or take an idea and adjust it. Please make sure to discuss it with us on [gitter](https://gitter.im/pmd/pmd), on our [mailing list](https://lists.sourceforge.net/lists/listinfo/pmd-devel) or [issue tracker](https://github.com/pmd/pmd/issues) beforehand.