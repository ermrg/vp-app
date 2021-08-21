$(document).ready(function() {
    //Bar analytics for single item
    Highcharts.chart('container', {
        chart: {
            type: 'column'
        },
        title: {
            text: 'Overall : Household by water resources'
        },
        subtitle: {
            text: 'Source: Individual Data Collection'
        },
        xAxis: {
            categories: [
                'कुबा',
                'खोला',
                'अन्य',
                'धारा',
                'मूल',
            ],
            crosshair: true
        },
        yAxis: {
            title: {
                text: 'Population'
            }
        },
        legend: {
            enabled: false,
        },
        tooltip: {
            valueSuffix: '(In Thousand)'
        },
        series: [{
            name: 'Population',
            data: [5920, 1900, 0, 2878, 1890]
        }]
    });

    //2.Bar analytics for double item
    Highcharts.chart('containerAge', {
        chart: {
            type: 'column'
        },
        title: {
            text: 'Overall: Population By Age Group'
        },
        subtitle: {
            text: 'Source: Individual Data Collection'
        },
        xAxis: {
            categories: [
                '0-4',
                '5-9',
                '10-14',
                '15-19',
                '20-24',
                '25-29',
                '30-34',
                '35-39',
                '40-44',
                '45-49',
                '50-54',
                '55-59',
                '60-64',
                '65-69',
                '70-74',
                '75+',
            ],
            crosshair: true
        },
        yAxis: {
            title: {
                text: 'Population'
            }
        },
        legend: {
            enabled: true,
        },
        series: [{
                name: 'Male',
                data: [100, 111, 124, 233, 444, 556, 665, 345, 554, 432, 678, 100, 111, 124, 233, 444]
            },
            {
                name: 'Female',
                data: [200, 233, 445, 562, 443, 455, 600, 100, 111, 124, 233, 444, 665, 666, 190, 120]
            }
        ]
    });


    //3.Pie analytics (Both Radialize/Build)
    // Radialize the colors
    Highcharts.setOptions({
        colors: Highcharts.map(Highcharts.getOptions().colors, function(color) {
            return {
                radialGradient: {
                    cx: 0.5,
                    cy: 0.3,
                    r: 0.7
                },
                stops: [
                    [0, color],
                    [1, Highcharts.Color(color).brighten(-0.3).get('rgb')] // darken
                ]
            };
        })
    });

    // Build the analytics
    Highcharts.chart('container1', {
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false,
            type: 'pie'
        },
        title: {
            text: 'वडा अनुसार परिवार'
        },
        subtitle: {
            text: 'वडा अनुसार परिवार'
        },
        tooltip: {
            pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
        },
        legend: {
            enabled: true,
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: {
                    enabled: true,
                    format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                    connectorColor: 'silver'
                },
                showInLegend: true
            }
        },
        series: [{
            name: 'Share',
            data: [
                { name: 'वडा १', y: 7 },
                { name: 'वडा २', y: 11 },
                { name: 'वडा ३', y: 9 },
                { name: 'वडा ४', y: 13 },
                { name: 'वडा ५', y: 10 },
                { name: 'वडा ६', y: 11 },
                { name: 'वडा ७', y: 9 },
                { name: 'वडा ८', y: 8 },
                { name: 'वडा ९', y: 12 },
                { name: 'वडा १०', y: 10 },

            ]

        }]
    });

   // population
   //  Highcharts.analytics('container3', {
   //      analytics: {
   //          plotBackgroundColor: null,
   //          plotBorderWidth: null,
   //          plotShadow: false,
   //          type: 'pie'
   //      },
   //      title: {
   //          text: 'वडा अनुसार परिवार'
   //      },
   //      subtitle: {
   //          text: 'वडा अनुसार परिवार'
   //      },
   //      tooltip: {
   //          pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
   //      },
   //      legend: {
   //          enabled: true,
   //      },
   //      plotOptions: {
   //          pie: {
   //              allowPointSelect: true,
   //              cursor: 'pointer',
   //              dataLabels: {
   //                  enabled: true,
   //                  format: '<b>{point.name}</b>: {point.percentage:.1f} %',
   //                  connectorColor: 'blue'
   //              },
   //              showInLegend: true
   //          }
   //      },
   //      series: [{
   //          name: 'Population',
   //          data: [
   //              { name: 'पुरुष', y: 7 },
   //              { name: 'महिला', y: 11 },
   //              { name: 'अन्य', y: 9 }
   //
   //          ]
   //
   //      }]
   //  });
});