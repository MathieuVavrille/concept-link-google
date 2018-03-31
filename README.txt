
Linker of concepts using google
by Mathieu Vavrille
spring 2018

--------------------


The goal of this script is to find the concepts that are close to each other
using google search.


--------------------


Dependencies: Python3, graphviz (pip3 install graphviz)

How to use

python3 ml_google.py concepts.txt


--------------------

Known bugs:

-If too many requests are done, google will just stop answering, so the program
will fail
-> maybe I could do a save of the data computed to restart the computation later
