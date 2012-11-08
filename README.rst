PyPanel
=======

A web hosting administration control panel inspired by `WebFaction's`_ control paenl.

.. _WebFaction's: http://www.webfaction.net

Goals
-----

* Built ontop of Ubuntu Server 12.04.
* Create sane and secure multi-user virtual hosting environments.
* Entirely written in Python using `Fabric`_, `Cuisine`_ and other libraries.
* Virtual hosting environment should support Python, Ruby and PHP app development. Possible inclusion of Node.js.
* Support multiple database servers including MySQL, PostgreSQL, Redis and others.
* Support multiple web servers (if the need exists), only supporting Nginx initially.
* Centralized multi-server remote administration capabilities via a REST interface.
* User-level and group-level resource management including disk/bandwidth quotas, memory/cpu usage, etc. (PAM limits?)

Supported Services
------------------

Below are a list of services being considered for support. This list is subject to change and will likely be paired down
toa single service to start.

* Web Servers: Nginx
* FTP Servers: ProFTPd, PureFTPd
* Database Servers: MySQL, PostgresSQL, Redis
* Mail Servers: Postfix, Courier/Dovecot

Help?
-----

This project is in its infancy. If you'd like to contribute just fork this repository and start making contributions via
pull requests.
