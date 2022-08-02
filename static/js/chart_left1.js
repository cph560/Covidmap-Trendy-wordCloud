var chartDom = document.getElementById('left1');
var chart_left1 = echarts.init(chartDom);
var ec_left1;

ec_left1 = {
    title: {
        text: 'COVID Trend',
        subtext: '',
        left: 'left',
        textStyle:{
            color:"#ffffff",
        }
    },
    tooltip:{
        trigger:'axis',
        axisPointer:{
            type:'line',
            linestyle:{
                color:'#444cb0'
            }
        }
    },
    xAxis: [{
        type: 'category',
        data: [],
        name:'Date',
        nameTextStyle:{
            color:"#fff",
        },
    }],

    yAxis: {
        type: 'value',
        name:'Number',
        nameTextStyle:{
            color:"#fff",
        },
        splitLine:{
            show:true,

        }
    },
    legend:{
        data:['Confirm','Suspect','Heal','Death'],
        textStyle:{
            color:'#ffffff'
        },
        left:'right',
    },

    series: [
        {
            name:'Confirm',
            data: [1, 230, 224, 218, 135, 147, 2660],
            type: 'line',
            smooth:true,

            
        },
        {               
            name:'Suspect',
            data: [150, 230, 224, 218, 135, 147, 345],
            type: 'line',
            smooth:true,

        },
        {
            name:'Heal',
            data: [32, 230, 224, 218, 135, 147, 35],
            type: 'line',
            smooth:true,
  
        },
        {
            name:'Death',
            data: [567, 230, 224, 218, 135, 147, 5645],
            type: 'line',
            smooth:true,

        },
    ],
    textStyle:{
        color:'#ffffff'
    },
    
    animationDuration:3000
};

chart_left1.setOption(ec_left1);
