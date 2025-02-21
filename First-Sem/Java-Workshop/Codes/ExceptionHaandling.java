 public class ExceptionHaandling {

    private boolean isLocked;
    private String contents;

    public ExceptionHaandling(boolean isLocked, String contents) {
        this.isLocked = isLocked;
        this.contents = contents;
    }

    public void open() {
        try {
            if (isLocked) {
                throw new LockedChestException("The chest is locked! Find the key.");
            }
            System.out.println("You opened the chest and found: " + contents);
        } catch (LockedChestException e) {
            System.out.println(e.getMessage()); // Print the error message
            // ... potentially handle the exception (e.g., search for the key)
        }
    }
}

class LockedChestException extends Exception {
    public LockedChestException(String message) {
        super(message);
    }
}
