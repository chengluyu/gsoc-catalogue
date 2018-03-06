
# [Performance Co-Pilot](http://pcp.io)

[Back to catalogue](../README.md#performance-co-pilot)

The Performance Co-Pilot is a toolkit designed for monitoring and managing system-level performance.  These services are distributed and scalable to accommodate very complex system configurations and performance problems.

PCP supports many different platforms, including (but not limited to) Linux, Mac OS X, Solaris and Windows.  From a high-level PCP can be considered to contain two classes of software utility:

###### PCP Collectors
These are the parts of PCP that collect and extract performance data from various sources, e.g. the operating system kernel.

###### PCP Monitors
These are the parts of PCP that display data collected from hosts (or archives) that have the PCP Collector installed.  Many monitor tools are available as part of the core PCP release, while other (typically graphical) monitoring tools are available separately in the PCP GUI or PCP WebApp packages.

The PCP architecture is distributed in the sense that any PCP tool may be executing remotely.  On the host (or hosts) being monitored, each domain of performance metrics, whether the kernel, a service layer, a database management system, a web server, an application, etc. requires a Performance Metrics Domain Agent (PMDA) which is responsible for collecting performance measurements from that domain.  All PMDAs are controlled by the Performance Metrics Collector Daemon (PMCD) on the same host.

Client applications (the monitoring tools) connect to PMCD, which acts as a router for requests, by forwarding requests to the appropriate PMDA and returning the responses to the clients.  Clients may also access performance data from a PCP archive for retrospective analysis.

# Application Instructions

* Twitter: Please read through the potential projects on the [Ideas page] (http://pcp.io/gsoc/2018/ideas.html) for the Performance Co-Pilot organisation.

Each project has an associated level of difficulty, prerequisite knowledge and mentors.  You are encouraged to contact individual mentors to seek clarification or further detail about individual projects that are of interest to you before you apply.

The mentors are experts in their fields who are volunteering time to help you.  Make the most of them - they are wonderfully kind and friendly people who want you to learn and succeed!

There is scope for extending or changing the projects somewhat to suit your goals.  Once you have decided on a general area, using one of the Ideas as a starting point, please put together a project proposal and send it to <pcp-mentors@groups.io>.  The proposal must outline your understanding of the topic, and provide a detailed description of what you aim to achieve.  It should also contain a short bio about yourself, your background and current skills.

Happy hacking!