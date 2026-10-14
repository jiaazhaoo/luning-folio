# Luning Li — academic homepage

Personal academic website of Dr Luning Li (Urban Big Data Centre, University of Glasgow), built with the [al-folio](https://github.com/alshedivat/al-folio) Jekyll template.

## Where to edit

| What                                     | File                                                                            |
| ---------------------------------------- | ------------------------------------------------------------------------------- |
| Bio, photo caption, address              | `_pages/about.md`                                                               |
| Photo                                    | `assets/img/prof_pic.jpg` (portrait, ~3:4)                                      |
| Publications                             | `_bibliography/papers.bib` (`selected = {true}` shows a paper on the home page) |
| News items                               | `_news/*.md`                                                                    |
| Research project pages                   | `_projects/*.md`                                                                |
| CV (web page and PDF)                    | `_data/cv.yml`                                                                  |
| Email / LinkedIn / ORCID / Scholar icons | `_data/socials.yml`                                                             |
| Site URL, name, SEO keywords             | `_config.yml`                                                                   |

## Deploy

The site is published from this repository (`jiaazhaoo/luning-folio`) to **https://jiaazhaoo.github.io/luning-folio/**.

Every push to `main` runs the **Deploy site** workflow, which renders `assets/pdf/Luning_Li_CV.pdf` from `_data/cv.yml`, builds the site and publishes it to the `gh-pages` branch. One-time setup: **Settings → Pages → Build and deployment → Deploy from a branch → `gh-pages` / `(root)`**.

To move to a custom domain later (for example a subdomain), set `url` to that domain and `baseurl` to empty in `_config.yml`, add a `CNAME` file with the domain, and point a DNS CNAME record at `jiaazhaoo.github.io`.

## Local preview

```bash
bundle install
bundle exec jekyll serve   # http://localhost:4000/luning-folio/
python3 bin/render_cv_pdf.py   # optional: needs `pip install "rendercv[full]" pyyaml`
```
