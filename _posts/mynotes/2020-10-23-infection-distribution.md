---
title: Negative Binomial Distributions Notes Friday Oct 23
categories: online
tags:
  - note taking
---

Using various sources.

My goal tonight is to Figure out how distribution of secondary attack rate changes in response to various incentives.

Outline:

- [x] Jot down some facts about negative binomial and gamma distributions based on [*that one paper*](../journal/superspreading-variation/)
- [ ] For each of the following social assumptions, compute what needs to be done to induce the desired distribution of contacts
  - [x] higher social capital means connections more productive
  - [ ] paramerterized utility that trades off between social and nonsocial activities
  - [ ] everyone has access to continuum of connections and
  - [ ] People seek out connections based on number of connections the other person has. A rich get richer type thing
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


Probably can't do all tonight, so goals tonight marked with + (Gosh, that was an optimistic plan.)

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

With $k=1$, a gamma distribution becomes an exponential distribution with rate $\lambda = \beta = \frac{1}{\mu}$



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

$$F(x;k,\mu) = {\gamma(k,\frac{k x}{\mu}) \over \Gamma(k)} = \frac{\int_0^{\frac{k x}{\mu}} t^{k-1} e^{-t} \; dt}{\int_0^\infty t^{k-1} e^{-t} \; dt}$$

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
- PDF: $\binom{x+r-1}{r-1} p^r (1-p)^x$ <!--= (-1)^x \binom{-r}{k}-->

$$f= \frac{(x+r-1)!}{(r-1)!x!}  p^r (1-p)^x$$

- CDF: 
 
$$\frac{\int}{}$$


#### Putting these together

If individual repr number $v$ is Gamma distributed with shape $k$, mean $R_0$, then 
Offspring distribution $Z$ negBin distributed with 
- $r=k$
- $\frac{q}{p} = \frac{1-p}{p} = \theta \equiv \frac{R_0}{k}$
  - so $q= \frac{\theta}{1+\theta} =\frac{\frac{R_0}{k}}{1+\frac{R_0}{k}} = \frac{R_0}{k+R_0}$
  - and $p = 1-q = \frac{k}{k+R_0} = (1+\frac{R_0}{k})^{-1}$
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

---

## Mixture Distributions

Here's my issue. I'm trying to fit the model from Gatz of individual reproductive number being gamma distributed to the number of contacts. But 

- That requires contact numbers to be real-valued (that's not too much of an onerous burden, since that's hiding the abstraction that 3.7 units of connection might very well be one large connection and a bunch of tiny .1 connection aquiantances)
- With a finite number of contacts, the individual offspring distribution or person $x$ wouldn't be Poisson. (There's a maximum, etc.)
  - integer $n$ contacts and $r$ transmission rate would lead to $Binom(n,r)$ distribution.
  - For large $n$ can be approximated by $Normal(np,np(1-p))$
  - Also, if we hold $np$ fixed and let $p\to 0$ while $n\to\infty$, we get Poisson at the limit.
  - Maybe also see notes abuot Beta distribution below.
  - Refer to the [Poisson limit theorem](https://en.wikipedia.org/wiki/Poisson_limit_theorem), aka the law of rare events. If $\lambda=\lim_{n\to\infty} np_n$ then

$$\lim_{n\to\infty}\binom{n}{k}p_n^k(1-p_n)^{n-k}=e^{-\lambda}\frac{\lambda^k}{k!}=Poisson(\lambda)\ PMF$$

- Still don't feel great about the whole pretending like small number of contacts is actually big number of contacts thing.
-  We get NegBinom by taking mixing process of Poisson where rate is gamma-distributed. What other mixture distributions are there? What's the general form here?

### Definition

- Select a random variable $X^\prime$ at random from a collection of such random variable $X$s.
- Realize $x$ by drawing from $X^\prime$
- The distribution of such draws of $x$ is our mixture variable

if $p(x;a)$ is a pdf parameterized by $a$, and $w(a)$ is also a probability distribution, then we can et a mixture pdf:

$$f(x)=\int_A w(a)p(x;a)\ da$$

> [Compound distributions](https://en.wikipedia.org/wiki/Compound_probability_distribution) are useful for modeling outcomes exhibiting overdispersion, i.e., a greater amount of variability than would be expected under a certain model. For example, count data are commonly modeled using the Poisson distribution, whose variance is equal to its mean. The distribution may be generalized by allowing for variability in its rate parameter, implemented via a gamma distribution, which results in a marginal negative binomial distribution. This distribution is similar in its shape to the Poisson distribution, but it allows for larger variances. Similarly, a binomial distribution may be generalized to allow for additional variability by compounding it with a beta distribution for its success probability parameter, which results in a beta-binomial distribution.

TODO: Maybe use that last bit and actaully make the transmissibility vary from person to person? Or just actually use binomial for individual offspring distribution?'

[Well written article with good clear examples](https://en.wikipedia.org/wiki/Overdispersion)

### Normal Distribution, just as a reminder.

PDF is $\frac{1}{\theta\sqrt{2\pi}}e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}$

### Beta Distribution

Kind of like the opposite of the Binom distribution. Gives distribtution over beliefs about the value of $p$ if we see $n$ events and $k$
 sucessses.
Note that $Beta(p;\alpha,\beta)=(n+1)Binom(k;n;p)$ when $\alpha=k+1$ and $\beta=n-k+1$.

> In Bayesian inference, the beta distribution is the conjugate prior probability distribution for the Bernoulli, binomial, negative binomial and geometric distributions.

(And Gamma distribution is the conjugate prior for the rate of a Poisson Distribution!)

PDF: 

$$\frac{x^{\alpha-1}(1-x)^{\beta-1}}{B(\alpha,\beta)} = x^{\alpha-1}(1-x)^{\beta-1}\cdot \frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}$$

CDF: regularized incomplete beta function:

$$\frac{B(x;a,b)}{B(a,b)}= \int_0^x t^{\alpha-1} (1-t)^{\beta-1}\; dt \cdot \frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}$$

