package solution;


/**
 * SuperUser
 * 
 * This class represents a super user.
 * A super user can create a league.
 * A super user is a user.
 * 
 * @param name The name of the super user.
 */

public class SuperUser extends User 
{

    public SuperUser(String name) {
        super(name);
    }

    /**
     * Create a league.
     */

    public void createLeague() 
    {
        League league = new League(this);
        join(league);
    }

}