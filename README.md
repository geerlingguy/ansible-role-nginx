# Ansible Role: Nginx

Installs Nginx on RHEL/CentOS 6.x.

This role installs the latest version of Nginx direct from the Nginx yum repository.

## Requirements

None.

## Role Variables

None.

## Dependencies

None.

## Example Playbook

    - hosts: server
      roles:
        - { role: geerlingguy.nginx }

## TODO

  - Make everything more configurable.
  - Make this role work with all flavors of linux (as supported by nginx repos).

## License

MIT / BSD

## Author Information

This role was created in 2014 by [Jeff Geerling](http://jeffgeerling.com/), author of [Ansible for DevOps](http://ansiblefordevops.com/).
