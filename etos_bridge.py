import sys, json, pathlib

def main():
    if len(sys.argv) < 4:
        raise SystemExit("Usage: etos_bridge.py <script_name> <input_path> <output_path>")

    script_name, input_path, output_path = sys.argv[1:4]
    input_file = pathlib.Path(input_path)
    output_file = pathlib.Path(output_path)

    if input_file.exists():
        data = json.loads(input_file.read_text())
    else:
        data = {}

    result = {
        "status": "ok",
        "script": script_name,
        "input": data
    }

    output_file.write_text(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
