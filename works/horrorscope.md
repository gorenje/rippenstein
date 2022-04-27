---
permalink: /works/horrorscope
layout: works
---

{% assign data=site.data.works.horrorscope %}
{% include worksection.html data=data %}

Our future is shrouded in a fog of the unknown. Gregorius has taken it upon himself to make a change for the better. Having been spiritually touched, Gregorius has been lucky enough to have peeked behind the curtains of the future.

Traditional horoscopes are horribly general and can fit to nearly any situation, making them useless for everyday use. HorrorScopes are highly optimised providing a detailed and for some, accurate account of the future.

Having gained a large seven figure investment from the seven largest futuring funds, HorrorScopes provides an unbounded and unparalleled clarity into the fogified future.

Powered by the DefEng (Defogification Engine&reg;) and based on the latest advancement of IMT (Infinite Monkeys Technology&reg;), HorrorScope provides a solid basis for Web 3.2.

Crystal Balls, Tarot Cards, Tea Leafs and other assorted earlier technologies have been infinitely hyperised by a harmonisation of IMT&reg; and DefEng&reg; breakthroughs.

Anxiety of the future will become a thing of the past - the blissful fear of the HorrorScope replacing the antiquated anxieties of the past.

Gregorius describes his work as a "*poke in the eye for those with eyes*".

And follows up with:

> *Traditional horoscopes are generally non-specific with enough interpretation, seem to fit to everyone everyday. But because of their interpretative nature, they predictive powers are limited or non-existent.*

> *HorrorScopes, on the other hand, are dangerously specific however are correct as often as any good horoscope, i.e. 0.00001% of the time. The unfortunate feature is that when a HorrorScope happens to be correct, it only results in more worldly misery.*

[Go to Calendar]({{ data.offsiteurl }})
[Go to Today](/horrorscope/YYYYMMDDD){: .todaylink }

*Warning*: As the Monkeys become yet more infinite, predictions may be adjusted and/or refined and/or changed. Be assured that the only certainity of the future is that there is a future.

<script type="text/javascript">
var add0 = function(r){ return (r < 10 ? "0" : "") + r; }

function replaceTodayLink() {
  var d = new Date();
  var m = add0(d.getMonth()+1);
  var y = d.getFullYear();
  var dy = add0( d.getDate() );

  document.querySelectorAll(".todaylink").forEach( function(elem) {
    elem.href = "/horrorscope/" + y + m + dy;
  })
}
window.onload = replaceTodayLink;
</script>

<style>
.todaylink {
float: right;
}
</style>
