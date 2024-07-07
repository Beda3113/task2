def merge_files(directory):
    """
    Объединяет файлы в указанном каталоге в один файл, отсортированный по количеству строк.
    """

    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    # Сортируем файлы по количеству строк
    sorted_files = sorted(files, key=lambda x: sum(1 for line in open(os.path.join(directory, x))))

    with open(os.path.join(directory, "merged_file.txt"), "w") as output_file:
        for file in sorted_files:
            with open(os.path.join(directory, file), "r") as input_file:
                lines = input_file.readlines()
                output_file.write(f"{file}\n{len(lines)}\n")
                output_file.writelines(lines)


# Пример использования
directory = "/path/to/your/directory"
merge_files(directory)
