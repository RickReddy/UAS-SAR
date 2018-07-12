Last login: Wed Jul  4 19:02:42 on ttys000
You have mail.
dhcp-18-111-113-177:~ Srikar$ git 
usage: git [--version] [--help] [-C <path>] [-c name=value]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           <command> [<args>]

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone      Clone a repository into a new directory
   init       Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add        Add file contents to the index
   mv         Move or rename a file, a directory, or a symlink
   reset      Reset current HEAD to the specified state
   rm         Remove files from the working tree and from the index

examine the history and state (see also: git help revisions)
   bisect     Use binary search to find the commit that introduced a bug
   grep       Print lines matching a pattern
   log        Show commit logs
   show       Show various types of objects
   status     Show the working tree status

grow, mark and tweak your common history
   branch     List, create, or delete branches
   checkout   Switch branches or restore working tree files
   commit     Record changes to the repository
   diff       Show changes between commits, commit and working tree, etc
   merge      Join two or more development histories together
   rebase     Reapply commits on top of another base tip
   tag        Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   fetch      Download objects and refs from another repository
   pull       Fetch from and integrate with another repository or a local branch
   push       Update remote refs along with associated objects

'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
dhcp-18-111-113-177:~ Srikar$ git clone git@github.com:RickReddy/UAS-SAR.git
Cloning into 'UAS-SAR'...
Warning: Permanently added the RSA host key for IP address '192.30.253.112' to the list of known hosts.
Enter passphrase for key '/Users/Srikar/.ssh/id_rsa': 
remote: Counting objects: 19, done.
remote: Compressing objects: 100% (17/17), done.
remote: Total 19 (delta 3), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (19/19), 12.15 KiB | 460.00 KiB/s, done.
Resolving deltas: 100% (3/3), done.
dhcp-18-111-113-177:~ Srikar$ git log
fatal: Not a git repository (or any of the parent directories): .git
dhcp-18-111-113-177:~ Srikar$ git commit
fatal: Not a git repository (or any of the parent directories): .git
dhcp-18-111-113-177:~ Srikar$ git add.
git: 'add.' is not a git command. See 'git --help'.

The most similar command is
	add
dhcp-18-111-113-177:~ Srikar$ git remote add origin remote git@github.com:RickReddy/UAS-SAR.git
fatal: Not a git repository (or any of the parent directories): .git
dhcp-18-111-113-177:~ Srikar$ git remote add origin git@github.com:RickReddy/UAS-SAR.git
fatal: Not a git repository (or any of the parent directories): .git
dhcp-18-111-113-177:~ Srikar$ list
-bash: list: command not found
dhcp-18-111-113-177:~ Srikar$ ls
AnacondaProjects		apmplanner2
AndroidStudioProjects		eclipse
Applications			git
Desktop				helloworld_1.py
Documents			hs_err_pid2661.log
Downloads			jxbrowser-browser.log
Google Drive			jxbrowser-chromium.log
Gradebook			jxbrowser-ipc.log
Library				jxbrowser-ipc.log.1
Movies				jxbrowser-ipc.log.1.lck
Music				jxbrowser-ipc.log.lck
Pictures			kethan.py
Public				line_follower_main.py
UAS-SAR				mapscache
Untitled.ipynb			sensor_vertical_flip_1.py
VirtualBox VMs			testing.ipynb
dhcp-18-111-113-177:~ Srikar$ cd UAS-SAR
dhcp-18-111-113-177:UAS-SAR Srikar$ git status
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   constants.py

no changes added to commit (use "git add" and/or "git commit -a")
dhcp-18-111-113-177:UAS-SAR Srikar$ git commit -m 'Initial test'
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
	modified:   constants.py

no changes added to commit
dhcp-18-111-113-177:UAS-SAR Srikar$ git add.
git: 'add.' is not a git command. See 'git --help'.

The most similar command is
	add
dhcp-18-111-113-177:UAS-SAR Srikar$ git add .
dhcp-18-111-113-177:UAS-SAR Srikar$ git commit -m 'Initial test'
[master c455280] Initial test
 1 file changed, 1 insertion(+), 1 deletion(-)
dhcp-18-111-113-177:UAS-SAR Srikar$ git push
Warning: Permanently added the RSA host key for IP address '192.30.253.113' to the list of known hosts.
Enter passphrase for key '/Users/Srikar/.ssh/id_rsa': 
Counting objects: 3, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 317 bytes | 317.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To github.com:RickReddy/UAS-SAR.git
   602a917..c455280  master -> master
dhcp-18-111-113-177:UAS-SAR Srikar$ git add .; git commit -m 'Message'; git push;
[master 5a9e5f9] Message
 1 file changed, 1 insertion(+)
Enter passphrase for key '/Users/Srikar/.ssh/id_rsa': 
To github.com:RickReddy/UAS-SAR.git
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'git@github.com:RickReddy/UAS-SAR.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
dhcp-18-111-113-177:UAS-SAR Srikar$ git merge
Already up to date.
dhcp-18-111-113-177:UAS-SAR Srikar$ git add 
Nothing specified, nothing added.
Maybe you wanted to say 'git add .'?
dhcp-18-111-113-177:UAS-SAR Srikar$ git add .; git commit -m 'Message'; git merge;
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
Already up to date.
dhcp-18-111-113-177:UAS-SAR Srikar$ git add .; git commit -m 'Message'; git merge;
[master 19db1e7] Message
 1 file changed, 1 insertion(+), 1 deletion(-)
