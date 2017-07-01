# aistats.github.io

The AISTATS current webpage.

This repository contains the current AISTATS conference page. Once the year has past it can be archived to aistats20XX and modified to form the next year's page.

Repository set up by Neil and conversion of the old javascript pages by Wittawat. Pages moved for the 2016 edition of the conference. 

## Archiving Last Year's Page

Each year the main web page needs to be archived to store as a previous year's conference. To do this, the first thing you need to do is duplicate this repository. 

1. Create the new repo in github by going to <https://github.com/organizations/aistats/repositories/new>, use the name coding `aistatsXXXX` where `XXXX` is the year of the archived conference. 

2. Give the conference a description, "Web page for the XXXX AISTATS Conference"

3. Do *not* create an initial README for the conference. 

4. Create the Repo.

5. Go to a suitable directory on your machine and type:

```git clone --bare https://github.com/aistats/aistats.github.io.git
mv aistats.github.io.git aistatsXXXX
cd aistatsXXXX
git branch -m gh-pages
git push --mirror https://github.com/aistats/aistatsXXXX.git
```
6. Edit the `_config.yml` file in the new repo to set `baseurl` to `aistatsXXXX`

7. Check that the archived page appears online at http://aistats.org/aistatsXXXX/

8. Update the original main repository at [https://github.com/aistats/aistats.github.io](https://github.com/aistats/aistats.github.io) for the current conference.
This will be used to host the current AISTATS.

## More information

* See
  a list of repositories of past web sites [here](https://github.com/aistats/).

* This link gives [Github help about project
pages](https://help.github.com/articles/user-organization-and-project-pages/)
(at the bottom), if we put the Jekyll files in **gh-pages** branch, the repository
will be served under http://aistats.github.io/aistats20xx. Note that the main
repository uses master branch, not gh-pages.

* When archiving to aistats20xx, it is necessary to modify the ``baseurl``
  entry of ``_config.yml`` from ``baseurl: ""`` to ``baseurl: "/aistats20xx"``
so that internal links in the web site are generated correctly.  

* ``baseurl:
""`` is used only in the current AISTATS site because its files are at the root
of aistats.github.io.


