function movekatalog() {
	let a = document.querySelector('.katalogi')
	if (a.style.top === '62px') {
		a.style.top = '-130%'
		// a.style.border = '1px rgba(225,225,225,0.3) solid';
		// a.style.borderTop= '0.1px rgba(0,0,0,0.3) solid';
		// a.style.borderBottom = '1px rgba(0,0,0,0.3) solid';
	} else {
		a.style.top = '62px'
		// a.style.border = '240px #FFF solid';
		// a.style.borderTop= '10px #FFF solid';
		// a.style.borderBottom = '200px #FFF solid';
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
//
// function moveqlavniytovarleft() {
// 	let a = document.querySelector('.slayd')
// 	let b = a.style.left.split('px')
// 	b = b.join('')
// 	b = +b
// 	if (b === 0) {
// 		b = b -130
// 		a.style.left = `${b}px`
// 	} else if (b === -1180) {
// 	} else if (b === -1030) {
// 		b-=150
// 		a.style.left = `${b}px`
// 	} else {
// 		b = b -210
// 		a.style.left = `${b}px`
// 	}
// }
//
// function moveqlavniytovarright() {
// 	let a = document.querySelector('.slayd')
// 	let b = a.style.left.split('px')
// 	b = b.join('')
// 	b = +b
// 	if (b===20) {
//
// 	} else if (b === 0) {
//
// 	}  else if (b === -130) {
// 		b = b + 150
// 		a.style.left = `${b}px`
// 	} else if (b === -340) {
// 		b+= 150
// 		a.style.left = `${b}px`
// 	} else {
// 		b += +210
// 		a.style.left = `${b}px`
// 	}
// }
let count;
function screensize() {
	let a = document.documentElement.scrollWidth
	if (a<500) {
		count = 1;
	} else if (a<702) {
		count = 2;
	} else if (a<904) {
		count = 3;
	} else if (a<99999) {
		count = 4;
	}
}
screensize()

/* конфигурация */
let width = 203;

let list = document.querySelector('.slayd-tovarov .slayd');
let listElems = document.querySelectorAll('.qlavniy-tovar');
let position = 0; // положение ленты прокрутки
document.querySelector('.p-slayder-tovarov').onclick = function() {
	// сдвиг влево
	position += width * count;
	// последнее передвижение влево может быть не на 3, а на 2 или 1 элемент
	position = Math.min(position, 0)
	list.style.marginLeft = position + 'px';
};
document.querySelector('.v-slayder-tovarov').onclick = function() {
	// сдвиг вправо
	position -= width * count;
	// последнее передвижение вправо может быть не на 3, а на 2 или 1 элемент
	position = Math.max(position, -width * (listElems.length-3 - count));
	list.style.marginLeft = position + 'px';
};































function showleftbar() {
	let a = document.querySelector('.left-bar')
	a.classList.toggle('show-bar')
	let b = document.querySelector('.mobile-petviy-stupen  .katalog')
	let c = document.querySelector('.close-bar')
	if (b.style.display === 'block') {
		b.style.display = 'none'
		c.style.display = 'block'
	} else {
		b.style.display = 'block'
		c.style.display = 'none'
	}
}


// var b = 0
// function moveqlavniytovarright() {
// 	let a = document.querySelectorAll('.qlavniy-tovar')
// 	let c = document.querySelector('.slayd')
//
// 	b -= 203
// 	c.style.left = `${b}px`
// 	console.log(b)
// }
//
// function moveqlavniytovarleft() {
// 	let a = document.querySelectorAll('.qlavniy-tovar')
// 	let c = document.querySelector('.slayd')
//
// 	b += 203
// 	c.style.left = `${b}px`
// 	console.log(b)
// }
//



function showpoiskovik() {
	let a = document.querySelector('.mobile-poiskovik')
	a.classList.toggle('show-poisk')
}

function mobileshowkatalog() {
	let a = document.querySelector('.mobile-list-katalog-tovarov')
	let c = document.querySelector('.mobile-list-katalog-tovarov ul')
	let b =document.querySelectorAll('.praviy-katalog')
	a.classList.toggle('showmlk')
	if ('showmlk' === a.className.split(' ')[1]) {
		for(let i = 0; i<b.length; i++) {
			let pkatalog = b[i]
			pkatalog.style.right = '-100%'
		}
		c.style.left = '0'

	}

}

function showpraviykatalog(i) {
	let a = document.querySelector(".mobile-list-katalog-tovarov ul")
	let b = document.querySelector(`.${i}`)
	a.style.left = '-100%'
	b.style.right = '3.8vw'
}

function backtokatalog(i) {
	let a = document.querySelector(".mobile-list-katalog-tovarov ul")
	let b = document.querySelector(`.${i}`)
	b.style.right = '-100%'
	a.style.left = '0'
}

const perexodi = document.querySelector('.perexodi-iz-mainpg')
function showperexodi() {
	alert(5)
	perexodi.style.display = 'flex'
}








// function moveqlavniytovarright() {
// 	let slayd = document.querySelector('.slayd')
// 	let a = getComputedStyle(slayd).width.split('px')
// 	a = a.join('')
// 	console.log(a)
// 	let b = document.querySelectorAll('.qlavniy-tovar').length
// 	console.log(a/b)
// }


