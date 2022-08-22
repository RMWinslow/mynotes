---
title: UMN banned from Linux kernel
categories: online
tags:
  - computer
  - ethics
  - code
---

Hey there, this entire blog is just for personal use, and you shouldn't be here.

This was written in a mentally compromised state. After checking over its content later, it's still more accurate than pretty much any account you'll read elsewhere, but like, it's double triple something that no one else should be reading.

Disclosure: I teach at UMN, but have no connection to the UMN CompSci department, and have never met anyone involved in this incident. But perhaps the name-affiliation has compromised my judgement? Personally, I think I just got triggered by people misrepresenting the story on the UofMN subreddit. But everyone thinks their interpretations are reasonable, so shrug.


---


There are [Headlines](https://www.theverge.com/2021/4/22/22398156/university-minnesota-linux-kernal-ban-research) about [umn.edu email addresses being banned from submitting contributions to the Linux kernel](https://cse.umn.edu/cs/statement-cse-linux-kernel-research-april-21-2021) after UMN researchers deliberately injected vulnerabilities into the code.

Except that's not quite what happened.

The timeline of events goes something like this:

- Professor [Kangjie Lu](https://www-users.cs.umn.edu/~kjlu/) and a graduate student [Qiushi Wu](https://qiushiwu.github.io/) worked together to publish a [paper](https://github.com/QiushiWu/qiushiwu.github.io/blob/main/papers/OpenSourceInsecurity.pdf) analyzing past vulnerabilities in the Linux kernel, and identify the most common ways in which past vulnerability-introducing patches have gone undetected. 
- They identify that many vulnerabilities are introduced in parts, which they call "immature vulnerabilities". Two minor bugfixes individually don't cause problems (in fact, each one fixes them), but together the two introduce a vulnerability. (Often these are introduced by maintainers rather than potentially malicous actors). They argue this is especially problematic because Linux patch guidelines specifically rule out preventative patches, so there is no way for contributors to point out and fix these half-bugs.
- As a proof-of-concept demonstrating the dangers of leaving such things unaddressed:
    - They identify three actual bugs in the Linux kernel.
    - For each bug, they prepare two versions of the bugfix.
        - Both versions fix the bug is no more than 5 lines of code.
        - Neither version introduces a vulnerability itself.
        - But one version is "correct"
        - while the other introduces a partial vulnerability that when combined with a prexisting partial vulnerability already present in Linux, could cause a UAF vulnerability.
    - From a random gmail account, they send the flawed code to the Linux community asking for feedback.
    - As soon as any maintainer replies indicating that the patch looks good, they immediately send a followup email pointing out the introduced UAF, request them not to post the flawed patch, and provided the corrected patch.
    - (I'm really not sure what the point of the proof of concept was? They already had plenty of historical examples of this kind of issue, and the paper would have been interesting enough without these. The PoC isn't even a major part of the paper (after reading the exchanges, this looks like it's because they bungled it and the results would have made them look like idiots))
<!--- This caused controversy back at the end of 2020. Examples of coverage:
    - https://twitter.com/kengiter/status/1330649965270589441-->
- After much [kerfluffle](https://www-users.cs.umn.edu/~kjlu/papers/clarifications-hc.pdf), UMN's IRB (retroactively?) okayed the research, and the IEEE approved it as well.
- Several months later a *different* UMN student, [Aditya Pakki](https://adityapakki.github.io/), submits [some code](https://lore.kernel.org/linux-nfs/20210407001658.2208535-1-pakki001@umn.edu/) to the Linux maintainers. 
- One of the maintainers, Greg KH, [says the contribution is obviously crap](https://lore.kernel.org/linux-nfs/YH5%2Fi7OvsjSmqADv@kroah.com/), and speculating that this is yet again the work of Professor Lu.
- Pakki ~~privately~~ complains to Greg about the accusations (but the email contains html and so doesn't go through to the mailing list, [according to Greg.](https://lore.kernel.org/linux-nfs/YIUMYYcf%2FVW4a28k@kroah.com/))
    - (This sending html-email thing seems to be a recurring issue from the UMN lads.)
- Greg [quotes his message](https://lore.kernel.org/linux-nfs/YH%2FfM%2FTsbmcZzwnX@kroah.com/) and publicly doubles down, claiming there is no possible way the proposed patch is legit, banning all future contributions from UMN, and [reverting all previous contributions](https://lore.kernel.org/lkml/20210421130105.1226686-1-gregkh@linuxfoundation.org/) from @umn.edu email addresses. (Technically it was a bulk review request, not a bulk reversion.)
    - Note that the two accounts of these events directly contradict. 
        - Greg says "You, and your group, have publicly admitted to sending known-buggy patches to see how the kernel community would react to them, and published a paper based on that work."
        - The paper from UMN does not include Pakki as a contributor, and Lu confirms that Pakki was not associated with this research. So there is no way that Pakki has 'admitted' to such a thing. His team, sure, in a sense.
        - Greg says 'Commits from @umn.edu addresses have been found to be submitted in "bad faith" to try to test the kernel community's ability to review "known malicious" changes'.
        - The paper claims that none of the changes came from @umn.edu addresses, later [confirmed](https://www-users.cs.umn.edu/~kjlu/papers/full-disclosure.pdf).
- Greg [posts](https://twitter.com/gregkh/status/1384785747874656257) these exchanges to twitter.
- Greg's account of events gets [posted](https://news.ycombinator.com/item?id=26887670) all over [social](https://old.reddit.com/r/linux/comments/mvpcff/statement_from_university_of_minnesota_cse_on/) [media](https://old.reddit.com/r/linux/comments/mvd6zv/greg_khs_response_to_intentionally_submitting/), and there is much wailing and gnashing of teeth.
- [Kangjie apologizes again for the methodology of his paper](https://lore.kernel.org/lkml/CAK8KejpUVLxmqp026JY7x5GzHU2YJLPU8SzTZUNXU2OXC70ZQQ@mail.gmail.com/), and Greg replies that the apology is meaningless until a list of demands are met.
- The list of demands are, in brief:
    1. Provide a list of all patches with known vulnerable-code submitted by the researchers.
    2. Withdraw publication of the work.
    3. Make sure UMN research has IRB approval in the future.
    4. Make sure UMN's IRB doesn't approve human experimentation in the future.
- UMN's computer science heads investigate, agree that Lu's research was disrespectful, and [respond to the Linux demands thusly](https://drive.google.com/file/d/1z3Nm2bfR4tH1nOGBpuOmLyoJVEiO9cUq/view):
    1. No such patches exist. No bugs were deliberately published to the Linux kernel by this research, deliberately or otherwise.
    2. Lu agrees. He's withdrawn the paper.
    3. This paper did have correct approval.
    4. "Human Subjects Research" is a legal term, and does not simply mean *any research that personally embarrasses Greg*. The IRB's job is to ensure that research meets legal standards, which they did in this case because the paper does. The research methods were indeed disrespectful, and legal standards are not the only ethical consideration that should be taken into account, but that's outside the purview of an IRB. (But the official response was much more polite. <!--The vitriol is entirely my own, and I would add that Greg seems like the kind of guy who calls the police over poor customer service.-->)
- After getting consent from the people involved, Lu and Wu release the [full logs](https://www-users.cs.umn.edu/~kjlu/papers/full-disclosure.pdf) of their conversations with the Linux community. 


---

Here's a highlight from an [email exchange back in August of 2020](https://lkml.org/lkml/2020/8/27/1197) (shortly after the deceptive commits) that's retroactively kind of funny:

Wu says that Linux is potentially vulnerable because 
> 1. Linux allows anyone to submit a patch because it is an open community.

Greg replies 
> And how is 1. a "risk"?

Wu:
> We are assuming the possibility of potential malicious commit contributors
and want to reduce the risk of accepting vulnerable patches from them.

Greg:
> No, you are thinking about this all wrong.
> 
> ALL contributors make mistakes, you should not be treating anyone
different from anyone else.  I think I probably have contributed more
bugs than many contributors, does that make me a "malicious"
contributor?  Or just someone who contributes a lot?
> 
> So checking on patches needs to be done for everyone, right?
> 
> We have an idea of "trust" in kernel development, it's how we work so
well.  I don't trust people not that they will always get things
"correct", but rather that they will be around to fix it when they get
it "wrong", as everyone makes mistakes, we are all human.
> 
> So we trust people who we accept pull requests from, we don't review
their contributions because we trust that they did, and again, they will
fix it when it goes wrong.

So if Wu and Lu's goal was to get Greg to rethink his stance on this position... mission accomplished... I guess?




Also, from the [disclosure document]](https://www-users.cs.umn.edu/~kjlu/papers/full-disclosure.pdf), it's now clear why the proof-of-concept wasn't a major part of the original paper. It's because they never actually really executed on it. They sent 5 patches from their fake gmail addresses:

1. Fig 11 - The first patch was meant to be buggy, but there was a bug in their bug and they accidentally submitted a correct bugfix.
2. Fig 9 - The second patch was buggy, but the maintainers caught the bug. Surprisingly, this is because *someone else* already submitted a [nearly identical patch](https://git.kernel.org/pub/scm/linux/kernel/git/gregkh/tty.git/commit/?h=tty-next&id=84ecc2f6eb1cb12e6d44818f94fa49b50f06e6ac) that was accepted and later had to be reverted.
    - The original buggy patch was submitted 2019-05-23, and committed by Greg 2019-05-24
    - [Greg](https://lore.kernel.org/lkml/20190524080200.GA19609@kroah.com/): "Any reason you keep dropping me from this thread? It's as if you don't want me to apply the patch :("
    - On 2019-06-04, Ben Hutchings [raises awareness](https://lore.kernel.org/lkml/20190604180039.gai2phwdxn7ias6n@decadent.org.uk/) of the introduced problem, and Greg [applies](https://git.kernel.org/pub/scm/linux/kernel/git/gregkh/tty.git/commit/?h=tty-next&id=15b3cd8ef46ad1b100e0d3c7e38774f330726820) the revert.
    - This series of events is described in [this talk](https://kernel-recipes.org/en/2019/talks/cves-are-dead-long-live-the-cve/) at [about 11 minutes in](https://youtu.be/HeeoTE9jLjM?t=665).
    - Fortunately the changes were reverted before the changes hit the public tree.
    - The talk is actually pretty interesting. There are [external databases](https://bugzilla.redhat.com/show_bug.cgi?id=1715491) of security issues. But they're gamed for resume building. Developers want their patches applied, and some major organizations require all CVE patches to be applied in their version. So devs will make a bogus CVE to force their patch into production. 
    - It also shows that Greg is aware of the issues raised in Lu's paper. So I think Greg's irrational response is less a general demeanor, and more that a conflux of bugbears combined together to drive him into a rage (the libel part was still not cool, Greg.)
    - Around [42 minutes](https://youtu.be/HeeoTE9jLjM?t=2492), some discussion of how applying a bug fix is worth the risk, because it's a 100% chance of a known public vulnerability vs a 0.01% chance of a new bug being introduced
        - There is later some pushback from an audience member about the assertion that such a tiny portion of patches later need to be reverted.
3. Fig 10 - The third patch was double buggy, and although nobody caught the deliberate bug, they did catch the accidental bug.
4. The fourth patch was similar. The deliberate bug went un-noticed, but a different problem was identified. "so my previous patch is meaningless... And sorry for bothering you." "Ok that's fine, thanks anyway!"
5. The last (chronologically first) was also accidentally a correct bugfix.


---


<!-- Greg claims that there is no reasonable explanation for Pakki's -->

<!--One of these accounts is a paper approved by an IRB and written as a presentation for the 42nd IEEE Symposium on Security and Privacy, and the other is an angry rant posted on twitter for social media validation. I wonder which one is more accurate. 🤔🤔🤔-->



My guesses (made before all the details came out) were
- The overconfidence of Pakki as percieved by Greg KH is simply plain old ESL troubles.
- Lu did not instruct Pakki to deliberately submit flawed code using his real name from a umn.edu address (95% confidence) (CORRECT)
- Pakki did not deliberately submit flawed code using his real name from a umn.edu address (80% confidence)(CORRECT)
- Pakki did not deliberately submit flawed code (70% confidence)(CORRECT)
- Prof Lu did have at least some connection to Pakki's bogus commit (90% confidence) (CORRECT)
    - Part of Lu's paper identified that the error code is especially prone to partial vulnerabilities and suggested the expanded use of static analyzers to catch such problems.
    - Lu also identified "refcount" as a potential source of accidental UAFs.
    - All of these are keywords that show up in Pakki's proposed fix, so it seems to me like Pakki read Lu's (his advisor) paper, tried to find and fix one of the partial vulnerabilities mentioned therein, and bungled it, maybe. 
    - Only 90% confidence because I'm just going on vague word association here, not actual understanding of the code.
- I also strongly suspect that Greg himself was one of the people who gave the thumbs up to one of the pieces of flawed code. I don't know the size of the community, which would be needed to actually assign a percentage confidence to that, and it would likely be a very low probability in any case, but it just *feels* poetically apt. (AMBIGUOUS)
    - None of the buggy patches submitted by Wu and Lu were accepted, let alone by Greg. 
    - But the reason one of the patches was rejected was because it was near-identical to a [previously submitted buggy patch](https://git.kernel.org/pub/scm/linux/kernel/git/gregkh/tty.git/commit/?h=tty-next&id=84ecc2f6eb1cb12e6d44818f94fa49b50f06e6ac). This patch was submitted by somebody else and committed to the kernel by Greg.
    - So on the one hand, my prediction was incorrect because Greg did not approve a known-flawed patch from Wu and Lu. On the other hand, my prediction was correct because he did kind-of approve that specific bug. 
    - Greg [did reply](https://lore.kernel.org/lkml/20200810075122.GA1531406@kroah.com/#t) to that patch from Lu, mentioning that he gave a whole [talk](https://kernel-recipes.org/en/2019/talks/cves-are-dead-long-live-the-cve/) about that change.
 






So what are the lessons to learn from this ordeal?
1. The legal requirements surrounding human subjects testing are not equivalent to the set of best ethical practices for doing research. 
2. Be honest and considerate whenever interacting with someone, even when the interactions don't technically count as experimentation. Even if you are studying a system, the people within that system deserve to be treated with respect.
3. If you are sufficiently prestigious within a community, you can make up claims which are easy to verify as false, and other people will uncritically repeat your lies.
    - **Prestigious Insider** says that **Shady Outsider** is a dirty rotten liar.
    - **Shady Outsider** has proof that **Prestigious Insider**'s claims are false.
    - But **Shady Outsider** is a liar! So they must be lying about their evidence as well!
    - This is yet more evidence about what a dirty rotten liar **Shady Outsider** is. Even if the initial transgression was forgiveable, falsfying evidence like this is unforgiveable.
    - [And thus does the entire community gleefully charge into hell.](https://en.wiktionary.org/wiki/Kafkatrap)
4. If you're like me and thought that Linux was secure because of word-of-mouth from techy communities, then you need to significantly lower your confidence in the Linux Kernel. After all, the community's  response to (admittedly disrespectful avenues of) criticism is to harass an uninvolved third party and revert a bunch of legitimate bugfixes.
    - Though in Greg's talk, he does argue that Google in particular is doing well on fixing bugs before peple even realize it, and that Pixel in particular is incredibly secure.
<!--5. Prof Kangjie Lu is probably a bit on the autism spectrum, and Greg Kroah-Hartman is either an idiot or a sociopath.-->

<!--
Oh damn! 

> On 4/21/21 8:21 AM, Kangjie Lu wrote:
> All of the commits sent by my students are in good faith to fix some bugs.


> Hi everyone,
> 
> I am so sorry for the concerns. I fully understand why the community is
> angry. Please allow me to have a very quick response, as Jiri requested. We
> will provide a detailed explanation later.
> 
> These are two different projects. The one published at IEEE S&P 2021 has
> completely finished in November 2020. My student Aditya is working on a new
> project that is to find bugs introduced by bad patches. Please do not link
> these two projects together.  I am sorry that his new patches are not
> correct either. He did not intentionally make the mistake.

VERDICT: I AM UNDERCONFIDENT







---

[Here's a summary and critical response](https://davisjam.medium.com/ethical-conduct-in-cybersecurity-research-86d13b6b6eed) by 
James Davis, a professor at Purdue, and the only person on the entire internet who bothered to read the paper in question.

It addresses the controversial paper, but doesn't talk about Greg KH's mistreatment of a student in April.


---

Hilariously, Greg's [twitter post](https://twitter.com/gregkh/status/1384785747874656257), 
says 
> Linux kernel developers ... have enough real work to do
But he made 190 reverts. A few of these were actually buggy, but none deliberately so. And most of the contributors who replied said that the original changes are fine, and not to revert. 

So Lu's paper fixed several bugs, but just did it in a way that prompted the uneccesary review of less than 15 lines of code. Greg's response prompted the unecessary review of thousands of lines of code. Great job, Greg. Very respectful of the community's time; totally not a narcissistic power move.

[One of the replies](https://lore.kernel.org/lkml/20210421180155.GA2287172@nvidia.com/) points out Greg's mistake. At least not all of the Linux maintainers are braindead.

To be fair, [one of the replies](https://lore.kernel.org/lkml/78ac6ee8-8e7c-bd4c-a3a7-5a90c7ccb399@roeck-us.net/) identifies one of Lu's contributions as malicious.
But not the one linked. 
Instead refers to c9c63915519b1def7043b184680f33c24cd49d7b ??? "hwmon: (lm80) fix a missing check of the status of SMBus read" [This one?](https://lore.kernel.org/lkml/20181221190134.930-1-kjlu@umn.edu/).
Ah nvm. Lu  [fixed the bug that was introduced](https://lore.kernel.org/lkml/4afeeb49-620d-5a9d-29fc-453f6118a944@roeck-us.net/), and this clearly wasn't part of the research everyone is so mad about, being from all the way back in 2018.


## The paper in question

Qiushi Wu and Kangjie Lu (2021), [On the Feasibility of Stealthily Introducing
Vulnerabilities in Open-Source Software via
Hypocrite Commits](https://github.com/QiushiWu/QiushiWu.github.io/blob/main/papers/OpenSourceInsecurity.pdf), working paper.

[And here are some clarifications.](https://www-users.cs.umn.edu/~kjlu/papers/clarifications-hc.pdf)


use-after-free
: Memory is freed without getting rid of the pointer to that memory. Then later, some other bit of code uses that chunk of memory, with the original dangling pointer still pointing to it, which can cause pramblems.

hypocrite commits
: a small patch that fixes a minor issue, but also introduces the missing pieces of an immature vulnerability.

> Note that the experiment was performed in a safe way—we
ensure that our patches stay only in email exchanges and will
not be merged into the actual code, so it would not hurt any
real users (see §VI-A for details).

immature vulnerabilities
: Half-baked vulnerabilities. Vulnerabilities usually involve several distant bits of borked code, and an immature vulnerability is a slightly borked bit of code that could potentially cause problems when combined with another not-yet-existing slightly borked bit of code.


The paper gives examples of cases in the past where a bug-fix introduced a UAF vulnerability to Linux code and went undetected for 5 years, and say that "even experienced maintainers may (un-
intentionally) submit vulnerability-introducing patches".

Looking through [a database of patches known to cause vulnerabilities in linux](https://www.cvedetails.com/product/47/Linux-Linux-Kernel.html?vendor_id=33), the researchers found that about 10% (138) were caused by bug fixes shorter than 30 lines.  

[Though here's an old Greg presentation saying CVEs are useless.](https://www.slideshare.net/ennael/kernel-recipes-2019-cves-are-dead-long-live-the-cve) Haven't read it so don't know why.

This is a problem because OSS projects reject preventative fixes. [According to this guide on Linux -stable releases](https://web.archive.org/web/20190825172947/https://www.kernel.org/doc/html/v4.10/process/stable-kernel-rules.html), 

> It must fix a real bug that bothers people (not a, “This could be a problem...” type thing).

And because some OSS, like android, rejects even legit patches if they don't have a proof of concept showing how an exploit could work. The authors claim that they "reported multiple patches
without a PoC for real bugs, and none of them was accepted."


Analysis of past 500 minor patches:

|Contributor|General Patches % |Vulnerable Patches %|
|---|---|---|
|Academia|1.0|1.5|
|Company|38.0|47.0|
|Maintainer|47.8|37.3|
|Personal|9.4|11.1|
|Organization|3.8|3.0|


"we find 457 memory-release functions in the
Linux kernel, and more than half of them do not even have
keywords like dealloc or release in the names, thus can
stealthily introduce the freed state"

Error paths are indentified as ideal places in which stealthy hypocritical commits can sneak in.

> Experiment overview. In this experiment, we leverage
program-analysis techniques to prepare three minor hypocrite
commits that introduce UAF bugs in the Linux kernel. The
three cases represent three different kinds of hypocrite commits:
(1) a coding-improvement change that simply prints an error
message, (2) a patch for fixing a memory-leak bug, and (3) a
patch for fixing a refcount bug. We submit the three patches
using a random Gmail account to the Linux community and
seek their feedback—whether the patches look good to them.
The experiment is to demonstrate the practicality of hypocrite
commits, and it will not introduce or intend to introduce actual
UAF or any other bug in the Linux kernel.

> In addition
to the minor patches that introduce UAF conditions, we also
prepare the correct patches for fixing the minor issues. We
send the minor patches to the Linux community through email
to seek their feedback. Fortunately, there is a time window
between the confirmation of a patch and the merging of the
patch. Once a maintainer confirmed our patches, e.g., an email
reply indicating “looks good”, we immediately notify the
maintainers of the introduced UAF and request them to not
go ahead to apply the patch. At the same time, we point out
the correct fixing of the bug and provide our correct patch.
In all the three cases, maintainers explicitly acknowledged
and confirmed to not move forward with the incorrect patches.
All the UAF-introducing patches stayed only in the email
exchanges, without even becoming a Git commit in Linux
branches.

> The experiment will not collect any personal data, individual
behaviors, or personal opinions. It is limited to studying the
patching process OSS communities follow, instead of individ-
uals. All of these emails are sent to the communities instead
of individuals. We also prevent the linkage to maintainers.
In particular, to protect the maintainers from being searched,
we use a random email account, and three cases presented in
§VI-C are redacted.

> The OSS communities are
understaffed, and maintainers are mainly volunteers. We respect
OSS volunteers and honor their efforts. Unfortunately, this
experiment will take certain time of maintainers in reviewing
the patches. To minimize the efforts, (1) we make the minor
patches as simple as possible (all of the three patches are less
than 5 lines of code changes); (2) we find three real minor
issues (i.e., missing an error message, a memory leak, and a
refcount bug), and our patches will ultimately contribute to
fixing them.

They develop a tool to identify potentially problematic dereferenced pointers or freed but non-nullified pointers.

Several hundred potential vulnerabilites are detected. They manually review 100 of them and select the three that they believe maintainers will be least likely to catch.

> All these experiments including the manual analysis
were finished within one week by one researcher. Note that
to prevent the cases from being re-identified in the code, we
simplify the code, and redact names of functions and variables.

Part VII tries to quantify and detect immature vulnerabilites.

A UAF has three pieces:
- free of a pointer without nullification
- a use of that pointer
- a specfic temporal order (use happens after free.)

>  By
searching the Git history in the past two years (from August
2018 to August 2020), we in total found 353 patches for fixing
refcount-leak bugs. As such, we believe that adversaries have
many opportunities to invoke refcount-decrementing functions
to trigger implicit releases. Similarly, we also measure the
opportunities for introducing memory release. The Git history
in the past two years shows 1,228 memory-leak bugs were fixed,
indicating that memory leak is also very common. Adversaries
can readily employ existing tools like Syzkaller [ 57 ] and
Hector [ 53 ] to find memory leaks. For example, we ran
Syzkaller on the latest version of the Linux kernel with a
regular desktop for only one week, and it successfully found
12 memory leaks. These results confirm that it is not hard for
adversaries to find opportunities to introduce object releases.

>  By
developing an LLVM pass, we collect freed pointers that are
not nullified or redefined. In this analysis, we only consider
kfree() as the release function. The analysis reports more
than 30K cases. Therefore, adversaries have a large number of
potential opportunities to introduce a use to form a UAF. As
shown in §VI, if we refine the results by only counting cases
that can be further used in error paths, we still have 4,657
candidate cases.

> We found that 1,085 objects are
referenced in concurrent functions, i.e., they can be used and
freed concurrently. Since these objects are likely protected
with locks (otherwise, they are already UAF), adversaries can
attempt to remove the locks or move the uses out of the critical
sections to introduce the use-after-free temporal order (e.g.,
the example shown in Figure 6).

Looking at past commit attempts, they quantify the commits that were rejected as causing UAF vulnerabilities of different types, and the ones that weere accepted and later found to cause vulnerabilities.

|Condition|CAtch rate %|
|---|---|
|Concurrency|19.4|
|Implicit Release|36.3|
|UAF in Error Paths|42.0|
|Alias|38.4|
|Indirect Call||
|Baseline|56.6|




The most annoying thing about the paper is that one of their proposed solutions to prevent this kind of thing is 

>  First, OSS projects would be suggested
to update the code of conduct by adding a code like “By
submitting the patch, I agree to not intend to introduce
bugs.”

🙄

> By introducing the liability, the
OSS would not only discourage malicious committers but also
raise the awareness of potential introduced bugs for benign
committers.

🙄🙄🙄

To be fair, some of their other suggestions are more reasonable 
- Improve fuzzers by having them emulate driver code (62% of linux kernel is driver code) and improve the coverage of error code.
- Accepting certain preventative patches
- Open veto ability of patches to a larger number of participants


> We summarized our findings and suggestions, and reported
them to the Linux community. Here we briefly present their
feedback. First, the Linux community mentioned that they will
not accept preventive patches and will fix code only when it
goes wrong. They hope kernel hardening features like KASLR
can mitigate impacts from unfixed vulnerabilities. Second, they
believed that the great Linux community is built upon trust.
That is, they aim to treat everyone equally and would not
assume that some contributors might be malicious. Third, they
mentioned that bug-introducing patches is a known problem
in the community. They also admitted that the patch review is
largely manual and may make mistakes. However, they would
do their best to review the patches. Forth, they stated that Linux
and many companies are continually running bug-finding tools
to prevent security bugs from hurting the world. Last, they mentioned that raising the awareness of the risks would be
hard because the community is too large.


lol
> Yin et al. [ 67 ] showed that
concurrency bugs are the most difficult to fix correctly, and
39% of concurrency bug fixes are incorrect

> hypocrite commits themselves
do not contain malicious functionalities or vulnerabilities, but
introduce vulnerability conditions


## Takeaways

My main takeway is that internet comments are garbage. Even on a website with a relatively educated userbase, most of the commentors haven't actually read what happened, and are instead spinning wild tales about what they imagined happened based on a one sentence summary of events.

Another takeaway is that I should significantly lower my prior that linux is actually secure. My confidence in linux as compared to other operating system was, if I'm being honest in self-reflection, largely founded based on comments by technically minded people on technically-minded internet communities (hacker news and various techie subreddits).
But here we have a concrete example where these same technically minded people are typing thousands of hateful comments, and most of them lack even the barest reading comprehension to understand that 
- the people who did the security research are different from the student who got into a pissfight with GKH. (They are from the same university, and to be fair, Lu is Pakki's advisor.)
- The deliberately vulnerability-introducing commits where not sent from umn.edu addresses
- The deliberately vulnerability-introducing commits did not actually make it into the linux kernel.

In fact, many commenters are explicitly arguing against these statements after being corrected.

Even some of the Linux community in the original messaging tree failed these basic reading comprehension tests

[Example 1](https://lore.kernel.org/linux-nfs/YICB3wiptvvtTeA5@mit.edu/):

> Of course, UMN researchers could just start using fake e-mail
addresses, or start using personal gmail or yahoo or hotmail
addresses.  (Hopefully at that point the ethics review boards at UMN
will be clueful enough to realize that maybe, just maybe, UMN
researchers have stepped over a line.)

[Example 2](https://lore.kernel.org/linux-nfs/CAHr+ZK8xp5QU8wQHzuNkJdsP20fC=nW4B33gwMUwHY82f_u5WA@mail.gmail.com/):

> Banning UMN seems to be a temporary solution. I don't disagree.
But it still might not prevent such proof-of-concept efforts: one
could use a non-campus address.

[Example 4:](https://lore.kernel.org/linux-nfs/6530850bc6f0341d1f2d5043ba1dd04e242cff66.camel@hammerspace.com/)
> <shrug>That's an easy thing to sidestep by just shifting to using a
private email address.</shrug>
> 
> There really is no alternative for maintainers other than to always be
sceptical of patches submitted by people who are not known and trusted
members of the community, and to scrutinise those patches with more
care.

[Non-example:](https://lore.kernel.org/linux-nfs/YIAmrgZ4Bnqo%2FnmI@unreal/)
> Right, my guess is that many maintainers failed in the trap when they
saw respectful address @umn.edu together with commit message saying
about "new static analyzer tool".

At least he acknowledges that he's just guessing.

[Here's a user saying that one of Greg's reverts was to a legit fix](https://lore.kernel.org/linux-nfs/20210421094241.1bb65758@gandalf.local.home/)

[Example 6:](https://lore.kernel.org/linux-nfs/YIAmy0zgrQW%2F44Hz@kroah.com/)

> If they just want to be jerks, yes.  But they can't then use that type
of "hiding" to get away with claiming it was done for a University
research project as that's even more unethical than what they are doing
now.

[Non-example:](https://lore.kernel.org/linux-nfs/821177ec-dba0-e411-3818-546225511a00@grundis.de/)

Astounding. I find the one person in the entire thread who actual read the paper everyone is complaining about, and they explicitly say "I'm not involved or affliated with the group or the kernel". 

[One of the commenters](https://lore.kernel.org/linux-nfs/YIAta3cRl8mk%2FRkH@unreal/) claims [this commit](https://github.com/torvalds/linux/commit/8e949363f017) (from 2019) by Pakki deliberately introduces a bug. The timeline seems off to me, and I don't know enough to check the code myself. I don't know whether its actually a bug or just jousting at windmills. 

Oh, the child comments argue it's not an actual bug. And the timeline seems old enough that if it is a bug, I'd wager on a genuinely accidental one.

Another child commenter points out the accused deliberate bug is the result of a [paper by Pakkit](https://www-users.cs.umn.edu/~kjlu/papers/crix.pdf), so unless Pakkit wrote a paper in 2019 as cover for somebody elses paper in 2020, this is probably not a example of a deliberately introduce UAF.


[Example 7](https://lore.kernel.org/lkml/nycvar.YFH.7.76.2104211628560.18270@cbobk.fhfr.pm/)


[Turns out the Linux ML is prone to bouts of extreme paranoia](https://lore.kernel.org/lkml/6406f3ad-141d-5533-c717-e11cea4e179e@roeck-us.net/)


[Example 8](https://lore.kernel.org/lkml/20210421154949.GA168854@roeck-us.net/)

[Example 9: A contributor exhibitting all the reading comrehension skills of a 4th grader. Round of applause everyone.](https://lore.kernel.org/lkml/YIBMKSovJumS79SR@pendragon.ideasonboard.com/)

Oh geez. After reading Lu's apology letter, I found [this news article](https://itwire.com/open-source/uni-bid-to-patch-up-with-linux-kernel-project-fails-to-move-maintainer.html). In the very first (nonbolded) sentences, they already are making major factual errors.




Oh, [here's Linus' response](https://itwire.com/open-source/torvalds-says-submitting-known-buggy-patches-is-a-breach-of-trust.html)

> "I don't really know what to say, I think the email thread is likely the most relevant information," Torvalds told iTWire in response to a query.
> 
> "I don't think it has been a huge deal _technically_, but people are pissed off, and it's obviously a breach of trust."
> 
> Torvalds added: "It's also annoying, because most of the patches are valid (and the ones that aren't are generally 'useless' rather than 'actively malicious'), so it's basically a huge waste of people's time to now go over those things again just because one source has shown itself to not be above board."

Oh no, even Linus has been misled about the situation. I mean, if this isn't a valid case of libel against GReg, I don't know what is. 

It looks like it might be a sticking point that the Linux lads demand a list of the buggy patches that made it into stable. But of course, Lu can't provide such a thing, because no such patches exist, which the linux lads would know if - and I'm repeating myself here - they had even basic levels of reading comprehension.

And is just bias making me uncharitable, or does this article read like the writer is terrified of Greg abusing them?

> Kroah-Hartman, normally a man who is the epitome of politeness, lost his cool when these patches were sent as it needlessly created additional work for him 

> Despite these provocations, Kroah-Hartman used polite language in responding to Pakki and the university.

Meanwhile the *polite* response in question is full of randomly capitalized words, starts with a snarky copypasta, and ends with a [\*plonk\*](https://en.wikipedia.org/wiki/Plonk_(Usenet))

[Similarly](https://itwire.com/open-source/uni-group-slammed-over-submitting-known-buggy-patches-to-linux-kernel.html), 

>  the normally mild-mannered Linux developer Greg Kroah-Hartman, the maintainer of the stable kernel
> ... But Kroah-Hartman was not buying this and did not mince his words when he responded. 

[Weird how this tweet is marked as sensitive.](https://twitter.com/k8em0/status/1384895263479902209)

Oh, [here's a twitter account](https://twitter.com/daniel_bilar) to follow. Lots of interesting links, and he is one of the dozen or so people who actually read Lu's paper.


[Example 32423423](https://www.labbott.name/blog/2021/04/21/breakingtrust.html)

This is a related blogpost which was retweeted by Greg. It's the most cogent and sensible response I've read, but the author still... didn't... read... Lu's... paper.

> This is a pretty poor attack vector since, again, to do something effective you would probably need multiple small patches.

> It would have been helpful to have a clear list of all patches submitted with a note of which ones were actually bad (at this point everyone seems to be playing guess the bad patch).

> The authors stated “We did not introduce or intend to introduce any bug or vulnerability in the Linux kernel.” Saying they did not introduce a vulnerability among any of the patches they submitted is a pretty strong statement. Non-malicious patches are still the most common way bugs are introduced and at least some of the presumably good patches were still flagged by maintainers. 

Yes! Which is one of the big things argued in Lu's paper.

I am in agreement with them about the assinaity of the CoC proposal in Lu's paper.


[Twitter user says IEEE already looked at the paper in question.](https://twitter.com/MortenLinderud/status/1384907194395766787) Also claims that IRB was post-factum.

---

[Okay, finally. Here's an in depth article by someone else who has actually read the paper.](https://davisjam.medium.com/ethical-conduct-in-cybersecurity-research-86d13b6b6eed)

> I have carefully read the authors’ paper [1] and their FAQ [2]. I believe that they acted in good faith. In their prior work they have made exemplary efforts to promote cybersecurity in major software projects, for which I thank them. However, in this case, they made an ethical misstep out of a misapprehension of what constitutes ethical conduct and human-subjects research in computing.


He sidesteps Greg's libel against Pakki, but that's more a matter of focus rather than an actual misrepresentation like every other account I've seen.


> Was this human-subjects research?  
**Arguments for “yes”**  
Let’s map the federal definition of human-subjects research to the authors’ research method #2 from above. 
The authors:
    - Interacted with living individuals (the Linux maintainers)  
    - Obtained information (whether the maintainers would approve a malicious commit)  
    - Analyzed that information (discussion of factors that lead to patch acceptance, and, as discussed in section 8.D, the maintainers’ perspectives on this experiment).  
> 
> I am not a lawyer, but that sure looks like the definition of human-subjects research to me.  
**Arguments for “no”**  
    - In their FAQ, the authors write “This is not considered human research. This project studies some issues with the patching process instead of individual behaviors” [2].  
    - The UMN IRB agreed with the authors. They (retroactively) approved the research protocol, and according to the authors this approval stated that the work did not involve human-subjects [2].*  
    - The IEEE S&P review committee agreed with the authors. According to the conference’s call for papers, which includes “Ethical Considerations for Human Subjects Research”, the reviewers reserve the right to reject papers that do not meet ethical standards. Since the paper was accepted despite having been conducted without oversight from the institution’s human-subjects review board (the IRB), it appears that the research community* agrees that this was not human-subjects research — or at least, not unethical human-subjects research.  
*I hesitate to paint with a broad brush, and I understand that individual community members may feel as I do…but the paper was accepted at the conference.

This feel reasonable, if not from an enforceable rules standpoint, at least from a post-hoc evaluation standpoint.

> If humans feel they have been experimented on, we should call this “human-subjects research” — despite what the authors, UMN’s IRB, and the research community say.

Among his recommendations for an improved study design, 
- Changing the patch to include non-functional issues seems like it elides the point of the paper about non-problems combining into problems.
- Informing some Linux higher-ups seems like it absolutely should have been done.
- The simulated review process is something I'd like to see not just in this study, but in more general applications. IRB simulated audits, code simulated audits. All sorts of stuff.

It seems rather silly when Davis suggests that even asking an expert for advice counts as doing experimentation on them and should be subject to a review board. But overall this article has been a balm to my soul.

I am at peace.

The only comment on the article is one of the Linux lads from the original email chain. At least now he is fair to Pakki. 

> Ultimately, the problem seems to be that the researchers aren't seeing the developers as human, but rather assuming that "the review process" is a free resource, which they can (ab-)use without any consequence in the course of doing their research. I suspect it was this dynamic which was the cause of the anger felt by some in the kernel community.

I mean, Greg's lies were also a pretty big source of the anger, but this is fair.




[Ooooh, shiny.](https://twitter.com/tomwarren/status/1384926961466847233)


[UMN's contributions to the Linux kernel appear to be vastly in good faith. Our review is ongoing...](https://twitter.com/kees_cook/status/1385354253552656384)

https://twitter.com/kernellogger/status/1386179536820350976
A random tweeter deep in the replies points out that Greg may have violated CoC

[Here's a twitter account with prejudices similar to my own.](https://twitter.com/DanielMicay)  

[My unpopular opinion for today: Reverting the entire history of contributions by UMN to the Linux kernel means reverting a lot of genuine security *fixes*, which will now be exploitable. This is not the right way to prove a point. This hurts Linux.](https://twitter.com/KentonVarda/status/1385074808015126532)
In fairness to Greg, the reverts won't be pushed until after they've been reviewed.

> Not to mention, re-reviewing hundreds of commits seems like a pretty big waste of maintainers' time in itself? Certainly much more time than was ever wasted reviewing three 5-liner vulnerable commits that weren't merged. This isn't rational, it's just anger and posturing.

I'm still inclined to lean towards ESL charitability, but eh.


- One of the other linux maintainers [acknowledges they were misled.](https://lwn.net/Articles/854319/)

They do insist on this silly list of commits thing (again, no commits happened)

Oh, and of course, they repeat the claim that Pakki was one of Lu's coauthors.
Sound the alarms! Linux is indeed maintained by illiterates.

[Okay, good. I'm not the only one who thinks Greg needs have his conduct formally rebuked](https://twitter.com/spendergrsec/status/1386331099102654472). [Open letter.](https://grsecurity.net/~spender/greg_kh_removal_from_coc.txt)


---

All this should really shift some probability mass from "linux is good actually" to "linux is a weird internet cult".

Ramp up the cult conclusion. Lots of people talking about how kind and gentle greg is, and 

And all the really hardcore computer science people I know prefer MacOS, so maybe I should be looking into building a hackintosh...






[Wowzer.](https://old.reddit.com/r/neoliberal/comments/mva5vo/discussion_thread/gvbwbpe/)

> I hope atleast the student fails to get their degree and gets kicked out, their advisor gets fired, and the college's accrediting agency decides to review if they should still be accredited.

I wonder if Pakki genuinely has a case for libel. This is crazy.
-->