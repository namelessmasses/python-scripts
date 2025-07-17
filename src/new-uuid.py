import argparse
import uuid
import hashlib
import sys
from pathlib import Path

def read_content(file_path, content):
    if file_path:
        p = Path(file_path)
        if not p.exists():
            raise FileNotFoundError(f"The specified file does not exist: {file_path}")
        return p.read_text(encoding='utf-8')
    elif content is not None:
        return content
    else:
        raise ValueError("Either file_path or content must be provided.")

def uuid5_sha1(namespace, name):
    # namespace: uuid.UUID object
    # name: string
    # Implements RFC 4122, version 5 UUID (SHA-1)
    name_bytes = name.encode('utf-8')
    ns_bytes = namespace.bytes
    # Per RFC 4122, namespace bytes must be in network order (big-endian)
    hash_bytes = hashlib.sha1(ns_bytes + name_bytes).digest()
    # Take the first 16 bytes
    uuid_bytes = bytearray(hash_bytes[:16])
    # Set version to 5
    uuid_bytes[6] = (uuid_bytes[6] & 0x0F) | 0x50
    # Set variant to RFC 4122
    uuid_bytes[8] = (uuid_bytes[8] & 0x3F) | 0x80
    return uuid.UUID(bytes=bytes(uuid_bytes))

def main():
    parser = argparse.ArgumentParser(description="Generate a UUIDv5 (SHA-1) from file or string content.")
    parser.add_argument('--FilePath', type=str, default=None, help='Path to input file')
    parser.add_argument('--Content', type=str, default=None, help='String content')
    parser.add_argument('--Context', type=str, default='6ba7b810-9dad-11d1-80b4-00c04fd430c8', help='Namespace UUID (default: ns:DNS)')
    args = parser.parse_args()

    try:
        content = read_content(args.FilePath, args.Content)
    except Exception as e:
        print(e, file=sys.stderr)
        sys.exit(1)

    try:
        context_uuid = uuid.UUID(args.Context)
    except Exception:
        print(f"Invalid context UUID: {args.Context}", file=sys.stderr)
        sys.exit(1)

    print(f"Length of content bytes: {len(content.encode('utf-8'))}")
    print(f"Content bytes: {'-'.join(f'{b:02X}' for b in content.encode('utf-8'))}")
    print(f"Using context GUID: {context_uuid}")

    result_uuid = uuid5_sha1(context_uuid, content)
    print(result_uuid)

if __name__ == "__main__":
    main()
