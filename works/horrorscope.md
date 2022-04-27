---
permalink: /works/horrorscope
layout: works
---

{% assign data=site.data.works.horrorscope %}
{% include worksection.html data=data %}

Our future is shrouded in a fog of the unknown. Gregorius having been lucky enough to have peeked behind the curtains of the future, has taken it upon himself to make a change for the better.

Traditional horoscopes are horribly general and can represent nearly any situation, making them useless for everyday use. HorrorScopes are highly optimised prediction technology. Providing a detailed and (for some) accurate account of the future.

Having gained a largish seven figure round-A seedfunding from (at least) the seven largest futuring funds, HorrorScopes provides unbounded and unparalleled clarity into the future.

Powered by the DefEng - Defogification Engine&reg; - and based on the latest and greatest advancement of IMT - **Infinite Monkeys Technology&reg;**, HorrorScope provides a solid basis for Web 3.2.

Older technology such as Crystal Balls, Tarot Cards, Tea Leafs, amongst others have been hyperised and integrated by a harmonisation of IMT&reg; and DefEng&reg; breakthroughs and learnings.

Anxiety of the future will become a thing of the past, being blissful replaced by the fear of HorrorScopes. The antiquated anxieties of the yesteryears will become just that: antiquated.

Gregorius describes his work as a:

> *poke in the eye for those with eyes*

And follows up with:

> *Traditional horoscopes are generally non-specific with enough interpretation, seem to fit to everyone everyday. But because of their interpretative nature, they predictive powers are limited or non-existent.*

> *HorrorScopes, on the other hand, are dangerously specific however are correct as often as any good horoscope, i.e. 0.00001% of the time. The unfortunate feature is that when a HorrorScope happens to be correct, it only results in more worldly misery.*

[Go to Calendar]({{ data.offsiteurl }})
[Go to Today](/horrorscope/YYYYMMDDD){: .todaylink }

*Warning*: As the Monkeys become yet more infinite, predictions may be adjusted and/or refined and/or changed. Be assured that the only certainity of the future is that there is a future.

*And always remember:* Predicting the future is not about being right tomorrow, it's about convincing someone today.

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
