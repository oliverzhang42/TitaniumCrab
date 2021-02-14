var data_list = [[], [], [], [], []] //entertainment, business, politics, sports, misc
var i;
var y_coords = []
var x_coords = []
var j;
var k;
for (j = 0; j < input_list.length; j++) {
    for (k = j; k < input_list.length; k++) {
        if (input_list[j]["metadata"]["viewCount"] < input_list[k]["metadata"]["viewCount"]) {
            tmp = input_list[j];
            input_list[j] = input_list[k];
            input_list[k] = tmp;
        }   
    }
}
for (i = 0; i < 100; i++) {
    var article = input_list[i]
    y_coords.push(article["coordinates"][1]);
    x_coords.push(article["coordinates"][0]);
    data_point = {
        name: article["metadata"]["category"],
        title: article["metadata"]["title"],
        author: article["metadata"]["author"],
        image: article["metadata"]["urlToImage"],
        x: article["coordinates"][0] * 100,
        y: article["coordinates"][1] * 100,
        z: 3,
        r: Math.sqrt(article["metadata"]["viewCount"]) * 0.1,
        summary: article["summary"],
        //summary: "lorem ipsum dolor",
        url: article["metadata"]["url"],
        //url: "https://google.com"
    }
    if (data_point.name == "business") {
        data_list[0].push(data_point)
    } else if (data_point.name == "entertaiment") {
        data_list[1].push(data_point)
    } else if (data_point.name == "politics") {
        data_list[2].push(data_point)
    } else if (data_point.name == "health") {
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
        labels: ['Business', 'Entertainment', 'Politics', 'Health', 'Miscellaneous'],
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
                },
                
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
                label: 'Health',
                data: data_list[3],
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
            {
                label: 'Miscellaneous',
                data: data_list[4],
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
        ]
    },
    options: {
        plugins: {
            datalabels: {
                
                font: {
                    weight: 'bold',
                },
                formatter: function(value, context) {
                    return "·"//context.dataset.data[context.dataIndex].name;
                },
                offset: 2,
                padding: 0,
                listeners: {
                    enter: function(context) {
                        var temp = document.getElementById("summary");
                        temp.innerHTML = '';
                        context.hovered = true;
                        var sumText = document.createElement("p");
                        sumText.innerHTML = context.dataset.data[context.dataIndex].summary;

                        var a = document.createElement('a');
                        var linkText = document.createTextNode(context.dataset.data[context.dataIndex].title);
                        a.appendChild(linkText);
                        a.href=context.dataset.data[context.dataIndex].url;
                        var element = document.getElementById("summary");
                        element.appendChild(a);
                        element.appendChild(sumText);
                        var img = document.createElement('img'); 
                        img.src = context.dataset.data[context.dataIndex].image; 
                        //img.style.width = "15em";
                        //img.style.height = "20em"; 
                        element.appendChild(img);
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
            enabled:false
        },
    }
});
