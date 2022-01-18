function fillPage(json) {
    let selector = $('.fakedata-table-body');
    if (selector.children().length === 1) {
        selector.empty();
    }
    for (let user of json.data) {
        appendUserToTable(user);
    }
}

function generateFakeData(size) {
    $.ajax({
        url: `/api/generate_fake_data?size=${size}`,
        method: 'get',
        success: fillPage
    });
}

function refreshAndGenerateFakeData(size, seed) {
    $.ajax({
        url: `/api/refresh_and_generate_fake_data?size=${size}&seed=${seed}`,
        method: 'get',
        success: fillPage
    });
}

function appendUserToTable(user) {
    let selector = $('.fakedata-table-body');
    selector.append(
        `<tr>
            <th scope="col" class="text-center">${user.id}</th>
            <th scope="col" class="text-center">${user.initials}</th>
            <th scope="col" class="text-center">${user.address}</th>
            <th scope="col" class="text-center">${user.telnumber}</th>
        </tr>`
    );
}

function render(size, seed) {
    refreshAndGenerateFakeData(size, seed);

    $(window).scroll(function() {
        if ($(window).scrollTop() + $(window).height() === $(document).height()) {
            generateFakeData(size);
        }
    });

    $('.download-excel-btn').click(function() {
        window.open('/download', '_blank').focus();
    });
    

}