Already up to date.
dhcp-18-111-113-177:UAS-SAR Srikar$ git push
Enter passphrase for key '/Users/Srikar/.ssh/id_rsa': 
To github.com:RickReddy/UAS-SAR.git
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'git@github.com:RickReddy/UAS-SAR.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
dhcp-18-111-113-177:UAS-SAR Srikar$ git pull
Enter passphrase for key '/Users/Srikar/.ssh/id_rsa': 
remote: Counting objects: 6, done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 6 (delta 3), reused 3 (delta 2), pack-reused 0
Unpacking objects: 100% (6/6), done.
From github.com:RickReddy/UAS-SAR
   c455280..0c8828c  master     -> origin/master
Auto-merging constants.py
CONFLICT (content): Merge conflict in constants.py
Automatic merge failed; fix conflicts and then commit the result.
dhcp-18-111-113-177:UAS-SAR Srikar$ git puhs
git: 'puhs' is not a git command. See 'git --help'.

The most similar command is
	push
dhcp-18-111-113-177:UAS-SAR Srikar$ git push
Enter passphrase for key '/Users/Srikar/.ssh/id_rsa': 
Enter passphrase for key '/Users/Srikar/.ssh/id_rsa': 
Enter passphrase for key '/Users/Srikar/.ssh/id_rsa': 
To github.com:RickReddy/UAS-SAR.git
 ! [rejected]        master -> master (non-fast-forward)
error: failed to push some refs to 'git@github.com:RickReddy/UAS-SAR.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
dhcp-18-111-113-177:UAS-SAR Srikar$ git merge
error: Merging is not possible because you have unmerged files.
hint: Fix them up in the work tree, and then use 'git add/rm <file>'
hint: as appropriate to mark resolution and make a commit.
fatal: Exiting because of an unresolved conflict.
dhcp-18-111-113-177:UAS-SAR Srikar$ git push
Enter passphrase for key '/Users/Srikar/.ssh/id_rsa': 
To github.com:RickReddy/UAS-SAR.git
 ! [rejected]        master -> master (non-fast-forward)
error: failed to push some refs to 'git@github.com:RickReddy/UAS-SAR.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
dhcp-18-111-113-177:UAS-SAR Srikar$ cd
dhcp-18-111-113-177:~ Srikar$ ssh pi@192.168.2.1
The authenticity of host '192.168.2.1 (192.168.2.1)' can't be established.
ECDSA key fingerprint is SHA256:kMdQgwLeqY76MCXzt1r75S8YqHRNoRPYO35+/ys8YjI.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '192.168.2.1' (ECDSA) to the list of known hosts.
pi@192.168.2.1's password: 
Permission denied, please try again.
pi@192.168.2.1's password: 
Permission denied, please try again.
pi@192.168.2.1's password: 
Linux raspberrypi 4.9.59-v7+ #1047 SMP Sun Oct 29 12:19:23 GMT 2017 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Tue Apr 10 13:43:44 2018 from 192.168.2.13
pi@raspberrypi:~ $ ls
PulsON_Code
pi@raspberrypi:~ $ cd PulsON_Code/
pi@raspberrypi:~/PulsON_Code $ ls
control_rtk  radar_params.conf  RPi_440_Control.py  RTK_Log.py  test.rtk
pi@raspberrypi:~/PulsON_Code $ vi RTK_Log.py 
pi@raspberrypi:~/PulsON_Code $ cd control_rtk
-bash: cd: control_rtk: Not a directory
pi@raspberrypi:~/PulsON_Code $ vi control_rtk
pi@raspberrypi:~/PulsON_Code $ vi radar_params.conf
pi@raspberrypi:~/PulsON_Code $ vi test.rtk
pi@raspberrypi:~/PulsON_Code $ vi radar_params.conf
pi@raspberrypi:~/PulsON_Code $ exit
logout
Connection to 192.168.2.1 closed.
dhcp-18-111-113-177:~ Srikar$ ssh pi@192.168.2.1
pi@192.168.2.1's password: 
Permission denied, please try again.
pi@192.168.2.1's password: 
Permission denied, please try again.
pi@192.168.2.1's password: 
Permission denied (publickey,password).
dhcp-18-111-113-177:~ Srikar$ ssh pi@192.168.2.1
pi@192.168.2.1's password: 
Permission denied, please try again.
pi@192.168.2.1's password: 
Permission denied, please try again.
pi@192.168.2.1's password: 
Linux raspberrypi 4.9.59-v7+ #1047 SMP Sun Oct 29 12:19:23 GMT 2017 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Tue Apr 10 14:19:01 2018 from 192.168.2.14
pi@raspberrypi:~ $ ls
PulsON_Code
pi@raspberrypi:~ $ cd PulsON_Code/
pi@raspberrypi:~/PulsON_Code $ ls
control_rtk  radar_params.conf  RPi_440_Control.py  RTK_Log.py  test.rtk
pi@raspberrypi:~/PulsON_Code $ vi control_rtk
pi@raspberrypi:~/PulsON_Code $ vi radar_params.conf
pi@raspberrypi:~/PulsON_Code $ vi radar_params.conf
pi@raspberrypi:~/PulsON_Code $ vi RPi_440_Control.py

# -*- coding: utf-8 -*-
"""
RPi_440_Control.py
Script for controlling the PulsON 440 radar over ethernet using a Raspberry Pi

Created on Thu Dec 21 10:21:29 2017

Updated on Thu Dec 21 2017
    Added basic functionality
Updated on Fri Dec 22 2017  
    Added quick look functionality
Updated on Fri Dec 29 2017  
    Tested and verified functionality v1.0
Updated on Wed Jan 3 2018
    Fixed data conversion, saving, and plotting bug. Updated to v1.03
Updated on Tue Apr 10 2018
    Fixed print syntax to enable Python 3 compatibility. Updated to v1.1

@author: Michael Riedl
"""

# -----------------------------------------------------------------------------
# SETUP
# -----------------------------------------------------------------------------

# Import the required modules
                                                              13,12         Top
