
function searchClasses(elem) {

    if (elem.length > 3) {

        $.ajax({
            url: "/api/v1/search?query=" + elem,
            type: "GET",
            success: (response) => {
                $(".search_query").empty()
                response && response?.data?.length > 0 ? response?.data?.map((ele) => {
                    // console.log(ele,"sajan mila kya")
                    $(".search_query").append(`
                    <div class="search_card p-1 m-1">
                        <a href="/class/${ele?.slug}">
                            <div class="d-flex searh_card_container">
                            <img src="${ele?.image}" alt="" />
                            <div class="card_name d-flex flex-wrap">
                                <div class="detail_tag ps-2">
                                    <div>
                                        <h6 class="m-0">${ele?.name}</h6>
                                    </div>
                                    <div class="search_detail d-flex gap-2 flex-wrap">
                                        <div class="class_price d-flex">
                                        <p class="m-0"><small>Price: ${ele?.price_currency}${ele?.price}  |</small></p>
                                        </div>
                                        <div class="class_duration d-flex">
                                        <p class="m-0"><small>Duration: ${ele?.length}  |</small></p>
                                        </div>
                                        <div class="class_level d-flex">
                                        <p class="m-0"><small>Level: ${ele?.experties_level}</small></p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            </div>
                        </a>
                    </div>
                    `)
                }) : console.log("chal bhag");


            },
            error: (response) => { console.log(response) }
        })
    }
    else {
        $(".search_query").empty()

    }
}

function fav_this_class(id_call,class_call,csrf_token,type,event){
    event.preventDefault();  
    event.stopPropagation(); 
    $.ajax({
        url: "/api/v1/interest-list",
        type: "POST",
        data : {service_id : id_call, csrfmiddlewaretoken : csrf_token},
        success: (response) => {
            // window.location.reload()
           $('.'+class_call).empty()
            if (type =='refresh'){
                window.location.reload()
            }
            else if (type =='empty'){
                $('.'+class_call).append('&#9829;')
                $('.'+class_call).attr('onclick',"fav_this_class("+id_call+",'fav_icon','"+csrf_token+"','fill',event)")
            }
            else{
                $('.'+class_call).append('&#9825;')
                $('.'+class_call).attr('onclick',"fav_this_class("+id_call+",'fav_icon','"+csrf_token+"','empty',event)")
            }
        },
        error: (response) => { console.log(response) }
    })
}