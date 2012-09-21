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

    $("#handle").draggable({
        axis: "x",
        containment: "#handle_container",
        drag: function() {
            var pos = parseInt($("#handle").css("left")) + 184;
            $("#idiv").css('left', pos);
            $("#il").css('width', pos);
        }
    });

});



(function() {
    $.fn.bgscroll = $.fn.bgScroll = function( options ) {
        current = 0;
        i = 0;
        l = 0;
        if( !this.length ) return this;
        if( !options ) options = {};
        if( !window.scrollElements ) window.scrollElements = {};
         
        for( var i = 0; i < this.length; i++ ) {
            var allowedChars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
            var randomId = '';
            for( var l = 0; l < 5; l++ ) randomId += allowedChars.charAt( Math.floor( Math.random() * allowedChars.length ) );
             
                this[ i ].current = 0;
                this[ i ].scrollSpeed = options.scrollSpeed ? options.scrollSpeed : 10;
                this[ i ].direction = options.direction ? options.direction : 'h';
                window.scrollElements[ randomId ] = this[ i ];
                 
                eval( 'window[randomId]=function(){var axis=0;var e=window.scrollElements.' + randomId + ';e.current -= 1;if (e.direction == "h") axis = e.current + "px 0";else if (e.direction == "v") axis = "0 " + e.current + "px";else if (e.direction == "d") axis = e.current + "px " + -e.current + "px";else if (e.direction == "n") l = -1000;$( e ).css("background-position", axis);}' );
                                                          
                setInterval( 'window.' + randomId + '()', options.scrollSpeed ? options.scrollSpeed : 10 );
           }
            return this;
        }
})(jQuery);



$(function() {
	$(".otvinta_span").click(function() {
		$(this).parent().addClass('otvinta_on');
		
		$(function() {
		    $('#f_heli_blade_stat').fadeOut(800);
		    
		    $('#f_heli_shade').fadeOut(1500);
		    
			$('#f_heli_blade_anim').fadeIn(1000).sprite({fps: 10, no_of_frames: 3});
			
		    $('#f_heli_ground').fadeOut(4000);
		    
		    $('#f_heli_ground img').animate({
			    width: '200px',
			    top: '400px',
			    left: '-100px'
			  }, 5000);
		    $('#f_clouds').fadeIn(3000);
		    
		    $('#f_clouds_clouds').bgscroll({scrollSpeed:10, direction:'d' });
		});
		
		return false;
	});
	
	
	$(".otvinta_on_span").click(function() {
		$(this).parent().removeClass('otvinta_on');
		
		$(function() {
		    $('#f_heli_ground img').css({'top' : '0', 'left' : '200px'});

		    $('#f_clouds').fadeOut(4000);

		    setTimeout(function() { 
			    $('#f_clouds_clouds').bgscroll({scrollSpeed:0, direction:'n' }),
			    $('#f_heli_blade_stat').fadeIn(800) 
		    }, 3000);
		    
		    setTimeout(function() { 
			    $('#f_heli_blade_anim').fadeOut(10).spStop(true),
			    $('#f_heli_blade_anim').destroy()
		    }, 3500);


		    $('#f_heli_ground').fadeIn(3000);
		    
		    $('#f_heli_ground img').animate({
			    width: '567px',
			    top: '108px',
			    left: '0'
			  }, 3000);
			  
		    $('#f_heli_shade').fadeIn(3500);
		});

		return false;
	});
});
