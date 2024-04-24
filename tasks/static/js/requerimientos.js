document.addEventListener('keyup', e => {
    var inputText=e.target.value.toString().toLowerCase();
    let tableBody = document.getElementById("tbody-requerimientos");
    let tableRows = tableBody.getElementsByTagName("tr");
    for (let i = 0; i < tableRows.length; i++) {
        let textoConsulta = tableRows[i].cells[1].textContent
            .toString()
            .toLowerCase();

        if (textoConsulta.indexOf(inputText) === -1) {
            tableRows[i].style.visibility = "collapse";
        } else {
            tableRows[i].style.visibility = "";
        }
    }
})

// function onInputChange() {
//     let inputText = document.getElementById("input-search").value.toString().toLowerCase();
//     console.log(inputText)

//     let tableBody = document.getElementById("tbody-requerimientos");
//     let tableRows = tableBody.getElementsByTagName("tr");
//     // console.log(tableRows)
//     for (let i = 0; i < tableRows.length; i++) {
//         // console.log(tableRows[i].cells[1].textContent);
//         let textoConsulta = tableRows[i].cells[2].textContent
//             .toString()
//             .toLowerCase();

//         if (textoConsulta.indexOf(inputText) === -1) {
//             tableRows[i].style.visibility = "collapse";
//         } else {
//             tableRows[i].style.visibility = "";
//         }
//     }
// }