

var chartDom = document.getElementById('right2');
var chart_right2 = echarts.init(chartDom);
var ec_right2;




ec_right2 = {
    
    title: {
        text: 'Chinese Trendy News',
        subtext: '',
        left: 'left',
        textStyle:{
            color:"#d9dcdf",
        }
    },
    series: [{
        type: 'wordCloud',

        shape: 'circle',


        keepAspect: false,


        left: 'center',
        top: 'center',
        width: '70%',
        height: '80%',
        right: null,
        bottom: null,


        sizeRange: [12, 55],


        rotationRange: [-90, 90],
        rotationStep: 45,



        gridSize: 1,


        drawOutOfBound: false,


        layoutAnimation: false,


        textStyle: {
            fontFamily: 'sans-serif',
            fontWeight: 'bold',

            color: function () {
                // Random color
                return 'rgb(' + [
                    Math.round(Math.random() * 255),
                    Math.round(Math.random() * 255),
                    Math.round(Math.random() * 255)
                ].join(',') + ')';
            }
        },
        emphasis: {
            focus: 'self',

            textStyle: {
                textShadowBlur: 10,
                textShadowColor: '#333'
            }
        },

        // Data is an array. Each array item must have name and value property.
        data: [{
            name: 'Farrah Abraham',
            value: 366,

        }]
    }]
}

ec_right2&&chart_right2.setOption(ec_right2);