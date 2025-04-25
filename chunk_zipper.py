import os
import zipfile
import argparse
import math
import glob

CHUNK_SIZE = 100 * 1024 * 1024  # 100 MB

def compress_directory(source_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    temp_zip = os.path.join(output_dir, "temp.zip")

    print(f"Zipping {source_dir} into {temp_zip}...")
    with zipfile.ZipFile(temp_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for foldername, subfolders, filenames in os.walk(source_dir):
            for filename in filenames:
                filepath = os.path.join(foldername, filename)
                arcname = os.path.relpath(filepath, start=source_dir)
                zipf.write(filepath, arcname)

    total_size = os.path.getsize(temp_zip)
    num_parts = math.ceil(total_size / CHUNK_SIZE)
    print(f"Splitting into {num_parts} parts...")

    with open(temp_zip, 'rb') as f:
        for i in range(num_parts):
            chunk_data = f.read(CHUNK_SIZE)
            part_filename = os.path.join(output_dir, f"part{str(i+1).zfill(2)}.zip")
            with open(part_filename, 'wb') as chunk_file:
                chunk_file.write(chunk_data)
            print(f"Created: {part_filename}")

    os.remove(temp_zip)
    print("Temporary file removed. Done.")

def extract_chunks(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    part_files = sorted(glob.glob(os.path.join(input_dir, "part*.zip")))
    if not part_files:
        print("No parts found in the specified directory.")
        return

    reassembled = os.path.join(input_dir, "reassembled.zip")

    print(f"Found parts: {part_files}")
    with open(reassembled, 'wb') as output:
        for part in part_files:
            with open(part, 'rb') as pf:
                output.write(pf.read())
    print(f"Reassembled into: {reassembled}")

    with zipfile.ZipFile(reassembled, 'r') as zipf:
        zipf.extractall(output_dir)
        print(f"Extracted to: {output_dir}")

    os.remove(reassembled)
    print("Removed reassembled zip.")

def main():
    parser = argparse.ArgumentParser(description="Chunked Zip Tool")
    subparsers = parser.add_subparsers(dest='command')

    compress_parser = subparsers.add_parser('compress')
    compress_parser.add_argument('source_dir', help="Directory to compress")
    compress_parser.add_argument('output_dir', help="Directory to save chunked zip parts")

    extract_parser = subparsers.add_parser('extract')
    extract_parser.add_argument('input_dir', help="Directory containing chunked parts")
    extract_parser.add_argument('output_dir', help="Directory to extract contents to")

    args = parser.parse_args()

    if args.command == 'compress':
        compress_directory(args.source_dir, args.output_dir)
    elif args.command == 'extract':
        extract_chunks(args.input_dir, args.output_dir)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

# python chunk_zipper.py compress ./windows ./win_c
# python chunk_zipper.py extract ./win_c ./windows
