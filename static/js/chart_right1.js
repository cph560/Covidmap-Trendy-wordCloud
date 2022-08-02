var chartDom = document.getElementById('right1');
var chart_right1 = echarts.init(chartDom);
var ec_right1;

ec_right1 = {
    title: {
        text: 'Top-5 Provinces of New_Case',
        subtext: '',
        left: 'left',
        textStyle:{
            color:"#d9dcdf",
        }

    },
    tooltip: {
        trigger: 'item'
    },
    xAxis:[{
        type: 'category',
        data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    }],
    yAxis: {
        type: 'value'
    },
    series: [
        {
        data: [120, 200, 150, 80, 70, 110, 130],
        type: 'bar',
        colorBy:"#f8f5ed",
        showBackground:true
        }
    ],
    textStyle:{
        color:'#ffffff'
    },
};

chart_right1.setOption(ec_right1);
