# Ansible Role: Nginx

[![Build Status](https://travis-ci.org/geerlingguy/ansible-role-nginx.svg?branch=master)](https://travis-ci.org/geerlingguy/ansible-role-nginx)

Installs Nginx on RedHat/CentOS or Debian/Ubuntu linux servers.

This role installs and configures the latest version of Nginx from the Nginx yum repository (on RedHat-based systems) or via apt (on Debian-based systems). You will likely need to do extra setup work after this role has installed Nginx, like adding your own [virtualhost].conf file inside `/etc/nginx/conf.d/`, describing the location and options to use for your particular website.

## Requirements

None.

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

    nginx_remove_default_vhost: false
    nginx_default_vhost_path: /etc/nginx/sites-enabled/default

Whether to remove the 'default' virtualhost configuration supplied by Nginx. Useful if you want the base `/` URL to be directed at one of your own virtual hosts configured in a separate .conf file. The `nginx_default_vhost_path` variable defines the path to the default vhosts file.

    nginx_user: "nginx"

The user under which Nginx will run. Defaults to `nginx` for RedHat, and `www-data` for Debian.

    nginx_worker_processes: "1"
    nginx_worker_connections: "8192"

`nginx_worker_processes` should be set to the number of cores present on your machine. Connections (find this number with `grep processor /proc/cpuinfo | wc -l`). `nginx_worker_connections` is the number of connections per process. Set this higher to handle more simultaneous connections (and remember that a connection will be used for as long as the keepalive timeout duration for every client!).

    nginx_client_max_body_size: "64m"

This value determines the largest file upload possible, as uploads are passed through Nginx before hitting a backend like `php-fpm`. If you get an error like `client intended to send too large body`, it means this value is set too low.

    nginx_keepalive_timeout: "65"

The keepalive timeout. Should be set higher (10s+) if you have more polling-style traffic (AJAX-powered sites especially), or lower (<10s) if you have a site where most users visit a few pages and don't send any further requests.

    nginx_proxy_cache_path: ""

Set as the `proxy_cache_path` directive in the `nginx.conf` file. By default, this will not be configured (if left as an empty string), but if you wish to use Nginx as a reverse proxy, you can set this to a valid value (e.g. `"/var/cache/nginx keys_zone=cache:32m"`) to use Nginx's cache (further proxy configuration can be done in individual server configurations).

## Dependencies

None.

## Example Playbook

    - hosts: server
      roles:
        - { role: geerlingguy.nginx }

## License

MIT / BSD

## Author Information

This role was created in 2014 by [Jeff Geerling](http://jeffgeerling.com/), author of [Ansible for DevOps](http://ansiblefordevops.com/).
