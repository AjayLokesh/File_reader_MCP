# File_reader_AI_agent
create MCP server to either list, read, or write files in your shared directory using claude LLM

change the files_directory location and "args" in claude_desktop_config.json accordingly

 # Features
Create .txt files with custom content

List all .txt files in a target directory

Read contents of individual files

Create files in common local system directories (Desktop, Documents, etc.)

Automatically bootstraps with a welcome.txt file on first run

Simple test endpoint to verify server functionality

# Directory Setup
The server uses a specific directory for storing its files:

C:/"whatever file path you want"

If the directory doesn't exist, it's created automatically. A default file welcome.txt is added with a welcome message on the first run.

# Requirements
Python 3.8+

fastmcp library (pip install fastmcp)

Running the Server (python file_reader_server.py)

This starts the FastMCP server and initializes the shared file directory.

# Tools
create_file(filename, content)
Create a new .txt file in the shared directory.

create_local_file(filename, content, location="desktop")
Create a .txt file in a local directory (Desktop, Documents, Downloads, or a custom path).

filename: Must end with .txt

location: Choose from "desktop", "documents", "downloads", or a full path

list_files()
Returns a list of all .txt files in the shared directory.

read_file(filename)
Reads and returns the content of the specified .txt file.

test_new_function()
Simple tool to verify that the FastMCP server is working.
