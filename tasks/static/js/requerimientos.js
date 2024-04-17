document.addEventListener('keyup', e => {

    if(e.target.matches('#input-search')){
        document.querySelector('.prueba').includes(e.target.value.tolowerCase())
    }

    console.log(e.target.value)
})