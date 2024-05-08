
class FileManagementTools:

    def create_file_content_string(file_path):
        file_content = ""
        my_file_path = file_path
        with open(my_file_path, 'r') as file:
            contents = file.read()
            if contents.strip():
                file_content += f"[CODE_BLOCK: {my_file_path}]\n{contents}\n[/CODE_BLOCK: {my_file_path}]\n"
        return file_content
