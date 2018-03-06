
# [Seastar](http://www.seastar-project.org/)

[Back to catalogue](../README.md#seastar)

Seastar is an advanced, open-source C++ framework for high-performance server applications on modern hardware. Seastar is the first framework to bring together a set of extreme architectural innovations, including:

Shared-nothing design: Seastar uses a shared-nothing model that shards all requests onto individual cores.
High-performance networking: Seastar offers a choice of network stack, including conventional Linux networking for ease of development, DPDK for fast user-space networking on Linux, and native networking on OSv.
Futures and promises: an advanced new model for concurrent applications that offers C++ programmers both high performance and the ability to create comprehensible, testable high-quality code.
Message passing: a design for sharing information between CPU cores without time-consuming locking.

# Application Instructions

* Twitter: Information for applicants
-----
Seastar's API can be referenced at: http://docs.seastar-project.org

Tutorial: https://github.com/scylladb/seastar/blob/master/doc/tutorial.md
This tutorial contains very useful information for understanding better the primitives provided by the framework, its programming model, how to efficiently debug a Seastar program, and so on.

If you have any question, feel free to send an e-mail to seastar's mailing list or contact the mentors directly. Feel free to contact Raphael directly, too, one of the org admins: raphaelsc@scylladb.com

Please also refer to FAQ available in the project's official website: http://www.seastar-project.org/
If you're interested in knowing more about Seastar, gather details about other potential ideas or make a proposal based on the ideas suggested, please send an e-mail to seastar-dev@googlegroups.com. We will be very happy to help.