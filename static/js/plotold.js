var data_list = [[], [], [], [], []] //entertainment, business, politics, sports, misc
var i;
console.log(input_list[0])
for (i = 0; i < input_list.length; i++) {
    var article = input_list[i]
    data_point = {
        name: article["metadata"]["category"],
        title: article["metadata"]["title"],
        author: article["metadata"]["author"],
        x: article["coordinates"][0],
        y: article["coordinates"][1],
        z: 3,
<<<<<<< Updated upstream
=======
<<<<<<< HEAD
        r: 25,
        summary: article["summary"],
        url: "https://google.com"
=======
>>>>>>> Stashed changes
        img_url: article["metadata"]["urlToImage"],
        summary: article["summary"]
>>>>>>> ae36814cee5373a8fc66efcbeca6af2349bc6fb7
    }
    if (data_point.name == "business") {
        data_list[0].push(data_point)
    } else if (data_point.name == "entertainment") {
        data_list[1].push(data_point)
    } else if (data_point.name == "politics") {
        data_list[2].push(data_point)
    } else if(data_point.name == "sports") {
        data_list[3].push(data_point)
    } else {
        data_list[4].push(data_point)
    }
}



var ctx = document.getElementById('myChart');
Chart.helpers.merge(Chart.defaults.global.plugins.datalabels, {
    color: 'black'
});
var myChart = new Chart(ctx, {
    type: 'bubble',
    data: {
        labels: ['Entertainment', 'Business', 'Technology', 'Politics', 'Sports', 'Miscellaneous'],
        datasets: [
            {
                label: 'Business',
                data: data_list[0],
                backgroundColor: 'rgba(237, 85, 100, 0.2)',
                hoverBackgroundColor: 'rgba(237, 85, 100, 0.5)',
                datalabels: {
                    listeners: {
                        click: function(context) {
                            window.open(context.dataset.data[context.dataIndex].url);
                        }
                    }
                }
            },
            {
                label: 'Entertainment',
                data: data_list[1],
                backgroundColor: 'rgba(255, 206, 84, 0.2)',
                hoverBackgroundColor: 'rgba(255, 206, 84, 0.2)',
                datalabels: {
                    listeners: {
                        click: function(context) {
                            window.open(context.dataset.data[context.dataIndex].url);
                        }
                    }
                }
            },
            {
                label: 'Politics',
                data: data_list[2],
                backgroundColor: 'rgba(160, 213, 104, 0.2)',
                hoverBackgroundColor: 'rgba(160, 213, 104, 0.5)',
                datalabels: {
                    listeners: {
                        click: function(context) {
                            window.open(context.dataset.data[context.dataIndex].url);
                        }
                    }
                }
            },
            {
                label: 'Miscellaneous',
                data: data_list[3],
                backgroundColor: 'rgba(172, 146, 235, 0.2)',
                hoverBackgroundColor: 'rgba(172, 146, 235, 0.5)',
                datalabels: {
                    listeners: {
                        click: function(context) {
                            window.open(context.dataset.data[context.dataIndex].url);
                        }
                    }
                }
            },
            {
                label: 'Sports',
                data: data_list[4],
                backgroundColor: 'rgba(79, 193, 232, 0.2)',
                hoverBackgroundColor: 'rgba(79, 193, 232, 0.5)',
                datalabels: {
                    listeners: {
                        click: function(context) {
                            window.open(context.dataset.data[context.dataIndex].url);
                        }
                    }
                }
            },
        ]
    },
<<<<<<< HEAD
    options: {
        onHover: function(context) {
            console.log(context.view.article.text);
=======
    legend: {
        enabled: false
    },
    title: {
        text: 'World News'
    },
    xAxis: {
        visible: false,
    },
    yAxis: {
        visible: false,
    },
    tooltip: {
        useHTML: true,
        headerFormat: '<table style="width:400px">',
        pointFormat: '<tr><th colspan="2"><h4>{point.title}</h4></th></tr>' +
            '<tr><th colspan="2"><img src={point.img_url} style="width:200px"></th></tr>' +
            '<tr><th>Author:</th><td>{point.author}</td></tr>' +
            '<tr><th>Summary:</th><td>{point.summary}</td></tr>',
        footerFormat: '</table>',
        followPointer: true
    },
    plotOptions: {
        series: {
            dataLabels: {
                enabled: true,
                format: '{point.name}'
            }
>>>>>>> ae36814cee5373a8fc66efcbeca6af2349bc6fb7
        },
        plugins: {
            datalabels: {
                font: {
                    weight: 'bold',
                },
                formatter: function(value, context) {
                    return context.dataset.data[context.dataIndex].name;
                },
                offset: 2,
                padding: 0,
                listeners: {
                    enter: function(context) {
                        context.hovered = true;
                        return true;
                    },
                    leave: function(context) {
                        context.hovered = false;
                        return true;
                    },
                },
                color: function(context) {
                    return context.hovered ? "black" : "grey";
                }
            }
        },
        scales: {
            yAxes: [{
                ticks: {
                    suggestedMin: -100,
                    suggestedMax: 100,
                    stepSize: 50,
                    display: false,
                },
                gridLines: {
                    display: false,
                    drawTicks: false,
                }
            }],
            xAxes: [{
                ticks: {
                    suggestedMin: -100,
                    suggestedMax: 100,
                    stepSize: 50,
                    display: false,
                },
                gridLines: {
                    display: false,
                    drawTicks: false,
                }
            }]
        },
        tooltips: {
            enabled: false,
        }
    }
});
