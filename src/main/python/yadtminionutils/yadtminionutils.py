import os


def get_files_by_template(common_name, list_of_templates):
    existing_file_list = []
    for file_to_test in [f.format(common_name) for f in list_of_templates]:
        if os.path.exists(file_to_test):
            existing_file_list.append(file_to_test)
    return existing_file_list
