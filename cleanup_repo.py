import os
import shutil

def merge_folders():
    src = 'submission'
    dst = '.'
    
    if not os.path.exists(src):
        print(f"Directory {src} does not exist.")
        return

    # Walk through submission folder
    for root, dirs, files in os.walk(src):
        # Calculate relative path
        rel_path = os.path.relpath(root, src)
        
        # Ensure destination directory exists
        dest_dir = os.path.join(dst, rel_path)
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
            
        for file in files:
            src_file = os.path.join(root, file)
            dst_file = os.path.join(dest_dir, file)
            
            # Copy file (overwrite if exists)
            shutil.copy2(src_file, dst_file)
            print(f"Copied {src_file} -> {dst_file}")

    print("Merge complete. You can now remove 'submission' folder safely.")

if __name__ == "__main__":
    merge_folders()
