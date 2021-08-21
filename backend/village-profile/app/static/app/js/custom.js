(function ($) {
    $(document).on('click', '.group-wrapper li', function (e) {
        e.preventDefault();
        e.stopPropagation();
        let uls = $(this).find('ul').length;
        if (uls) {
            if ($(this).hasClass('active-g')) {
                $(this).removeClass('active-g');
                $(this).addClass('collapsed');
                $(this).find('li').removeClass('active-g');
            } else {
                $(this).removeClass('collapsed');
                $(this).find('li').removeClass('collapsed');
                $(this).addClass('active-g');
                $(this).find('li').addClass('active-g');
            }
        } else {
            $(this).removeClass('active-g');
            $(this).addClass('no-child');
        }
    });
})(jQuery)
