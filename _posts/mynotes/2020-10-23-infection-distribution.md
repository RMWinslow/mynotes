---
title: Negative Binomial Distributions Notes Friday Oct 23
categories: online
tags:
  - note taking
---

Using various sources.

My goal tonight is to Figure out how distribution of secondary attack rate changes in response to various incentives.

Outline:

- [ ] Jot down some facts about negative binomial and gamma distributions based on [*that one paper*](../journal/superspreading-variation/)
- [ ] For each of the following social assumptions, compute what needs to be done to induce the desired distribution of contacts
  - [ ] higher social capital means connections more productive
  - [ ] paramerterized utility that trades off between social and nonsocial activities
  - [ ] everyone has access to continuum of connections and
- [ ] For each of the above social setups and each of the below gov responses, calculate how distribution changes.
  - disease models
    - [ ] multiplying utility by a scaling factor dependent on how many connections you have. Eg penalty from disease is that you might die and stop expiriencing life. +
  - gov models
    - [ ] ignorance, no containment +
    - [ ] just letting everyone know + (above)
    - [ ] letting everyone know and they see the social connections of neighbors 
    - [ ] locking down random people +
    - [ ] locking down socialites
    - [ ] locking down people with higher chance of being sick but not necessarily the socialites
    - [ ] shutting down portion of connections for everyone +
    - [ ] imposing cost on connections +
    - [ ] imposing cost on connections above a certain threshold


Probably can't do all tonight, so goals tonight marked with +

---

## Some facts about the distributions in question

### gamma Distribution

#### interesting tidbits 

Distribution of $v$, individual reprodcutive number, is best described in cases like SARS, using gamma dist with mean $\mu = R_0$ and dispersion $k$

This dist has maximum entropy of all distributions such that 
- $E[X] = \mu$
- $E[\ln x] = \psi (k) - \ln \frac{1}{\mu}$
  - where $\psi(k) = \frac{\Gamma^\prime(k)}{\Gamma(k)}$
  - alt $\psi(k)=\frac{\partial}{\partial k} \ln \Gamma (k)$

