

function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}
function readURL(input) {
    if (input.files && input.files[0]) {
        let reader = new FileReader();
        reader.onload = function (e) {
            $("#imagePreview").css('background-image', 'url(' + e.target.result + ')');
            $('#imagePreview').hide();
            $('#imagePreview').fadeIn(650);
        }
        reader.readAsDataURL(input.files[0]);
    }
}
$("#imageUpload").change(function () {
    //https://developer.mozilla.org/en-US/docs/Web/API/
    //https://webkul.com/blog/send-images-through-ajax/
    let formData = new FormData();
    let file = this.files[0];
    let url = $(this).attr("data-url");
    if (formData) {
        formData.append('image', file);
        //console.log(formData.get('image'));
        $.ajax({
            headers: { "X-CSRFToken": getCookie("csrftoken") },
            url: url,
            type: 'POST',
            data: formData,
            cache: false,
            processData: false,
            contentType: false,
            dataType: 'json',
            beforeSend: () => {
            },
            success: (data) => {
                if(data.is_save){
                    location.reload();
                }
            },
            complete: (data) => {

            },
            error: (data) => {
            }

        });
    }
    readURL(this);
});


