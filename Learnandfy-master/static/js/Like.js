$('#Like-btn').on({
    'click': function() {
        if ($('#Like').attr('src') == "/static/images/Like.svg") {
            $('#Like').attr('src', "/static/images/Liked.svg");
            $('#Dislike').attr('src', "/static/images/Dislike.svg");
        } else {
            $('#Like').attr('src', "/static/images/Like.svg");
        }
    }
  });
  
  $('#Dislike-btn').on({
    'click': function() {
        if ($('#Dislike').attr('src') == "/static/images/Dislike.svg") {
            $('#Dislike').attr('src', "/static/images/Disliked.svg");
            $('#Like').attr('src', "/static/images/Like.svg");
        } else {
            $('#Dislike').attr('src', "/static/images/Dislike.svg");
        }
    }
  });
  
