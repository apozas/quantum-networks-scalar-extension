[![DOI](https://zenodo.org/badge/.svg)](https://zenodo.org/badge/latestdoi/)

## Computational appendix of *[Bounding the sets of classical and quantum correlations in networks](https://www.arxiv.org/abs/1904......)*

This is a repository containing the computational appendix of the article "*Bounding the sets of classical and quantum correlations in networks*. Alejandro Pozas-Kerstjens, Rafael Rabelo, Lukasz Rudnicki, Rafael Chaves, Daniel Cavalcanti, Miguel Navascués, and Antonio Acín. [arXiv:1904......](https://www.arxiv.org/abs/1904......)." It provides tools for performing scalar extension of moment matrices in order to develop SDP hierarchies (in the spirit of the Navascués-Pironio-Acín hierarchy) that bound the set of correlations compatible with quantum causal networks with causally-independent parties.

All code is written both in Python. It requires [Ncpol2sdpa](https://ncpol2sdpa.readthedocs.io/en/stable/), NumPy, [PICOS](https://picos-api.gitlab.io/picos/) <= 1.1.3.post8, and SciPy.

The file `scalar_extension_tools.py` contains the functions related to generating the extension and the corresponding constraints in the SDP, and a notebook is provided to show some examples.
