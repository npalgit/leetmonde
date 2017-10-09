/**
 * @FileName    db
 * @Description
 * @Author      yangchao
 * @Email       lemon@ofchao.bid
 * @Version
 * @Date        22:41 12/13/15
 */
$("document").ready(function(){

    var diffculty = $($('strong')[2]).text().substr(0, 1);
    var title = $('.question-title h3').text();
    $('.question-title h3').text(title + '(' + diffculty + ')');
});