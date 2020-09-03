var ytd = data['ytd'];
var ytd  = ytd.map(Number);
var sal = data['sal'];
var bestFit = data['best_fit'];
var tickers = data['tickers'];

var comp = {
  name: 'Compensation',
  x: sal,
  y: ytd,
  mode: 'markers',
  text: tickers,
  marker: {
    color: '#e78300',
    size: 3,
  }
};

var best_fit = {
  name: 'Linear Model',
  x: sal,
  y: bestFit,
  mode: 'lines',
  hoverinfo: 'skip',
  line: {
    color: 'black',
  },
  type: 'scatter',
}

var layout = {
  autosize: true,
  plot_bgcolor: "#202225",
  paper_bgcolor: "#202225",
  hovermode: 'closest',
  xaxis: {
    title: "CEO Compensation",
  },
  yaxis: {
    title: "YTD Return",
    ticksuffix: '%',
  },
  legend: {
    'orientation': 'h',
    x: 0.35,
    y:1.3,
  },
}

var data = [comp, best_fit];

Plotly.newPlot('plot', data, layout, {displayModeBar: false});
window.onresize = function() {
  Plotly.relayout('plot', {
      'xaxis.autorange': true,
      'yaxis.autorange': true
  });
};
