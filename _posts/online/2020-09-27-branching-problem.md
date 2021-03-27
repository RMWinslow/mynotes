---
title: "Branching problems"
excerpt_separator: "<!--more-->"
categories:
  - online
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


---

## Factorial Moment generating function:

Pgf is special case of [Factorial moment generating function](https://en.wikipedia.org/wiki/Factorial_moment_generating_function) when $X$ is discrete rv with only the counting numbers as support.

More general form is that if $X$ is a real-valued random variable, then 

$$M_X(\maltese) = E[\maltese^X] = \int \maltese^x f(x) \ dx$$

Domain is all $\maltese\in\Complex$ where this exists.

I want to check if this has the same convinient properties as the PGF:

### Moment properties

$$M_X(1) = E[1^X] = \int 1^x f(x) \ dx = \int f(x) \ dx = 1$$

$$M_X^\prime (\maltese) = \int x \maltese^{x-1} f(x) \ dx$$

$$M_X^\prime (1) = \int x f(x) \ dx = E[X]$$

### Multiplying by constant


$$M_X(\maltese^a) = E[({\maltese^a})^X] = E[\maltese^{aX}]$$

And if $S\equiv aX$, then 

$$M_S(\maltese) = E[\maltese^S] = E[\maltese^aX]$$

So $M_{aX}(\maltese) = M_X(\maltese^a)$

### Adding independent RVs

Let $X,Y$ be independent real-valued random variables.
$M_X$ is the FMGF for $X$, 
and $M_Y$ is the FMGF for $Y$.

And $S$ is the some of the two. $S\equiv a X+ bY$.
Then the FMGF for $S$ is 

$$M_S(\maltese)=E[\maltese^{a X+ bY}] 
= \int \maltese^s f_S(s) \ ds
= \int\int \maltese^x f(x) \ dx\ dy
$$


$$M_S(\maltese)
=E[\maltese^{S}]
=E[\maltese^{a X+ bY}]
=E[\maltese^{aX} \maltese^{bY}] 
$$

$$M_S(\maltese) = \int \int \maltese^{ax} \maltese^{by} f_X(x) f_Y(y)\ dx\ dy$$


$$M_S(\maltese) = 
\int \maltese^{ax}  f_X(x) \ dx \int \maltese^{by}  f_Y(y) \ dy$$

$$M_{aX+bY}(\maltese) = M_S(\maltese) = M_X(\maltese^a)M_Y(\maltese^b)$$

In particular, if $Y$ and $X$ are iid, then

$$M_{X+Y}= M_X(\maltese)M_Y(\maltese) = M_X(\maltese)M_X(\maltese) = M_X^2(\maltese)$$

And the sum of $N$ iid draws from $X$ has pgf $M_X^N(\maltese)$

### Random number of IID Random Variables

$N$ is an independent real-valued random variable
with FMGF $M_N$

$$X_1,X_2,X_3,...X_N$$
are iid.
Each has the same FMGF $M_X$.

$$S\equiv \sum_{i=1}^N X_i$$
has FMGF $M_S$

Then 

$$M_S(\maltese) = E[\maltese^S] = E[\maltese^{\sum_{i=1}^N X_i}]$$

$$M_S(\maltese) = E\left[ E[\maltese^{\sum_{i=1}^N}]\ |\  N \right]
= E\left[ (M_X (\maltese))^N \right]
= M_N(M_X (\maltese))$$




So all the same old properties apply.



















