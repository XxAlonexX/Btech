class Pokemon {
    String type;

    public Pokemon(String type) {
        this.type = type;
    }
}

class Pikachu extends Pokemon {
    public Pikachu() {
        super("Electric"); 
    }

    void thunderbolt() {
        System.out.println("Pikachu used Thunderbolt!");
    }
}

class Raichu extends Pikachu {
    void thunder() {
        System.out.println("Raichu used Thunder!");
    }
}
class MultilevelInheritance{
    public static void main(String[] args) {
        Raichu Kid = new Raichu();
        Kid.thunderbolt();
    }
}