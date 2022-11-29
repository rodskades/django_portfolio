const skills = document.querySelectorAll('.skills-item');
const descricao0 = document.querySelector('.descricao0');
const descricao1 = document.querySelector('.descricao1');
const descricao2 = document.querySelector('.descricao2');
const descricao3 = document.querySelector('.descricao3');
const descricao4 = document.querySelector('.descricao4');
const descricao5 = document.querySelector('.descricao5');
const descricao6 = document.querySelector('.descricao6');
const descricao7 = document.querySelector('.descricao7');
const descricao8 = document.querySelector('.descricao8');
const aboutskills = [
                    gettext('<p>Linguagem de programação open-source.</p>'),
                    gettext('<p>Framework para desenvolvimento web utilizando Python.</p>'),
                    gettext('<p>Banco de dados SQL, sendo atualmente um dos mais populares da Oracle Corporation.</p>'),
                    gettext('<p>Banco de dados SQL de open-source.</p>'),
                    gettext('<p>Biblioteca escrita em C que implementa um banco de dados SQL.</p>'),
                    gettext('<p>Banco de dados NoSQL de open-source que utiliza documentos semelhantes a JSON.</p>'),
                    gettext('<p>Armazenamento de estrutura de dados em memória, utilizado como um banco de dados NoSQL.</p>'),
                    gettext('<p>Banco de dados NoSQL de open-source conhecido pela facilidade de uso.</p>'),
                    gettext('<p>Sistema de controle de versões distribuído, usado principalmente no desenvolvimento de software.</p>')
]

skills.forEach(  (elemento, index) => {
    let index1 = index;
    if (index1 == 0) {
      elemento.addEventListener('mouseover', (evento) => {
          descricao0.innerHTML = `<p>${aboutskills[index1]} </p>` ;
      } )
      elemento.addEventListener('mouseout', (evento, elemento,) => {
          descricao0.innerHTML = '';
      } )
    }
    if (index1 == 1) {
      elemento.addEventListener('mouseover', (evento) => {
          descricao1.innerHTML = `<p>${aboutskills[index1]} </p>` ;
      } )
      elemento.addEventListener('mouseout', (evento, elemento,) => {
          descricao1.innerHTML = '';
      } )
    }
    if (index1 == 2) {
      elemento.addEventListener('mouseover', (evento) => {
          descricao2.innerHTML = `<p>${aboutskills[index1]} </p>` ;
      } )
      elemento.addEventListener('mouseout', (evento, elemento,) => {
          descricao2.innerHTML = '';
      } )
    }
    if (index1 == 3) {
      elemento.addEventListener('mouseover', (evento) => {
          descricao3.innerHTML = `<p>${aboutskills[index1]} </p>` ;
      } )
      elemento.addEventListener('mouseout', (evento, elemento,) => {
          descricao3.innerHTML = '';
      } )
    }
    if (index1 == 4) {
      elemento.addEventListener('mouseover', (evento) => {
          descricao4.innerHTML = `<p>${aboutskills[index1]} </p>` ;
      } )
      elemento.addEventListener('mouseout', (evento, elemento,) => {
          descricao4.innerHTML = '';
      } )
    }
    if (index1 == 5) {
      elemento.addEventListener('mouseover', (evento) => {
          descricao5.innerHTML = `<p>${aboutskills[index1]} </p>` ;
      } )
      elemento.addEventListener('mouseout', (evento, elemento,) => {
          descricao5.innerHTML = '';
      } )
    }
    if (index1 == 6) {
      elemento.addEventListener('mouseover', (evento) => {
          descricao6.innerHTML = `<p>${aboutskills[index1]} </p>` ;
      } )
      elemento.addEventListener('mouseout', (evento, elemento,) => {
          descricao6.innerHTML = '';
      } )
    }
    if (index1 == 7) {
      elemento.addEventListener('mouseover', (evento) => {
          descricao7.innerHTML = `<p>${aboutskills[index1]} </p>` ;
      } )
      elemento.addEventListener('mouseout', (evento, elemento,) => {
          descricao7.innerHTML = '';
      } )
    }
    if (index1 == 8) {
      elemento.addEventListener('mouseover', (evento) => {
          descricao8.innerHTML = `<p>${aboutskills[index1]} </p>` ;
      } )
      elemento.addEventListener('mouseout', (evento, elemento,) => {
          descricao8.innerHTML = '';
      } )
    }
} );
