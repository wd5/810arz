$(function() {
    $(".fancybox-thumb").fancybox({
        prevEffect	: 'none',
        nextEffect	: 'none',
        helpers	: {
            title	: {
                type: 'outside'
            },
            overlay	: {
                opacity : 0.8,
                css : {
                    'background-color' : '#000'
                }
            },
            thumbs	: {
                width	: 50,
                height	: 50
            }
        }
    });

    $('.fancybox').fancybox({helpers: {overlay : {opacity: 0.5}}});


	$("div.next" ).live('click', function() {
        $('.gellery_in li').first().animate({width: 0}, 200, function(){
            $(this).appendTo('.gellery_in');
            $(this).css('width','auto')
        });
    });


    $('.load_purch').live('click',function(){
        var el = $(this);
        var parent = $('.load_block');
        $.ajax({
            url: "/load_items_by_ids/",
            data: {
                load_ids: $('#all_loaded_ids').val(),
                m_name: $('#m_name').val(),
                a_name: $('#a_name').val(),
                loaded_count: $('#loaded_count').val()
            },
            type: "POST",
            success: function(data) {

                parent.find('tbody').append(data)

                $('#all_loaded_ids').val($('#new_loaded_ids').val())
                $('#loaded_count').val($('#count').val())


                var rc = $('#remaining_count').val()
                if (rc<=0)
                    {$('.btn').remove()}

                $('#new_loaded_ids').remove()
                $('#remaining_count').remove()
                $('#count').remove()

            }
        });

        return false;
    });

    $('.load_docs').live('click',function(){
        var el = $(this);
        var parent = $('.load_block');
        $.ajax({
            url: "/load_items_by_ids/",
            data: {
                load_ids: $('#all_loaded_ids').val(),
                m_name: $('#m_name').val(),
                a_name: $('#a_name').val(),
                loaded_count: $('#loaded_count').val()
            },
            type: "POST",
            success: function(data) {

                parent.find('tbody').append(data)

                $('#all_loaded_ids').val($('#new_loaded_ids').val())
                $('#loaded_count').val($('#count').val())


                var rc = $('#remaining_count').val()
                if (rc<=0)
                    {$('.btn').remove()}

                $('#new_loaded_ids').remove()
                $('#remaining_count').remove()
                $('#count').remove()

            }
        });

        return false;
    });

});