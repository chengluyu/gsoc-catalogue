
# [The syslog-ng project.](https://syslog-ng.org/)

[Back to catalogue](../README.md#syslog-ng)

Why syslog-ng?

With syslog-ng, you can collect logs from wide range of sources, process them in near real-time and deliver them to a wide variety of destinations.

syslog-ng allows you to flexibly collect, parse, classify, and correlate logs from across your infrastructure (even from routers, embedded systems) and store or route them to log analysis tools.

By integrating with the newest big data tools it is possible to deliver log messages to kafka and elasticsearch, even store logs in hdfs with high performance.

Support for common inputs

syslog-ng not only supports legacy BSD syslog (RFC3164) and the enhanced RFC5424 protocols but also JavaScript Object Notation (JSON) and journald message formats.

Flexible data extraction

Working with unstructured data? That's not a problem: syslog-ng comes with a set of built-in parsers, which you can combine to build very complex things.

Simplify complex log data

Even if you need to collect logs from a diverse range of sources, syslog-ng's patterndb allows you to correlate events together and transform them into a unified format.

Databases destinations

If you need to store your log messages in a database, you don't need to look any further! We have SQL (MySQL, PostgreSQL, even Oracle!), MongoDB. We also support inserting messages into Redis, if that's what you are after.

Message queue support

syslog-ng supports the Advanced Message Queuing Protocol (AMQP) and the Simple Text Oriented Messaging Protocol (STOMP) too, with more in the pipeline.

Support language bindings

Want to deliver log messages to new system, that is not supported by any of the log management systems, then you can easily integrate it with syslog-ng by few lines of Python code implementing new destination. Not only destinations could be implement, but other items of the processing pipeline (e.g.: filter, parser, etc) and not only in Python language but also in Java.

# Application Instructions

* Twitter: https://github.com/balabit/syslog-ng/wiki/GSoC2018