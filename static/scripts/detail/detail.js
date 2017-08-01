/* 下载链接组切换 */
$(".download_title").click(function (e){
    var target = $(e.target),
        idx = target.index();

    $(".download_title.current").removeClass("current");
    $($(".download_title").eq(idx)).addClass("current");

    $(".download .links_container:visible").hide();
    $($(".download .links_container").eq(idx)).show();
});

/* 全选 */
$(".links_container .check_all").click(function (e){
     var target = $(e.target),
         isChecked = target.prop("checked");

     $(target).parents(".links_container").find(".check_all").each(function (i, el){
         isChecked ? $(el).prop("checked", true) : $(el).removeProp("checked");
     });

     $(target).parents(".links_container").find(".item_checker").each(function (i, el){
         isChecked ? $(el).prop("checked", true) : $(el).removeProp("checked");
     });
});

/* 选择一个项 */
$(".links_container .item_checker").click(function (e){
     var target = $(e.target);

     var list = $(target).parents(".links_container").find(".item_checker").toArray();

     var isAllChecked = list.every(function (el){
         return $(el).prop("checked") !== false
     });

     $(target).parents(".links_container").find(".check_all").each(function (i, el){
         isAllChecked ? $(el).prop("checked", true) : $(el).removeProp("checked");
     });

});