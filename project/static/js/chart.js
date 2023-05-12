

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
