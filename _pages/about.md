---
permalink: /about/
title: "About"
---

This repo is for collecting all of my reading notes in a centralized place.
This isn't the typical use-case for a blog template, 
and these posts aren't really meant to be perused through and read by other people, 
though I might share a post with someone.
If you've found yourself here that way, please don't judge me too harshly for the messiness of this site.


The advantages of using a blog template are that I can search through posts, and organize things by tag.
Also, because it's hosted on github pages, I can very easily access and even edit these notes from any platform or device. 

<!--I was inspired to set things up this way after reading about the initial impetus behind html is to make hardware irrelevant when it came to sharing data among CERN researchers. 
Well, I'm trying to make hardware relevant for my own notes as well. 
(And file hosting is too bulky and won't render markdown with latex, of course.)-->

### Category Meanings

This repo is for absolutely any informative media I consume.
The Category label is used to split things up by the medium:

- **talk** for seminars, job market talks and the like, which aren't part of a recurring workshop
- **class** for any meetings I attend repeatedly. Nowadays, that will simply be workshops.
- **youtube** for any videos I watch online, including recordings of talks that I didn't actually "attend"
- **journal** for working papers and published research articles
- **textbook** for longform published reference material
- **online** for things like blogposts, wiki articles, and news stories

### Linking images.

To link images, I put images in the /img/ folder and link them in markdown use the format:

```
![DESCRIPTION](../../img/FILENAME)
```

This is the most concise format I've found which both works in Github's markdown preview and also compiles correctly using the site's theme. I thought the baseurl config would like me drop the "../..", but alas.
