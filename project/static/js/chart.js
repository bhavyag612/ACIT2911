

  monthly=new Chart("myChart", {
  type: "pie",
  data: {
    labels: data.xValues,
    datasets: [{
      backgroundColor: data.barColors,
      data: data.yValues
    }]
  },
  options: {
    title: {
      display: true,
      text: "Expenses"
    }
  }
});
  weekly=new Chart("myChartWeek", {
  type: "pie",
  data: {
    labels: data.xValues,
    datasets: [{
      backgroundColor: data.barColors,
      data: data.yValues
    }]
  },
  options: {
    title: {
      display: true,
      text: "Expenses"
    }
  }
});
  daily=new Chart("myChartDay", {
  type: "pie",
  data: {
    labels: data.xValues,
    datasets: [{
      backgroundColor: data.barColors,
      data: data.yValues
    }]
  },
  options: {
    title: {
      display: true,
      text: "Expenses"
    }
  }
});
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