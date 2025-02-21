class Important_Q3{

// Method overloading case1 "Automatic promotion";   // Working
    /*
void show(int a){
    System.out.println("Int");
}
void show(String a){
    System.out.println("String");
}
// void show(char a){
//     System.out.println("Character");
// }
public static void main(String[] args) {
    Important_Q3 x = new Important_Q3();
    x.show(8);
    x.show("a");
    x.show('a');
}
    */


// One type is promoted to implicitly if no mathcing data is found as bellow diagram

// -------------------------------------------------------------------------------------------------------------------

// Method overloading case2 :
// While resolving overloaded methods complete will always give diffrent for the child type argument
// void show(String Buffer a){
//     System.out.println("Object Method");
// }
// void show(String a){
//     System.out.println("String");
// }
// // void show(char a){
// //     System.out.println("Character");
// // }
// public static void main(String[] args) {
//     Important_Q3 x = new Important_Q3();
//     x.show(8);
//     x.show("a");
//     x.show('a');
// 

// -------------------------------------------------------------------------------------------------------------------
// Case 3  // Working
// public class CharacterBuilder {

//     public static void main(String[] args) {
//         StringBuffer characterDescription = new StringBuffer("A mysterious adventurer"); 

//         // Simulate game events that add to the character's description
//         exploreAncientRuins(characterDescription);
//         defeatPowerfulMonster(characterDescription);
//         discoverHiddenTreasure(characterDescription);

//         // Print the final character description
//         System.out.println("Character Description:\n" + characterDescription.toString());
//     }

//     // Simulate exploring ancient ruins
//     private static void exploreAncientRuins(StringBuffer description) {
//         description.append(" who has delved into forgotten depths, ");
//     }

//     // Simulate defeating a powerful monster
//     private static void defeatPowerfulMonster(StringBuffer description) {
//         description.append(" and vanquished fearsome beasts, ");
//     }

//     // Simulate discovering hidden treasure
//     private static void discoverHiddenTreasure(StringBuffer description) {
//         description.append(" now seeks the legendary treasure of the Lost City.");
//     }
// }

// -------------------------------------------------------------------------------------------------------------------

// Case 4 
// void show(int a, float b){
//     System.out.println("Int and Float");
// }
// void show(float a, int b){
//     System.out.println("Float and Int");
// }
// public static void main(String[] args) {
//     Important_Q3 x = new Important_Q3();
//     x.show(8, (float) 0.2);
//     x.show((float) 0.5, 11);
// }

// -------------------------------------------------------------------------------------------------------------------

// Case 5  // Working
// void show(int a){
//     System.out.println("Int and Float");
// }
// void show(int...a ){             // Allows use to pass 0 or more arguments;
//     System.out.println("Float and Int");        
// }
// public static void main(String[] args) {
//     Important_Q3 x = new Important_Q3();
//     x.show(8);
//     x.show(10,20,30);
// }
}