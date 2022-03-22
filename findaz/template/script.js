function fshowfilter() {
	let a = document.querySelector('.fsf')
	a.classList.toggle('aaa')
}

function vshowfilter() {
	let a = document.querySelector('.vsf')
	a.classList.toggle('aaa')
}

function tshowfilter() {
	let a = document.querySelector('.tsf')
	a.classList.toggle('aaa')
}

function cshowfilter() {
	let a = document.querySelector('.csf')
	a.classList.toggle('aaa')
}

function pshowfilter() {
	let a = document.querySelector('.psf')
	a.classList.toggle('aaa')
}


function showallbrands() {
	let a = document.querySelectorAll('#brands')
	for (let i of a) {
		if (i.checked == true) {
			i.checked = false
		} else {
			i.checked = true
		}
	}
}	
