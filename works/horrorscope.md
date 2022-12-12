---
permalink: /works/horrorscope
layout: works
title: Horrorscopes
date: 2022-12-15 00:00:00 +0000
image: /f/i/horrorscope.svg
---

{% assign data=site.data.works.horrorscope %}
{% include worksection.html data=data %}

Our future is shrouded in a fog of the unknown. Gregorius having been lucky enough to have peeked behind the curtains of the future, has taken it upon himself to make a change for the better.

Traditional horoscopes are horribly general and can represent nearly any situation, making them useless for everyday use. HorrorScopes are highly optimised prediction technology. Providing a detailed and (for some) accurate account of the future.

The seven largest and finest futuring funds have come together to provide a seven-figure A-round seed-funding. With that, HorrorScope&reg; is able to view, with unparalleled clarity and unlimited timeframes, into the future.

Powered by the DefEng - **Defogification Engine&reg;** - and based on the latest and greatest advancement of IMT - **Infinite Monkeys Technology&reg;**, HorrorScope provides a solid basis for Web 3.2.

Older technology such as Crystal Balls, Tarot Cards, Tea Leafs (amongst others) have been incorporated and hyperised by a harmonisation of IMT and DefEng breakthroughs and learnings.

Anxiety of the future will become a thing of the past, being blissful replaced by the fear of HorrorScopes. The antiquated anxieties of yesteryears will become just that: antiquated.

Gregorius describes his work as a:

> *A poke in the eye for those with eyes*

And follows up with:

> *Traditional horoscopes are extremely non-specific and with enough interpretation, seem to fit to everyone everyday. Because of their interpretative nature, they predictive powers are limited or non-existent.*

> HorrorScopes, on the other hand, are dangerously specific. Unfortunately their correctiveness is bearly as good as traditional horoscopes, i.e., hardly ever.

> *But when a HorrorScope happens to be correct, it only results in more worldly misery. Thankfully there has been no known incidence of "HorrorScope Correctness".*

[Todays HorrorScope](/horrorscope/YYYYMMDDD){: .todaylink }
[Calendar]({{ data.offsiteurl }}){: .calendar }

*Warning:* As the Monkeys become yet more infinite, predictions may be adjusted and/or refined and/or changed. Be assured that the only certainty of the future is that there is a future.

*Danger:* Predicting the future is not about being right tomorrow, it's about convincing someone today.

## Interested?

Thanks to [ChatGPT](https://chat.openai.com/chat), an investment opportunity has opened:

> Dear Investors,

> We are excited to introduce DarkHorizons, a new venture that combines the ancient art of astrology with the thrilling world of horror. Our team of skilled writers will create daily, weekly, and monthly HorrorScopes for all 12 astrological signs, infusing each prediction with a touch of the supernatural and the terrifying.

> Our unique approach to horoscopes will set us apart from the competition and appeal to a wide audience of horror fans and astrology enthusiasts alike. We plan to distribute our HorrorScopes through a combination of online platforms, including our own website and social media channels, as well as through partnerships with popular horror websites and magazines.

> We are seeking funding to support the development and launch of our company. Our team has extensive experience in astrology, writing, and the horror genre, and we are confident in our ability to create a successful and profitable business. We have outlined a detailed business plan and budget, which is included in the attached documents.

> We appreciate your consideration and look forward to the opportunity to discuss our proposal further.

> Sincerely,<br>
> Gregorius Rippenstein<br>
> Founder, DarkHorizons Pty. Ltd.

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
.calendar { float: right; }
</style>
