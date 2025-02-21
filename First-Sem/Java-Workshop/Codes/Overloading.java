class Gabrial{
    public void Player(int Health, String code){        // Int and String Parameters
        System.out.println("NPC RUN's");
    }
    public void Player(int i, int d, String Name){      // Int, Int and String Parameters
        System.out.println("Player Run's");
    }
    public void Player(double i, double  j, String Name){      // Double, Double and String Parameters
        System.out.println("Boss NPC Run's");
    }

    public static void main(String[] args) {
        Gabrial n = new Gabrial();
        n.Player(100, "NPC0384");
        n.Player(500,  6362, "XxAlonexX");
        n.Player(100, 0.52, "Again_NPC");
    }
}
