ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $ROOT
# Extract the last part of the folder path (the folder name)
ROOT_FOLDER_NAME="$(basename "$ROOT")"
mkdir app app/routers app/services app/models .env .env/$ROOT_FOLDER_NAME
python3 -m venv .env/$ROOT_FOLDER_NAME
echo "Virtual environment created at $ROOT/.env/$ROOT_FOLDER_NAME"
echo "To activate:"
echo "source $ROOT/.env/$ROOT_FOLDER_NAME/bin/activate"
