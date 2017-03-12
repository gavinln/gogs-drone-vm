@echo off

set KEY_FILE=/c/Users/gavin/.ssh/id_rsa
set BASH_CMD="C:\Program Files\Git\usr\bin\bash.exe"

%BASH_CMD% -c "eval `ssh-agent`; ssh-add $KEY_FILE; vagrant ssh -- -t '. /etc/profile; bash -l'"
