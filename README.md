# ansible-role-dci-feeders

An Ansible role that deploys the necessary playbook for a host to act as a DCI feeder


## Pre-requisites

This role heavily relies on [python-dciclient](https://github.com/redhat-cip/python-dciclient) and [dci-ansible](https://github.com/redhat-cip/dci-ansible).
If those are not installed, they should be installed before using this role.


## Role Variables


The variables of this role are :

  * `components`: A list of components to check if a new version is available.


### Example

```
---
