from pathlib import Path
from fastmcp import FastMCP

# Configuration
files_directory = Path("C:/Users/ajlok/Programming/MCP server (py)/MCP server test/mcp_test_files")

# Create the FastMCP instance
mcp = FastMCP("File Reader Server")

def ensure_directory_exists():
    """Create directory if it doesnt exist"""
    files_directory.mkdir(parents = True, exist_ok = True)
    
    #Create a sample file if directory is empty
    sample_file = files_directory / "welcome.txt"
    if not sample_file.exists():
        sample_file.write_text(
            "Welcome\n\nFastMCP seerver created"
        )
        print(f"Created sample file: {sample_file}")

@mcp.tool()
def create_file(filename: str, content: str) -> str:
    """Create a new text file with
    Args:
        filename: Name of the file to be created (must end with .txt)
        content: Content to write onto the file
    """
    ensure_directory_exists()
    
    #Ensures filename ends with .txt
    if not filename.endswith(".txt"):
        filename += ".txt"
    
    file_path = files_directory / filename
    
    try:
        file_path.write_text(content, encoding='utf-8')
        return f"Successfully created file: {filename}"
    except Exception as e:
        return f"Error creating file: {str(e)}"

@mcp.tool() #created after all other tools and is the only one that can access other locations
def create_local_file(filename: str, content: str, location: str = "desktop") -> str:
    """Create a file directly on your local file system
    Args:
        filename: Name of the file to be created (must end with .txt)
        content: Content to write onto the file
        location: Where to save ('desktop', 'documents', 'downloads', or full path)
    """
    if not filename.endswith(".txt"):
        filename += ".txt"
    
    # Define common locations
    home = Path.home()
    locations = {
        "desktop": home / "Desktop",
        "documents": home / "Documents", 
        "downloads": home / "Downloads",
        "current": files_directory
    }
    
    # Determine save location
    if location in locations:
        save_path = locations[location] / filename
    else:
        # Treat as custom path
        save_path = Path(location) / filename
    
    try:
        # Create directory if it doesn't exist
        save_path.parent.mkdir(parents=True, exist_ok=True)
        save_path.write_text(content, encoding='utf-8')
        return f"Successfully created file: {save_path}"
    except Exception as e:
        return f"Error creating local file: {str(e)}"

@mcp.tool()
def test_new_function() -> str:
    """Simple test function"""
    return "New function is working!"

@mcp.tool()
def list_files() -> str:
    """List all text files in the directory."""
    ensure_directory_exists()
    
    files = list(files_directory.glob("*.txt"))
    # file_list = [f.name for f in files]
    file_list = []
    for f in files:
        file_list.append(f.name)
    
    if file_list:
        file_info = "\n".join([f"- {name}" for name in file_list])
        return f"Text files found:\n{file_info}"
    else:
        return "No text files found in the directory."

@mcp.tool()
def read_file(filename: str) -> str:
    """Read the content of a specific text file.
    
    Args:
        filename: Name of the file to read
    """
    ensure_directory_exists()
    
    file_path = files_directory / filename
    
    if not file_path.exists():
        return f"{filename} not found"
    
    if not file_path.suffix == ".txt":
        return "Only .txt files are supported"
    
    try:
        content = file_path.read_text(encoding='utf-8')
        return f"Content of {filename}:\n\n{content}"
    except Exception as e:
        return f"Error reading file {filename}: {str(e)}"

if __name__ == "__main__":
    ensure_directory_exists()
    print(f"Starting FastMCP File Reader Server...")
    print(f"Files directory: {files_directory}")
    mcp.run()

