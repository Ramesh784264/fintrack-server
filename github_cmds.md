# stage a file ready for commit 
git add {fine_name} or . to stage all files

# commit staged files
git commit -m "commit message here"

# push local change to git
git push origin main (main is the branch name)  

# to create a new branch 
git checkout -b feature/server-file-create (feature/server-file-create is the branch name)

# to delete a local branch 
git branch -d feature/server-file-create (feature/server-file-create is the branch name)

# to switch branch
git checkout main (main is the branch name)

# pull online changes to local branch (main)
git pull origin main

# to merge feature branch to main branch
# before this command checkout to main 
git merge feature/server-file-create

