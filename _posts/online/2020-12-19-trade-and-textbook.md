---
title: International Trade Summary and example of online textbook
categories: online
tags:
  - teaching
  - trade
  - website
---

While reviewing fro my trade prelim, I came across [this webpage.](https://saylordotorg.github.io/text_international-business/s06-01-what-is-international-trade-th.html) It has some useful notes; not directly useful for my review, but there's interesting bits in there. But more importantly, I really like the format, and it's published on github pages, so I want to see if it's use a jekyll theme or something easy to mimic like that.

## The website itself.

### Things I like: 
- Lightweight layout
- Colored boxes for summaries
- Nav links at top and bottom. Link to ToC, next section, and previous section.

### The guts of the site

css of the site is title bookhub.css.
Unfortunately bookhub is a very common name for services so if that is a public thing, can't find it.

Root site of saylordotorg.github.io returns 404, so all the individual books are being kept in seperate repos. Makes sense.

[Here's the repo for this book.](https://github.com/saylordotorg/text_international-business/)

Each section folder just contains the images for that section, and the image names look like the kind of messy jumble that's autogenned by some creation suite.

the page files are stored as html files, and each paragraph has a similarly autogenned id.
Things like "fwk-168388-ch01_s00_p13"

So this has the look of something written in another language. Maybe LaTeX, and then transformed into a website. Rather than something written natively as web content.

### Browsing [some other books](https://www.saylor.org/books/#stem) on the same site

[Some of the books](https://saylordotorg.github.io/text_intermediate-algebra/s04-02-operations-with-real-numbers.html) use mathjax for rendering. I guess that's a clue

I don't know. Maybe it's a wordpress theme.


## Also, notes on the actual content: Quick review of trade theories.

Missing out on most of what I was studying, but seems well written for intro level

### Country-based theories

#### Mercantilism
Current Account surplus is most important. Countries flourish by amassing a giant pile of gold. Prosperity? Utility? Pfff. What's the point of living if your king can't Scrooge McDuck it up?

#### Absolute Advantage
Countries do the stuff they're best at and trade for stuff they aren't best at.

#### Comparative Advantage
Countries do the stuff for which they have the lowest opportunity cost, even if they aren't the best at doing that thing

#### Heckscher-Ohlin
Countries specialize in making the stuff which is relatively intensive in a factor of production (labor or capital) that they have lots of. Unfortunately, Leontief noticed that US had lots of capital but *importing* capital-intensive goods

#### Firm-based theories
Linder: People with similar income levels have similar preferences, and thus trade occurs among firms in similarly wealthy countries.

#### Product Life Cycle
New products produced in only inventing country. While mature standardized products occur wherever most effective to make.

#### Global Strategic Rivalry 
Firms try to overcome and implement barriers to entry.

#### Porter something something
(1) local market resources and capabilities, (2) local market demand conditions, (3) local suppliers and complementary industries, and (4) local firm characteristics


