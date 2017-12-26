// Load the Visualization API and the corechart package.
google.charts.load('visualization', {'packages':['corechart', 'bar']});

// Set a callback to run when the Google Visualization API is loaded.
// google.charts.setOnLoadCallback(drawPieChart);
google.charts.setOnLoadCallback(drawBoxesChart);

var boxesData;
var boxesChart;

function drawBoxesChart() {

  //Create data table.
  boxesData = new google.visualization.DataTable();
  boxesData.addColumn('string', '');
  boxesData.addColumn('number', 'Transfer');
  boxesData.addColumn('number', 'Standard');

  var total_boxes = 0;

  {% for hour in boxes %}
    boxesData.addRows([
      ['{{ hour.ConfirmedHour }}', {{ hour.Transfer }}, {{ hour.Standard }}]
    ]);
    total_boxes += {{hour.Cnt}};
  {% endfor %}

  //Chart options
  var options = {
    chart: {
      title: '',
      height: '100%',
    },
    backgroundColor: 'transparent',
    hAxis: {
      title: null,
      format: 'h:mm a',
    },
    legend: {
      position: 'right',
    },
    bars: 'vertical',
    isStacked: true,
    focusTarget: 'category',
  };

  boxesChart = new google.charts.Bar(document.getElementById('col_chart_div'));
  boxesChart.draw(boxesData, google.charts.Bar.convertOptions(options));

  $('#total_boxes').text(total_boxes);