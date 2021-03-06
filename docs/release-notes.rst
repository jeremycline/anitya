=============
Release Notes
=============

dev (master)
============

Dependencies
------------

* Drop the dependency on the Python ``bunch`` package as it is not used.

* There is no longer a hard dependency on the ``rpm`` Python package.

* Introduce a dependency on the Python ``social-auth-app-flask-sqlalchemy`` and
  ``flask-login`` packages in order to support authenticating against OAuth2,
  OpenID Connect, and plain OpenID providers.

* Introduce a dependency on the Python ``blinker`` package to support signaling
  in Flask.

* Introduce a dependency on the Python ``pytoml`` package in order to support
  a TOML configuration format.


Backwards-incompatible Changes
------------------------------

* Dropped support for Python 2.6

* Added support for Python 3.4+

APIs
^^^^

A number of functions that make up Anitya's Python API have been moved
(`#503 <https://github.com/release-monitoring/anitya/pull/503>`_). The full
list of functions are below. Note that no function signatures have changed.

* ``anitya.check_release`` is now ``anitya.lib.utilities.check_project_release``.

* ``anitya.fedmsg_publish`` is now ``anitya.lib.utilities.fedmsg_publish``.

* ``anitya.log`` is now ``anitya.lib.utilities.log``.

* ``anitya.lib.init`` is now ``anitya.lib.utilities.init``.

* ``anitya.lib.create_project`` is now ``anitya.lib.utilities.create_project``.

* ``anitya.lib.edit_project`` is now ``anitya.lib.utilities.edit_project``.

* ``anitya.lib.map_project`` is now ``anitya.lib.utilities.map_project``.

* ``anitya.lib.flag_project`` is now ``anitya.lib.utilities.flag_project``.

* ``anitya.lib.set_flag_state`` is now ``anitya.lib.utilities.set_flag_state``.

* ``anitya.lib.get_last_cron`` is now ``anitya.lib.utilities.get_last_cron``.


Deprecations
------------

* Deprecated the v1 HTTP API.


Features
--------

* Introduced a new set of APIs under ``api/v2/`` that support write operations
  for users authenticated with an API token.

* Configuration is now TOML format.

* Added a user guide to the documentation.

* Added an admin guide to the documentation.

* Automatically generate API documentation with Sphinx.

* Introduce httpdomain support to document the HTTP APIs.

* Add initial support for projects to set a "version scheme" in order to help
  with version ordering. At the present the only version scheme implemented is
  the RPM scheme.

* Add support for authenticating using a large number of OAuth2, OpenID Connect,
  and OpenID providers.

* Add a fedmsg consumer that integrates with libraries.io to provide more timely
  project update notifications.

* Add support for running on OpenShift with s2i.

* Switch over to pypi.org rather than pypi.python.org

* Use HTTPS in backend examples, default URLs, and documentation.


Bug Fixes
---------

* Fixed deprecation warnings from using ``flask.ext`` (#431).

* Fix the NPM backend's update feed.


Developer Improvements
----------------------

* Fixed all warnings generated from building the Sphinx documentation and
  introduce tests to ensure there are no regressions (#427).

* Greatly improved the unit tests by breaking monolithic tests up.

* Moved the unit tests into the ``anitya.tests`` package so tests didn't need
  to mess with the Python path.

* Fixed logging during test runs

* Switched to pytest as the test runner since nose is dead.

* Introduced nested transactions for database tests rather than removing the
  database after each test. This greatly reduced run time.

* Added support for testing against multiple Python versions via tox.

* Added Travis CI integration.

* Added code coverage with pytest-cov and Codecov integration.

* Fixed all flake8 errors.

* Refactored the database code to avoid circular dependencies.

* Allow the Vagrant environment to be provisioned with an empty database.


v0.11.0
=======

Released February 08, 2017.

* Return 4XX codes in error cases for /projects/new rather than 200 (Issue #246)

* Allow projects using the "folder" backend to make insecure HTTPS requests
  (Issue #386)

* Fix an issue where turning the insecure flag on and then off for a project
  resulted in insecure requests until the server was restarted (Issue #394)

* Add a data migration to set the ecosystem of existing projects if the backend
  they use is the default backend for an ecosystem. Note that this migration
  can fail if existing data has duplicate projects since there is a new
  constraint that a project name is unique within an ecosystem (Issue #402).

* Fix the regular expression used with the Debian backend to strip the "orig"
  being incorrectly included in the version (Issue #398)

* Added a new backend and ecosystem for https://crates.io (Issue #414)

* [insert summary of change here]


v0.10.1
=======

Released November 29, 2016.

* Fix an issue where the version prefix was not being stripped (Issue #372)

* Fix an issue where logs were not viewable to some users (Issue #367)

* Update anitya's mail_logging to be compatible with old and new psutil
  (Issue #368)

* Improve Anitya's error reporting via email (Issue #368)

* Report the reason fetching a URL failed for the folder backend (Issue #338)

* Add a timeout to HTTP requests Anitya makes to ensure it does not wait
  indefinitely (Issue #377)

* Fix an issue where prefixes could be stripped further than intended (Issue #381)

* Add page titles to the HTML templates (Issue #371)

* Switch from processes to threads in the Anitya cron job to avoid sharing
  network sockets for HTTP requests across processes (Issue #335)
