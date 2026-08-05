# 10_files_exceptions/code/file_with_exceptions.py
# Standard pattern: reading a file with proper error handling

def read_file_safely(path):
    """Read file contents. Returns content or None on error."""
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return None
    except PermissionError:
        print(f"Error: No permission to read '{path}'.")
        return None
    except UnicodeDecodeError:
        # Try with different encoding
        try:
            with open(path, "r", encoding="latin-1") as file:
                return file.read()
        except Exception as e:
            print(f"Error: Encoding issue — {e}")
            return None

content = read_file_safely("output.txt")
if content:
    print(content)

content = read_file_safely("nonexistent.txt")
print(content)  # None