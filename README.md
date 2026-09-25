# 2025_EMAC_ADS_project

NASA-funded ASCL project to register suitable EMAC entries, expose links
to EMAC on ASCL records, and provide Zenodo concept DOIs and preferred
citation info to ADS.

## Operarations

The Makefile self-documents the capabilities:

It scrapes all EMAC software, and generates a simple list of all EMACS
software, as well as (where applicable) the ASCL ID, which can be
compared with the previous version of this list to see what is new and
what was modified.  Typical entries looks as follows (see the emac.list file):

2020-03-07T03:35:00+00:00 2207-170 N/A      HELIOS
2020-03-07T03:35:00+00:00 2207-171 1906.016 PandExo
2020-03-07T03:35:00+00:00 2207-173 1710.003 EXOFAST
...
2026-09-01T18:46:18.970777+00:00 2609-001 N/A      NIRC2Pol-DPP
2026-09-08T13:53:29.319430+00:00 d8f8691d-575b-437a-9a4e-70cba599abba 1905.007 Astrocut
2026-09-08T18:53:45.832424+00:00 2609-003 N/A      PlanetSolver

where the first column is the EMAC modification date, followed by the
EMAC-ID, the ASCL-ID and finally the name of the sofware asset.

The software is put together such that it can be use to automated
comparisons for a weblog, but this has not been activated yet.





## Links

* https://emac.gsfc.nasa.gov/  - Exoplanet Modeling and Analysis Center (EMAC) 
* https://ascl.net
* https://zenodo.org/
* https://ui.adsabs.harvard.edu/ - Astrophysics Data System 
* https://github.com/Heliophysics-Software-Search-Interface   HSSI repos
