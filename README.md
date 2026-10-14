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

## Deploy on GitHub Pages

1. Create a public repository named `<username>.github.io` and push this folder to its `main` branch.
2. In `_config.yml`, set `url: https://<username>.github.io` (keep `baseurl:` empty). Update `website` in `_data/cv.yml` too.
3. In the repository, go to **Settings → Actions → General → Workflow permissions** and choose **Read and write permissions**.
4. Push. The **Deploy site** workflow builds the site, renders `assets/pdf/Luning_Li_CV.pdf` from `_data/cv.yml`, and publishes to the `gh-pages` branch.
5. In **Settings → Pages**, set the source to **Deploy from a branch → `gh-pages` / root**.

## Local preview

```bash
bundle install
bundle exec jekyll serve   # http://localhost:4000
python3 bin/render_cv_pdf.py   # optional: needs `pip install "rendercv[full]" pyyaml`
```
