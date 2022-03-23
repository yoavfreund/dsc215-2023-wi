---
layout: default
title: Week 4 – Least Squares, Regression, and Correlation
nav_exclude: true
---

<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>

# Week 4 – Least Squares, Regression, and Correlation

---

## Lecture (January 31st) 👨‍🏫

- [blank slides 😶](../../slides/lec04.pdf)
- [annotated slides 😊](../../slides/lec04-annotated.pdf)
- [recording 🎥](https://youtu.be/uwXWAuwER3c)

---

## Readings 📖

- Rose, [How the Idea of a 'Normal' Person Got Invented](https://www.theatlantic.com/business/archive/2016/02/the-invention-of-the-normal-person/463365/)
- Clayton, [How Eugenics Shaped Statistics](https://nautil.us/how-eugenics-shaped-statistics-9365/)
- Sonabend, [Statistics, Eugenics, and Me](https://towardsdatascience.com/statistics-eugenics-and-me-29eaf43efac7)
- Rosenfeld, [The invention of correlation.](https://higherlogicdownload.s3.amazonaws.com/AMSTAT/1484431b-3202-461e-b7e6-ebce10ca8bcd/UploadedImages/Classroom_Activities/HS_6_Correlation_Francis_GALTON.pdf)

Optional:
- YouTube: [Least Squares as a Maximum Likelihood estimator](https://www.youtube.com/watch?v=_-Gnu498s3o) (highly recommended)
- MathIsFun, [Quincrux Explained](https://www.mathsisfun.com/data/quincunx-explained.html)
- Galton, [Kinship and Correlation](https://galton.org/essays/1890-1899/galton-1890-nareview-kinship-and-correlation.html)
- Rehmeyer, [Darwin: The reluctant mathematician](https://www.sciencenews.org/article/darwin-reluctant-mathematician)
- PSU, [Maximum Likelihood Estimation](https://online.stat.psu.edu/stat415/lesson/1/1.2)
- [The Normal Share of Paupers](https://www.statistics.com/the-normal-share-of-paupers/)

---

## Homework 4 (due Sunday, February 6th at 11:59PM) ([solutions](https://campuswire.com/c/GCAB4734F/feed/20)) 📝

Submit your answers as a PDF to Gradescope by the due date for full credit. We encourage you to discuss the readings and questions with others in the course, but all work must be your own. **Remember to use Campuswire if you need guidance!**

Homework 4 will be finalized by Tuesday.

### Question 0

The Data Science Student Representatives created a survey for you to voice your opinion about what you love in DSC 90, and how we can improve the class and the department!

Feel free to talk about the topics covered in this course, the quality of the lectures, homeworks, and readings, and anything else you feel is relevant and constructive. As you know, this is a brand-new class, and we'd really appreciate any constructive feedback.

Please [click here](https://docs.google.com/forms/d/e/1FAIpQLSdUW_3PHsp_6XD0kKQMwU9Ck__aAgQDNGW8eBO1tDVce95ZCA/viewform) to complete the survey. If you aren't able to access it, make sure you're logged into your UCSD Google account.

### Question 1

Karl Pearson, one of Galton's disciples and collaborators, created a journal that is today known as the Annals of Human Genetics.
- What was the journal originally known as?
- What was the subtitle of the journal? What is the significance of that subtitle?
- Why was the name of the journal eventually changed?

### Question 2

This question is contained with a Jupyter Notebook, which is [linked here](http://datahub.ucsd.edu/user-redirect/git-sync?repo=https://github.com/dsc-courses/dsc90-2022-wi&subPath=homework/hw04/hw04-student.ipynb). All of your answers (including screenshots of your code) should end up in your submitted PDF; you will not be submitting this notebook anywhere.

### Question 3

This question introduces a bit of background that will be helpful in the coming week.

Recall, in lecture we considered an example where we flipped a coin 10 times and saw the sequence HTTHTTTTTH. For an arbitrary bias $$p$$, the probability of that sequence is $$p^3 (1-p)^7$$. However, $$p^3 (1-p)^7$$ is **not** the probability of seeing 3 heads and 7 tails. To compute that, we'd need to consider all of the different orders in which we could see 3 heads and 7 tails – for example, HHHTTTTTTT, HTHTHTTTTT, etc. Each of these orderings has the same probability, $$p^3 (1-p)^7$$.

So, $$P(\text{3 heads, 7 tails}) = (\text{# of ways of flipping 3 heads and 7 tails}) \cdot p^3 (1-p)^7$$. As you will learn in DSC 40A (if you haven't already), the number of ways of flipping 3 heads and 7 tails is $${10 \choose 3}$$, pronounced "10 choose 3". If you're not familiar with this notation, watch [this video](https://www.youtube.com/watch?v=4j2mFGkvwWE) and [this video](https://www.youtube.com/watch?v=lR6FeO5Pgss).

The general probability distribution we've discussed here is called the **binomial distribution**, which determines the probability of seeing $$k$$ successes in $$n$$ trials of an experiment in which each trial succeeds with probability $$p$$, independent of all other trials. It says that the probability of $$k$$ successes is

$$P(\text{$k$ successes}) = {n \choose k} p^k (1-p)^{n-k}$$

(Previously, $$k = 3$$, $$n = 10$$, and $$p$$ was unknown.)

To make sure you're comfortable with the idea, answer the following question:

Each time I call my grandma, she answers the phone with probability 0.6. I call her 5 times. What is more likely – her answering twice, or her answering four times? Find the probability of both events. Write out both answers symbolically, and then use a calculator to evaluate them as decimals. If you'd like to use Python to evaluate the result as a decimal, the function `comb(n, k)` in the Python package `scipy.special` calculates $${n \choose k}$$.