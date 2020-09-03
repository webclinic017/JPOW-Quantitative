var date = current_sentiment['Date'];
var positive_sentiment = current_sentiment['sentiment'];
var prior_sentiment  = current_sentiment['prior_sentiment'];

//update last update date
document.getElementById('last-update').innerHTML = "Last Update: " + date;

//plot gauge chart
var data = [
	{
		domain: { x: [0, 1], y: [0, 1] },
		value: positive_sentiment,
    delta: { reference: prior_sentiment},
		type: "indicator",
		mode: "gauge+number+delta",
    gauge: { axis: { range: [0, 100] } }
	}
];

var layout = {autosize: true, plot_bgcolor: "#202225", paper_bgcolor: "#202225", };
Plotly.newPlot('sentgauge', data, layout, {displayModeBar: false});
window.onresize = function() {
    Plotly.relayout('sentgauge', {
        'xaxis.autorange': true,
        'yaxis.autorange': true
    });
};

var hist_dates = historical_sentiment['Date'];
var hist_sent = historical_sentiment['sentiment'];
var hist_spy_dates = spy['Date'];
var hist_close = spy['closing price'];

//plot sentiment data
var sentiment_plot = {
  x: hist_dates,
  y: hist_sent,
  name: 'Retail Positive Sentiment',
  mode: 'lines',
  line: {
    color: '#14b366',
  }
};

var spy_plot = {
  x: hist_spy_dates,
  y: hist_close,
  name: 'S&P500 Closing Price',
  yaxis: 'y2',
  mode: 'lines',
  line: {
    color: '#1E90FF',
  }
};

var layout = {
  autosize: true,
  plot_bgcolor: "#202225",
  paper_bgcolor: "#202225",
  yaxis: {
    ticksuffix: '%',
    showtickprefix: 'all',
    tickfont: {
      color: 'white',
    },
  },
  yaxis2: {
    tickprefix: '$',
    overlaying: 'y',
    side: 'right',
    tickfont: {
      color: 'white',
    },
    tickformat: ',d',
  },
  xaxis: {
    title: "Date",
    tickformat: '%b-%d',
    nticks: 25,
    rangeslider: {},
    tickfont: {
      color: 'white',
    },
  },
  legend: {
    'orientation': 'h',
    x: 0.35,
    y:1.3,
  }
};

var data = [sentiment_plot, spy_plot];
Plotly.newPlot('plot', data, layout, {displayModeBar: false});
window.onresize = function() {
  Plotly.relayout('plot', {
      'xaxis.autorange': true,
      'yaxis.autorange': true
  });
};
