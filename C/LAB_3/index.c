#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Node {
	char *word;
	struct Node *prev;
	struct Node *next;
} Node;

Node *create_node(const char *word) {
	// Выделяем память под узел
	Node *new_node = (Node *)malloc(sizeof(Node));
	if (new_node == NULL) {
		printf("Ошибка: Не удалось выделить память для узла\n");
		return NULL;
	}

	// Выделяем память под слово и копируем его
	new_node->word = (char *)malloc(strlen(word) + 1);
	if (new_node->word == NULL) {
		printf("Ошибка: Не удалось выделить память для слова\n");
		free(new_node); // Освобождаем память узла
		return NULL;
	}
	strcpy(new_node->word, word);

	// Инициализируем указатели
	new_node->prev = NULL;
	new_node->next = NULL;

	return new_node;
}

char **split_to_words(const char *str, size_t *word_count) {
	*word_count = 0;
	size_t buffer_size = 10; // Начальный размер массива слов
	char **words = (char **)malloc(buffer_size * sizeof(char *));
	
	if (words == NULL) {
		fprintf(stderr, "Ошибка: не удалось выделить память для массива слов\n");
		return NULL;
	}

	const char *start = str;
	while (*start) {
		// Пропускаем разделители
		while (*start && !((*start >= 'a' && *start <= 'z') || (*start >= 'A' && *start <= 'Z'))) {
			start++;
		}

		// Находим конец слова
		const char *end = start;
		while (*end && ((*end >= 'a' && *end <= 'z') || (*end >= 'A' && *end <= 'Z'))) {
			end++;
		}

		// Если нашли слово
		if (start != end) {
			size_t word_length = end - start;
			char *word = (char *)malloc(word_length + 1);
			if (word == NULL) {
				fprintf(stderr, "Ошибка: не удалось выделить память для слова\n");
				// Освобождаем уже выделенные слова
				for (size_t i = 0; i < *word_count; i++) {
					free(words[i]);
				}
				free(words);
				return NULL;
			}
			strncpy(word, start, word_length);
			word[word_length] = '\0';

			// Добавляем слово в массив
			if (*word_count >= buffer_size) {
				buffer_size *= 2;
				char **new_words = (char **)realloc(words, buffer_size * sizeof(char *));
				if (new_words == NULL) {
					fprintf(stderr, "Ошибка: не удалось увеличить массив слов\n");
					for (size_t i = 0; i < *word_count; i++) {
						free(words[i]);
					}
					free(words);
					return NULL;
				}
				words = new_words;
			}

			words[(*word_count)++] = word;
			start = end;
		} else {
			break;
		}
	}

	return words;
}

int are_permutations(const char *word1, const char *word2) {
	// Если длины слов не совпадают, они не могут быть перестановками
	if (strlen(word1) != strlen(word2)) {
		return 0; // Ложь
	}

	// Массивы для подсчета букв (английский алфавит)
	int count1[26] = {0};
	int count2[26] = {0};

	// Подсчет букв в первом слове
	for (size_t i = 0; word1[i] != '\0'; i++) {
		if (word1[i] >= 'a' && word1[i] <= 'z') {
			count1[word1[i] - 'a']++;
		} else if (word1[i] >= 'A' && word1[i] <= 'Z') {
			count1[word1[i] - 'A']++;
		}
	}

	// Подсчет букв во втором слове
	for (size_t i = 0; word2[i] != '\0'; i++) {
		if (word2[i] >= 'a' && word2[i] <= 'z') {
			count2[word2[i] - 'a']++;
		} else if (word2[i] >= 'A' && word2[i] <= 'Z') {
			count2[word2[i] - 'A']++;
		}
	}

	// Сравнение частот букв
	for (int i = 0; i < 26; i++) {
		if (count1[i] != count2[i]) {
			return 0; // Ложь
		}
	}

	return 1; // Истина
}

void append_node(Node **head, const char *word) {
	// Создаем новый узел
	Node *new_node = create_node(word);
	if (new_node == NULL) {
		return; // Если произошла ошибка, ничего не делаем
	}

	// Если список пуст
	if (*head == NULL) {
		*head = new_node; // Новый узел становится началом списка
		return;
	}

	// Ищем конец списка
	Node *tail = *head;
	while (tail->next != NULL) {
		tail = tail->next;
	}

	// Добавляем новый узел в конец
	tail->next = new_node;
	new_node->prev = tail;
}

void remove_permutations(Node **head, const char *target) {
	if (*head == NULL) {
		printf("Список пуст\n");
		return;
	}

	Node *current = *head;
	while (current != NULL) {
		Node *next_node = current->next;
		
		// Проверяем, является ли слово перестановкой
		if (are_permutations(current->word, target)) {
			// Удаляем узел из списка
			if (current->prev != NULL) {
				current->prev->next = current->next;
			} else {
				*head = current->next; // Обновляем голову списка, если удаляем первый элемент
			}

			if (current->next != NULL) {
				current->next->prev = current->prev;
			}

			free(current->word); // Освобождаем память слова
			free(current); // Освобождаем сам узел
		}

		current = next_node;
	}
}

void free_list(Node *head) {
	Node *current = head;
	Node *next;

	while (current != NULL) {
		next = current->next;
		free(current->word);  // Освобождаем память для слова
		free(current);		// Освобождаем память для узла
		current = next;
	}
}

int main() {
	Node *list = NULL; // Создаем пустой двусвязный список

	printf("Введите строку: ");
	
	// Ввод строки
	char input[256];
	if (scanf(" %[^\n]", input) != 1) {
		printf("Ошибка: Некорректная строка\n");
		return 1;
	}

	size_t word_count;
	char **words = split_to_words(input, &word_count);
	if (words == NULL) {
		printf("Ошибка при разбиении строки на слова.\n");
		return 1;
	}

	printf("Разбито на %zu слов(а):\n", word_count);
	for (size_t i = 0; i < word_count; i++) {
		printf("%s ", words[i]);
	}
	printf("\n");

	// Добавление слов в список
	for (size_t i = 0; i < word_count; i++) {
		append_node(&list, words[i]);
	}

	// Ввод слова-перестановки
	printf("\nУдалить все слова, являющимися перестановками слова: ");
	char target_word[256];
	if (scanf(" %[^\n]", target_word) != 1) {
		printf("Ошибка при получении слова для удаления.\n");
		for (size_t i = 0; i < word_count; i++) {
			free(words[i]);
		}
		free(words);
		free_list(list);
		return 1;
	}

	printf("Удаление всех слов, являющихся перестановками слова: \"%s\"\n", target_word);
	remove_permutations(&list, target_word);

	// Вывод оставшихся слов в списке
	Node *current = list;
	printf("\nОстались слова:\n");
	while (current != NULL) {
		printf("%s ", current->word);
		current = current->next;
	}
	printf("\n");

	// Освобождение памяти
	for (size_t i = 0; i < word_count; i++) {
		free(words[i]);
	}
	free(words);
	free_list(list);

	return 0;
}