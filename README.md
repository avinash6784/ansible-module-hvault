# ansible-module-hvault
Ansible Module for Hasicorp Vault API Interaction

## Description
- Ansible Module for Hasicorp vault Interaction with  basic future added, like as seal/unseal vault, read vault secrets, write vault secrets...

## Usage and Examples

```yml
   - name: Check vault status
     hvault:
       host: localhost
   - name: Check vault seal-status
     hvault:
       host: localhost
       action: seal-status
   - name: Vault-Seal
     hvault:
       host: localhost
       action: seal
       root_token: c91044e8-375b-812c-502e-08ba46ec3c89
   - name: Vault-unSeal
     hvault:
       host: localhost
       unseal_key: '{"key":"B1hErjugs20NrK7V3uTgcAiusE1fKpWEHSD+2/xgTxU="}'
       action: unseal
   - name: Vault-Write secrets
     hvault:
       host: localhost
       action: write
       secret_path: 'myscret'
       secret_to_write: '{ "password":"12345"}'
       root_token: c91044e8-375b-812c-502e-08ba46ec3c89
   - name: Vault-Read secrets
     hvault:
       host: localhost
       action: read
       secret_path: 'myscret1'
       root_token: c91044e8-375b-812c-502e-08ba46ec3c89
     resgister: response
```

**Get more information and documentation, please use following ansible-doc command**
```sh
ansible-doc hvault
```

## Author Information

This module was created by [Avinash Pawar](http://devopstechie.com).
