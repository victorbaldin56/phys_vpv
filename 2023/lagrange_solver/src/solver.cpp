/**
 * @file
 * @brief An implemetation of the Lagrange problem solver.
 * 
 * @copyright Copyright (C) Victor Baldin, 2024.
 */
#include "solver.h"

static void solve_lagrange_pol(double alpha, double coords[]);
static double find_real_root(const double roots[], size_t roots_size, 
                             double min, double max);

double* solve_lagrange_problem(size_t n_cases)
{
    assert(n_cases);   // To prevent division by zero.

    const size_t n_points = 3;
    double* solutions = (double*)calloc(n_points * n_cases, sizeof(*solutions));
    if (!solutions)
        return NULL;

    size_t i = 0;
    double width = 1 / (double)n_cases;
    for (double alpha = 0.0; alpha < 1.0; alpha += width, i += 3)
        solve_lagrange_pol(alpha, solutions + i);

    return solutions; 
}    

void print_lagrange_coords_to_csv(const double solutions[], size_t n_cases)
{
    assert(solutions);
    assert(n_cases);

    printf("alpha,L1,L2,L3\n");
    
    double alpha = 0;
    double width = 1 / (double)n_cases;
    for (size_t i = 0; i < n_cases; i++, alpha += width)
        printf("%lf,%lf,%lf,%lf\n", alpha, solutions[3 * i], 
                                    solutions[3 * i + 1], 
                                    solutions[3 * i + 2]);
}

static void solve_lagrange_pol(double alpha, double coords[])
{
    assert(isfinite(alpha));
    assert(coords);

    double l_coeffs[][6] = {
        {  alpha, 0,    -alpha, 3 - 2 * alpha, 3 - alpha, 1 },
        { -alpha, 0,     alpha, 3 - 2 * alpha, 3 - alpha, 1 },
        {  alpha, 0, 2 - alpha, 3 - 2 * alpha, 3 - alpha, 1 },
    };

    double l_roots[3][10] = { 0 };

#define ARRAY_SIZE(ARRAY) sizeof(ARRAY) / sizeof(ARRAY[0])
    
    gsl_poly_complex_workspace* workspace = 
        gsl_poly_complex_workspace_alloc(ARRAY_SIZE(l_coeffs[0]));
    
    for (size_t i = 0; i < ARRAY_SIZE(l_coeffs); i++)
        gsl_poly_complex_solve(l_coeffs[i], ARRAY_SIZE(l_coeffs[0]), 
                               workspace, l_roots[i]);

    gsl_poly_complex_workspace_free(workspace);

    double min[] = { -1,        0, -INFINITY };
    double max[] = {  0, INFINITY,        -1 };

    for (size_t i = 0; i < ARRAY_SIZE(l_roots); i++)
        coords[i] = find_real_root(l_roots[i], ARRAY_SIZE(l_roots[i]), 
                                   min[i], max[i]);

#undef ARRAY_SIZE
}

static inline bool is_equal(double a, double b)
{
    return (abs(a - b) < 1e-15) ? true : false;
}

static double find_real_root(const double roots[], size_t roots_size,
                             double min, double max)
{
    assert(roots);

    for (size_t i = 0; i < roots_size; i += 2)
        if (min <= roots[i] && roots[i] <= max && is_equal(roots[i + 1], 0))
            return roots[i];

    return NAN;
}
