


git --version 


# initialize repo
git init




git add index.html

git status

git commit -m "initial contents of public_html" --author="brentnorthcutt <brent@tiled.co>"

git log

git --no-pager log

git show 689d95a874ba16149a80d2f08daa16ff15bf5b81

git show-branch --more=10

git --no-pager diff d3e3270ddd30f52004a30e405aec151381aa0939 689d95a874ba16149a80d2f08daa16ff15bf5b81

git clone public_html my_website
     
     ls -lsa public_html my_website
     diff -r public_html my_website


# git diff

git --no-pager diff

git --no-pager diff --staged



# git log

git log

git log --oneline

git log --oneline --graph

git --no-pager log

git --no-pager log -p


# git commit 

git commit -m

git commit -am

git commit --amend

# git reset 

_--mixed flage takes items out of the thier 'add'status_

git reset --mixed

_--hard not takes items out their 'added' status, they make the working tree state consistent with
what was last committed

# tagging

git tag i_was_here

git tag remember_to_tell_bob_to_rewrite_this newfeature


# git merge

git merge experimental


# git stash

    git stash
    git stash list
    git stash show stash@{0}
    git stash show --patch stash@{0}
    git stash apply stash@{0}

    git stash pop




# creating a repo

## create a new repository on the command line
    
    echo "# website" >> README.md
    git init
    git add README.md
    git commit -m "first commit"
    git branch -M main
    git remote add origin git@github.com:rbnorth/website.git
    git push -u origin main

## push an existing repository from the command line

    git remote add origin git@github.com:rbnorth/website.git
    git branch -M main
    git push -u origin main





# configuration files

## repository-specific
    
    .git/config

## User-specific

    ~/.gitconfig

## System-wide

    /etc/gitconfig


_set global_
    
    git config --global user.name "brent northcutt"
    git config --global user.email "brent@tiled.co"

_set repoitory-specific_
    
    git config user.user "brent northcutt"
    git config user.email "brent@tiled.co"


git config -l

git config --unset --global user.email


## alias
git config --global alias.show-graph 'log --graph --abbrev-commit --pretty=oneline'



git rm data

git checkout HEAD -- data


git mv stuff newstuff


git --no-pager log --follow data

git --no-pager log -1 --pretty=oneline

git --no-pager log -1 --pretty=oneline 616a0bdb6a6d942


# branches

git branch

git show-branch

git checkout 
