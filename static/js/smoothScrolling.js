$(function() {
    $('[data-toggle="elementscroll"]').click(function() {
        if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') 
                && location.hostname == this.hostname) {

            var target = $(this.hash);
            target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
            if (target.length) {
                $('html,body').animate({
                    scrollTop: target.offset().top -57 //head space
                }, 1000); //scroll speed
                return false;
            }
        }
    });
});

    $(function() {
$('html, body').hide();
if (window.location.hash) {
        setTimeout(function() {
                $('html, body').scrollTop(0).show();
                $('html, body').animate({
                        scrollTop: $(window.location.hash).offset().top -57 // head space
                        }, 1000) //scrollspeed
        }, 0);
}
else {
        $('html, body').show();
}   
    });