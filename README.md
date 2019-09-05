# Overview

This project implements a Scrapy scraper for the articles of the Italian website http://www.wired.it.

Please, note that the articels are published - at the time of writing - with a Creative Commons license.

The crawler follows the site map and, for each article, extracts:

* category
* copyright
* text
* title
* URL

# Data snapshots

Snapshots of the data can be found in the `corpora` folder.

# Goals

The crawled data are meant to be used as "training corpus" in Automatic Text Classification tasks - as explained in the essay ["What is the best method for Automatic Text Classification?"](https://medium.com/@piercarlo_slavazza/what-is-the-best-method-for-automatic-text-classification).
