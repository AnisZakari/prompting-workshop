---
layout: default
title: FAQ TheSpoon
---

<img src="prompting-workshop/img/the_spoon.png" alt="TheSpoon Logo" width="250">

# 🥄 FAQ TheSpoon

Bienvenue dans l'univers velouté de TheSpoon. Toutes les réponses à vos questions sont juste là :

{% for item in site.data.faq_the_spoon.faq %}
<h2 style="color: #e67e22; font-weight: 600;">{{ item.question }}</h2>

{{ item.answer }}

---
{% endfor %}
