---
layout: default
title: Week 3 – Aggregation and Least Squares
nav_exclude: true
---

<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>

# Week 3 – Aggregation and Least Squares

---

## Lecture (January 24th) 👨‍🏫

- [blank slides 😶](../../slides/lec03.pdf)
- [annotated slides 😊](../../slides/lec03-annotated.pdf)
- [code 💻](http://datahub.ucsd.edu/user-redirect/git-sync?repo=https://github.com/dsc-courses/dsc90-2022-wi&subPath=lecture/lec03/lec03.ipynb)
- [recording 🎥](https://youtu.be/tOknmjne2VA)

---

## Readings 📖

Required:
- Kopf, [The Discovery of Statistical Regression](https://priceonomics.com/the-discovery-of-statistical-regression/)
- At least one of the following 3:
    - NCSU, [Right Ascension](https://www.physics.ncsu.edu/classes/astron/Right_Ascension.html)
    - Richmond, [A Review of Coordinates](http://spiff.rit.edu/classes/phys440/lectures/coords/coords.html)
    - [YouTube: Right Ascension and Declination, explained.](https://www.youtube.com/watch?v=g7DlB5lYm9g)
- UCAR, [Tycho Brahe's Observations and Instruments](https://www2.hao.ucar.edu/Education/FamousSolarPhysicists/tycho-brahes-observations-instruments)
- Farebrother, [Boscovich, Rogerius Josephus](https://encyclopediaofmath.org/wiki/Boscovich,_Rogerius_Josephus) (don't spend too long trying to understand the math if it is unfamiliar, but do read it)

---

## Homework 3 (due Sunday, January 30th at 11:59PM) ([solutions](https://campuswire.com/c/GCAB4734F/feed/19)) 📝

Submit your answers as a PDF to Gradescope by the due date for full credit. We encourage you to discuss the readings and questions with others in the course, but all work must be your own. **Remember to use Campuswire if you need guidance!**

<br>

### Question 1
First, make sure that you've read [The Discovery of Statistical Regression](https://priceonomics.com/the-discovery-of-statistical-regression/).

(a) Who found the connection between least squares and probability? (Just the name will suffice.)

(b) You may notice the priority dispute between Legendre and Gauss for the discovery of least squares resembles an earlier priority dispute, regarding the creation of calculus. In both cases (least squares and calculus), one individual published their work first, while the other claimed to have known about the idea before it was first published. In both cases, who published their work first? (Just the names of both individuals will suffice.)


### Question 2

King Triton, UCSD's mascot, has come up with a new way of measuring time. His new time format, called Triton Time, is well-suited to describing periods of time relative to the academic quarter, which is 10 weeks long.

<center><img src='https://www.ucsandiegotenniscamps.com/images/ContactLogo15.jpg' width=100></center>

He defines the units of Triton Time as follows:
- 1 Triton Degree (TD) is equal to 10 weeks
- 1 Triton Minute (TM) is equal to 1/10th of a TD
- 1 Triton Second (TS) is equal to 1/7th of a TM
- 1 Triton Nanosecond (TN) is equal to 1/48th of a TS

Times in Triton Time are specified in ordered quadruplets, starting with a T. For example, $$T(2, 1, 4, 3)$$ corresponds to 2 TD + 1 TM + 4 TS + 3 TN.

a) Convert $$T(4, 3, 2, 5)$$ to regular days, hours, and minutes (e.g. "$$a$$ days,  $$b$$ hours, and $$c$$ minutes", where $$a$$, $$b$$, and $$c$$ are whole numbers).

b) Convert $$79 + \frac{7}{48}$$ days into Triton Time. That is, specify your answer as $$T(a, b, c, d)$$, where $$a$$, $$b$$, $$c$$, and $$d$$ are whole numbers. Make sure to confirm your answer by converting it back into days.

_Hint:_ Look closely at the definitions of each of the four components of Triton Time – the denominators might seem familiar.

c) Triton Time is not nearly as fine-grained as our regular method of measuring time. What is the level of precision of Triton Time?

For example, if your answer is "one minute", you're saying that it's possible to pick two times that are exactly one regular minute apart and specify them both with different Triton Times, but it is not possible to do this with any amount of regular time less than one minute.

### Question 3

This question is contained with a Jupyter Notebook, which is [linked here](http://datahub.ucsd.edu/user-redirect/git-sync?repo=https://github.com/dsc-courses/dsc90-2022-wi&subPath=homework/hw03/hw03-student.ipynb). All of your answers (including screenshots of your code) should end up in your submitted PDF; you will not be submitting this notebook anywhere.