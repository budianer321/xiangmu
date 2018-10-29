$(function() {
    $('img').each(function() {
        var imgpath = $(this).attr('src')
        // imgpath = imgpath.slice(3)
        imgpath = "{% static '" + imgpath +  "' %}"
        $(this).attr('src', imgpath)
    })

    console.log($('body').html())
})