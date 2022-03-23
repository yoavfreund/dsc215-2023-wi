---
layout: default
title: Week 6 – Visualization
nav_exclude: true
---

<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>

# Week 6 – Visualization

---

## Lecture (February 14th) ❤️

- [blank slides 😶](../../slides/lec06.pdf)
- [code 💻](http://datahub.ucsd.edu/user-redirect/git-sync?repo=https://github.com/dsc-courses/dsc90-2022-wi&subPath=lecture/lec06/lec06.ipynb)
- [recording 🎥](https://youtu.be/SM1WQBgu0eI)

---

## Readings 📖

- [YouTube: A Brief History of Data Visualization](https://www.youtube.com/watch?v=N00g9Q9stBo): watch at least the first 20 minutes
- [YouTube: Hans Rosling's 200 Countries, 200 Years, 4 Minutes](https://www.youtube.com/watch?v=jbkSRLYSojo)
- [History of Scatterplots: A Timeline](https://cdn.knightlab.com/libs/timeline3/latest/embed/index.html?source=1lqjE7RKyvhfa_zqt6EuQUK051O8thpMxbHBfYeQeUcA&font=Lustria-Lato&lang=en&initial_zoom=2&height=650)

Optional:
- Rosenfeld, [Origins of graphs in statistics – William Playfair (1759-1823)](https://higherlogicdownload.s3.amazonaws.com/AMSTAT/1484431b-3202-461e-b7e6-ebce10ca8bcd/UploadedImages/Classroom_Activities/HS_3_Origins_of_graphs_in_statistics.pdf)
- Friendly, [The Golden Age of Statistical Graphics](https://arxiv.org/pdf/0906.3979.pdf)

---

## Homework 6 (due Sunday, February 27th at 11:59PM) ([solutions](https://campuswire.com/c/GCAB4734F/feed/44)) 📝

Submit your answers as a PDF to Gradescope by the due date for full credit. We encourage you to discuss the readings and questions with others in the course, but all work must be your own. **Remember to use Campuswire if you need guidance!**

The content of Homework 6 can be found in [this Jupyter Notebook](http://datahub.ucsd.edu/user-redirect/git-sync?repo=https://github.com/dsc-courses/dsc90-2022-wi&subPath=homework/hw06/hw06-student.ipynb). Submission instructions for Homework 6 can be found below.

## Submission Instructions

You will submit your work as a website on GitHub Pages in which all 3 of your visualizations are embedded. Here's what you need to do:

### Step 1: Creating a GitHub Account and a Blank Website

1. Create a [GitHub](http://github.com) account if you don't already have one.
2. Create a new **public repository** ("repo"). Call it `dsc90-wi22-hw06`. Add a README.md that says "Homework 6 for History of Data Science, Winter 2022 @ UC San Diego."
3. Enable GitHub Pages for your new repo. Follow these steps:
    - From the main page of your repo, click "Settings" in the menu at the top.
    - Click "Pages" in the menu on the left (it should be under "Code and Automation").
    - Under "Source", change "None" to "main". Click "Save".
    - Under "Theme Chooser", click "Choose a theme". It will allow you to choose one of several themes; pick the one you like the most and click "Select theme". If you end up not liking your choice, you can always come back to this menu and change the theme, so don't worry. **Note:** If you are brought to a page that has you try and edit your file (it may say something like "Edit new file"), just click "Cancel".
    - After you follow these steps, your site will be public. You will be shown its URL; it will be in the form `<your github username>.github.io/dsc90-wi22-hw06`.
    
<br>

### Step 2: Background

**Note:** This is not a tutorial on how to use Git and GitHub. If you have prior experience with GitHub, it is **highly** recommended that you **clone** your repo locally and edit the necessary files there. This has the added benefit of allowing you to preview your site locally (i.e. on your computer) before making any changes public; if you're interested in following this route, check out [these instructions](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll). 

If you don't clone your website's repo locally, you can also edit the necessary files in your repo directly at [github.com](https://github.com), though in the future you will want to avoid doing this.

The `README.md` file is where all of the content for your website will live. `.md` denotes Markdown, which is the markup language that Jupyter Notebooks use to format text cells. Under the hood, GitHub Pages uses a library called [Jekyll](https://jekyllrb.com) to convert `README.md` to the standard HTML file format. The beauty of Markdown is that it allows us to format text and images with relatively lightweight syntax. Markdown also allows us to use regular HTML code, which is how we'll embed your maps and plots in `README.md`. (There's another file in your repo, called `_config.yml` – it serves to tell GitHub Pages which theme you chose along with other information. You don't have to edit it, though you can.)

Your job is to now edit `README.md` so that it contains all three of your visualizations, along with a little bit of text (one sentence) describing each one.

<br>

### Step 3: Downloading and Embedding Visualizations

The first important step is downloading all 3 of your visualizations as `.html` files. We've defined a function, `write_file`, in your homework notebook that you'll need along the way. Here's how to use it:

**To download `folium` maps as HTML (Question 1)**

Suppose the variable name you assigned your map to was `snow_map`, and you want to save it to `snow-map.html`. You should then run

<br> 

```py
write_file('snow-map.html', snow_map._repr_html_())
```
This will create a `snow-map.html` file in your DataHub that contains a stand-alone version of your map. Download this file to your computer and open it, and double-check that it renders the map you created before. Place this `.html` file in your website repo (either by placing it in the folder that you've cloned locally or by uploading it to your repo from GitHub's website).

<br> 
**To download `plotly` graphs as HTML (Question 2-3)**

Suppose the variable name you assigned to your `plotly` plot was `fig`, and you want to save it to `plotly-fig.html`. You should then run

```py
write_file('plotly-fig.html', fig.to_html())
```
Do this for both of your `plotly` plots, download the resulting plots to your computer, double-check that they look correct, and also add them both to your website's repo.

<br> 

**To embed other `.html` files in your `README.md`**

Now you should have 3 `.html` files in your repo. We will use the HTML `<iframe>` tag to embed all three of these within `README.md`.

Let's suppose I want to embed my map from Question 1, and it is saved in my repo as `snow-map.html`. In my `README.md`, I would write:

```html
<iframe src='../snow-map.html' width=800 height=600 frameBorder=0></iframe>
```
- `src` specifies the path to the file.
- At least for the `folium` map, `width` and `height` should reflect the `width` and `height` arguments you chose in your notebook.
- `frameBorder=0` removes a border from the map to make it look like it's directly embedded in your website.

Try and get this to work with just a single visualization first, before attempting to embed your other two visualizations. At this stage, you should **commit and push** your changes on GitHub. After a few minutes, your site should contain your embedded visualization! Once you see that it worked, add your other two visualizations. (You may not have set `width` and `height` when creating your `plotly` graphs – I've found that `width=800` and `height=600` work well as arguments in `iframe`.)

<br>

### Step 4: Polishing `README.md`

At this point, your `README.md` might look something like this:

```md
<iframe src='../snow-map.html' width=800 height=600 frameBorder=0></iframe>

<iframe src='../galton-scatter.html' width=800 height=600 frameBorder=0></iframe>

<iframe src='../france-pop.html' width=800 height=600 frameBorder=0></iframe>
```

Now, your job is to:
1. Add a heading at the top of your website that contains the homework assignment name and your name
    - For instance, on separate lines you may write `# Homework 6 – History of Data Science` and `## King Triton (triton@ucsd.edu)` (but with your name and email)
2. Headings before each visualization specifying which question it belongs to
    - For instance, before the Snow map you might write `## Question 1`
3. A one-sentence explanation of each visualization immediately above or below it

This is the bare minimum that's required: you can add other things to your site as well if you'd like. Tip: To space things out vertically, put `<br>` on a new line on its own. (This is the equivalent of hitting enter several times in a Word doc.)

Once you're done, commit and push your changes again. Your site should reflect your changes within a few minutes.

<br>

### Step 5: Submitting

There are two final steps involved in submitting – you **must** follow both:
1. Upload the Jupyter Notebook you used to create your visualizations to the Homework 6 assignment on Gradescope.
2. Post a link to your GitHub Pages site in [this thread](https://campuswire.com/c/GCAB4734F/feed/24) on Campuswire.

<br>