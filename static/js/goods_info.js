$(function(){
	// $(".bags").click(function() {
     //    console.log("你点击了")
    // })
// 		$.getJSON("../JSON/goods_info.json",function(data){
// 			console.log("new"+data)
// 			for(var j=0;j<data.length;j++){
// 				var cart_obj=data[0]
// 				var goodsName=cart_obj.name;
// 	//		console.log(name)
// 				var goodsDes=cart_obj.des;
// 	//		console.log(des)
// 				var goodsPrice=cart_obj.dis;
// 				var goodsImg=cart_obj.img;
// 				var goodsID=cart_obj.id;
// 	//				  console.log(price)
// 		}
//
// 		//要先判断之前购物车是否有商品 有的话就要换成对象的形式 没有则为空
// 			var goodsList=$.cookie("cart")?JSON.parse($.cookie("cart")):[];
//
// 			var isExists=false;
// 			for(var i=0;i<goodsList.length;i++){
// 				var obj=goodsList[i];
// 				if(goodsName==obj.name){
// 					obj.num++
// 				//return false
// 					isExists=true;
// 				}
// 			}
// 			if(!isExists){
// 				var goods={
// 				img:goodsImg,
// 				name:goodsName,
// 				des:goodsDes,
// 				price:goodsPrice,
// 				num:1,
// 				id:goodsID
// 			}
// 			goodsList.push(goods)
// 			}
//
// 			$.cookie("cart",JSON.stringify(goodsList),{expires:10,path:"/"})
// 			console.log($.cookie("cart"))
//
// 			var goodsLists=$.cookie("cart");
//
// 			if(goodsLists){
//
//
// 				goodsLists=JSON.parse($.cookie("cart"));
// 			//	console.log(goodsLists)
// 			$(".cart_n").remove();
// 			$(".new_cart").show()
// 			var numArr=[];
// 				for(var i=0;i<goodsLists.length;i++){
// 					var goods=goodsLists[i];
// //					var p=$("<p class='new_cart'>有新的商品加入 快去购物车查看吧</p>")
// //					p.appendTo($(".cart"))
//
// 					var num=goods.num;
// 					numArr.push(num);
// 					var sum=0;
// 					for(var k=0;k<numArr.length;k++){
// 						sum=sum+numArr[k];
// 					}
// 					$("t").html(sum);
// 				}
// 			}
// 		})
// 	})
// 		var goodsLists=$.cookie("cart");
// 		goodsLists=JSON.parse($.cookie("cart"));
// 			//	console.log(goodsLists)
// 			$(".cart_n").remove();
// 			$(".new_cart").show()
// 		var numArr=[];
// 			for(var i=0;i<goodsLists.length;i++){
// 				var goods=goodsLists[i];
//
//
// 				var num=goods.num;
// 				numArr.push(num);
// 				var sum=0;
// 				for(var k=0;k<numArr.length;k++){
// 					sum=sum+numArr[k];
// 				}
// 				$("t").html(sum);
// 			}
//
	// 加操作
    $('.bt-wrapper .add').click(function () {
     //    // 商品ID
     //    var goodsid = $(this).attr('goodsid')
     //  va // that为了解决，在ajax中，this指向问题
     //    // var $that = $(this)
     //    $.get('/addcart/', function (response) {
            // console.log(response)
            // if (response.status == -1){ // 未登录
            //     window.open('/login/', target="_self")
            // } else if (response.status == 1){   // 添加成功
            //     pass
                // $that.prev().show().html(response.number)
                // $that.prev().prev().show()
            // }
            var num = parseInt($('.num').html())
            // console.log(num)
            num += 1
             // console.log(num)
            // console.log(num)
            $('.num').html(num)
        })
    // })
    // 减操作
    $('.bt-wrapper .red').click(function () {
     //    // 商品ID
     //    var goodsid = $(this).attr('goodsid')
     //  va // that为了解决，在ajax中，this指向问题
     //    // var $that = $(this)
     //    $.get('/addcart/', function (response) {
            // console.log(response)
            // if (response.status == -1){ // 未登录
            //     window.open('/login/', target="_self")
            // } else if (response.status == 1){   // 添加成功
            //     pass
                // $that.prev().show().html(response.number)
                // $that.prev().prev().show()
            // }
            var num = parseInt($('.num').html())
            console.log(num)
            if (num<1)
                $('.num').html(num)
            else
            num -= 1
             console.log(num)
            // console.log(num)
            $('.num').html(num)
        })
    // })
    $('.pro_btn .bot').click(function () {
        var goodsid = $(this).attr('goodsid')
        var number = $('.num').html()
         // console.log(goodsid)
         console.log(number)
        // var $that = $(this)
        $.get('/addcart/',{'goodsid':goodsid,'number':number}, function (response) {
            console.log(goodsid)


        })
    })
})
