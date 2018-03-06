
# [Xi Editor Project](https://github.com/google/xi-editor)

[Back to catalogue](../README.md#xi-editor-project)

The xi-editor project is an attempt to build a high quality text editor,
using modern software engineering techniques. It is initially built for
Mac OS X, using Cocoa for the user interface. There are also frontends for
other operating systems available from third-party developers.

Goals include:

* ***Incredibly high performance***. All editing operations should commit and paint
  in under 16ms. The editor should never make you wait for anything.

* ***Beauty***. The editor should fit well on a modern desktop, and not look like a
  throwback from the ’80s or ’90s. Text drawing should be done with the best
  technology available (Core Text on Mac, DirectWrite on Windows, etc.), and
  support Unicode fully.

* ***Reliability***. Crashing, hanging, or losing work should never happen.

* ***Developer friendliness***. It should be easy to customize xi editor, whether
  by adding plug-ins or hacking on the core.

Please refer to the [November 2017 roadmap](https://github.com/google/xi-editor/issues/437)
to learn more about planned features.

# Application Instructions

* Twitter: The best way to apply is to pick a major project on the roadmap or in the issue tracker, and indicate that you want to work on it - can be in the issue if you don't mind your interest being public, or privately.

A major focus this summer will be building out the plug-in ecosystem (currently there's a fairly complete syntax highlighting plugin but the rest are prototypes). Great projects would include:

* Connecting xi-editor to the Language Server protocol

* Building really good code search features, perhaps using kythe as the back-end

* Using parser expression grammars (PEGs) to make a higher performance syntax highlighter

* Extending the UI and writing a plugin for version control (git) integration