# ansible-role-dci-import-keys

An Ansible role that automates the process of key retrieval for DCI's RemoteCI.


## Pre-requisites

This role relies on [python-dciclient](https://github.com/redhat-cip/python-dciclient) and [dci-ansible](https://github.com/redhat-cip/dci-ansible).

If those are not installed, they should be installed before using this role.


## Role Variables

| Variable name | Required | Default | Type | Description |
|---------------|----------|---------|------|-------------|
| dci_import_keys_remoteci_id | True | N/A | UUID | ID of the remoteci to retrieve the SSL info for |


### Example

```
- hosts: localhost
  vars:
    dci_import_keys_remoteci_id: XXX
  roles:
    - dci-import-keys
```

### License

Apache 2.0


### Author Information

Distributed-CI Team  <distributed-ci@redhat.com>
