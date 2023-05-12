// //hidding/displaying radio tags:
// var expense_btn = document.querySelector('.expensebtn');
// var income_btn = document.querySelector('.incomebtn');
// const expense_tags = document.querySelector('.expense-tags');
// const income_tags = document.querySelector('.income-tags');


// income_tags.style.visibility = 'hidden';

// function showExpenseTags(){
//     expense_tags.style.visibility = 'visible';
//     income_tags.style.visibility = 'hidden';
// }

// function showIncomeTags(){
//     expense_tags.style.visibility = 'hidden';
//     income_tags.style.visibility = 'visible';
// }

// expense_btn.addEventListener("click", showExpenseTags);
// income_btn.addEventListener("click", showIncomeTags);

//hidding/displaying radio tags:
// var expense_btn = document.querySelector('.expensebtn');
// var income_btn = document.querySelector('.incomebtn');
// const expense_tags = document.querySelector('.expense-tags');
// const income_tags = document.querySelector('.income-tags');

// const food_btn = document.querySelector('#foodbtn');
// const transportation_btn = document.querySelector('#transportationbtn');
// const home_btn = document.querySelector('#homebtn');
// const health_btn = document.querySelector('#healthbtn');
// const other_expense_btn = document.querySelector('#otherbtn');

// const paycheck_btn = document.querySelector('.paycheck_btn');
// const gift_btn = document.querySelector('.gift_btn');
// const interest_btn = document.querySelector('.interest_btn');
// const other_income_btn = document.querySelector('.other_btn');

// income_tags.style.visibility = 'hidden';

// function showExpenseTags(){
//     expense_tags.style.visibility = 'visible';
//     income_tags.style.visibility = 'hidden';
//     food_btn.parentElement.style.display = 'block';
//     transportation_btn.parentElement.style.display = 'block';
//     home_btn.parentElement.style.display = 'block';
//     health_btn.parentElement.style.display = 'block';
//     other_expense_btn.parentElement.style.display = 'block';
//     paycheck_btn.parentElement.style.display = 'none';
//     gift_btn.parentElement.style.display = 'none';
//     interest_btn.parentElement.style.display = 'none';
//     other_income_btn.parentElement.style.display = 'none';
// }

// function showIncomeTags(){
//     expense_tags.style.visibility = 'hidden';
//     income_tags.style.visibility = 'visible';
//     food_btn.parentElement.style.display = 'none';
//     transportation_btn.parentElement.style.display = 'none';
//     home_btn.parentElement.style.display = 'none';
//     health_btn.parentElement.style.display = 'none';
//     other_expense_btn.parentElement.style.display = 'none';
//     paycheck_btn.parentElement.style.display = 'block';
//     gift_btn.parentElement.style.display = 'block';
//     interest_btn.parentElement.style.display = 'block';
//     other_income_btn.parentElement.style.display = 'block';
// }

// expense_btn.addEventListener("click", showExpenseTags);
// income_btn.addEventListener("click", showIncomeTags);


//hidding/displaying radio tags:
var expense_btn = document.querySelector('.expensebtn');
var income_btn = document.querySelector('.incomebtn');
const expense_tags = document.querySelector('.expense-tags');
const income_tags = document.querySelector('.income-tags');

// Initially hide income tags
income_tags.style.display = 'none';

function showExpenseTags(){
    expense_tags.style.display = 'flex'; // show expense tags
    income_tags.style.display = 'none'; // hide income tags
}

function showIncomeTags(){
    expense_tags.style.display = 'none'; // hide expense tags
    income_tags.style.display = 'flex'; // show income tags
}

expense_btn.addEventListener("click", showExpenseTags);
income_btn.addEventListener("click", showIncomeTags);


