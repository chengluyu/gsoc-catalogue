
# [Internet Systems Consortium](http://www.isc.org)

[Back to catalogue](../README.md#internet-systems-consortium)

[ISC](https://www.isc.org/mission/) is the organization behind the ongoing development and distribution of the name server software, **BIND**. Our team of engineers helps drive the DNS standards and author the reference implementation that is then distributed as commercial-quality open source software for the Internet community. ISC provides the same leadership both in standards development and software for the DHCP protocol: **ISC DHCP** and **Kea**. Over the years, the ISC team has written over [60 RFCs](https://www.isc.org/community/rfcs/isc-rfcs/); we are proud of our substantial contributions to the [Internet Engineering Task Force](http://ietf.org).

Administrators adopting Kea are looking for new ways to manage their core network services. They are attracted by Kea's separation of lease data from network communications, that facilitates centralized provisioning. They want to leverage Kea's hooks api and REST api to integrate DHCP with other network operations. As the explosion of containerized applications is breaking the old 1:1 relationship of IP addresses to machines, they need more flexibility and automation for services like DNS updating. The Kea team are looking for contributors who want to help us bring this core network management service into the 21st century by improving and extending the monitoring, provisioning, extensibility and performance.

ISC is a non-profit company. Our open source software is freely available on our website and on [https://github.com/isc-projects](github). ISC work is supported by the sale of software support contracts, and by donations from users who want to see free open source maintained and extended for everyone.

# Application Instructions

* Twitter: Please visit [Kea website](http://kea.isc.org), or the [ISC website](https://www.isc.org) for more information.

If you are interested, we recommend joining the [kea-dev mailing list](https://lists.isc.org/mailman/listinfo/kea-dev) or at least reading the recent archives of that or [Kea-users](https://lists.isc.org/mailman/listinfo/kea-users). Discuss your ideas with the developers on kea-dev, or you can email us privately at info@isc.org. 

To apply,  please look at the list of proposed projects at http://kea.isc.org/wiki/KeaIdeas.  If there is an idea that you are interested in proposing, the first step is to come up with some requirements and a proposed design. For examples, see some of the requirements and designs we have written for other Kea features (these larger and more complex than a typical summer project however): http://kea.isc.org/wiki/HARequirements, http://kea.isc.org/wiki/SharedSubnets, http://kea.isc.org/wiki/Commands. 

Technical Skills needed for success:
Kea implements the DHCP standards developed by the technical community in the IETF. General knowledge of DHCP, IPv6 and network operations in general are extremely helpful for these projects.  

Kea is written in C++11. The Kea project uses Google test, Google benchmarks, provides a REST interface and can use a number of DB backends: MySQL, Postgres, and Cassandra.  Experience with these technologies will give you a head start on the project. 

If you join this project, you will learn how to create professional-quality code: we do rigorous code reviews, require unit tests, written requirements and user and developer documentation.