---
layout: page
title: ai4scmed
subtitle: multiscale AI for single-cell based precision medicine
permalink: /
redirect_from:
  - /about/
  - /about.html
---

# General Presentation

AI4scMed is a consortium (2023-2027) from the [PEPR Santé Numérique](https://www.inria.fr/fr/pepr-sante-numerique-projets) headed by INRIA-INSERM. It gathers researchers from different institutions on AI developments for single-cell biology applied to precision medicine. 

# Abstract 

Cell-based precision medicine holds revolutionary potential for healthcare, but realizing its full potential demands a deep understanding of disease variability and multiscale aspects. Single-cell (sc) multi-omics offers a unique way to obtain molecular profiles of individual cells and predict disease trajectories. To harness this complexity, new AI breakthroughs are needed. Our consortium will tackle methodological challenges to bridge the gap between sc data and personalized treatments, resolving cell type differences and integrating sc-multi-omics with imaging for spatial insights.

Addressing the complexity of the human body and combining genomics with other assays, we will develop AI-based methods to handle, integrate, analyze, and visualize multiscale complexity in diseases. Our developments will leverage cutting-edge AI for sc-genomic data analysis. To infer causal mechanisms at different levels, we'll use causal/logical/stochastic modeling to integrate heterogeneous data and account for temporal scales and biophysical priors.

We'll create network inference methods to understand molecular mechanisms in clinical samples, identifying key genes and predicting therapeutic impacts. Precision medicine must also integrate variability across different cell decision levels. We aim to build predictive models, digital twins, to enable data-driven personalized treatments by connecting intracellular dynamics, biochemical processes, cell populations, and tissue-level organization.

{% for post in site.wps %}
    {% include wps.html %}
{% endfor %}

