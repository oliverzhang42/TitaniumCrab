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
        img_url: article["metadata"]["urlToImage"],
        summary: article["summary"]
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
Highcharts.chart('container', {
    chart: {
        type: 'bubble',
        plotBorderWidth: 1,
        zoomType: 'xy'
    },
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
        },
        bubble: {
            minSize: 0,
            maxSize: 50
        }
    },
    series: [
        {
            data: data_list[0],
            color: "#2f7ed8"
        },
        {
            data: data_list[1],
            color: "#0d233a"
        },
        {
            data: data_list[2],
            color: "#8bbc21"
        },
        {
            data: data_list[3],
            color: "#910000"
        },
        {
            data: data_list[4],
            color: "#1aadce"
        }
    ]
});
