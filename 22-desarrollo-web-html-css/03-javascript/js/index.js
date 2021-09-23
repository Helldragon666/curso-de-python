

console.log('Holi de nuevo ;3');

let nombre = 'Yonatan'
let altura = 163;

//document.write([nombre, altura]);

imprimirDatos(nombre, altura);



function imprimirDatos(nombre, altura) {
    const div = document.querySelector('div')

    const parrafo = document.createElement('p');
    div.appendChild(parrafo);

    if (altura > 170) {
        parrafo.textContent = `${nombre} ${altura} muy alto :0`;
    } else {
        parrafo.textContent = `${nombre} ${altura}`;
    }

    for (let index = 0; index < 3; index++) {
        parrafo.textContent += 'Holi ;3'
    }
}


let nombres = ['yon', 'carlos'];