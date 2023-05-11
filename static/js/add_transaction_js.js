//hidding/displaying radio tags:
var expense_btn = document.querySelector('.expensebtn');
var income_btn = document.querySelector('.incomebtn');
const expense_tags = document.querySelector('.expense-tags');
const income_tags = document.querySelector('.income-tags');

income_tags.style.visibility = 'hidden';

function showExpenseTags(){
    expense_tags.style.visibility = 'visible';
    income_tags.style.visibility = 'hidden';
}

function showIncomeTags(){
    expense_tags.style.visibility = 'hidden';
    income_tags.style.visibility = 'visible';
}

expense_btn.addEventListener("click", showExpenseTags);
income_btn.addEventListener("click", showIncomeTags);



