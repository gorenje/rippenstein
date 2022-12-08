---
permalink: /works/taboo-tiles
layout: works
title: Taboo Tiles
css: tabootiles
date: 2022-12-23 00:00:00 +0000
image: /f/i/tt-white.png
---

{% assign data=site.data.works.tabootiles %}
{% include worksection.html data=data %}

> **Taboo Tiles**, noun
>> Image in the form of a tile, with a topic and a link. Topics are societal taboos, thoughts that are swept under the societal carpet. A single red or blue dot in the middle bring artistic pleasure, nothing more.

All societies have the taboo topics, thoughts and ideas that are not discussed nor questioned. Be it life, death or the universe.  There are countless topics that a society refuses to address, ignoring the elephant in the room, while the china tableware is being broken.

For instance Western society does not question democracy nor capitalism, Eastern society does not question human rights nor societal nonconformity. These are very broad and generalised examples however they make the point.

Settings exists which allow taboo topics to be confronted, two being comedial and artistic. Some artists question society by seizing on taboo topics and making them the focus of their art. Some comedians use taboo topics to humorously poke fingers into societal eyes. However rarely do these approaches trigger a societal debate or if they do, the debate quickly degenerates into personal attacks on the originator, since who are they to question society? There other forms in which taboo topics are addressed, [Adam Curtis](https://en.wikipedia.org/wiki/Adam_Curtis) does a great job explaining many via the medium of documentaries using archival material. There are numerous sci-fi authors that have addressed topics that question the societal form.

But have these approaches worked as we still face many of the same issues that have already been highlighted.

Taboo tiles are an attempt to find another approach. An approach which redefines the context in which taboo topics are raised. People are used to dismissing art as either good or bad but only the few engage with the artwork, comedians are either funny or not but only the few allow their opinions to be influenced by comedians.

And who am I to question the societal form? I'm neither artist, nor comedian nor academic, I am simply a father with concerns for the future. Does this make my opinions any less valuable than anyone elses? The great promise of democracy is that *all* voices are heard, regardless of status. I have no hope that this approach will actually be any more successful than all the others but at least I can tell my children: I tried.

Taboo tiles are neither swipe-able nor clickable nor tappable nor scannable and definitely not eatable. Simple images, simple messages and a simple short links. They are scalable and printable, but more importantly they are copyable and type-able.

*Written words endure, read words fade.*

Taboo tiles have links to be typed into browsers. In the short moment that it takes to type nine characters into the browser, the reader is given a moment of reflection: what will they discover? What is the topic concerning itself with? In an age of tap, click, swipe and stare, people have come used to *consuming* content but not *reflection upon* content.

Those that have the time to type in a link might also have the time to reflect on the content. Reflection is a luxury in a world that is constantly screaming for our attention. But reflection and confronting uncomfortable topics has become a societal need. We are entering the age of confrontation and exiting the comfortable age of conformity.

<hr class="tabootiles"/>

{% for data in site.data.works.tabootiles.tiles -%}
  {% assign d=data[1] %}
  {% assign k=data[0] %}
  {% include tabootile.html data=d abbr=k %}
{% endfor %}

<div style="clear: both; padding-top: 15px;"></div>
