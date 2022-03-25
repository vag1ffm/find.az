function movekatalog() {
	let a = document.querySelector('.katalogi')
	if (a.style.top === '62px') {
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

	for (let i of x) {
		i.classList.remove('show');
		i.parentElement.style.backgroundColor = '#fff'
	}

	let a = document.querySelector(`.${i}`)
	a.classList.add('show');
	a.parentElement.style.backgroundColor = '#d3d3d3'
}

function moveqlavniytovarleft() {
	let a = document.querySelector('.slayd')
	let b = a.style.left.split('px')
	b = b.join('')
	b = +b
	if (b === 0) {
		b = b -130
		a.style.left = `${b}px`
	} else if (b === -1180) {
	} else if (b === -1030) {
		b-=150
		a.style.left = `${b}px`
	} else {
		b = b -210
		a.style.left = `${b}px`
	}
}

function moveqlavniytovarright() {
	let a = document.querySelector('.slayd')
	let b = a.style.left.split('px')
	b = b.join('')
	b = +b
	if (b===20) {

	} else if (b === 0) {

	}  else if (b === -130) {
		b = b + 150
		a.style.left = `${b}px`
	} else if (b === -340) {
		b+= 150
		a.style.left = `${b}px`
	} else {
		b += +210
		a.style.left = `${b}px`
	}
}

