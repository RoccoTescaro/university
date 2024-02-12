package test;
import org.junit.Test;

import solution.SuperUser;
import solution.User;
import solution.League;

public class LeagueTest
{

    @Test
    public void testLeague()
    {
        System.out.println(" LeagueTest.testLeague()");

        SuperUser user1 = new SuperUser("peter");
        User user2 = new User("fireship");

        League league = new League(user1);

        assert league.getOwner().getName().equals("peter");
    }

    @Test
    public void testLeague2()
    {
        System.out.println(" LeagueTest.testLeague2()");

        SuperUser user1 = new SuperUser("peter");
        User user2 = new User("fireship");

        League league = new League(user1);

        league.add(user2);

        assert league.getMembers().size() == 1;
        //failing assert
        //assert user1.getName().equals("fireship");
    }

}