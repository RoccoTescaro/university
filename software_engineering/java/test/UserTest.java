package test;
import org.junit.Test;

import solution.User;

public class UserTest
{

    @Test
    public void testUser()
    {
        System.out.println(" UserTest.testUser()");

        User user1 = new User("peter");
        User user2 = new User("fireship");

        assert user1.getId() != user2.getId();
    }

    @Test
    public void testUser2()
    {
        System.out.println(" UserTest.testUser2()");

        User user1 = new User("peter");
        User user2 = new User("fireship");

        assert user1.getName().equals("peter");
    }

}