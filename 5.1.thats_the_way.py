from os import listdir, path


def get_deep_files(dir_path):
    deep_files = []
    for filename in listdir(dir_path):
        if filename.startswith("deep"):
            deep_files.append(path.basename(filename))
    return deep_files


def read_dir_path_from_user():
    while True:
        dir_path = input("Enter directory path: ")
        if path.exists(dir_path):
            return dir_path
        else:
            print("Directory does not exist. Please enter a valid directory path.")


def print_files_names(deep_files):
    print("The files:")
    for filename in deep_files:
        print(f"{filename} ")


def main():
    dir_path = read_dir_path_from_user()
    deep_files = get_deep_files(dir_path)
    print_files_names(deep_files)


if __name__ == "__main__":
    main()
