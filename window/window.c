/**
 * @file main.c
 * @brief test
 * @author yuki
 * @date 2019/05/27
 */

#include <stdio.h>
#include <stdlib.h>

//! The window index.
size_t window_index = 0;

//! The window size.
size_t window_size = 0;

//! The buffer of window.
double *window = NULL;

/**
 * @brief Create a window buffer of size.
 * @param[in] size The initial size of window.
 * @detail This is the designated initializer for window buffer. When using window, you must use this function.
 */
void window_init(const size_t size) {
    window_index = 0;
    window_size = size;
    window = malloc(sizeof(double) * window_size);

    for (size_t i = 0; i < window_size; i++) window[i] = 0.0;
}

/**
 * @brief Push a new element to the end of the window.
 * @param[in] in The new element.
 * @detail Use this method to push a single element to the end of window buffer.
 */
void window_push(const double in) {
    window[window_index++] = in;
    window_index = window_index % window_size;
}

/**
 * @brief Close a window buffer.
 * @detail Use this method to close window buffer.
 */
void window_close() {
    free(window);
    window = NULL;
}

/**
 * @brief Main method.
 * @detail Sample method for window.
 */
int main(const int argc, const char *argv[]) {
    const size_t size = 5;

    const double weight[] = { 1, 2, 3, 4, 5 };
    window_init(size);
    for (size_t i = 0; i < 10; i++) {
        window_push(i + 1);

        double res = 0.0;
        double all = 0.0;
        for (size_t j = 0; j < window_size; j++) {
            res += window[j];
            all += 1.0;
        }
        printf("%lf, ", res / all);

        res = 0.0;
        all = 0.0;
        for (size_t j = 0; j < window_size; j++) {
            res += weight[j] * window[(window_index + j) % size];
            all += weight[j];
        }
        printf("%lf\n", res / all);
    }

    window_close();

    return 0;
}
