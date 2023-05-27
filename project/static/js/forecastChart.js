const data={
  xValues: Object.keys(expense_d),
  yValues: Object.values(expense_d)
}
const datain={
  xValues: Object.keys(income_d),
  yValues: Object.values(income_d)
}
const monthBtn = document.getElementById('btn-month');
const month = document.getElementById('month');
forecast=new Chart("forecast", {
    type: "line",
    data: {
      labels: data.xValues,
      datasets: [{
        label: "Expenses",
        backgroundColor:"rgba(0,0,0,0)",
        borderColor: "rgba(200,0,0,1)",
        data: data.yValues
      },
      {
        label:"Income",
        backgroundColor:'rgb(0,0,0)',
        borderColor: "rgba(0,200,0,1)",
        data:datain.yValues
      }]
    }
  });