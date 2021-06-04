document.addEventListener('DOMContentLoaded', function() {
    var is_admin = JSON.parse(document.getElementById('json-admin').value)
    var initialLocaleCode = 'tr';
    var localeSelectorEl = document.getElementById('locale-selector');
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        //contentHeight: 800,
        height: 800,
        width: 600,
        headerToolbar: {
            left: 'prevYear,prev,next,nextYear today',
            center: 'title',
            right: 'dayGridMonth,dayGridWeek,dayGridDay'
            },
        initialView: 'dayGridMonth',
        timeZone: 'UTC',
        eventSources: [
            {
            events: JSON.parse(document.getElementById('json').value),
            //color: 'blue',     // an option!
            //textColor: 'white' // an option!
            }
        ],
        locale: initialLocaleCode,
        buttonIcons: false,
        selectable:is_admin ? true : false,
        editable:is_admin ? true : false,
        navLinks:true,
        selectHelper: true,
        dayMaxEvents: true,
        businessHours: true,

        //unselect: function(param){},
        select: function(info){
            Swal.fire({
                title: 'Etkinlik Oluştur',
                html: 
                `
                <form method="POST" id="create-form" class="ui form">
                <div class="field">
                <label>Başlık</label><input type="text" id="id_title" name="title" /> 
                </div>
                <div class="field">
                <label>Başlangıç Tarihi</label><input type="date" id="id_start_date" name="start_date" value='${info.startStr}'/> <input type="time" id="id_start_time" name="start_time" /> 
                </div>
                <div class="field">
                <label>Bitiş Tarihi</label><input type="date" id="id_end_date" name="end_date" value='${info.endStr}'/> <input type="time" id="id_end_time" name="end_time" />
                </div>
                </form>
                `,
                inputAttributes: {
                    autocapitalize: 'off'
                },
                showCancelButton: true,
                confirmButtonText: 'Ekle',
                showLoaderOnConfirm: true,

                allowOutsideClick: () => !Swal.isLoading()
                }).then((result) => {
                if (result.isConfirmed) {
                    $.ajax({
                        type: 'POST',
                        url: '/main/add-new-event/',
                        data: {
                            'csrfmiddlewaretoken': document.querySelector('[name=csrfmiddlewaretoken]').value,
                            'title': $('#id_title').val(),
                            start_date: $('#id_start_date').val(),
                            start_time: $('#id_start_time').val(),
                            end_date: $('#id_end_date').val() ? $('#id_end_date').val() : null,
                            end_time: $('#id_end_time').val() ? $('#id_end_time').val() : null,
                        },
                        success: (response) => {
                            Swal.fire({
                                position: 'top-end',
                                icon: 'success',
                                title: 'Etkinlik Başarıyla Kaydedildi',
                                showConfirmButton: false,
                                timer: 2000,
                            })
                        },
                        error: (response) => {
                            Swal.fire('Hata',`${response.responseJSON.message ? response.responseJSON.message : 'Bir Hata Oluştu!'}`, 'error')
                        }
                    })
                }
                })
        },
        navLinkDayClick: function(date, jsEvent) {
            //console.log('day', date.toISOString());
            //console.log('coords', jsEvent.pageX, jsEvent.pageY);
            },
        eventResize: (info) => {
            console.log(is_admin)
            Swal.fire({
                title: 'Değişikliği Kabul Ediyor Musunuz ?',
                icon: 'question',
                showCancelButton: true,
                confirmButtonText: 'Evet',
                cancelButtonText: 'Hayır',
                cancelButtonColor: 'red',
            }).then((result) => {
                if (result.isConfirmed){
                    $.ajax({
                        type:'POST',
                        url:'/main/drag-event/',
                        mode: 'same-origin',
                        data: { 
                            'id': info.event.id,
                            'start':info.event.start.toISOString(),
                            'end':info.event.end ? info.event.end.toISOString() : null, 
                            'csrfmiddlewaretoken': document.querySelector('[name=csrfmiddlewaretoken]').value,
                        },
                        success: (response) => {
                            Swal.fire(
                                'Başarılı!',
                                'Değişiklik Yapıldı.',
                                'success'
                            )
                        },
                        error: (response) => {
                            Swal.fire('Hata','Bir Hata Oluştu','error')
                            info.revert()
                        }
                    })
                }
                else{
                    info.revert()
                } 
                
            }) 
        },
        eventClick: function(info) {
            console.log(info.event.start.toISOString())
            var is_admin = JSON.parse(document.getElementById('json-admin').value)
            const sweetalert = () => {Swal.fire(`<p style='font-size:14px;'>
            Etkinlik: ${info.event.title}
            Başlangıç Tarihi: ${info.event.start.toUTCString()}
            ${info.event.end ? `Bitiş Tarihi: ${info.event.end.toUTCString()}` : ''}
            </p>`)}
            
            if (is_admin){
                Swal.fire({
                    title: 'Değişiklik yapmak istiyor musunuz?',
                    showDenyButton: true,
                    showCancelButton: true,
                    confirmButtonText: `Güncelle`,
                    denyButtonText: `Sil`,
                    cancelButtonText: 'Etklinlik Bilgisini Göster'
                    }).then((result) => {
                    /* Read more about isConfirmed, isDenied below */
                    if (result.isConfirmed) {
                        Swal.fire({
                            title:'Etkinlik Bilgilerini Güncelle',
                            html:`
                            <form method="POST" id="create-form" class="ui form">
                            <div class="field">
                            <label>Başlık</label><input type="text" id="id_title" name="title" value='${info.event.title}' /> 
                            </div>
                            <div class="field">
                            <label>Başlangıç Tarihi</label><input type="date" id="id_start_date" name="start_date" value='${info.event.start.toISOString().split('T')[0]}'/> <input type="time" id="id_start_time" name="start_time" value='${info.event.start.toISOString().split('T')[1].split('.')[0]}' /> 
                            </div>
                            
                            <div class="field">
                            <label>Bitiş Tarihi</label><input type="date" id="id_end_date" name="end_date" value='${ info.event.end ? info.event.end.toISOString().split('T')[0] : null}'/> <input type="time" id="id_end_time" name="end_time" value='${ info.event.end ? info.event.end.toISOString().split('T')[1].split('.')[0]: null}' />
                            </div>
                            </form>
                            `,
                            showCancelButton: true,
                            confirmButtonText: 'Değişiklikleri Uygula',
                        }).then((result) => {
                            if(result.isConfirmed){
                                $.ajax({
                                    method: 'POST',
                                    url: '/main/update-event/',
                                    data: {
                                        'csrfmiddlewaretoken': document.querySelector('[name=csrfmiddlewaretoken]').value,
                                        'title': $('#id_title').val(),
                                        id: info.event.id,
                                        start_date: $('#id_start_date').val(),
                                        start_time: $('#id_start_time').val(),
                                        end_date: $('#id_end_date').val() ? $('#id_end_date').val() : null,
                                        end_time: $('#id_end_time').val() ? $('#id_end_time').val() : null,
                                    },
                                    success: (response) => {
                                        Swal.fire({
                                            position: 'top-end',
                                            icon: 'success',
                                            title: 'Etkinlik Başarıyla Güncellendi.',
                                            showConfirmButton: false,
                                            timer: 2000,
                                        })
                                    },
                                    error: (response) => {
                                        Swal.fire('Hata',`${response.responseJSON.message ? response.responseJSON.message : 'Bir Hata Oluştu!'}`, 'error')
                                    }
        
                                })
                            }
                        
                        })
                    } else if (result.isDenied) {
                        Swal.fire({
                            title: 'Bu Etkinliği Silmek İstediğinize Emin Misiniz ? Bu İşlem Geriye Alınamaz !',
                            icon: 'danger',
                            showCancelButton: true,
                            confirmButtonText: 'Sil',
                            confirmButtonColor: 'red',
                        }).then((result) => {
                            if (result.isConfirmed){
                                $.ajax({
                                    method: 'POST',
                                    url:'/main/delete-event/',
                                    data: {
                                        'csrfmiddlewaretoken': document.querySelector('[name=csrfmiddlewaretoken]').value,
                                        id: info.event.id
                                    },
                                    success: (response) => {
                                        Swal.fire({
                                            position: 'top-end',
                                            icon: 'success',
                                            title: 'Etkinlik Başarıyla Silindi.',
                                            showConfirmButton: false,
                                            timer: 2000,
                                        })
                                    },
                                    error: (response) => {
                                        Swal.fire('Hata','Bir Hata Oluştu!', 'error')
                                    }
                                })
                            }
                        })
                    }
                    else{
                        sweetalert()
                    }
                    })
            }
            else{
                sweetalert()
            }
    
        // change the border color just for fun
            //info.el.style.borderColor = 'red';
        },
        //eventMouseEnter: function( mouseEnterInfo ) {},
        //eventMouseLeave: function ( mouseLeaveInfo ) {},
        //eventDragStart: function( info ) { console.log('drag start: ',info) },
        //eventDragStop: function( info ) { console.log('drag stop: ',info) },
        eventDrop: function( info ) { 
            //console.log(info.event.start.toISOString())
            Swal.fire({
                title: 'Değişikliği Onaylıyor musunuz ?',
                text: `Bu etkinliğin başlangıç tarihini ${info.event.start} ${info.event.end ? `bitiş tarihini ${info.event.end}` : ''} olarak ayarlayacaksınız.`,
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Onayla',
                cancelButtonText: 'İptal',
                }).then((result) => {
                if (result.isConfirmed) {
                    $.ajax({
                        type:'POST',
                        url:'/main/drag-event/',
                        mode: 'same-origin',
                        data: { 
                            'id': info.event.id,
                            'start':info.event.start.toISOString(),
                            'end':info.event.end ? info.event.end.toISOString() : null, 
                            'csrfmiddlewaretoken': document.querySelector('[name=csrfmiddlewaretoken]').value,
                        },
                        success: (response) => {
                            Swal.fire(
                                'Başarılı!',
                                'Değişiklik Yapıldı.',
                                'success'
                            )
                        },
                        error: (response) => {
                            Swal.fire('Hata','Bir Hata Oluştu','error')
                            info.revert()
                        }
                    })
                }
                else{
                    info.revert()
                }
                })
            },
        //dateClick: (info) => {
        //    console.log(info.dateStr)
        //    console.log(info)
        //}

    });

    //calendar.on('dateClick', function(info) {
    //    console.log('clicked on ' + info.dateStr);});
    
    calendar.render();
    
    // build the locale selector's options
    calendar.getAvailableLocaleCodes().forEach(function(localeCode) {
        var optionEl = document.createElement('option');
        optionEl.value = localeCode;
        optionEl.selected = localeCode == initialLocaleCode;
        optionEl.innerText = localeCode;
        localeSelectorEl.appendChild(optionEl);
    }); //bu yukarıda eklediğim locales-all.js'den gelen verileri aşağıdaki locale-selector combobox'ına ekliyor.

    // when the selected option changes, dynamically change the calendar option
    localeSelectorEl.addEventListener('change', function() {
        if (this.value) {
        calendar.setOption('locale', this.value);
        }
    });

});

