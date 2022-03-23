function movekatalog() {
	let a = document.querySelector('.katalogi')
	if (a.style.top == '62px') {
		a.style.top = '-100%'
		a.style.border = '1px rgba(225,225,225,0.3) solid';
		a.style.borderTop= '0.1px rgba(0,0,0,0.3) solid';
		a.style.borderBottom = '1px rgba(0,0,0,0.3) solid';
	} else {
		a.style.top = '62px'
		a.style.border = '240px #FFF solid';
		a.style.borderTop= '10px #FFF solid';
		a.style.borderBottom = '200px #FFF solid';
	}
}

function showkatalog(i) {
	let x = document.querySelectorAll('.list-katalog-list');
	let y = document.querySelectorAll('.listi-kategori > li');
	for (let i of x) {
		i.classList.remove('show');
		i.parentElement.style.backgroundColor = '#fff'
	}

	let a = document.querySelector(`.${i}`)
	a.classList.add('show');
	a.parentElement.style.backgroundColor = '#d3d3d3'
}

// function showklistkataloglist() {
// 	let a = document.querySelector('.list-katalog-list')
//
//
// }


