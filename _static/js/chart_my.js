
am5.ready(function() {

// Create root element
// https://www.amcharts.com/docs/v5/getting-started/#Root_element
var root = am5.Root.new("chartdiv");


// Set themes
// https://www.amcharts.com/docs/v5/concepts/themes/
root.setThemes([
  am5themes_Animated.new(root),
  am5themes_Kelly.new(root)
]);


// Create chart
// https://www.amcharts.com/docs/v5/charts/radar-chart/
var chart = root.container.children.push(am5radar.RadarChart.new(root, {
  panX: false,
  panY: false,
  wheelX: "panX",
  wheelY: "zoomX"
}));


// Create axes and their renderers
// https://www.amcharts.com/docs/v5/charts/radar-chart/#Adding_axes
var xRenderer = am5radar.AxisRendererCircular.new(root, {});
xRenderer.labels.template.setAll({
  radius: 10
});

var xAxis = chart.xAxes.push(am5xy.CategoryAxis.new(root, {
  maxDeviation: 0,
  categoryField: "field",
  renderer: xRenderer,
  tooltip: am5.Tooltip.new(root, {})
}));

var yAxis = chart.yAxes.push(am5xy.ValueAxis.new(root, {
  renderer: am5radar.AxisRendererRadial.new(root, {})
}));


// Create series
// https://www.amcharts.com/docs/v5/charts/radar-chart/#Adding_series
var series = chart.series.push(am5radar.RadarLineSeries.new(root, {
  name: "Series",
  xAxis: xAxis,
  yAxis: yAxis,
  valueYField: "skills",
  categoryXField: "field",
  tooltip:am5.Tooltip.new(root, {
    labelText:"{valueY}"
  })
}));

series.strokes.template.set("strokeWidth", 2);
series.bullets.push(function() {
  return am5.Bullet.new(root, {
    sprite: am5.Circle.new(root, {
      radius: 5,
      fill: series.get("fill"),
      strokeWidth: 2,
      stroke: root.interfaceColors.get("background")
    })
  })
})


// Set data
// https://www.amcharts.com/docs/v5/charts/radar-chart/#Setting_data
var data = [{
  "field": "HTML",
  "skills": 90
}, {
  "field": "CSS",
  "skills": 90
}, {
  "field": "JS",
  "skills": 40
}, {
  "field": "C/C++",
  "skills": 30
}, {
  "field": "Python",
  "skills": 15
}, {
  "field": "ReadTheDocs",
  "skills": 99
}, {
  "field": "Figma",
  "skills": 80
}, {
  "field": "Git",
  "skills": 60
}, {
  "field": "Qt",
  "skills": 40
}];
series.data.setAll(data);
xAxis.data.setAll(data);

// Animate chart and series in
// https://www.amcharts.com/docs/v5/concepts/animations/#Initial_animation
series.appear(1000);
chart.appear(1000, 100);


}); // end am5.ready()
