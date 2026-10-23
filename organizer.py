import os
import shutil

def organize_directory(target_dir):
    # 2. Define the extension mapping dictionary
    EXTENSION_MAP = {
        # Documents
        '.pdf': 'Documents', '.docx': 'Documents', '.doc': 'Documents', 
        '.xlsx': 'Documents', '.xls': 'Documents', '.csv': 'Documents', 
        '.pptx': 'Documents', '.txt': 'Documents', '.md': 'Documents',

        # Images
        '.jpg': 'Images', '.jpeg': 'Images', '.png': 'Images', 
        '.gif': 'Images', '.svg': 'Images', '.webp': 'Images',

        # Videos
        '.mp4': 'Videos', '.mkv': 'Videos', '.mov': 'Videos', '.avi': 'Videos',

        # Archives
        '.zip': 'Archives', '.rar': 'Archives', '.tar': 'Archives', '.gz': 'Archives',

        # Code
        '.py': 'Code', '.js': 'Code', '.ts': 'Code', '.html': 'Code', 
        '.css': 'Code', '.java': 'Code', '.cpp': 'Code', '.json': 'Code'
        }
    
    
    # Track statistics for the execution summary
    summary = {cat: 0 for cat in EXTENSION_MAP.values()}
    summary['Others'] = 0
    total_relocated = 0
    errors_encountered = 0

    print(f"Scanning directory: {target_dir}\n" + "-"*40)

    try:
        # 3. Use os.scandir() to look through the directory efficiently
        with os.scandir(target_dir) as entries:
            for entry in entries:
                # Process only files (skip directories and the script itself)
                if entry.is_file() and entry.name != 'organizer.py':
                    file_path = entry.path
                    file_name = entry.name
                    
                    # Extract the extension (lowercase to match the map)
                    _, ext = os.path.splitext(file_name)
                    ext = ext.lower()
                    
                    # Determine target subfolder category
                    if ext in EXTENSION_MAP:
                        category = EXTENSION_MAP[ext]
                    else:
                        category = 'Others'  # Default folder for unmapped extensions
                        
                    # Create the full path for the destination directory
                    dest_dir = os.path.join(target_dir, category)
                    dest_path = os.path.join(dest_dir, file_name)
                    
                    # 4. Implement try-except blocks to catch specific exceptions
                    try:
                        # Dynamically create the category subfolder if it doesn't exist
                        if not os.path.exists(dest_dir):
                            os.makedirs(dest_dir)
                            
                        # Use shutil.move() to relocate files safely
                        shutil.move(file_path, dest_path)
                        
                        # Update counts
                        summary[category] += 1
                        total_relocated += 1
                        print(f"[MOVED] {file_name} -> /{category}")
                    # if file with this name exists
                    except FileExistsError:
                        print(f"[WARNING] Skipping '{file_name}': A file with this name already exists in the destination folder.")
                        errors_encountered += 1
                    # permission problem
                    except PermissionError:
                        print(f"[ERROR] Permission Denied: Could not move '{file_name}'. Access is restricted.")
                        errors_encountered += 1
                    except Exception as e:
                        print(f"[ERROR] Failed to move '{file_name}': {e}")
                        errors_encountered += 1

    except FileNotFoundError:
        print("[CRITICAL] The specified directory does not exist.")
        return
    except PermissionError:
        print("[CRITICAL] Access to the specified root directory is denied.")
        return

    # 5. Print a formatted execution summary
    print("\n" + "="*40)
    print("         EXECUTION SUMMARY         ")
    print("="*40)
    print(f"Total Files Relocated: {total_relocated}")
    print(f"Errors Encountered   : {errors_encountered}\n")
    print("Breakdown by Folder:")
    for folder, count in summary.items():
        if count > 0:
            print(f"  - /{folder}: {count} file(s)")
    print("="*40)

if __name__ == "__main__":
    # Get the directory where the script is located (change this string if targeting a different folder)
    current_directory = os.path.dirname(os.path.abspath(__file__))
    organize_directory(current_directory)
