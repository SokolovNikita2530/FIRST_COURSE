#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <float.h>
#include <string.h>

#define N 20

void generate_matrix(float matrix[N][N], int n)
{
	srand(time(NULL));

	for (int i = 0; i < n; i++)
        {
                for (int j = 0; j < n; j++)
                {
                        matrix[i][j] = 0.0f + (rand() / (float)RAND_MAX) * (10.0f - 0.0f);
                }
        }
}


void print_matrix(float matrix[N][N], int n)
{
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			printf("%f ", matrix[i][j]);
		}
		printf("\n");
	}
}

void enter_matrix(float matrix[N][N], int n)
{
	for (int i = 0; i < n; i++)
        {
                for (int j = 0; j < n; j++)
                {
                        scanf("%f", &matrix[i][j]);
                }
        }
}

void find_area_min_and_generate_matrix(float matrix[N][N], int n, int pos_i, int pos_j)
{
	if (pos_i > n && pos_j > n)
	{
		print_matrix(matrix, n);
	}
	else 
	{
		float area_min = FLT_MAX;

		for (int i = pos_i; i < n; i++) 
		{	
			int start_pos, end_pos;
			
			if (pos_j - (i - pos_i) < 0)
			{
				start_pos = 0;
			}
			else
			{
				start_pos = pos_j - (i - pos_i);
			}

			if (pos_j + (i - pos_i) >= n)
			{
				end_pos = n - 1;	
			}
			else
			{
				end_pos = pos_j + (i - pos_i);
			}

			for (int j = start_pos; j <= end_pos; j++)
			{
				if (matrix[i][j] < area_min)
				{
					area_min = matrix[i][j];
				}
			}
		}
		
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				matrix[i][j] = area_min;
			}
		}
	}	
}	

int main(void)
{
	int n;
	float matrix[N][N];
	char ans[10];

	printf("Enter matrix size from 1 to 20 inclusive (N x N): ");
	scanf("%d", &n);

	if (n > 20 || n < 1)
	{
		printf("Wrong matrix size!\n");
		return 1;
	}
	
	if (n > 5)
	{	
		printf("Generate a matrix? (Y/N): ");
		scanf("%9s", ans);
		if (strcmp(ans, "Y") == 0)
		{	
			generate_matrix(matrix, n);	
		}
		else if (strcmp(ans, "N") == 0){
			printf("Enter matrix elements: \n");
                        enter_matrix(matrix, n);
		}
		else {
			printf("Ok, bro, no, it's not.");
                        printf("\n");
                        printf("Enter matrix elements: \n");
                        enter_matrix(matrix, n);
		}
	}
	
	printf("Enered matrix: \n");
	print_matrix(matrix, n);
	printf("\n");

	printf("Transformed matrix: \n");
	find_area_min_and_generate_matrix(matrix, n, 4, 3);
	print_matrix(matrix, n);
	printf("\n");
	
	return 0;
}
