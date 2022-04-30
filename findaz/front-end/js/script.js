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


/* конфигурация */
let width = 203;
let count = 1;
let position = 0;


let btnMoveLefts = document.querySelectorAll('.v-slayder-tovarov')
btnMoveLefts.forEach(btnMoveLeft => btnMoveLeft.addEventListener("click", (event)=>{
	let a = event.target
	let list = a.closest('.ryad-tovarov').querySelector('.slayd')
	let listElems = list.querySelectorAll('.qlavniy-tovar')
	position = list.style.marginLeft.split('px').join('')
	position -= width * count;
	position = Math.max(position, -width * (listElems.length-4 - count));
	list.style.marginLeft = position + 'px';
}))

let btnMoveRights = document.querySelectorAll('.p-slayder-tovarov')
btnMoveRights.forEach(btnMoveRight => btnMoveRight.addEventListener("click", (event)=>{
	let a = event.target
	let list = a.closest('.ryad-tovarov').querySelector('.slayd')
	position = list.style.marginLeft.split('px').join('')
	position =+position+ width * count;
	position = Math.min(position, 0)
	list.style.marginLeft = position +'px';

}))


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


const secondForm = document.querySelector('.main-of-salers .second')
const firstForm = document.querySelector('.main-of-salers .first')

console.log(firstForm, secondForm)
function nextForm() {
	let name = document.querySelector('.main-of-salers .name input'),
		surname = document.querySelector('.main-of-salers .surname input'),
		dataOfBirth = document.querySelector('.main-of-salers .data-of-birth'),
		email = document.querySelector('.main-of-salers .email'),
		mobilNumber = document.querySelector('.main-of-salers .mobil-numb'),
		occumation = document.querySelector('.main-of-salers .occupation'),
		address = document.querySelector('.main-of-salers .address')
	if(name.value === '' && surname.value ==='' && dataOfBirth.value ==='' && email.value ==='' && mobilNumber.value ==='' && occumation.value ==='' && address.value ==='') {
		name.style.border = '2px red solid'
	} else {
		firstForm.style.left = '-100%'
		secondForm.style.right = '0'
	}
	console.log(name.value  === '', surname.value === '')


}
function backForm() {
	firstForm.style.left = '0'
	secondForm.style.right = '-100%'
}





















function  usloviye() {
	let UsloviyeInput = document.querySelector('.checkbox-uslov input[type="checkbox"]')
	if (UsloviyeInput.checked === true) {
		document.querySelector('.zareq-button').removeAttribute('disabled' )
	} else {
		document.querySelector('.zareq-button').setAttribute('disabled', true)
	}
}

const tovarLeftPhotos = document.querySelectorAll('.tovar-photo-change')
tovarLeftPhotos.forEach(tovarLeftPhoto => tovarLeftPhoto.addEventListener('click', (event) => {
	let a = event.target
	let imgSrc = a.src
	let mainPhoto = a.closest('.tovar-photos').querySelector('.main-photo img')
	mainPhoto.style.opacity = '0'
	mainPhoto.style.transition = '0.4s'
	setTimeout(()=>{
		mainPhoto.src = imgSrc
		mainPhoto.style.opacity = '1'
	},400)

}))



function showAddBar() {
	let leftAddBar = document.querySelector('.add-left-bar')
	let divTexts = document.querySelectorAll('.add-left-bar>ul>li>.left>div')
	let leftIconOfAngels = document.querySelectorAll('.add-left-bar>ul>li>i')
	divTexts.forEach(divText => {
		if (divText.style.display !== 'none') {
			divText.style.display = 'none';
			divText.style.opacity = '0';
		} else {
			divText.style.display = 'block';
			divText.style.opacity = '1';
		}
	})
	leftIconOfAngels.forEach(leftIconOfAngel => {
		if (leftIconOfAngel.style.display !== 'none') {
			leftIconOfAngel.style.display = 'none';
			leftAddBar.style.width = '60px';
		} else {
			leftIconOfAngel.style.display = 'block';
			leftIconOfAngel.style.opacity = '1';
			leftAddBar.style.width = '213px';
		}
	})
}











// window.addEventListener('click', (event)=>{
// 	console.log(event.view.innerWidth)
// 	if (event.view.innerWidth <=700) {
// 		showAddBar()
// 	}
// 	console.log(event.view.innerWidth)
// })
//
