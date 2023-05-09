[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.2646262.svg)](https://doi.org/10.5281/zenodo.2646262)

## Computational appendix of *[Bounding the sets of classical and quantum correlations in networks](https://arxiv.org/abs/1904.08943)*

This is a repository containing the computational appendix of the article "*Bounding the sets of classical and quantum correlations in networks*. Alejandro Pozas-Kerstjens, Rafael Rabelo, Lukasz Rudnicki, Rafael Chaves, Daniel Cavalcanti, Miguel Navascués, and Antonio Acín. [Phys. Rev. Lett. 123, 140503 (2019)](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.123.140503) ([arXiv:1904.08943](https://arxiv.org/abs/1904.08943))." It provides tools for performing scalar extension of moment matrices in order to develop SDP hierarchies (in the spirit of the Navascués-Pironio-Acín hierarchy) that bound the set of correlations compatible with quantum causal networks with causally-independent parties.

All code is written both in Python. It requires [Ncpol2sdpa](https://ncpol2sdpa.readthedocs.io/en/stable/), NumPy, [PICOS](https://picos-api.gitlab.io/picos/) <= 1.1.3.post8, and SciPy.

The file `scalar_extension_tools.py` contains the functions related to generating the extension and the corresponding constraints in the SDP, and a notebook is provided to show some examples.

If you would like to cite this work, please use the following format:

A. Pozas-Kerstjens, R. Rabelo, L. Rudnicki, R. Chaves, D. Cavalcanti, M. Navascués, and A. Acín, _Bounding the sets of classical and quantum correlations in networks_, Phys. Rev. Lett. **123**, 140503 (2019), arXiv:1904.08943

```
@article{scalarextension,
  title = {Bounding the Sets of Classical and Quantum Correlations in Networks},
  author = {Pozas-Kerstjens, Alejandro and Rabelo, Rafael and Rudnicki, \L{}ukasz and Chaves, Rafael and Cavalcanti, Daniel and Navascu\'es, Miguel and Ac\'{\i}n, Antonio},
  journal = {Phys. Rev. Lett.},
  volume = {123},
  issue = {14},
  pages = {140503},
  numpages = {6},
  year = {2019},
  month = {Oct},
  publisher = {American Physical Society},
  doi = {10.1103/PhysRevLett.123.140503},
  url = {https://link.aps.org/doi/10.1103/PhysRevLett.123.140503},
  archivePrefix = {arXiv},
  eprint = {1904.08943}
}
```
