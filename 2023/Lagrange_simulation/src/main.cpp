/**
 * @file
 * @brief Main fucntion for the Lagrange Simulator app.
 * 
 * @copyright Copyright (C) Victor Baldin, 2024.
 */
#include <assert.h>
#include <getopt.h>
#include <stdio.h>
#include <stdlib.h>

#include <SFML/Graphics.hpp>

#include "simulator.h"

static void draw_test_window()
{
    sf::RenderWindow window(sf::VideoMode(800, 600), "Test");
    sf::RectangleShape rect;
    sf::View view;
    view.setCenter(0, -300);
    window.setView(view);
    rect.setFillColor(sf::Color::Green);
    rect.setPosition(sf::Vector2f(0, 600));
    while (window.isOpen()) { 
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed)
                window.close();
        }
    }
}

int main(int argc, char* argv[])
{
    while (optind < argc) {
        // TODO: more help.
        const char help_msg[] = "Lagrange Simulator (C) Victor Baldin, 2024\n";
        
        const option long_options[] = {
            {  "help", no_argument, nullptr, 'h' },
            { nullptr,           0, nullptr,  0  },
        };

        int ch = getopt_long(argc, argv, "h", long_options, nullptr);
        switch (ch) {
        case -1:
            // TODO: input file support.
            return EXIT_FAILURE;
        case 'h':
            puts(help_msg);
            return EXIT_SUCCESS;
        case '?':
            puts(help_msg);
            return EXIT_FAILURE;
        default:
            assert(0 && "Unhandled enum value in switch");
        }
    }
    
    draw_test_window();
    return EXIT_SUCCESS;
}
