var form = document.getElementById('form')
var table = document.getElementById('table')

function getParameters(form) {
    const rows = form.rows.value;
    const cols = form.cols.value;

    const intRows = parseInt(rows) || 0
    const intCols = parseInt(cols) || 0

    return [intRows, intCols]
}

function calculateEven(rows, row, col) {
    return col*rows - row + 1;
}

function calculateOdd(rows, row, col) {
    return (col - 1)*rows + row;
}

function createTable(event) {
    event.preventDefault();
    table.innerHTML = "";
    const [rows, cols] = getParameters(form);

    if (!rows || !cols) {
        return false;
    }

    for (let row = 1; row <= rows; row++) {
        const tableRow = table.insertRow();

        for (let col = 1; col <= cols; col++) {
            const cell = tableRow.insertCell();
            let value;

            if (col === 1) {
                value = row;
            } else if (col % 2 == 0) {
                value = calculateEven(rows, row, col);
            } else {
                value = calculateOdd(rows, row, col);
            }

            console.log(value);

            cell.innerHTML = value;
        }
    }

    return true;
}

form.addEventListener('submit', createTable);
