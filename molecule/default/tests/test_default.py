import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_ssl_cert_file(host):
    f = host.file('/etc/ssl/repo/dci.crt')
    assert f.exists
    assert f.is_file
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o644
    assert f.contains('-----BEGIN CERTIFICATE-----')
    assert f.contains('-----END CERTIFICATE-----')


def test_ssl_key_file(host):
    with host.sudo():
        f = host.file('/etc/ssl/repo/dci.key')
        assert f.exists
        assert f.is_file
        assert f.user == 'root'
        assert f.group == 'root'
        assert f.mode == 0o600
        assert f.contains('-----BEGIN PRIVATE KEY-----')
        assert f.contains('-----END PRIVATE KEY-----')
