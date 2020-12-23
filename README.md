# Workshop developing Ansbile Modules

This repository can be used to setup a training environment.

# Overview

```text
+----- your machine ------+
| vagrant ssh controlnode |
+-------------------------+
          |
          V
+--- controlnode ---+    +--- managednode ---+
| ansible-playbook\ | -> |                   |
| prepare.yml       |    |                   |
+-------------------+    +-------------------+
```

There are three machines here:

- your machine: That's your laptop or workstation.
- controlnode: That's the machine where you will write your code.
- managednode: That's the machine that will be used as a victim.

# Setup

On your laptop, have these requirements installed:

- ansible
- vagrant

Both can be installed using pip, brew, apt-get, yum, dnf, whatever.

```shell
ansible-galaxy install -r roles/requirements.yml
vagrant up
ansible-playbook prepare.yml
```

Now login to your controlnode using:

```shell
vagrant ssh controlnode
```

Test the connection from controlnode to managednode using:

```
ansible -m ping all
```

# Reset

In case you need to restart:

```
vagrant destroy
ansible-playbook prepare.yml
vagrant up
```

# Prepare a lab

In case you want to "skip" typing, you can prepare for a lab using these commands:

```shell
ansible-playbook prepare-2.yml
```

|playbook     |when to run                 |
|-------------|----------------------------|
|prepare.yml  |at the start of the workshop|
|prepare_2.yml|before starting part 2      |
|prepare_3.yml|before starting part 3      |
|prepare_4.yml|before starting part 4      |
|prepare_5.yml|before starting part 5      |
|prepare_6.yml|at the end of the workshop  |