Relationship to Gamma distribution (but which characterization?! Argh, wiki...):

$$lim_{n\to\infty} n\cdot Beta(k,n) = Gamma(k,1)$$

$$\text{Independent }X\sim Gamma(k_a,\theta), Y\sim Gamma(k_b,\theta), \text{ then } \frac{X}{X+Y}\sim Beta(k_a,k_b)$$

> The beta distribution can be used to model events which are constrained to take place within an interval defined by a minimum and maximum value. For this reason, the beta distribution — along with the triangular distribution — is used extensively in PERT, critical path method (CPM), Joint Cost Schedule Modeling (JCSM) and other project management/control systems 

<!---PERT three-point estimation for Beta distribution:

$$\mu \approx \frac{min +4\cdot mode + max}{6}$$-->

Can compound with [negbinom](https://en.wikipedia.org/wiki/Beta_negative_binomial_distribution)

.

Ah, now I see the light. I can just make the binomial distribution go continuous with a bit of Gamma patooey

$$Binom(n_x, r) = \binom{n_x}{k} p^k (q-p)^{n-k} =  \frac{n!}{k!(n-k)!} p^k (q-p)^{n-k} =  \frac{\Gamma(n+1)}{\Gamma(k+1)\Gamma(n-k+1)} p^k (q-p)^{n-k}$$

### [Beta-binomial Distribution](https://en.wikipedia.org/wiki/Beta-binomial_distribution)

>  arising when the probability of success in each of a fixed or known number of Bernoulli trials is either unknown or random

> It also approximates the binomial distribution arbitrarily well for large α and β. Similarly, it contains the negative binomial distribution in the limit with large β and n. 


---

### Probability-generating functions

#### factorial moment generating function

$$G_X(😬)\equiv E[😬^X] = \sum_{x=0}^\infty \left[ p_X (x) \cdot 😬^x \right]$$

<!--$$\int f_x (x) z^x \ dx$$
Only defined for discrete. Woops-->

If $X \sim aY+bW$, then $G_X(😬)=G_Y(😬^a)\cdot G_W(😬^b)$.



Derivative wrt 😬 is $\sum_{x=0}^\infty \left[x \cdot p_X (x) \cdot 😬^{x-1} \right]$  and therefore 

$$G^\prime(1)=E[X]$$

$0^0\equiv 1$, whereas $0^x=0$ for any other $x$. As such, 

$$G_X(0) = \sum_{x=0}^\infty \left[ p_X (x) \cdot 0^x \right] = p_0$$

If $X$ is constant and equal to 1, then $G_X(😬)=😬$ 

#### Branching:

If $X_1,...,X_N$ are iid draws, and $N$ is also random noneg integer, and $S=\sum_{i=0}^N X_i$, then $G_S(😬)=G_N(G_X(😬))$. 

This means if N iid to the $X$s, then $G_S(😬)=G_X(G_X(😬))$. 

In a branching process, the offspring distribution $Z$ tells us the number of branching processes to start next period. So if $G=G_Z$, and the 0th generation has 1 individuals, then
- The number of offspring in the first generation has generating function $G(😑)$
- '' in the second generation '' $G(G(😑)) = G^2(😑)$
- '' in the third generation '' $G(G((😑))) = G^3(😑)$
- '' in the $g$th generation is $G^g(😑)$

The probability of extinction by the $g$th generation is $G^g(0)$. Ultimate extinction probability $G^\infty(0)$ has the property that $G^\infty(0)=G(G^\infty(0))$. $G$ is monotone and convex-down, so at most one solution to this on (0,1). 

Iff $\mu_X = G^\prime(1)\geq 1$, then unique positive solution for $G^\infty(0)$. If $\mu_X < 1$, then $G^\infty(0)=0$  

If a minor outbreak does go extinct, then total outbreak size is implicitly defined by the pgf $G_\Sigma(😑)=G(G_\Sigma(😑))\cdot😑$, which can be solved numerically.

- pgf for number of children $=G(😑)$
- pgf for size of lineage (them+descendents) of each child $\equiv G_\Sigma(😑)$
- $\therefore$ pgf for number of descendents you have $=G(G_\Sigma(😑))$
- And the pgf for constant $1$ is $😑$. Therefore pgf for $1+X$ is $😑\cdot G_X(😑)$ 


*All this stuff from The Theory of Branching Processes* 
<!--Pgf for negBinom (actually, wikipedia is contradictory on this. Might have to work out myself.): 

$$\left(\frac{p}{1-(1-p)z}\right)^r$$-->

Also we can get the pmf back out

$$p_X(x) = \frac{1}{k!}\frac{\partial^k}{\partial x^k} G_0 |_{x=0}  $$

If $G_0$ is the pgf for degree of vertices, then the pgf for degree of vertices found by following a random edge (*vertices weighted by degree*) will be 

$$x\frac{G_0^\prime (x)}{G_0^\prime (1)}$$

Exclude the edge we left and we get pgf for degree distribution of node we reach by moving along an edge.

$$G_1(x) = \frac{G_0^\prime (x)}{G_0^\prime (1)} = \frac{G_0^\prime (x)}{\mu_n}$$

pgf of number of open edges from a node, if each edge is iid open with probability $T$:

$$G_0 (x;T) = G_0(1+xT-T)$$

---

## Setup for endogenous connections

We need to figure out what underlying distribution of *something or other* results in a distribution of contacts with the desired properties.

If we want social connections with gamma distribution $V$ distributed according to $F_V(n)$, and if social connections are a function $g_v(x)$ of some parameter $x$ from distribution $X$, then if $g$ is strictly increasing over the support of $X$:

- $V = g_v(X)$
- $X = g^{-1}_v(V)$
- The distribution of X over its support is 

$$F_X(x) = F_V(g_v(x))$$

- pmf is likewise

$$f_X(x) = f_v(g_v(x))\cdot \frac{\partial g_v(x)}{\partial x}$$

It's that simple.

### higher social capital means connections more productive, fixed cost of maintaining connection

Each person $x\in(0,1)$ has some randomly determined exogenous level of social skill or social capital $\kappa_{x}$. 
If the process for generating $\kappa$ has distribution function $F_{\kappa}$, 
then without loss of generality, we can order the indices so that $F_{\kappa}(\kappa_{x})=Pr(\kappa\leq\kappa_{x})=x$

If the maintenance of each social connection requires effort which incurs exogenous disutility $\varpi$,
then person x's utility as a function of their choice of social connections is 
 
$$U_{x}(n)=\frac{1}{1-\alpha}\kappa_{x}n^{1-\alpha}-\varpi n$$

If $n(x)$ denotes person x's optimal number of social connections, then 

$$n(x)=\left(\frac{\kappa_{x}}{\varpi}\right)^{1/\alpha}$$






---

"Overdispersion" when variance-to-mean ratio greater than 1

---



### Changing the distribution


---

## Other facts about Probability distributions













































---