/**
 * @file
 * @brief Main function for lagrange solver.
 * 
 * @copyright Copyright (C) Victor Baldin, 2024.
 */
#include "solver.h"

int main()
{
    const size_t n_points = 1000;
    double* solutions = solve_lagrange_problem(n_points);
    print_lagrange_coords_to_csv(solutions, n_points);
    free(solutions); 
    return 0;
}
