#!/bin/sh

ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa -N ''
echo 'eval $(ssh-agent -s)' >> ~/.bash_profile
echo 'ssh-add ~/.ssh/id_rsa' >> ~/.bash_profile
source ~/.bash_profile
