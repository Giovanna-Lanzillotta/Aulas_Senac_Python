class Pessoa{
    constructor(nome, email){
        this.nome = nome;
        this.email = email;
    }
}

class Aluno extends Pessoa{
    constructor(nome,email,matricula, escolaridade){
        super(nome, email)
        this.matricula = matricula;
        this.escolaridade = escolaridade;
    }

}

class Professor extends Pessoa{
    constructor(nome,email,titulacao,salario){
        super(nome,email)
        this.titulacao = titulacao;
        this.salario = salario;
    }
}

//var pessoa1 = new Pessoa("Vanessa" , "van@gmail.com")
//console.log(pessoa1)
var aluno1 = new Aluno("Ana","ana@gmail.com",123,"SC")
console.log(aluno1)
var professor1 = new Professor("Vanessa","vanessa@gmail.com","doutorado",40000)
console.log(professor1)