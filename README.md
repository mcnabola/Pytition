# UL petitions
There is a need for a specific petition service for the University of Limerick. Historically, petitions relating to the university on public forums such as change.org have been brought to the attention of the university however **anyone** can sign these petition thus a petition with a 1000 signatures means little to them. If we can guarentee that only UL members, staff & students can sign a petiton and verify their signature with an email confirmation. Petitions can be viewed with higher regard.  


[![Build Status](http://jenkins.sionneau.net:8080/buildStatus/icon?job=Pytition/master)](http://jenkins.sionneau.net:8080/job/Pytition/job/master/) [![Coverage status](https://img.shields.io/jenkins/coverage/cobertura/http/jenkins.sionneau.net:8080/job/Pytition/job/master.svg)](http://jenkins.sionneau.net:8080/job/Pytition/job/master/lastBuild/cobertura/) [![Documentation Status](https://readthedocs.org/projects/pytition/badge/?version=latest)](https://pytition.readthedocs.io/en/latest/?badge=latest)

# Pytition

## Why using Pytition?

* Because it allows you to host petitions without compromising the privacy of your signatories.
* No tracking, ever: CSS, JS and all resources are self-hosted. Pytition does not use CDN.
* Nice UI: Bootstrap 4 + JQuery 3.
* Based on solid backend technology: Django.
* Responsive UI: works well on phones/tablets/laptops/desktops.
* If you host an instance of Pytition, you can guarantee your signatories that their informations won't leak to third parties.
* It is Open Source and Free Software.

## Features

* [x] Multi-lingual UI with i18n: English, French, Italian, Occitan, Spanish.
* [x] You can pre-visualize petitions before publishing them.
* [x] Easy to use: petition content is typed-in via TinyMCE editors (like WordPress).
* [x] You can setup real SMTP account for the confirmation e-mail so that it is less likely considered as SPAM.
* [x] Supports Open Graph tags to provide description and image to allow nice cards to be shown when people post the petition link on social networks.
* [x] You can propose your signatories to subscribe to a newsletter/mailinglist (via HTTP GET/POST or EMAIL methods).
* [x] You can export signatures in CSV format.
* [x] Support for several organizations on the same Pytition instance [v2.0](https://github.com/pytition/Pytition/milestone/2)
  * Fine grain per-user per-organization permissions
* [x] Email retry support through the use of a mail queue middleware
* [x] Nice (multiple) permlink support for each petition

## Install development environment

See [dev/CONTRIBUTE.md](dev/CONTRIBUTE.md)

## Installing in production

See https://pytition.readthedocs.io/en/latest/installation.html#manual-installation-recommended-for-production
