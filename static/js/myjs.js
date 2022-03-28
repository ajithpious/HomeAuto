function update() {

    $.ajax({
        url: '/getstatus',
        dataType: 'json',
        beforeSend: function() {
            $('#loader').removeClass('hidden')
            $('#AC').addClass('hide')
        },
        success: function(data, status, xhr) {

            // console.log(data)
            // let columns = JSON.parse(data.columns);
            // let values = JSON.parse(data.data);
            // let table = document.querySelector("table[id='rowsTable']");
            // table.innerHTML = "";
            // generateTable(table, values)
            // generateTableHead(table, columns)
            let chk1 = document.querySelector("input[id='chk1']");
            let chk2 = document.querySelector("input[id='chk2']");
            let p = document.querySelector("p[id='temp']");
            if (data.context.stat == 1) {
                chk1.checked = true
            } else {
                chk1.checked = false
            }
            console.log(data)
            console.log()
            p.innerHTML = data.value

        },
        complete: function() {
            $('#loader').addClass('hidden');
            $('#AC').removeClass('hide')
        }


    });

}

function command() {
    let chk1 = document.querySelector("input[id='chk1']");
    let valuebool = chk1.checked
    let value = 1
    if (valuebool == false) {
        value = 0
    }
    console.log(value)
    $.ajax({
        url: '/command',
        data: {
            "value": value
        },
        dataType: 'json',
        beforeSend: function() {
            chk1.disabled = true
        },
        error: function(xhr, textStatus, error) {

            console.log(error)
        },
        success: function(data, status, xhr) {
            console.log(data)
        },
        complete: function() {
            chk1.disabled = false
        }


    });

}