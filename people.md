---
layout: page
title: People
subtitle: More about us…
---

## Permanent staff

{% for post in site.peoples %}
    {% if post.position == "Permanent researcher" %}
        {% include archive-people.html %}
    {% endif %}
{% endfor %}

## Postdoctoral researcher

{% for post in site.peoples %}
    {% if post.position == "postdoc" %}
        {% include archive-people.html %}
    {% endif %}
{% endfor %}


## PhD students

{% for post in site.peoples %}
    {% if post.position == "phd_student" %}
        {% include archive-people.html %}
    {% endif %}
{% endfor %}



