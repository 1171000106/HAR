#include <float.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TEACHER_MAX 2000
#define FEATURE_MAX 10

size_t teacherSize;
double **teacherData;

size_t kValue;

/**
 * For init knn function.
 */
void initKnn(const size_t k) {
    kValue = k;
    teacherSize = 0;

    teacherData = (double **)malloc(sizeof(double *) * TEACHER_MAX);
    for (size_t i = 0; i < TEACHER_MAX; i++) {
        teacherData[i] = (double *)malloc(sizeof(double) * FEATURE_MAX);
    }
}

void closeKnn() {
    for (int i = 0; i < TEACHER_MAX; i++) {
        free(teacherData[i]);
    }

    free(teacherData);
}

void split(const char *in, char delim, double **data) {
    size_t dataSize = strlen(in);

    size_t findex = 0;
    size_t cindex = 0;

    char c[50];
    for (size_t i = 0; i < dataSize; i++) {
        if (findex == FEATURE_MAX) break;

        if (in[i] == delim) {
            c[cindex] = '\0';
            data[0][findex] = atof(c);

            findex++;
            cindex = 0;
        } else {
            c[cindex++] = in[i];
        }
    }

    if (findex < FEATURE_MAX) {
        c[cindex] = '\0';
        data[0][findex++] = atof(c);
    }
}

/*+
 * Load data from file of filename.
 * param[in] fileName Teacher data file name.
 */
void loadData(const char *fileName) {
    FILE *read;

    if ((read = fopen(fileName, "r")) == NULL) {
        printf("Error. File not found.");
        exit(1);
    }

    char input[1000];

    while (fscanf(read, "%s", input) != EOF) {
        split(input, ',', &teacherData[teacherSize]);
        teacherSize++;
    }

    fclose(read);
}

int find_size_t(size_t *in, size_t size, size_t target) {
    for (size_t i = 0; i < size; i++) {
        if (in[i] == target) {
            return i;
        }
    }

    return -1;
}

size_t rateOfLabeles(size_t *in) {
    size_t fIndex = 0;
    size_t *labeles = (size_t *)malloc(kValue * sizeof(size_t));
    size_t *counter = (size_t *)malloc(kValue * sizeof(size_t));

    // init
    for (size_t i = 0; i < kValue; i++) {
        labeles[i] = -1;
        counter[i] = 0;
    }

    for (size_t i = 0; i < kValue; i++) {
        size_t label = in[i];

        int index = find_size_t(labeles, fIndex, label);
        if (index != -1) {
            counter[index] += 1;
        } else {
            labeles[fIndex] = label;
            counter[fIndex] += 1;
            fIndex += 1;
        }
    }

    size_t ret = -1;
    size_t max = 0;
    for (size_t i = 0; i < fIndex; i++) {
        if (max < counter[i]) {
            max = counter[i];
            ret = labeles[i];
        }
    }

    free(labeles);
    free(counter);

    return ret;
}

size_t recognize(double *data) {
    double *distData = (double *)malloc(kValue * sizeof(double));
    size_t *labeles = (size_t *)malloc(kValue * sizeof(size_t));

    for (size_t i = 0; i < kValue; i++) {
        distData[i] = DBL_MAX;
        labeles[i] = -1;
    }

    for (size_t i = 0; i < teacherSize; i++) {
        double dist = 0.0;

        for (size_t j = 0; j < FEATURE_MAX - 1; j++) {
            dist += ((teacherData[i][j] - data[j]) * (teacherData[i][j] - data[j]));
        }

        dist = sqrt(dist);
        for (size_t j = 0; j < kValue; j++) {
            if (dist > distData[j] && j > 0) {
                for (size_t k = 0; k < (j - 1); k++) {
                    distData[k] = distData[k + 1];
                    labeles[k] = labeles[k + 1];
                }

                distData[j - 1] = dist;
                labeles[j - 1] = teacherData[i][FEATURE_MAX - 1];
                break;
            } else if (dist < distData[j] && j == (kValue - 1)) {
                for (size_t k = 0; k < (j - 1); k++) {
                    distData[k] = distData[k + 1];
                    labeles[k] = labeles[k + 1];
                }
                distData[j] = dist;
                labeles[j] = teacherData[i][FEATURE_MAX - 1];
                break;
            }
        }
    }

    size_t ret = rateOfLabeles(labeles);

    free(distData);
    free(labeles);

    return ret;
}

int main(const int argc, const char *argv[]) {
    initKnn(5);

    // file name of teacher data.
    loadData("sample.csv");

    double inputData[] = { 4, 5, 6, 7, 8, 9,10,11,12 };
    size_t res = recognize(inputData);
    printf("INFO: res = %lu\n", res);

    closeKnn();

    return 0;
}
