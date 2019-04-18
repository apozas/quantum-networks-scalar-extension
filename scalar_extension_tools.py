################################################################################
#---------------Functions for scalar extension of moment matrices--------------#
################################################################################
# Alejandro Pozas-Kerstjens, 2019

from __future__ import print_function, division
from ncpol2sdpa import generate_variables, flatten
from ncpol2sdpa.nc_utils import get_all_monomials
from numpy import prod, iscomplex, isscalar
from sympy import Symbol, S
from sympy.physics.quantum.operator import HermitianOperator

def fix_moments(moments, tolerance):
    '''Removes residual imaginary parts and moments that evaluate to zero but
    are written as some residual floating-point number.

    :param moments: correlators of some obervables
    :type moments: dict
    :param tolerance: maximum value which will be regarded as numerical noise
    :type tol: float

    :returns: dict of fixed moments
    '''
    assert tolerance > 0, 'The tolerance should be positive'
    for moment, item in moments.items():
        # Check and fix residual complex noises
        if iscomplex(item):
            if abs(item.imag) > tolerance:
                raise Exception('Your moment ' + moment +
                                ' has a complex expectation value')
            moments[moment] = item.real
            item = item.real
        # Check and fix residual real noises
        if isscalar(item):
            if abs(item) < tolerance:
                moments[moment] = 0
        else:
            if len(item.args) > 1:
                if ((item.args[0].is_constant())
                    and (abs(item.args[0]) < tolerance)):
                    moments[moment] = 0
    return moments

def get_factorization_constraints(parties, moments, substitutions, level,
                                  all_parties=False, return_column_names=False):
    '''Creates all the constraints in moments related to n-locality, namely
    the factorizations <P_i P_j...> = <P_i><P_j>..., where P_i, P_j, ... are
    collections of operators of spacelike-separated parties i, j...

    :param parties: list of measurements for each of the parties spacelike
                    separated. The structure is [party1, party2...], where
                    party_i are the measurements of party i, arranged in
                    the structure [meas1, meas2...], where meas_i is a
                    list containing the symbols of the operators of
                    measurement i.
    :type parties: list of lists of lists of sympy.core.Symbol
    :param moments: known moments obtained with get_moment_constraints.
    :type moments: dict
    :param substitutions: Measurement constraints (commuting, projective...)
                          for the operators involved. Required by
                          get_all_monomials.
    :type substitutions: dict
    :param level: level of the moment matrix
    :type level: int
    :param all_parties: Optional flag for specifying whether the columns for all
                        parties should be created instead of a minimal set.
    :type all_parties: bool
    :param return_column_names: Optional flag to return the moments to which
                                the extra columns correspond
    :type return_column_names: bool

    :returns momentsbilocal: dict with <P_i P_j...> = <P_i><P_j>... constraints.
    :returns extracolumns: list of sympy.core.Symbol that correspond to the
                           extra monomials created.
    :returns columnsnames: list of original monomials corresponding to the
                           names of the extra monomials created.
    '''
    # Factorizations will at most be of size 1|2*level-1
    parties_moments = [get_all_monomials(flatten(party), None,
                                         substitutions, 2 * level - 1)[1:]
                                                           for party in parties]
    # Strictly speaking, we need to build extra columns of all except one party
    # to sucessfully implement all factorization constraints.
    if not all_parties:
        parties_moments = parties_moments[:-1]

    # Generate commuting symbols for all the additional columns
    parties_columns = [generate_variables(
                           str(party_moments[0])[0].split('_')[0].lower() + '_',
                                          len(party_moments))
                                           for party_moments in parties_moments]
    # Substitute symbols whose values are known
    parties_columns = [[moments.get(
                          parties_moments[i][parties_columns[i].index(element)],
                                    element)
               for element in party] for i, party in enumerate(parties_columns)]
    # Obtain actual additional columns
    extracolumns = [extra for extra in flatten(parties_columns)
                                                   if isinstance(extra, Symbol)]
    columnsnames = [symbol for i, symbol in enumerate(flatten(parties_moments))
                                 if flatten(parties_columns)[i] in extracolumns]

    # Add identities for later computations
    partiesplus1 = [party_moments + [S.One]
                                           for party_moments in parties_moments]
    extramomentsplus1 = [extracols + [1] for extracols in parties_columns]

    momentsbilocal = {}
    for monomial in get_all_monomials(flatten(parties), None,
                                      substitutions, 2 * level)[1:]:
        monomial = monomial.as_ordered_factors()
        party_monomials = [[element for element in monomial
                             if element in flatten(party)] for party in parties]
        factors = [prod(party) for party in party_monomials]
        if len(monomial) <= level:
            for z in flatten([extracolumns, 1]):
                key = prod([factor for factor in [z] + factors if factor != 1])
                if all_parties:
                    item = prod([z] +
                        [extramomentsplus1[i][partiesplus1[i].index(factors[i])]
                                                   for i in range(len(factors))]
                                )
                else:
                    item = prod([z] +
                        [extramomentsplus1[i][partiesplus1[i].index(factors[i])]
                                             for i in range(len(factors) - 1)] +
                                [moments.get(factors[-1], factors[-1])]
                                )
                if key != item:
                    momentsbilocal[key] = item
        else:
            if prod([len(party_monomial) < 2 * level
                                        for party_monomial in party_monomials]):
                key = prod([factor for factor in factors if factor != 1])
                if all_parties:
                    item = prod(
                        [extramomentsplus1[i][partiesplus1[i].index(factors[i])]
                                                  for i in range(len(factors))])
                else:
                    item = prod(
                        [extramomentsplus1[i][partiesplus1[i].index(factors[i])]
                                             for i in range(len(factors) - 1)] +
                                [moments.get(factors[-1], factors[-1])]
                                )
                if key != item:
                    momentsbilocal[key] = item
    if return_column_names:
        return momentsbilocal, extracolumns, columnsnames
    return momentsbilocal, extracolumns

def get_moments_extracols(known_moments, extracolumns):
    '''Creates the entries in the moments dictionary that correspond to known
    correlators times some extra moment in the matrix columns, replacing the
    correlator with its numerical value

    :param known_moments: known values of the correlators
    :type known_moments: dict
    :param newcolumns: labels of the additional columns (additional moments)
                       in the moment matrix.
    :type newcolumns: dict of sympy.core.symbol.Symbol
    '''
    moments_extra = {}
    for key, val in known_moments.items():
        for extra_col in extracolumns:
            moments_extra[key * extra_col] = val * extra_col
    return moments_extra
