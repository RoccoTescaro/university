
public class Application
{

    public static void main(String[] args)
    {
        User user1 = new User("peter");
        User user2 = new User("fireship");

        System.out.println(user1.getName() + " id: " + user1.getId());
        System.out.println(user2.getName() + " id: " + user2.getId());        
    }

}