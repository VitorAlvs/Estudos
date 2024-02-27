let listadeCarros = [
    {
        "nome": "Carro 1",
        "img": "img/Carro (1).jpg ",
        "descricao": "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Nemo, consectetur totam. Corporis rem temporibus, facilis, quasi accusamus esse tenetur odit sit dolorum aspernatur vitae dignissimos deserunt iusto officiis dolor? Minima."
    },
    {
        "nome": "Carro 2",
        "img": "img/Carro (2).jpg",
        "descricao": "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Nemo, consectetur totam. Corporis rem temporibus, facilis, quasi accusamus esse tenetur odit sit dolorum aspernatur vitae dignissimos deserunt iusto officiis dolor? Minima."
    },
    {
        "nome": "Carro 3",
        "img": "img/Carro (3).jpg",
        "descricao": "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Nemo, consectetur totam. Corporis rem temporibus, facilis, quasi accusamus esse tenetur odit sit dolorum aspernatur vitae dignissimos deserunt iusto officiis dolor? Minima."
    },
    {
        "nome": "Carro 4",
        "img": "img/Carro (4).jpg",
        "descricao": "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Nemo, consectetur totam. Corporis rem temporibus, facilis, quasi accusamus esse tenetur odit sit dolorum aspernatur vitae dignissimos deserunt iusto officiis dolor? Minima."
    },
    {
        "nome": "Carro 5",
        "img": "img/Carro (5).jpg",
        "descricao": "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Nemo, consectetur totam. Corporis rem temporibus, facilis, quasi accusamus esse tenetur odit sit dolorum aspernatur vitae dignissimos deserunt iusto officiis dolor? Minima."
    },
    {
        "nome": "Carro 6",
        "img": "img/Carro (6).jpg",
        "descricao": "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Nemo, consectetur totam. Corporis rem temporibus, facilis, quasi accusamus esse tenetur odit sit dolorum aspernatur vitae dignissimos deserunt iusto officiis dolor? Minima."
    }
]

listadeCarros.map((carro, posicao)=>{
        let cardCarro = document.getElementById("cards");
        cardCarro.innerHTML += `
        <div class="col-md-4">
            <div class="card m-2">
                <img src="${carro.img}" class="card-img-top" alt="...">
                <div class="card-body">
                    <h5 class="card-title">${carro.nome}</h5>
                    <a href="#" class="btn btn-secondary" onclick="zoomImg('${posicao}')"><i class="bi bi-zoom-in "></i></a>

                </div>
            </div>
        </div>`
    }
)

function zoomImg(posicao){
    let carrosele = listadeCarros[posicao];
    document.getElementById("nomeCarro").innerHTML = carrosele.nome;
    document.getElementById("descricao").innerHTML = carrosele.descricao;
    document.getElementById("imgModal").src = carrosele.img;

    new bootstrap.Modal('#zoomimg').show();
}

function alterarTema(){
    let tema = document.querySelector("html").getAttribute("data-bs-theme");
    if(tema === "dark"){
        document.querySelector("html").setAttribute("data-bs-theme", "light");
        document.querySelector("#alterarTema").innerHTML = `<i class="bi bi-moon-fill"></i>`;
    } else{
        document.querySelector("html").setAttribute("data-bs-theme", "dark");
        document.querySelector("#alterarTema").innerHTML = `<i class="bi bi-brightness-high-fill"></i>`
    }
}