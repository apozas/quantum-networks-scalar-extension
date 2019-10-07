[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.2646262.svg)](https://doi.org/10.5281/zenodo.2646262)

## Computational appendix of *[Bounding the sets of classical and quantum correlations in networks](https://arxiv.org/abs/1904.08943)*

This is a repository containing the computational appendix of the article "*Bounding the sets of classical and quantum correlations in networks*. Alejandro Pozas-Kerstjens, Rafael Rabelo, Lukasz Rudnicki, Rafael Chaves, Daniel Cavalcanti, Miguel Navascués, and Antonio Acín. [Phys. Rev. Lett. 123, 140503 (2019)](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.123.140503) ([arXiv:1904.08943](https://arxiv.org/abs/1904.08943))." It provides tools for performing scalar extension of moment matrices in order to develop SDP hierarchies (in the spirit of the Navascués-Pironio-Acín hierarchy) that bound the set of correlations compatible with quantum causal networks with causally-independent parties.

All code is written both in Python. It requires [Ncpol2sdpa](https://ncpol2sdpa.readthedocs.io/en/stable/), NumPy, [PICOS](https://picos-api.gitlab.io/picos/) <= 1.1.3.post8, and SciPy.

The file `scalar_extension_tools.py` contains the functions related to generating the extension and the corresponding constraints in the SDP, and a notebook is provided to show some examples.
