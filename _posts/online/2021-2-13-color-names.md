---
title: More notes about colors
categories: online
tags:
  - colors
  - art 
---

Previous post talked about math of color perception.

But what are colors called?

## Universal color names

[Basic Colour Terms.](https://en.wikipedia.org/wiki/Color_term)

Berlin and Kay (1969) 
argue color names in languages follow heirarchy.

First **Black** and **white**, then **red**, then **green** and **yellow**, then **blue**, the **brown**, and finally **purple**, **pink**, **orange**, and **grey**.

[Hungary has two words for red.](https://en.wikipedia.org/wiki/Hungarian_language#Two_words_for_%22red%22)

Wikipedia has several color wheels.

[This one](https://en.wikipedia.org/wiki/Color_term#/media/File:RBG_color_wheel.svg) 
is RGB based as has Red, Orange, Yellow, Chartreuse, GReen, Spring Green, Cyan, Azure, Blue, Violet, Magenta, Rose.

[This one](https://en.wikipedia.org/wiki/Teal#/media/File:Color_star-en_(tertiary_names).svg)
is RYB based and has Red, Vermilion, Orange, Amber, Yellow, Chartreuse, Green, Teal, Blue, Violet, Purple, Magenta


---


## XKCD survey.

XKCD had big survey asking people to name colours. [Results here.](https://blog.xkcd.com/2010/05/03/color-survey-results/)

Conceptually similar to [Moroney color naming experiment](http://people.csail.mit.edu/jaffer/Color/Dictionaries#cne-2007)

Distinct english color names among xkcd readers (admitedly distinct sample)
compared to so-called universals. 
Teal is strongly recognized.
Indigo not so much

Datapointed has [interesting visualization here.](http://www.datapointed.net/2010/06/xkcd-color-name-strata/) And [another](http://www.datapointed.net/2010/09/men-women-color-names/).

Graph analysis [on the wolfram blog](https://community.wolfram.com/groups/-/m/t/434022)
TODO: come back and read connectiosn to percolation.

I think [this project](http://vis.stanford.edu/color-names/) uses the xkcd data to model color names.
Can type in a name to get colors and similar colors.
Also has [analyzer](http://vis.stanford.edu/color-names/analyzer/) to check whether color palette can be easily described.
Shows that Berlin Kay's model matches the xkcd data pretty well.
[Color dictionary.](http://vis.stanford.edu/color-names/dictionary/)

Tangentially related: [Semantically resonant color selection](http://vis.stanford.edu/papers/semantically-resonant-colors)


[This page](https://matplotlib.org/devdocs/tutorials/colors/colors.html#comparison-between-x11-css4-and-xkcd-colors) on the docs for matplotlib compares standard color names to the names from the xkcd survey.

Want to look at word cloud of xkcd results but site down. Here's a [article](https://www.huffpost.com/entry/luminosos-color-survey_n_1935562?utm_hp_ref=technology) about the wordcloud. The [blog](https://web.archive.org/web/20130211140557/http://blog.lumino.so/2012/10/02/the-color-cloud-an-interactive-visualization-of-color-names/) is still viewable though.

---

## [Catalog of color dictionaries](http://people.csail.mit.edu/jaffer/Color/Dictionaries)

Hah, [Aubrey Jaffer](http://people.csail.mit.edu/jaffer/) has an [interesting](http://people.csail.mit.edu/jaffer/YMBAMI) website.

[Has lots of useful info about color.](http://people.csail.mit.edu/jaffer/Color/)

[Pretty color Catalog](http://people.csail.mit.edu/jaffer/Color/xkcd.pdf)

Found [this nifty color wheel](http://www.procato.com/color+wheel/) there. Sites a bit broken.

[Horticulture color chart.](http://people.csail.mit.edu/jaffer/Color/H.htm) 
[Rocks.](http://people.csail.mit.edu/jaffer/Color/RC.htm)
[Soil.](http://people.csail.mit.edu/jaffer/Color/SC.htm)

NBS-ICCS [tries to give simple descriptive color names](https://web.archive.org/web/20121103030619/http://tx4.us/nbs-iscc.htm)

### ISCC-NBS Colors

In fact, I like these print-ready colors so much I'm going to copy some of the codes here

Name | html | example 
:-:|:-:|:-:
Vivid Pink | #ffb5baff | $\colorbox{#ffb5ba}{\color{#ffb5ba} X }$
Vivid Red | #be0032 | $\colorbox{#be0032}{\color{#be0032} X }$
Vivid Orange | #f38400 | $\colorbox{#f38400}{\color{#f38400} X }$
Strong Brown | #593319 | $\colorbox{#593319}{\color{#593319} X }$
Vivid Yellow | #f3c300 | $\colorbox{#f3c300}{\color{#f3c300} X }$
Light Olive | #867e36 | $\colorbox{#867e36}{\color{#867e36} X }$
Vivid Chartreuse | #8db600 | $\colorbox{#8db600}{\color{#8db600} X }$
Vivid Green | #008856 | $\colorbox{#008856}{\color{#008856} X }$
Vivid Blue | #00a1c2 | $\colorbox{#00a1c2}{\color{#00a1c2} X }$
Vivid Purple | #9a4eae | $\colorbox{#9a4eae}{\color{#9a4eae} X }$
White | #f2f3f4 | $\colorbox{#f2f3f4}{\color{#f2f3f4} X }$
Medium Gray | #848482 | $\colorbox{#848482}{\color{#848482} X }$
Black | #222222 | $\colorbox{#222222}{\color{#222222} X }$

Based on Munsell.
[Visualization](http://pteromys.melonisland.net/munsell/)

This system is still used for applicatiosn like [soil color categorization.](https://biophysics.sbg.ac.at/protocol/soilchart.pdf)

[.](http://www.colorwiki.com/wiki/Test_Images)

[An extension for the colors of light.](https://nvlpubs.nist.gov/nistpubs/jres/31/jresv31n5p271_A1b.pdf). Not quite satisfied.

[This software](http://www.uco.es/semanticolor/JFCS/) has aNBS color list that seems similar but slightly tweaked. Maybe they actually did the conversion themselves? No, because it includes Foster's guesses.


---

More recently, Paul Centore [performed a more direct conversion of Munsell to sRGB](https://www.munsellcolourscienceforpainters.com/ISCCNBS/ISCCNBSSystem.html)

Name | html | example 
:-:|:-:|:-:
red | #b92842 | $\colorbox{#b92842}{\color{#b92842} X }$
reddish orange | #d7472a | $\colorbox{#d7472a}{\color{#d7472a} X }$
orange | #dc7d34 | $\colorbox{#dc7d34}{\color{#dc7d34} X }$
orange yellow | #e3a045 | $\colorbox{#e3a045}{\color{#e3a045} X }$
yellow | #d9b451 | $\colorbox{#d9b451}{\color{#d9b451} X }$
greenish yellow | #d0c445 | $\colorbox{#d0c445}{\color{#d0c445} X }$
yellow green | #a0c245 | $\colorbox{#a0c245}{\color{#a0c245} X }$
yellowish green | #4ac34d | $\colorbox{#4ac34d}{\color{#4ac34d} X }$
green | #4fbf9a | $\colorbox{#4fbf9a}{\color{#4fbf9a} X }$
bluish green | #43bdb8 | $\colorbox{#43bdb8}{\color{#43bdb8} X }$
greenish blue | #3ea6c6 | $\colorbox{#3ea6c6}{\color{#3ea6c6} X }$
blue | #3b74c0 | $\colorbox{#3b74c0}{\color{#3b74c0} X }$
purplish blue | #4f47c6 | $\colorbox{#4f47c6}{\color{#4f47c6} X }$
violet | #7842c5 | $\colorbox{#7842c5}{\color{#7842c5} X }$
purple | #ac4ac3 | $\colorbox{#ac4ac3}{\color{#ac4ac3} X }$
reddish purple | #bb30a4 | $\colorbox{#bb30a4}{\color{#bb30a4} X }$
purplish red | #ba2b77 | $\colorbox{#ba2b77}{\color{#ba2b77} X }$
white | #e7e1e9 | $\colorbox{#e7e1e9}{\color{#e7e1e9} X }$
gray | #938e93 | $\colorbox{#938e93}{\color{#938e93} X }$
black | #2b292b | $\colorbox{#2b292b}{\color{#2b292b} X }$
purplish pink | #e589bf | $\colorbox{#e589bf}{\color{#e589bf} X }$
pink | #e68697 | $\colorbox{#e68697}{\color{#e68697} X }$
yellowish pink | #ea9a90 | $\colorbox{#ea9a90}{\color{#ea9a90} X }$
reddish brown | #7a2c26 | $\colorbox{#7a2c26}{\color{#7a2c26} X }$
brown | #7f4829 | $\colorbox{#7f4829}{\color{#7f4829} X }$
yellowish brown | #976b39 | $\colorbox{#976b39}{\color{#976b39} X }$
olive brown | #7f6129 | $\colorbox{#7f6129}{\color{#7f6129} X }$
olive | #72672c | $\colorbox{#72672c}{\color{#72672c} X }$
olive green | #3e501f | $\colorbox{#3e501f}{\color{#3e501f} X }$


---

US government has a [conceptually similar catalog](http://www.colorserver.net/). 
[History.](http://colorserver.net/articles/info_fs595_history.htm)
[Code structure.](http://colorserver.net/articles/info_fs595_numbering.htm)
Obselete for most applications, but considered the standard for military color descriptions.

Another good site [here](https://www.december.com/html/spec/colornames.html). [Colorimetry comparison.](http://www.triplenine.org/Vidya/OtherArticles/ColorimetryReference.aspx)

[To read later](http://www.ilkeratalay.com/colorspacesfaq.php#purpose)

[Big list of comparisons](https://web.archive.org/web/20120215182401/https://tx4.us/moacolor.htm)

---

[slides](https://magrawala.github.io/cs448b-wi20/assets/slides/Lec11-color.pdf) with pictures of some of this info.

[Name that color](https://chir.ag/projects/name-that-color/#6195ED)

---

To read: [This page on the history of colorsystems](http://www.colorsystem.com/?page_id=31). Found the link [here.](https://www.thenbs.com/knowledge/specifying-colour)

---

The  Bezold-Briicke Phenomenon is where changing the luminance of a light changes its percieved hue. It makes yellows look more blue and vice versa?

Why does gimp have different LCh than hsluv or my calcs?