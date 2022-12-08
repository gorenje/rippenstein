---
permalink: /works/hamoni
title: Musical Matching Mates
layout: works
date: 2022-12-20 00:00:00 +0000
image: /f/i/hamoni.png
---

{% assign data=site.data.works.hamoni %}
{% include worksection.html data=data %}

Hamoni Music - Spotify dating app that matches users on their musical tastes.

Basically it works my comparing peoples playlists with one another and if there are overlaps, there is a match. That's the basic premise of the app.

It has some other features, for example showing you other users who listen to the current song you're playing. Instead of playing playlists, you play users. When you play a user, 15 random songs are picked from their playlists that aren't in your playlists. This then gives you a better impression what the user generally listens to.

Project was not accepted by Spotify since they don't like their users data being stored and analysed by third parties. Obviously if I'm going to analyse playlists, I need to store them. Pity really.

So the app remains in "family & friend" mode. Which in Spotify terms me that I can whitelist twenty-five emails for people who can use the app.

I still use the Hamoni to find interesting music that other people listen to, so it wasn't all a WoT (waste of time).

## Conflict of Interest?

Strangely other dating platforms have a certain amount of interest in keeping people on their platform. Just imagine if everyone found their perfect partner and left the platform! So I suspect (I have no prove of this) that most dating platforms don't show you your perfect-perfect match.

Now if Spotify were to implement their own dating app, they wouldn't have this conflict of interest - their cash cow is their music player.

It is similar to Amazon undercutting merchants on their platform, even at a loss to them. Amazon simply recovers their loses from AWS which is hugely profitable. Not every small business has a server rack to cross-finance themselves - Amazon does.

Either way, it is for the good that I didn't continue with Hamoni else I would have also gotten into that conflict of interest!

## Detail workings

So how did I get any data at all? Well public playlists are just that. So taking my playlists and doing searches got me other peoples playlists. So I don't need people on the platform to have their *public* data.

What about contacting other listeners? Well that was a problem that I spent a good hard long time thinking about. It is a problem since I didn't want people harassing each other or sending dick-pics. Unfortunate truth is, if there is an input field, dick-pics will be sent.

So I decided to have a swipe mechanism - left and right. If two users swipe right (i.e. like each other), then they can send each other track recommendations.

A track recommendation can then be sent by either user. If the user who receives the track recommendation then sends a track recommendation back, the two users may communicate with one another. There is no text field inputs in any of those interactions. And there are at least two interactions that each user has to do in order to communicate - i.e. both parties need to be aware of the other party.

As aside: the app tells you if a track that you are about to send to a user is known to them, i.e. in one of their playlists. So there is no duplication.

If at any time one of the users unlikes the other (i.e., swipes left on a user), all contact is blocked.

For those unfamiliar with Spotify, Spotify does not allow any form of communication between users on their platform. The only thing users can do is follow each other.

## Quirks

Spotify has profile pictures. These are linked to a sources. In the case of people who login in with Facebook, these are linked to Facebook servers. Meaning that, using peoples profile links, I know whether they are Facebook users or not. This doesn't happen (at least I didn't notice it) with Google or Email logins.

Another thing I noticed was that there are definitely users on Spotify who see it as a dating platform, or at least as a supplement to other dating platforms. How do I know this? You only have to look at their profile pictures and user names. It's not rocket science!

Apparently there have been studies on what people listen to most and like the most. One result was that peoples musically tasted is defined when they are between nineteen and twenty-two, i.e., those are they favourite songs. Taking the average release dates of tracks in peoples playlists could determine their age.

[Go to Hamoni]({{ data.offsiteurl }})
