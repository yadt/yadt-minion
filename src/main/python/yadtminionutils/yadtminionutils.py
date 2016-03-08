import os


def get_files_by_template(common_name, filename_templates):
    existing_files = []
    files_to_test = [template.format(common_name)
                     for template in filename_templates]
    for file_to_test in files_to_test:
        if os.path.exists(file_to_test):
            existing_files.append(file_to_test)
    return existing_files
