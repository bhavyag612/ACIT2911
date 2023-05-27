const monthBtn = document.getElementById('btn-month');
const weekBtn = document.getElementById('btn-week');
const dayBtn = document.getElementById('btn-day');
const month = document.getElementById('month');
const week = document.getElementById('week');
const day = document.getElementById('day');
const incomeBtn = document.getElementById('income');
const expenseBtn = document.getElementById('expenses');

let opt= 'Expenses';
let endDate;

  let keyvalues = {};
  const barColors = [
      "#b91d47",
      "#00aba9",
      "#2b5797",
      "#e8c3b9",
      "#fc8d62",
      "#c6e2ff",
      "#f5deb3",
      "#d2b4de",
      "#4b0082",
      "#dda0dd",
      "#7b68ee",
      "#1e7145"
  ];
  function defaultValue(){
    currentDate=new Date()
    startDate = new Date(currentDate.getFullYear(), 0, 1);
    var days = Math.floor((currentDate - startDate) /
        (24 * 60 * 60 * 1000));     
    var dateWeek = Math.ceil(days / 7);
    var currentMonth=("0" + (currentDate.getMonth() + 1)).slice(-2)
    var currentDay=("0" + currentDate.getDate()).slice(-2)
    month.value=`${currentDate.getFullYear()}-${currentMonth}`
    week.value=`${currentDate.getFullYear()}-W${dateWeek}`
    day.value=`${currentDate.getFullYear()}-${currentMonth}-${currentDay}`
    updateChartData()
  }
  
  function updateChartData() {
      monthkeyvalues = {};
      weekkeyvalues={};
      daykeyvalues={};
      const year = (week.value.substring(0, 4));
      const weekNumber = (week.value.substring(6, 8));
      const startDate = new Date(year, 0, 1 + (weekNumber - 1) * 7)
      account_data.transactions.forEach(function(transaction) {
        trans_date=new Date(transaction.date_created)
          if (trans_date.toISOString().includes(month.value)) {
            if(opt==='Expenses'){
              if (transaction.amt < 0) {
                  if (transaction.tag in monthkeyvalues) {
                      monthkeyvalues[transaction.tag] += transaction.amt;
                  } else {
                      monthkeyvalues[transaction.tag] = transaction.amt;
                  }
              }
            }
          else{
            if (transaction.amt > 0) {
                if (transaction.tag in monthkeyvalues) {
                    monthkeyvalues[transaction.tag] += 0-transaction.amt;
                } else {
                    monthkeyvalues[transaction.tag] = 0-transaction.amt;
                }
            }
            }
          }
          const formatDate= new Date(transaction.date_created)
          var endDate=new Date(startDate)
          endDate.setDate(startDate.getDate() + 7);
          if(formatDate>startDate && formatDate<=endDate){
            if (opt==='Expenses'){
              if (transaction.amt < 0) {
                    if (transaction.tag in weekkeyvalues) {
                        weekkeyvalues[transaction.tag] += transaction.amt;
                    } else {
                        weekkeyvalues[transaction.tag] = transaction.amt;
                    }
                }
              }
              else{
                if (transaction.amt > 0) {
                      if (transaction.tag in weekkeyvalues) {
                          weekkeyvalues[transaction.tag] += 0-transaction.amt;
                      } else {
                          weekkeyvalues[transaction.tag] = 0-transaction.amt;
                      }
                  }
              }
          }
          if(trans_date.toISOString().includes(day.value)){
            if(opt==='Expenses'){
              if (transaction.amt < 0) {
                    if (transaction.tag in daykeyvalues) {
                        daykeyvalues[transaction.tag] += transaction.amt;
                    } else {
                        daykeyvalues[transaction.tag] = transaction.amt;
                    }
                  }
              }
            else{
              if (transaction.amt > 0) {
                    if (transaction.tag in daykeyvalues) {
                        daykeyvalues[transaction.tag] += 0-transaction.amt;
                    } else {
                        daykeyvalues[transaction.tag] = 0-transaction.amt;
                    }
                }
            }
          }
      });
      monthly.options.title.text=opt
      monthly.data.labels = Object.keys(monthkeyvalues);
      monthly.data.datasets[0].data = Object.values(monthkeyvalues).map(val => 0 - val);
      monthly.update();
      weekly.options.title.text=opt
      weekly.data.labels = Object.keys(weekkeyvalues);
      weekly.data.datasets[0].data = Object.values(weekkeyvalues).map(val => 0 - val);
      weekly.update();
      daily.options.title.text=opt
      daily.data.labels = Object.keys(daykeyvalues);
      daily.data.datasets[0].data = Object.values(daykeyvalues).map(val => 0 - val);
      daily.update();
  }

  const data = {
      xValues: Object.keys(keyvalues),
      yValues: Object.values(keyvalues).map(val => 0 - val),
      barColors: barColors
  };
  
  document.addEventListener('DOMContentLoaded', function () {
    defaultValue();
    incomeBtn.addEventListener('click',()=>{
      opt='Income';
      updateChartData();
    })
    expenseBtn.addEventListener('click',()=>{
      opt='Expenses';
      updateChartData();
    })
    monthBtn.addEventListener('click', updateChartData);
    weekBtn.addEventListener('click', updateChartData);
    dayBtn.addEventListener('click', updateChartData);
  });

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
      text: opt
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
      text: opt
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
      text: opt
    }
  }
});
