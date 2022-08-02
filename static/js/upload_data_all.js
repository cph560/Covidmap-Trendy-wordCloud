function gettime(){
    $.ajax({
        url:'/time',
        
        timeout:10000,
        success:function(data){$('#time').html("TIME:  "+data)},
        error: function(){
            console.error('Fail to request time')
        }

    });
}



setInterval(gettime,1000);

function upload_mid1(){
    $.ajax({
        url:'/mid1',
        success:function(data){
            console.log(data);
            $('.number h1').eq(0).text(data.confirm);
            $('.number h1').eq(1).text(data.new_case);
            $('.number h1').eq(2).text(data.heal);
            $('.number h1').eq(3).text(data.death);

        },error: function(){
            console.error('Fail to request Mid1 data')
        }
        
    });
}
upload_mid1()

function upload_mid2(){
    $.ajax({
        url:'/mid2',
        success:function(data){
            console.log(data);
            ec_mid2.series[0].data=data.key;
            chart_mid2.setOption(ec_mid2);


        },error: function(){
            console.error('Fail to request Mid2 data')
        }
        
    });
}
upload_mid2()

function upload_left1(){
    $.ajax({
        url:'/left1',
        success:function(data){
            console.log(data);
            ec_left1.xAxis[0].data=data.date;
            ec_left1.series[0].data=data.confirm;
            ec_left1.series[1].data=data.suspect;
            ec_left1.series[2].data=data.heal;
            ec_left1.series[3].data=data.dead;
            chart_left1.setOption(ec_left1);


        },error: function(){
            console.error('Fail to request Left1 data')
        }
        
    });
}
upload_left1()

function upload_left2(){
    $.ajax({
        url:'/left2',
        success:function(data){
            console.log(data);
            ec_left2.xAxis[0].data=data.date;
            ec_left2.series[0].data=data.confirm_add;
            ec_left2.series[1].data=data.suspect_add;
            ec_left2.series[2].data=data.heal_add;
            ec_left2.series[3].data=data.dead_add;
            chart_left2.setOption(ec_left2);


        },error: function(){
            console.error('Fail to request Left2 data')
        }
        
    });
}
upload_left2()

function upload_right1(){
    $.ajax({
        url:'/right1',
        success:function(data){
            console.log(data);
            ec_right1.xAxis[0].data=data.province;
            ec_right1.series[0].data=data.confirm_add;
            chart_right1.setOption(ec_right1);


        },error: function(){
            console.error('Fail to request Right1 data')
        }
        
    });
}
upload_right1()

function upload_right2(){
    $.ajax({
        url:'/right2',
        success:function(data){
            console.log(data);
            
            ec_right2.series[0].data=data.key;
            chart_right2.setOption(ec_right2);


        },error: function(){
            console.error('Fail to request Right2 data')
        }
        
    });
}
upload_right2()

function upload_word_l2(){
    $.ajax({
        url:'/word_l2',
        success:function(data){
            console.log(data);
            
            ec_left2.series[0].data=data.key;
            chart_left2.setOption(ec_left2);


        },error: function(){
            console.error('Fail to request Left2 data')
        }
        
    });
}
upload_word_l2()