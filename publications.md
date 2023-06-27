---
layout: page
title: Publications
---

 
Open access articles or preprints <nobr>(<i class="ai ai-fw
ai-open-access-square"></i>)</nobr> are linked below. Supplementary materials
on GitHub <nobr>(<i class="fa fa-github" aria-hidden="true"></i>)</nobr> and
OSF <nobr>(<i class="ai ai-fw ai-osf"></i>)</nobr> for each publication are
linked below the citation.


{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
{% endfor %}
