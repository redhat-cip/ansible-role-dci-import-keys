# ansible-role-dci-import-keys

An Ansible role that automates the process of key retrieval for DCI's RemoteCI.


## Pre-requisites

This role relies on [python-dciclient](https://github.com/redhat-cip/python-dciclient) and [dci-ansible](https://github.com/redhat-cip/dci-ansible).

If those are not installed, they should be installed before using this role.


## Role Variables


The variables of this role are :

  * `remoteci_id`: ID of the RemoteCI to retrieve the keys for


### Example

```
- hosts: localhost
  vars:
    remoteci_id: XXX
  roles:
    - dci-import-keys
```

### License

Apache 2.0


### Author Information

Distributed-CI Team  <distributed-ci@redhat.com>
