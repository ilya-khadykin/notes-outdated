# python
All things related to Python, my experiments and code snippets

## Code examples in this repository include:

* object-oriented programming
    - `DogClass.py` shows as a very basic example of a Constractor, Accessor and Mutator methods, as well as Operator Overloading
* real world examples
    - **Graphite Metric Reporting Script** uses [Graphite Render API] to report via email the current state of monitored system; it utilizes the code from the following modules: `urllib`, `json`, `time`, `datetime`, `pytz`, `smtplib`, `email`
* `ReadingSingleLineformFilePattern.py` shows how to read one line of a text file using `for` loop
* `ReadMultipleLinesfromFile.py` shows how to read multiple lines of a text file using `while` loop
* `AccumulatorPattern.py` shows an Accumulator Pattern in action
* [ParsingArgumentsFromCommandLine.py] is an example of how to pass your own arguments to your scripts using `argparse`
* [BannerGrabbing.py] is a simple example of how to get an information about a remote host's webserver using `socket` and `re` modules
* [NetworkServerWithSocket.py] - basic example of a network server created with `socket`
* [UsingSSLwithSocket.py] - how to use SSL with `socket`
* [SendingEmailsUsingSMTP.py] - sending email messages using SMTP protocol with `smtplib`
* [ParallelExecutioner.py] - Thread Pool example which can be used for sending HTTP requests (for example) in Parallel 

[Graphite Render API]: <http://graphite.readthedocs.org/en/latest/render_api.html>
[ParsingArgumentsFromCommandLine.py]: <https://github.com/m-a-ge/python/blob/master/ParsingArgumentsFromCommandLine.py>
[BannerGrabbing.py]: ./BannerGrabbing.py
[NetworkServerWithSocket.py]: ./NetworkServerWithSocket.py
[UsingSSLwithSocket.py]: ./UsingSSLwithSocket.py
[SendingEmailsUsingSMTP.py]: ./SendingEmailsUsingSMTP.py
[ParallelExecutioner.py]: ./threading_example/ParallelExecutioner.py