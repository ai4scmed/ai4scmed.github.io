# HOW TO update stuff on our wonderful website


* Log into your github account and make sure the computer you are on has been listed through a ssh key
* Clone the repo:

`git clone git@github.com:ai4scmed/ai4scmed.github.io.git`

If you have an authentification error,  try using the https protocol

`git clone https://github.com/ai4scmed/ai4scmed.github.io.git`


Now the fun can start!

NB: if you want to avoid to enter your SSH passphrase upon each action, you can used `ssh-add` once and for all on your computer.


So then the process is:
- make changes to the site
- push
- take a coffee!
- look at the webpage!


To be noted:
* Index page is layed out in `about.md`
* The rest are markdown pages. See [here for a cheat sheet.](https://www.markdownguide.org/cheat-sheet/)
* Stored files are in the **files** folder
* Publications are automatically listed from the **_publications** folder via the publications.md file.


## Adding and updating members

Members are compiled automatically from the markdown files in `_peoples`.

- To add a picture, (git) add the image in `assets/img/people/` and update the
  header.
- Here's an example of template:

        ---
        title: "Nelle Varoquaux"
        name: "Nelle Varoquaux"
        collection: peoples
        permalink: /people/nelle_varoquaux
        image: nelle.png
        position: "Permanent researcher"
        website: "https://nellev.github.io/"
        github: "https://github.com/nellev"
        googlescholar: "https://scholar.google.fr/citations?user=8QspsP0AAAAJ&hl=en"
        orcid: "https://orcid.org/0000-0002-8748-6546"
        osf: "https://osf.io/duxyk/"
        ---

        **[Nelle Varoquaux](https://nellev.github.io)** is a machine.  

    You can add more markdown text here.


## Adding publications

We will use HAL to deposit publications and automatically create a publication list. More to come on that matter later.
