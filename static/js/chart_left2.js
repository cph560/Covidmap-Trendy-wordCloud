var chartDom = document.getElementById('left2');
var chart_left2 = echarts.init(chartDom);
var ec_left2;

ec_left2 = {
    title: {
        text: 'New_Confirm',
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
        data:['confirm_add','suspect_add','heal_add','dead_add'],
        textStyle:{
            color:'#ffffff'
        },
        left:'right',
    },

    series: [
        {
            name:'confirm_add',
            data: [1, 230, 224, 218, 135, 147, 2660],
            type: 'line',
            smooth:true,

            
        },
        {               
            name:'suspect_add',
            data: [150, 230, 224, 218, 135, 147, 345],
            type: 'line',
            smooth:true,

        },
        {
            name:'heal_add',
            data: [32, 230, 224, 218, 135, 147, 35],
            type: 'line',
            smooth:true,
  
        },
        {
            name:'dead_add',
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

chart_left2.setOption(ec_left2);