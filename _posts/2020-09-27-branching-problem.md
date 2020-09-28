---
title: "Superspreading and the effect of individual variation on disease emergence"
excerpt_separator: "<!--more-->"
categories:
  - online reference
tags:
  - disease 
  - risk
  - contagion
  - population
---

Notes from the wikipedia article on [Branching Process](https://en.wikipedia.org/wiki/Branching_process)
And from the supplementary notes from [this paper](https://www.nature.com/articles/nature04153).

## From wiki

Useful for modelling population, spread of surnames, propagation of nuetrons in reactor

Big question is ultimate extinction probability, that size of some generation is zero.

[Wald's Equation](https://en.wikipedia.org/wiki/Wald%27s_equation) implies that if expected number of children of each individual is $\mu$, then  expected size of generation $n$ is $\mu^n$

TODO to do

## From the linked paper, in the context of outbreak spread

We have a probability generating function $g$ of  the offspring distribution $Z$
$$g(s)=\sum_{j=0}^\infty Pr(Z=j) s^j$$

Important properties: $R_0$ is $g^\prime (1)$. And chance that a person doesn't spread is $Pr(Z=0)=g(0)$.

$n$th iterates: $g_0(s)\equiv s$, $g_1(s)\equiv g(s)$, $g_{n+1}(s)\equiv g(g_n(s))$.

When $R_0 > 1$, prob of disease extinction as $n\to\infty$ after we introduce one infection $q\in(0,1)$ is the unique solution to $q=g(q)$

pgf for total number of infected individuals of a minor outbreak is defined implicitly: $G(s)=sg(G(s))$. Expectation is $G^\prime (1)$.

* If $v$  drawn from pdf $f_v (u)$, then Poisson tranmission with mean $v$ distributed as $f_v (u)$ has pgf 
$$g(s)=\int_0^\infty e^{-u(1-s)}f_v(u)\ du$$

* If $v$ constant at $R_0$ then pgf is $g(s)=e^{-R_0 (1-s)}$

* If $v$ is exponentially distributed with mean $R_0$, then offspring distribution is geometric with mean $R_0$ and pgf $g(s)=(1+R_0 (1-s))^{-1}$

* If $v$ is gamma dist, mean $R_0$, dispersion $k$, offspring is neg binomial, same mean and dispersion, pgf:
  $$g(s)\left(1+\frac{R_0}{k}(1-s)\right)^{-k}$$


If $Z$ is a negative binomial distribution $Z \sim NegB(R_0, k)$, then the pgf is 
$$g(s) = \left(1 + \frac{R_0}{k}(1-s)\right)^{-k} $$

Apply population wide control and 
$$g_{pop}(s) = \left(1 + (1-c)\frac{R_0}{k}(1-s)\right)^{-k} $$














