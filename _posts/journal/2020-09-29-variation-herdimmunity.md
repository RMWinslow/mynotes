---
title: "Individual variation in susceptibility or exposure to SARS-CoV-2 lowers the herd immunity threshold"
excerpt_separator: "<!--more-->"
categories:
  - journal
tags:
  - disease 
  - risk
  - contagion
  - population
  - networks
---

Individual variation in susceptibility or exposure to SARS-CoV-2 lowers the
herd immunity threshold    
M. Gabriela M. Gomes ,, *, Rodrigo M. Corder  , Jessica G. King  , Kate E. Langwig  , Caetano Souto-Maior  , Jorge Carneiro  , Guilherme Gonçalves  , Carlos Penha-Gonçalves  , Marcelo U. Ferreira  , Ricardo Aguas    
medRxiv preprint May 21 2020  


> **One Sentence Summary:** Models that curtail individual variation in susceptibility or exposure
to infection overestimate epidemic sizes and herd immunity thresholds. 
---



> Although estimates vary, simple calculations suggest that herd immunity to SARS-
CoV-2 requires 60-70% of the population to be immune. By fitting epidemiological models that 
allow for heterogeneity to SARS-CoV-2 outbreaks across the globe, we show that variation in
susceptibility or exposure to infection reduces these estimates


Basic idea is that the people most likely to get sick are then most likely to become immune from that sickness.
Thus the natural spread of disease, unlike random vaccination, has a built in selection mechanism to target the individuals who need it most (in the societal sense of "need")

> We integrate
continuous distributions of susceptibility or connectivity in otherwise basic epidemic models for
COVID-19 and show that as the coefficient of variation (CV) increases from 0 to 4, the herd
immunity threshold declines from over 60% (4, 5) to less than 10%. 

coefficient of variation is the ratio of standard deviation $\sigma$ to absolute mean $| \mu |$

## continuous transmission in heterogenous populations

susceptibility parameter $x$

$\dot{S}(x)=-\lambda x S(x)$

$\dot{E}(x)=\lambda x S(x)-\delta E(x)$

$\dot{I}(x)=\delta E(x)-\gamma I(x)$

$\lambda$ represents the "average force of infection" and $\lambda = \frac{\beta}{N} \int \rho E(x) + I(x) \, dx$

$$R_0 = \langle x \rangle \frac{\beta}{N} (\frac{\rho}{\delta} + \frac{1}{\gamma})$$

$\rho$ is "a factor measuring the infectivity of individuals in compartment E in relation to those
in I" and $\langle x \rangle$ is mean susceptibility at time 0.

Before epidemic, susceptibility has pdf $q(x)$ with mean $1$ and coefficient of variation $CV=\langle (x-1)^2 \rangle$

$R_{eff}=R_t=$ susceptibility at time $t$ multplied by $R_0$

> Countries where suppression of the initial outbreak was more successful, such as Austria, have
acquired less immunity and therefore the potential for future transmission in the respective
populations remains naturally larger. However, also in these situations, expectations for the 5
potential of subsequent waves is much reduced by variation in susceptibility to infection.

> Susceptibility factors were implemented as gamma
distributions... 
Consensus parameter values
$\delta=1/4$ per day...
$\gamma=1/4$ per day...
$\rho=0.5$

> In a directly transmitted infectious disease, such as COVID-19, variation in exposure to infection
is primarily governed by patterns of connectivity among individuals. We incorporate this in the
system (Equation 1) by adding variation in infectivity and assuming a positive correlation
between susceptibility and infectivity.
Formally this corresponds to modifying the force of
infection ... and basic reproductive number as  
> 
> $$\lambda = \frac{\beta}{N} \frac{\int x [\rho E(x) + I(x)] \, dx}{\int x q(x) \, dx}$$
> 
> $$R_0 = \frac{\langle x^2 \rangle}{\langle x \rangle} \frac{\beta}{N} (\frac{\rho}{\delta} + \frac{1}{\gamma})$$
> 
> where $\langle x^2 \rangle$ and $\langle x \rangle$ are second and first moments of distribution $q(x)$ prior to the epidemic



## Herd immunity - the intersting beet













