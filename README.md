# gogs-drone-vm

* Source code - [Github][10]
* Author - Gavin Noronha - <gavinln@hotmail.com>

[10]: https://github.com/gavinln/gogs-drone-vm

## About

This project provides a [Ubuntu (18.04)][20] [Vagrant][30] Virtual Machine
(VM) with [Docker][40] installed using [Ansible][50].

[20]: http://releases.ubuntu.com/18.04/
[30]: http://www.vagrantup.com/
[40]: https://www.docker.com/
[50]: https://www.ansible.com/

It is used to setup [Gogs][60] a self-hosted Git service. It also includes
the [Drone][70] continuous integration service.

[60]: https://gogs.io/
[70]: http://try.drone.io/

## Setup manually

### Setup Gogs

1. Download Gogs
curl -O https://dl.gogs.io/0.11.86/gogs_0.11.86_linux_amd64.tar.gz

2. Extract Gogs

```
tar -xvzf gogs_0.11.86_linux_amd64.tar.gz
```

3. Change to the Gogs directory

```
cd gogs
```

4. Run gogs

```
./gogs web
```

1. Go to the Gogs page http://192.168.33.10:3000/

2. Set the following options and click register

```
Change the Database Type to SQLite3
Change the Domain to 192.168.33.10
Change the SSH Port to 10022
Do not select "Use Builtin SSH Server"
Keep the HTTP port at 3000
Change the Application URL to http://192.168.33.10:3000/
```

3. Click "Install Gogs"

### Register for an account

1. Click Register to sign up for an account

2. Enter details and click "Create New Account"

### Create a new repository

1. Open your browser to http://192.168.33.10:3000/

2. Click "Sign In", enter username and password and login

3. Click plus on "My repositories" to create a new repository

4. Enter repository name as gogs-drone-vm

5. Click "Create Respository"

### Setup private key for authentication

1. Open your browser to your settings pages

```
http://192.168.33.10:3000/user/settings
```

2. Click "SSH Keys" and "Add Key"

3. Copy your public key (use any Key name) on Windows

```
%USERPROFILE%\.ssh\id_rsa.pub
```

4. Click add key

### Push your git project to the Gogs repository

1. Go to your Git repository gogs-drone-vm

2. Add the gogs repository as a remote repository

```
git remote add gogs http://192.168.33.10:3000/gavin/gogs-drone-vm.git
```

3. Remove old key if necessary (not necessary if using http)

```
ssh-keygen -R [192.168.33.10]:10022
```

4. Push your code to the gogs repo

```
git push gogs master
```

### Start Drone

1. Start Drone using the script
/vagrant/script/start-drone-container.sh

2. Connect to Drone UI ad http://192.168.33.10

3. Login using your Gogs username (not email addres) and password as Drone is
   setup to use Gogs

### Setup repository on Drone

1. Click menu on top right

2. Select account

3. Turn on switch on the gogs-drone-vm

4. Automatically run build when you push to repository

## Setup using Docker compose

### Running the VM

1. Change to the root of the project

```
cd gogs-drone-vm
```

2. Check drone and gogs version in the following files

```
ansible/vars/main.yml
server/docker-compose.yml
```

3. To start the virtual machine(VM) type

```
vagrant up
```

4. Connect to the VM

```
vagrant ssh
```

### Using Docker images

1. Display docker images

```
docker images
```

2. Run a Docker image

```
docker run -ti --rm busybox:1.25
```

## Links

[Gogs and drone using Docker compose][100]

[100]: https://medium.com/@jonas.d.isberg/gogs-drone-using-docker-compose-49b50e0fc6f8

## Requirements

The following software is needed to get the software from github and run
Vagrant to set up the Python development environment. The Git environment
also provides an [SSH  client][200] for Windows.

* [Oracle VM VirtualBox][210]
* [Vagrant][220]
* [Git][230]

[200]: http://en.wikipedia.org/wiki/Secure_Shell
[210]: https://www.virtualbox.org/
[220]: http://vagrantup.com/
[230]: http://git-scm.com/
