# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidycensus(RPackage):
    """Load US Census Boundary and Attribute Data as 'tidyverse' and 'sf'-Ready
    Data Frames.

    An integrated R interface to the decennial US Census and American Community
    Survey APIs and the US Census Bureau's geographic boundary files. Allows R
    users to return Census and ACS data as tidyverse-ready data frames, and
    optionally returns a list-column with feature geometry for all Census
    geographies."""

    cran = "tidycensus"

    version('1.2.2', sha256='5cdbb92314061c9d8d3d62f623699fa115d7faae1f4a961d55ab905538f8e7cc')
    version('1.2.1', sha256='b42f113c7925f8ad350f24077f6ed4d2c31d5fff45efd94639109478174a396c')
    version('1.1', sha256='8914fdec64a86896f1faa3a92272d1cd008a194af4cd86eba2d69df5707062c0')
    version('0.11', sha256='da2fba4cd987615dedd22f64d9f38804f4e2161af31bacf1f3b5a013d71fdd43')
    version('0.9.2', sha256='2454525301caff9eaaf6ebe14f58706ece1fbace6187ce8bf3fff04c842b9536')
    version('0.3.1', sha256='d03cbee7abbf87bb4ce2e649726bdd143d47b549f30b5a11aaaa6c4aff78e778')

    depends_on('r@3.3.0:', type=('build', 'run'))
    depends_on('r-httr', type=('build', 'run'))
    depends_on('r-sf', type=('build', 'run'))
    depends_on('r-dplyr@0.7.0:', type=('build', 'run'))
    depends_on('r-dplyr@0.8.0:', type=('build', 'run'), when='@0.11:')
    depends_on('r-dplyr@1.0.0:', type=('build', 'run'), when='@1.1:')
    depends_on('r-tigris', type=('build', 'run'))
    depends_on('r-stringr', type=('build', 'run'))
    depends_on('r-jsonlite@1.5.0:', type=('build', 'run'))
    depends_on('r-purrr', type=('build', 'run'))
    depends_on('r-rvest', type=('build', 'run'))
    depends_on('r-tidyr@0.7.0:', type=('build', 'run'))
    depends_on('r-tidyr@1.0.0:', type=('build', 'run'), when='@0.11:')
    depends_on('r-rappdirs', type=('build', 'run'))
    depends_on('r-readr', type=('build', 'run'))
    depends_on('r-xml2', type=('build', 'run'))
    depends_on('r-units', type=('build', 'run'))
    depends_on('r-rlang', type=('build', 'run'), when='@0.11:')
    depends_on('r-crayon', type=('build', 'run'), when='@1.1:')
    depends_on('r-tidyselect', type=('build', 'run'), when='@1.2.1:')
