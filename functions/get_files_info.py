import os

def get_files_info(working_directory, directory="."):
  dir_name = 'current' if directory == '.' else f"'{directory}'"
  header = (f"Result for {dir_name} directory:\n")
  
  try:
    absolute_path = os.path.abspath(os.path.join(working_directory, directory))

    if not absolute_path.startswith(os.path.abspath(working_directory)):
      raise Exception(f"Cannot list \"{directory}\" as it is outside the permitted working directory")

    if not os.path.isdir(absolute_path):
      raise Exception(f"{directory} is not a directory")

    contents = sorted(os.listdir(absolute_path), key=lambda name: (os.path.isdir(os.path.join(absolute_path, name)), name.lower()))

    report = []

    for item in contents:
      file_path = os.path.join(absolute_path + os.sep, item)
      report.append(f" - {item}: file_size={os.path.getsize(file_path)} bytes, is_dir={os.path.isdir(file_path)}")
    
    return header + "\n".join(report)
  
  except Exception as e:
    return str(f"{header}    Error: {e}")
