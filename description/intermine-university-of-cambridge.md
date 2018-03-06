
# [InterMine](http://intermine.org/)

[Back to catalogue](../README.md#intermine-university-of-cambridge)

# What is InterMine?
InterMine integrates data from different biological sources, providing a web-based user interface for querying and analysing the data. Users can automatically generate code to run queries using our [client libraries in R, Python, Perl, Ruby, Java, and Javascript](http://intermine.readthedocs.io/en/latest/web-services/#api-and-client-libraries).
## What technologies do we use? 
InterMine core is built in Java, and all data are stored in PostgreSQL. We have a legacy JSP-based user interface, with a Clojurescript user interface in early beta. We're also keen on browser-based datavis tools that use of our API, so you'll see a lot of Javascript (or languages that compile to Javascript, like Clojurescript and Coffeescript). Our client libraries provide opportunities to write code in several other languages.
## What sort of data does InterMine have? 
Since InterMine is open source, many research organisations around the world run InterMines with their own data, ranging from mice and fruit flies to a broad range of plants. Visit the [InterMine Registry](http://registry.intermine.org/) to see them all. (The registry was written by a GSoC student last year!) Most InterMines also have a "data sources" tab which tells you more about where the data in that specific instance originates. 
## What kind of problems does InterMine solve?
Genomic data is often messy, and there is a lot of it. Scientists use different terms to mean the same thing, and even assign the same gene different names! How can we handle this ambiguity? How can we help the end user make sense of data that is so diverse and complex? 
One way to help scientists analyse data is to provide visualisations, so we’re always excited to add and adapt different ways to display our data. How do you visualise the features inside a protein, or the interactions between two sets of genes? 
Code you write for InterMine can have a large impact - since there are dozens of different InterMines, you can often write code to work with one InterMine and with little or no effort, port it to another InterMine with different data.

# Application Instructions

* Twitter: Hello, and thank you for considering InterMine as your mentor organisation for Google Summer of Code! Please visit our [GSoC project ideas page](http://intermine.org/gsoc/project-ideas/2018/) and browse through the ideas. If one of them looks like it might interest you, contact the mentors directly to express your interest and discuss the projects further. 

## A few tips 
- Send us your CV / resume and tell us why you think you'd be a good choice for this project. 
- Now's the time to tell us what you can do! If you've written code, share it with us. A uni coding assignment is a good example of your work even if you don't have anything else. 
- Try to upload your code to GitHub (or a similar repository) if you can. Remember that if it's easy for us to examine and run, we're more likely to be interested than if all we receive is a zip file with no instructions. 
- A little-known secret: Open source code isn't only about the code. We'd also like to see evidence of your communication, project management, and documentation skills.
- Biology knowledge is a bonus but is definitely not required. 
- Please visit our [GSoC site](http://intermine.org/gsoc/guidance/students-applying/) for full guidance and application details.

## Custom ideas
If you're comfortable enough with InterMine's APIs (or data, or codebase) to propose your own project idea, we'd love to discuss it with you! Please drop an email to info@intermine.org to sound out your idea.