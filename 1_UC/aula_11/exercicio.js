/*1.crie uma classe animal com os atributos: nome, data de nascimento, origem
crie duas classes: cachorro e gato contendo os atributos: cor, peso
crie um método para a classe  Animal: método emitirSom()
faça com que as classes cachorro e gato herdem de Animal
nas classes cachorro e gato,implemente este método e faça com que o som emitido pelo cachorro seja diferente 
do som emitido pelo gato*/
class Animal{
    constructor(nome,dataNascimento,origem){
        this.nome = nome;
        this.dataNascimento = dataNascimento;
        this.origem = origem;
       }
       emitirSom(){}
    }

class Cachorro extends Animal{
    constructor(nome,dataNascimento,origem,cor,peso){
        super(nome,dataNascimento,origem)
        this.cor = cor;
        this.peso = peso;
        }
        emitirSom(){
            console.log("AU AU")
           }
    }

class Gato extends Animal{
    constructor(nome,dataNascimento,origem,cor,peso){
        super(nome,dataNascimento,origem)
        this.cor = cor;
        this.peso = peso;
    }
    emitirSom(){
        console.log("MIAU")
       }
}

var cachorro1 = new Cachorro("Toby","12/12/12","srd","caramelo","10kg")
console.log(cachorro1)
cachorro1.emitirSom()
var gato1 = new Gato("Thor","10/10/10","srd","cinza","6kg")
console.log(gato1)
gato1.emitirSom()