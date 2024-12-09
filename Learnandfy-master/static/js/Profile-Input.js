
$(function(){
    $('input[name="rad"]').click(function(){
        var $radio = $(this);
        var initial=true;
        
        // if this was previously checked
        if ($radio.data('waschecked') == true)
        {
            $radio.prop('checked', false);
            $radio.data('waschecked', false);
        }
        else
            $radio.data('waschecked', true);
        if(initial==true){
            
            $('.mainbar').addClass("disabled");

            initial=false;

        }
        
        $('.Student').click(function(){
            $('.mainbar').removeClass("disabled");
            $('.sidebar').addClass("disabled");

        });

        $('.Professional').click(function(){
            $('.sidebar').removeClass("disabled");
            $('.mainbar').addClass("disabled");

        });
        
        // remove was checked from other radios
        $radio.siblings('input[name="rad"]').data('waschecked', false);
    });
});