Release notes
=============

2021-10-25 (release 1.0)
  * **netlab up** enables *LLDP passthrough* on Linux bridges created with *libvirt* Vagrant plugin
  * Cleanup: remove the old CLI commands and related documentation

  :doc:`More details <release/1.0>`

2021-10-13 (release 0.9.3)
  * Add **netlab up** and **netlab down** commands
  * Add static node IDs and interface addresses

  :doc:`More details <release/0.9>`

2021-10-08 (release 0.9.2)
  * Add a simple YAML-based inventory file to replace **ansible_inventory** if you happen to hate Ansible.

  :doc:`More details <release/0.9>`

2021-09-19 (release 0.9.1)
  * End hosts in network labs (Linux VMs or containers)

  :doc:`More details <release/0.9>`

2021-08-20 (release 0.9)
  * Topology graphs (physical topology and BGP sessions)
  * YAML or JSON representation of transformed network topology
  * Generic output framework

  :doc:`More details <release/0.9>`

2021-07-09 (release 0.8)
  * Python package
  * Unified CLI
  * Support for Cumulus VX and Nokia SR Linux containers
  * Installation and testing scripts

  :doc:`More details <release/0.8>`

2021-05-31 (release 0.7)
  * EIGRP configuration module
  * BGP parameters: advertise_loopback, originate prefixes, community propagation
  * BGP IPv6 address family configuration
  * OSPF reference bandwidth
  * IS-IS P2P network type on all P2P links (not just unnumbered)
  * Single-module initial configuration
  * Python type hinting and mypy checks

  :doc:`More details <release/0.7>`

2021-05-24 (`release 0.6.3 <https://github.com/ipspace/netsim-tools/releases/tag/release_0.6.3>`_)
  * BGP configuration module
  * IS-IS configuration module
  * Segment Routing with MPLS
  * OSPF configuration improvements: external links and passive interfaces
  * FRR and Cumulus VX support
  * Installation playbook
  * Bug fixes

  :doc:`More details <release/0.6>`

2021-04-11 (`release 0.5 <https://github.com/ipspace/netsim-tools/releases/tag/release_0.5>`_)
  * containerlab support
  * Flexible virtualization provider framework

  :doc:`More details <release/0.5>`

2021-03-26 (`release 0.4 <https://github.com/ipspace/netsim-tools/releases/tag/release_0.4>`_)
  * Unnumbered interfaces
  * Configuration modules framework
  * Baseline OSPF module

  :doc:`More details <release/0.4>`

2021-01-24 (`release 0.3 <https://github.com/ipspace/netsim-tools/releases/tag/release_0.3>`_)
  * Support for multiple virtualization providers
  * Vagrant with VirtualBox
  * EOS and Nexus OS supported on Vagrant/VirtualBox
  * Device images (Vagrant boxes) are configurable in the defaults

  :doc:`More details <release/0.3>`

2021-01-12 (`release 0.2 <https://github.com/ipspace/netsim-tools/releases/tag/release_0.2>`_)
   Major refactoring of addressing configuration

   * Structured address pools (loopback, lan, p2p)
   * IPv4 and IPv6 support
   * Initial configuration modules updated to work in dual-stack or IPv6-only environments

2021-01-07 (`release 0.11 <https://github.com/ipspace/netsim-tools/releases/tag/release_0.11>`_)
   Arrcus ArcOS support contributed by Dave Thelen

   Refactored configuration gathering -- use explicit **device_facts** modules or platform-specific tasks
   for platforms that don't gather device configuration with fact-gathering module
2020-12-21
   Nexus 9300v support
2020-12-17
   Initial release (IOSv, CSR, EOS)

.. toctree::
   :caption: Individual release notes
   :maxdepth: 2

   release/1.0.md
   release/0.9.md
   release/0.8.md
   release/0.7.md
   release/0.6.md
   release/0.5.md
   release/0.4.md
   release/0.3.md
..
