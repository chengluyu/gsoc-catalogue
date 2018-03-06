
# [languagetool.org](https://languagetool.org)

[Back to catalogue](../README.md#languagetoolorg)

### What

LanguageTool scans texts for style, spelling, and grammar errors. In some cases, it can even find semantic issues. For example, what could be wrong about "Thursday, 27 June 2017"? Well, 27 June 2017 was not on a Thursday, and LanguageTool detects that.

LanguageTool supports more than 20 languages (to a different degree), including English, Russian, German, Polish, Spanish, and French.

### How

Internally, LanguageTool uses four different approaches to find errors:
* it scans for known error pattern with a pattern languages similar to regular expressions, but more powerful
* it uses Java code to find errors that are too complex for the error-pattern approach
* it uses statistics to find uncommon sequences of words
* it uses artificial intelligence to see if commonly confused words are used properly (like ad/add or cease/seize)

### The Future

Artificial intelligence will be the main approach in the future to detect text errors. We're looking for your help and ideas to apply AI to the proofreading problem, for example by using a seq2seq approach like in machine translation.

LanguageTool is also an end user application, and users want LanguageTool to be integrated in the software they already use. We're looking for integrations into tinyMCE, CKEditor, and many others (your suggestions are welcome). Plus, the existing browser add-on for Firefox and Chrome needs major UI improvements.

# Application Instructions

* Twitter: Requirements depend on what part of LanguageTool you'd like to work on:

**User interface / browser add-on**
* requires knowledge of Javascript and web technologies

**Core logic of error detection, using AI**
* requires knowledge of at least one machine learning framework
* requires enough Java knowledge to integrate the results (not necessarily the training) into our existing Java code

**Core logic of error detection**
* requires good knowledge of Java and being a native speaker of the language you're going to improve the error detection for

In any case, we expect you to have a close look at our ideas list at http://wiki.languagetool.org/missing-features and check out the existing code at https://github.com/languagetool-org/. Once you have a better idea of what you'd like to do, please contact us at https://forum.languagetool.org to introduce yourself. We'll try to find a small task for you get started. Or even better, you fix one of the existing bugs and submit a pull request.