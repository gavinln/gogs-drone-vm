# gogs-drone-vm

* Source code - [Github][10]
* Author - Gavin Noronha - <gavinln@hotmail.com>

[10]: https://github.com/gavinln/gogs-drone-vm

# About

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

## Running the VM

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


## Using Docker images

1. Display docker images

    ```
    docker images
    ```

2. Run a Docker image

    ```
    docker run -ti --rm busybox:1.25
    ```

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
