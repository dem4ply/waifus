================================================
Creation of the virtual environment with Vagrant
================================================

Vagrant_ is a command line tool whose main objective is the creation of
virtual machines, quickly, flexibly and reproducibly.
It is developed in Ruby, it is open source and cross platform.
Vagrant allows us to easily create an environment with the configuration we
need (operating system, libraries, applications, etc).

In addition, we must install a virtualization tool. In our case we use
VirtualBox_, since it is free and available on the most important platforms.

============
Dependencies
============

Install `vagrant <https://www.vagrantup.com/>`_
and `virtualbox <https://www.virtualbox.org/>`_

==========
How to use
==========

The initial configuration of the virtual machine that we are going to
create will be defined in the Vagrantfile file of this repository.
For start the virtual machine you put in the root of the repository and

execute the command:

.. code-block:: bash

	vagrant up 
...

=====
hosts
=====

* api clients: api.sigrha.client.aptude.com
* frontend: sigrha.aptude.com
