jQuery(function ($) {

    $(".sidebar-dropdown > a").click(function() {
  $(".sidebar-submenu").slideUp(200);
  if (
    $(this)
      .parent()
      .hasClass("active")
  ) {
    $(".sidebar-dropdown").removeClass("active");
    $(this)
      .parent()
      .removeClass("active");
  } else {
    $(".sidebar-dropdown").removeClass("active");
    $(this)
      .next(".sidebar-submenu")
      .slideDown(200);
    $(this)
      .parent()
      .addClass("active");
  }
});

$("#close-sidebar").click(function() {
  $(".page-wrapper").removeClass("toggled");
});
$("#show-sidebar").click(function() {
  $(".page-wrapper").addClass("toggled");
});


});

$(document).ready(function(){
  $('#id_login').submit(function(e){
    e.preventDefault()
    var serializedData = $(this).serialize()
    var href = $(this).attr('href')
    
    console.log(serializedData)
    $.ajax({
      type:'POST',
      url:'/user/login/',
      data: serializedData,
      success: function(response){
        Swal.fire("Giriş Başarılı","Ana sayfaya yönlendiriliyorsunuz","success")
        setTimeout(() => {window.location = href},2000)
      },
      error: function(response){
        Swal.fire("Hata",`${response.responseJSON.message}`,"error")
      }
    })
  })
})


$(document).ready(function(){
  $('#load_form').submit(function(e){
      e.preventDefault()
      var limit = $(this).attr('limit')
      var page = document.getElementById('pagination')
      var pagination_div = $('#pagination-div')
      var serializedData = $(this).serialize()

      $.ajax({
          type:'GET',
          url:'/article/load-more/',
          data: serializedData,
          success: (response) => {
            pagination_div.append(response.articles_html)
              if (page.value >= limit ){
                  $('#submit_button').hide()
              }
              page.value = parseInt(page.value)+1
          }
      })
  })
})


$(document).ready(function(){
  $('#duyuru_id').submit(function(e){
      for (var instance in CKEDITOR.instances)
        CKEDITOR.instances[instance].updateElement()
      // CKEDITOR içerisindeki verilerin ajax'a gitmemesi veya 2 kere istek atınca ilk yazılı olanını gitmesini engellemek için submit fonk'unun başına bunu koyuyorum.

      //Aslında success'de yaptığım ckeditor içindeki yazıları silme işlemini yukarıyada koyabilirim, updateElement() işini ilk başta yaptığım için veri serialize oluyor ama ajax istediği hata verirse içerideki değerleri silmemesi için success içerisine koyuyorum.

      e.preventDefault()

      var serializedData = $(this).serialize()

      $.ajax({
          type:'POST',
          url:'/announcement/add/',
          data:serializedData,
          success: (response) => {
            Swal.fire('Başarılı', 'Duyuru Başarıyla Yayınlandı', 'success')
            $('#duyuru_id')[0].reset();
            for (var instance in CKEDITOR.instances)
              CKEDITOR.instances[instance].setData('', function () { this.updateElement() })
            //CKEDITOR.instances.theInstance.setData( '', function() { this.updateElement(); } )
          },
          error: function(response){
              Swal.fire('Hata','Duyuru Yayınlanırken Bir Sorun Oluştu','error')
          }

      })
  })
})


$(document).ready(function() {
  $(".word").fancybox({
   'width': 600, // or whatever
   'height': 320,
   'type': 'iframe'
  });
 }); //  ready 