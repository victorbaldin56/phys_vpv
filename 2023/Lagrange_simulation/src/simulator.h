/**
 * @file 
 * @brief Main Simulator header.
 * 
 * @copyright Copyright (C) Victor Baldin, 2024.
 */
#ifndef SIMULATOR_H_
#define SIMULATOR_H_

#include <assert.h>

#include <SFML/Graphics.hpp>

/**
 * @brief
 */
class Simulator {
public:
    
    /**
     * @brief
     */
    Simulator();

    /**
     * 
     */
    void init();

    /**
     * @brief
     */
    bool check();

private:
    sf::Font font;
};

#endif // SIMULATOR_H_
