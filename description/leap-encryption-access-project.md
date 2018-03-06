
# [LEAP Encryption Access Project](https://leap.se)

[Back to catalogue](../README.md#leap-encryption-access-project)

LEAP is a dedicated to giving all internet users access to secure communication. Our focus is on adapting encryption technology to make it easy to use and widely available. We want to make it possible for any service provider to easily deploy secure services, and for people to use these services without needing to learn new software or change their behavior. These services are based on open, federated standards, but done right: the provider does not have access to the user’s data, and we use open protocols in the most secure way possible.

On the server side we have created the LEAP Platform, a “provider in a box” set of complementary packages and server recipes automated to lower the barriers of entry for aspiring secure service providers. On the client side, we have created a cross-platform application called Bitmask that automatically configures itself once a user has selected a provider and which services to enable. Bitmask provides a local proxy that a standard email client can connect to, and allows for easy one-click Virtual Private Network (VPN) service.

The LEAP email system has several security advantages over typical encryption applications: if not already encrypted, incoming email is encrypted so that only the recipient can read it; email is always stored client-encrypted, both locally and when synchronized with the server; all message relay among service providers is required to be encrypted when possible; and public keys are automatically discovered and validated. In short, the Bitmask app offers full end-to-end encryption, quietly handling the complexities of public key encryption and allowing for backward compatibility with legacy email when necessary. Because the LEAP system is based on open, federated protocols, the user is able to change providers at will, preventing provider dependency and lock-in.

# Application Instructions

* Twitter: Hi! We're glad that you're interested in LEAP. Please read a bit about what we do, and get familiar with our existing codebase.

First of all, have a look at the project's ideas page. Come talk to as at IRC: #leap (at freenode) if you need advice for your proposal.

One important piece of advice is: be very honest about what your skills and motivations are. You don't need to be an uber-hacker to contribute something small and beautiful to the project: after all, it's more about the journey than arriving there in a rush.

That said, we hope than we can have great fun together, and get some nice lines of code written!

some tips
========

* have a look at the example projects in the project's ideas page, there are ideas for a great diversity of skills and difficulties.
* we prefer projects that are completely isolated from the main codebase.
* we prefer things that start small and can grow afterwards. go for a soledad-based hello-world app in a new language (golang? rust?) if you feel excited about the idea. the important thing is to get started, completion and correctness can be added later.
* if you think you have a good idea and it's not in the list, don't be shy and tell us about it.
* don't hesitate to make lots of questions to us before sending your proposal.
* not everything is code: tell us a bit about yourself and what are your motivations.