let chart_mid2 = echarts.init(document.getElementById('mid2'));

var myData = [{'name':'上海',"value":1000}, {'name':'浙江',"value":200}];



var ec_mid2 = {
    title: {
        text: 'New_Case MAP',
        subtext: '',
        left: 'center',
        textStyle:{
            color:"#d9dcdf",
        }

    },
    tooltip: {
        trigger: 'item'
    },
    
    visualMap: {
        show: true,
        type: 'piecewise', 
        textStyle: {
            fontSize: 8,
            color: '8A3310'
        },
        pieces: [
            { gte: 10000, color: '#b80909' },
            { gte: 1000, lt: 9999, color: '#e64546' },
            { gte: 100, lt: 999, color: '#f57567' },
            { gte: 10, lt: 99, color: '#ff9985' },
            { gte: 1, lt: 9, color: '#ffe5db' },
            { value: 0, color: '#fff' },
        ],
        hoverLink:true,

    },
    
    series: [{
        name: 'New_Case',
        type: 'map',
        mapType: 'china',
        roam: true, 

        itemStyle: {
            normal: {
                borderWidth: .5,
                borderColor: '#009FE8',
                areaColor: '#FFF'
            },
            emphasis: { 
                borderWidth: .5,
                borderColor: '#4B0082',
                areaColor: '#e5b8d5'
            }
        },
        label: {
            normal: {
                show: true,
                fontSize: 10
            },
            emphasis: {
                show: true,
                fontSize: 13
            }
        },
        data: myData
    }]
    
};
chart_mid2.setOption(ec_mid2)