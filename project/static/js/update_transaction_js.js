var expense_btn = document.getElementById("expenseBTN")
var income_btn = document.getElementById("incomeBTN")
const expense_tags = document.querySelector('.expense-tags');
const income_tags = document.querySelector('.income-tags');

// Initially hide income tags
income_tags.style.display = 'none';

function showExpenseTags() {
  expense_tags.style.display = 'flex'; // show expense tags
  income_tags.style.display = 'none'; // hide income tags
}

function showIncomeTags() {
    expense_tags.style.display = 'none'; // hide expense tags
  income_tags.style.display = 'flex'; // show income tags
}

expense_btn.addEventListener('click', showExpenseTags);
income_btn.addEventListener('click', showIncomeTags);
