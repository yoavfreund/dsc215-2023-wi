---
layout: default
title: Week 2 – Calculus, Aggregation
nav_exclude: true
---

<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>

# Week 2 – Calculus, Aggregation

---


## Lecture (January 10th) 👨‍🏫

- [blank slides 😶](../../slides/lec02.pdf)
- [annotated slides 😊](../../slides/lec02-annotated.pdf)
- [recording 🎥](https://youtu.be/nNKV-deBHZ4)

---

## Readings 📖

Required:
- Wikipedia, [Quadrature of the Parabola](https://en.wikipedia.org/wiki/Quadrature_of_the_Parabola)
- [YouTube: Visual Proof: 1/4 + 1/16 + 1/64 + ... - Sum of Infinite Series](https://www.youtube.com/watch?v=iTdpl-FZD0o)
- [YouTube: Intro to Data Science: Historical Context](https://www.youtube.com/watch?v=aECk8s0FS7Q)
- Staples, [Fermat's technique of finding areas under curves](https://files.eric.ed.gov/fulltext/EJ720046.pdf)
- O'Connor and Robertson, [A history of the calculus](https://mathshistory.st-andrews.ac.uk/HistTopics/The_rise_of_calculus/)
- Raper, [The shock of the mean](https://rss.onlinelibrary.wiley.com/doi/full/10.1111/j.1740-9713.2017.01087.x)


Optional:
- Monks, [Fermat's Method for Finding Maxima and Minima](https://digitalcommons.ursinus.edu/cgi/viewcontent.cgi?article=1011&context=triumphs_calculus): recommended supplement to our treatment of Fermat's adequality
- Williams, [Beginnings of the Calculus](https://mathed.byu.edu/~williams/Classes/300F2011/PDFs/PPTs/Beginnings%20of%20the%20Calculus.pdf): highly recommended lecture slides if you're interested in learning more about the development of calculus during the Scientific Revolution
- Allain, [Planetary Motion Smackdown](https://www.wired.com/story/planetary-motion-smackdown/): shows how Kepler's laws and Newton's laws are related
- Levenson, [The Truth About Isaac Newton's Productive Plague](https://www.newyorker.com/culture/cultural-comment/the-truth-about-isaac-newtons-productive-plague): interesting perspective, but not all that related to course material
- Keats, [Radical insights from The Seven Pillars of Statistical Wisdom](https://www.newscientist.com/article/mg23030740-900-radical-insights-from-the-seven-pillars-of-statistical-wisdom/): similar to "The shock of the mean", but more brief

---

## Homework 2 (due Friday, January 21st at 11:59PM) ([solutions](https://campuswire.com/c/GCAB4734F/feed/13)) 📝

Submit your answers as a PDF to Gradescope by the due date for full credit. We encourage you to discuss the readings and questions with others in the course, but all work must be your own. **Remember to use Campuswire if you need guidance!**

<br>

### Question 1

Below in <span style="color:blue;">blue</span> is the parabola $$y = x^2$$, and in <span style="color:red;">red</span> is the line $$y = 2x + 8$$.

<div align=center>

<img src='../../images/hw02-parabola.png' width=350>

</div>

(a) **Without** using integration, determine the area between the given line and parabola.

This will involve a few steps. First, you'll need to find the third point on the triangle that Archimedes specified in _Quadrature of the Parabola_. Some guiding questions:

- What is the slope of the red line?
- What is the slope of the tangent line to the parabola at any given point on the parabola? (What is the derivative of the parabola?)
- At what point on the parabola is the slope of the tangent line equal to the slope of the red line?

Once you've identified the third point, you can use [this online calculator](https://keisan.casio.com/exec/system/1223520411) to find the area of that triangle (unless you'd rather do it yourself for practice). Then, you should be able to use a result from class. Show all of your steps, and remember to ask for help if you need it.

(b) If you're familiar with integration, compute the area between the given line and parabola using integration, and show that your answer is the same as your answer in part (a).

(Note: If you know how to take an integral, you are expected to do this question.)

### Question 2

Consider the function

$$f(x) = x(48 - x^2)$$

(a) Using Fermat's method of adequality, determine the value of $$x$$ that maximizes $$f(x)$$. Is this a local or global maximum? Show your work.

(b) Using Fermat's method of adequality, determine the slope of the tangent line to $$f(x)$$ at $$x = 1$$. Verify that your answer is correct by finding $$f'(x)$$ and evaluating $$f'(1)$$. Show your work.

(c) Repeat part (b), but at $$x = 0$$. What issue do you run into?

### Question 3

Show that Fermat's method for finding the slope of the tangent line is equivalent to

$$\text{slope} = \frac{f(x+e) - f(x)}{e}$$

Does the _quotient_ on the right look familiar – if so, what does it resemble?

Hopefully, by answering this question, it is slightly more clear why Fermat's method of adequality involves dividing by $$e$$ and then setting $$e$$ to 0.

### Question 4

One aggregation strategy that was used centuries ago involved picking the number halfway between the smallest and largest numbers in a dataset. In today's terminology, we'd call this number the "midrange".

$$\text{Midrange} = \frac{\text{Max}(x) + \text{Min}(x)}{2}$$

For each of the following conditions, specify a set of 5 unique numbers that satisfies the given condition. In each case, compute the midrange and mean and show that the condition holds. Afterwards, give a one sentence answer to the question, "for what kinds of datasets is the midrange close to the mean?"

(a) Midrange = mean

(b) Midrange > mean

(c) Midrange < mean