Exponential distribution is special case.
If $k$ is integer, then gamma is same as [Erlang dist](https://en.wikipedia.org/wiki/Erlang_distribution), which is sum of $k$ iid exponential dists.
And exp dist is dist of time between Poisson events. So gamma is like a generalization which allows us to wait for multiple hits and much much more.



#### Properties of gamma distribution

Note that it is often characterized using
$\alpha \equiv k$; 

**scale** 
: $\theta \equiv {\mu \over k}$; 

and **rate** 
: $\beta \equiv \frac{1}{\theta} = \frac{k}{\mu}$


##### pdf:

$$f(x;k,\beta) = \frac{\beta^k x^{k-1} e^{-\beta x}}{\Gamma(k)}$$

$$f(x;k,\mu) = \frac{k^k x^{k-1} e^{-\frac{kx}{\mu}}}{\mu^k \Gamma(k)}$$

<!--If $k\in\mathbb{Z}$, then 

$$f(x;k,\beta) = \frac{\beta^k x^{k-1} e^{-\beta x}}{(k-1)!}$$-->

##### cdf:

$$F(x;k,\beta) = {\gamma(k,\beta x) \over \Gamma(k)} = \frac{\int_0^{\beta x} t^{k-1} e^{-t} \; dt}{\int_0^\infty t^{k-1} e^{-t} \; dt}$$

$$F(x;k,\beta) = {\gamma(k,\frac{k x}{\mu}) \over \Gamma(k)} = \frac{\int_0^{\frac{k x}{\mu}} t^{k-1} e^{-t} \; dt}{\int_0^\infty t^{k-1} e^{-t} \; dt}$$

##### Mean

$$\mu = k\theta = \frac{k}{\beta}$$

##### Variance

$$\sigma^2 = k\theta^2 = \frac{k}{\beta^2} = \frac{\mu^2}{k} $$

##### Skewness

$$+ \frac{2}{\sqrt{k}}$$

##### Scaling

If $X \sim Gamma(k,\theta)$, then for $c > 0$, 

$$cX \sim Gamma(k,c\theta)$$

If $X \sim Gamma(k,\beta)$, then for $c > 0$, 

$$cX \sim Gamma(k,{\beta \over c})$$

If $X \sim Gamma(k,\mu)$, then for $c > 0$, 

$$cX \sim Gamma(k,c\mu)$$

##### Laplace Transform

$$F(s) = (1+\frac{\mu}{k}s)^{-k}$$



#### Gamma functions

Distribution name comes from use of gamma functions.

##### Big boy gamma function:

$$\Gamma(k) \equiv \int_0^\infty t^{k-1} e^{-t} \; dt$$

If $k\in\mathbb{Z_+}$, then $\Gamma(k)=(k-1)!$

##### Incomplete gamma functions

$$\Gamma(k,🍌) \equiv \int_🍌^\infty t^{k-1} e^{-t} \; dt $$

$$\gamma(k,🍌) \equiv \int_0^🍌 t^{k-1} e^{-t} \; dt $$


#### What distribution of contacts yields a gamma dist of $v$?

The answer is simple: a gamma distribution. Each draw of $v$ is the *expected* number of secondary cases caused by a person. If tranmissions are iid, then the expected number of transmissions is simply the number of contacts multplied by the transmission rate per contact $r$. Each draw $v=x$ corresponds to the draw of a person with $x \over r$ contacts.

So distribution of social contacts should be gamma distributed with mean $R_0 / r$ and dispersion $k$. (see scaling properties [above](#scaling))

To get distribution of actual infections, we then use negative binomial distribution.

---
### Negative Binomial Distribution

> The gamma distribution is also used to model errors in multi-level Poisson regression models, because a mixture of Poisson distributions with gamma distributed rates has a known closed form distribution, called negative binomial.

Models number of failures before a number of sucesses. 

Equivalently, this is the continuous mixture of Poisson and Gamma, where the Poisson arrival rate is Gamma distributed.

> That is, we can view the negative binomial as a Poisson(λ) distribution, where λ is itself a random variable, distributed as a gamma distribution with shape = r and scale θ = (1-p)/p or correspondingly rate β = p/(1-p). (*fractions flipped*)

SARS spread (*offspring distribution*) is best modelled using Negative  distribution 


#### From the [Gatz superspreading paper](https://www.robertmwinslow.com/notes/journal/superspreading-variation/#further-reading-and-thinking)

$v$ is gamma-distributed with dispersion $k$ and mean $R_0$, then offspring distribution $Z$ is negBinom with 

- mean $R_0$
- variance $R_0 (1+\frac{R_0}{k})$
- variance-to-mean ratio of $1+\frac{R_0}{k} = \frac{k+R_0}{k}$

#### Properties of Negative Binomial Distribution

*wikipedia page is kind of a mess, changing its definitions mid-paragraph. [Better page.](https://mathworld.wolfram.com/NegativeBinomialDistribution.html)*

What is that probability over $x$, that we get our $r$th success on the $x+r$th trial, after $x$ failures? 
(Each trial has chance of success $p$, chance of failure $q=1-p$.)

- mean $\mu=\frac{rq}{p} = \frac{r\cdot(1-p)}{p}$ 
  - Thus $p = \frac{r}{\mu+r}$
- variance $\sigma^2 = \frac{rq}{p^2} = \mu \frac{\mu+r}{r}$
- skewness $\frac{2-p}{\sqrt{rq}}$
- variance-to-mean ratio of $\frac{r}{\mu+r}$


#### Putting these together

If individual repr number $v$ is Gamma distributed with shape $k$, mean $R_0$, then 
Offspring distribution $Z$ negBin distributed with 
- $r=k$
- $\frac{q}{p} = \frac{1-p}{p} = \theta \equiv \frac{R_0}{k}$
  - so $q= \frac{\theta}{1+\theta} =\frac{\frac{R_0}{k}}{1+\frac{R_0}{k}} = \frac{R_0}{k+R_0}$
  - and $p = 1-p = \frac{k}{k+R_0} = (1+\frac{R_0}{k})^{-1}$
- Mean: $\mu = r\frac{q}{p} = k \frac{R_0}{k} = R_0$
- Variance: $\sigma^2 = \mu \frac{\mu+r}{r} =  R_0 \frac{R_0 + k}{k} = R_0 \cdot (\frac{R_0}{k}+1)$
- Variance-to-mean ratio: $1+\frac{R_0}{k} = \frac{k+R_0}{k}$




---

### Parameters for SARS2

Based on various linked articles from [here](https://www.robertmwinslow.com/notes/online/atlantic-k/), seems likes SARS2 has parameters roughly
- $k=0.1-0.25$
- $R_0 =$ all over the place
- $r=.53-.87$ but that's for one specific choir practice.
- [This study](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7185944/) found transmission rate (secondary attack rate) anywhere from 6-14%. See Table 3.