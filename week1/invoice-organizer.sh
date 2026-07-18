# ======================================================
# Invoice Organizer v2.0 (Advanced)
# Supports optional month folders
# ======================================================

set -euo pipefail

show_help() {
    echo "Invoice Organizer v2.0"
    echo ""
    echo "Usage: ./invoice-organizer.sh <filename> <year> [month]"
    echo ""
    echo "Examples:"
    echo "  ./invoice-organizer.sh my-invoice.pdf 2026"
    echo "  ./invoice-organizer.sh quote.pdf 2026 07"
}

if [[ "${1:-}" == "--help" || "${1:-}" == "-h" ]]; then
    show_help
    exit 0
fi

if [ $# -lt 2 ] || [ $# -gt 3 ]; then
    echo "Error: Wrong number of arguments."
    show_help
    exit 1
fi

FILENAME="$1"
YEAR="$2"
MONTH="${3:-}"

BASE_DIR="invoices"

if ! [[ "$YEAR" =~ ^[0-9]{4}$ ]]; then
    echo "Error: Year must be 4 digits"
    exit 1
fi

if [ -n "$MONTH" ]; then
    if ! [[ "$MONTH" =~ ^(0[1-9]|1[0-2])$ ]]; then
        echo "Error: Month must be 01-12"
        exit 1
    fi
fi

if [ ! -f "$FILENAME" ]; then
    echo "Error: File not found: $FILENAME"
    exit 1
fi

if [ -n "$MONTH" ]; then
    TARGET_DIR="$BASE_DIR/$YEAR/$MONTH"
    FILE_PREFIX="INV-$YEAR-$MONTH"
else
    TARGET_DIR="$BASE_DIR/$YEAR"
    FILE_PREFIX="INV-$YEAR"
fi

mkdir -p "$TARGET_DIR"

if [ -n "$MONTH" ]; then
    COUNT=$(find "$TARGET_DIR" -maxdepth 1 -name "INV-$YEAR-$MONTH-*.pdf" 2>/dev/null | wc -l)
else
    COUNT=$(find "$TARGET_DIR" -maxdepth 1 -name "INV-$YEAR-*.pdf" 2>/dev/null | wc -l)
fi

NEXT_NUM=$((COUNT + 1))
printf -v PADDED_NUM "%04d" "$NEXT_NUM"

NEW_FILENAME="${FILE_PREFIX}-${PADDED_NUM}.pdf"
NEW_PATH="$TARGET_DIR/$NEW_FILENAME"

mv "$FILENAME" "$NEW_PATH"

echo "✅ Success!"
echo "   Original : $FILENAME"
echo "   New path : $NEW_PATH"

