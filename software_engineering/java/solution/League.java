package solution;

import java.util.HashSet;
import java.util.Set;

/**
 * League
 * 
 * This class represents a league.
 * A league has a single owner and a set of members.
 * The owner of a league is a SuperUser. 
 * The members of a league are Users.
 *
 * @param owner The owner of the league.
 */

public class League 
{
    private SuperUser owner;
    private Set<User> members = new HashSet<User>();

    public League(SuperUser owner)
    {
        this.owner = owner;
    }

    /**
     * Get the owner of the league.
     * 
     * @return The owner of the league.
     */

    public SuperUser getOwner()
    {
        return owner;
    }

    /**
     * Get the members of the league.
     * 
     * @return The members of the league.
     */

    public Set<User> getMembers()
    {
        return members;
    }

    /**
     * Add a member to the league.
     * 
     * @param user The user to add to the league.
     * @return itself for chaining.
     */

    public League add(User user)
    {
        user.join(this);
        members.add(user);

        return this;
    }

    /**
     * Remove a member from the league.
     * 
     * @param user The user to remove from the league.
     * @return itself for chaining.
     */

    public League remove(User user)
    {
        user.leave(this);
        members.remove(user);

        return this;
    }
}