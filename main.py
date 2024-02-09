#$libaries
import os

##object orientation
def createRepository(_branchName, _originName, _linkGit, _commitMessage):
    os.system("git init")
    os.system("git branch -m " + _branchName)
    os.system("git remote add " + _originName + " " + _linkGit)
    os.system("git add *")
    os.system("git commit -m \"" + _commitMessage + "\"")
    os.system("git push " + _originName + " " + _branchName)

##body
##Branch name
print("Welcome from GAP(Git Authpub Program)!\nPlease start writing the branch name or press Ctrl C to exit (default: master):")
branchName = input()

if branchName == "" :
    branchName = 'master'

##Origin name
print("please add a remote name (default: origin)")
originName = input()

if originName == "":
    originName = 'origin'

##link .git
print("now add the repository link.git")
linkGit = input()

while linkGit == "":
    print("you need add a repository link.git")
    linkGit = input()

##commit message
print("write your commit message (default: first commit)")
commitMsg = input()

if commitMsg == "":
    commitMsg = "first commit"

##send new repository
createRepository(branchName, originName, linkGit, commitMsg)

print("finish, repository: " + linkGit +  ", branch: \"" + branchName + " on origin: " + originName + ", created")