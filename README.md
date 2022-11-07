# AC-Web-Crawling

There are several Columbia series that are regularly deposited into AC. These are both sent to AC staff as well as manually searched for by AC staff at irregular interviews. These items are also individually cataloged by AC staff. It would be better if there were scripts developed to harvest these works, and their metadata, which AC staff could run regularly.

**Here are the website topics:**

1. Center on Japanese Economy and Business
2. Columbia FDI Perspectives
3. Community College Research Center
4. Columbia Economics Discussion Paper Series




A script that will save all desired works (pdfs) from a website, and also produce a csv file with information harvested from the website (such as author, article title, etc.)

Each website will have slightly different specifications.

Ideally, there will ultimately be a script/program for each website, but to start, completely one as a proof of concept would be ideal.


---

The JapanesePaper folder contains the web crawling script for downloading the raw data from websites including report number, link, author and etc. 

ACnotebook folder contains the ipynb file for data cleaning and pdf downloading: It returns 3 csv files: cleaned metadata as required, the outliers need to be handled manually and files which have a indirect downloadable link.

