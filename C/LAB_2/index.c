#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <float.h>

void generate_matrix(float **matrix, int n)
{
	srand(time(NULL));

	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			matrix[i][j] = 0.0f + (rand() / (float)RAND_MAX) * (10.0f - 0.0f);
}


void print_matrix(float **matrix, int n)
{
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
			printf("%.2f ", matrix[i][j]);

		printf("\n");
	}
}

void enter_matrix(float **matrix, int n)
{
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			if(scanf("%f", &matrix[i][j]) != 1)
			{
				printf("Invalid input");
				exit(1);
			}
}

void find_area_min_and_generate_matrix(float **matrix, float **transformed_matrix, int n)
{
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++) {
			float area_min = FLT_MAX;

			for (int k = i; k < n; k++) {
				int offset = k - i;

				int start_pos = (j - offset < 0) ? 0 : j - offset;
				int end_pos = (j + offset >= n) ? n - 1 : j + offset;

				for (int l = start_pos; l <= end_pos; l++) 
					if (area_min > matrix[k][l]) area_min = matrix[k][l];
			}

			transformed_matrix[i][j] = area_min;
		}
}	

int main(void)
{
	int n;
	float **matrix, **transformed_matrix;

	printf("Enter matrix size from 1 to 20 inclusive (N x N): ");
	if (scanf("%d", &n) != 1) 
	{
		printf("Invalid input.\n");
		return 1;
	}
	
	if (n > 20 || n < 1)
	{
		printf("Wrong matrix size!\n");
		return 1;
	}
	
	matrix = (float**)malloc(n * sizeof(float*));
	if (matrix == NULL) return -1;
	for (int i = 0; i < n; i++)
	{
		matrix[i] = (float*)malloc(n * sizeof(float));
		if (matrix[i] == NULL) return -1;
	}

	transformed_matrix = (float**)malloc(n * sizeof(float*));
	if (transformed_matrix == NULL) return -1;
	for (int i = 0; i < n; i++)
	{
		transformed_matrix[i] = (float*)malloc(n * sizeof(float));
		if (transformed_matrix[i] == NULL) return -1;
	}

	//enter_matrix(matrix, n);
	generate_matrix(matrix, n);
	find_area_min_and_generate_matrix(matrix, transformed_matrix, n);

	printf("Enered matrix: \n");
	print_matrix(matrix, n);
	printf("\n");

	printf("Transformed matrix: \n");
	print_matrix(transformed_matrix, n);
	printf("\n");

	for (int i = 0; i < n; i++)
	{
		free(matrix[i]);
		free(transformed_matrix[i]);
	}
	free(matrix);
	free(transformed_matrix);
	
	return 0;
}
