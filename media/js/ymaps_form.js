$(function(){
    var id = $('input[name="url"]').val()
if (id=='/admin/siteblocks/settings/3/')
    {
        $('.value').append('<input id="id_map" type="text" class="vTextField" name="map" maxlength="1">')

        $('#id_map').replaceWith('<div id="admin_map" style="height:450px;width:680px;"></div>');

        var geopoint = $('#id_value').val();

        var scale = 15;
        var flag = true;
        if (geopoint == ''){
            geopoint = '52.0354,113.482';
            geopoint = geopoint.split(',');
            scale = 11;
            flag = false;
        }
        else{
            geopoint = geopoint.split(',');
        }


            ymaps.ready(function () {
                var map = new ymaps.Map("admin_map",
                    {
                        center: [geopoint[0],geopoint[1]],
                        zoom: scale,
                        type: "yandex#publicMap"
                    }
                );

                map.controls.add("zoomControl");
                var placemark;
                if(flag){
                    placemark = new ymaps.Placemark(
                        [geopoint[0],geopoint[1]],
                        {
                            'balloonContent': $('#id_title').val()
                        }
                    );

                    map.geoObjects.add(placemark);
                }

                map.events.add('click', function (e) {
                    if(placemark){
                        map.geoObjects.remove(placemark);
                    }
                    map.balloon.close();
                    var coords = e.get('coordPosition');
                    $('#id_value').val(coords);

                    map.balloon.open(coords,
                    {
                        contentHeader: 'Адрес',
                        contentBody: '<p>'+ $('#id_title').val() +'</p>' +
                            '<p>Координаты: ' + [
                                coords[0].toPrecision(6),
                                coords[1].toPrecision(6)
                            ].join(', ') + '</p>',
                        contentFooter: '<sup>Щелкните еще раз</sup>'
                    });

                    placemark = new ymaps.Placemark(
                        [coords[0],coords[1]],
                        {
                            'balloonContent': $('#id_title').val()
                        }
                    );
                    map.geoObjects.add(placemark);



                });

            });

    }

});