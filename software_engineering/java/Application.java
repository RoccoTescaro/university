
public class Application
{

    public static void main(String[] args)
    {
        User user = new User("John", "password");
        System.out.println(user.getName());
        System.out.println(user.getPassword());
    }

}