# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Httpd(AutotoolsPackage):
    """The Apache HTTP Server is a powerful and flexible HTTP/1.1 compliant
    web server."""

    homepage = "https://httpd.apache.org/"
    url = "https://archive.apache.org/dist/httpd/httpd-2.4.43.tar.bz2"

    license("Apache-2.0")

    version("2.4.59", sha256="ec51501ec480284ff52f637258135d333230a7d229c3afa6f6c2f9040e321323")
    version("2.4.55", sha256="11d6ba19e36c0b93ca62e47e6ffc2d2f2884942694bce0f23f39c71bdc5f69ac")

    # https://nvd.nist.gov/vuln/detail/CVE-2022-31813
    version(
        "2.4.43",
        sha256="a497652ab3fc81318cdc2a203090a999150d86461acff97c1065dc910fe10f43",
        deprecated=True,
    )
    version(
        "2.4.41",
        sha256="133d48298fe5315ae9366a0ec66282fa4040efa5d566174481077ade7d18ea40",
        deprecated=True,
    )
    version(
        "2.4.39",
        sha256="b4ca9d05773aa59b54d66cd8f4744b945289f084d3be17d7981d1783a5decfa2",
        deprecated=True,
    )
    version(
        "2.4.38",
        sha256="7dc65857a994c98370dc4334b260101a7a04be60e6e74a5c57a6dee1bc8f394a",
        deprecated=True,
    )

    depends_on("c", type="build")  # generated

    depends_on("m4", type="build")
    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("apr")
    depends_on("apr-util")
    depends_on("pcre")

    def configure_args(self):
        spec = self.spec
        config_args = [
            f"--with-apr={spec['apr'].prefix}",
            f"--with-apr-util={spec['apr-util'].prefix}",
        ]
        return config_args
