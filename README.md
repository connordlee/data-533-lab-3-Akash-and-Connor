# data-533-lab-2-Akash-and-Connor
Data 533 Lab 2 for Akash Dhatavkar and Connor Lee

## Package Description

The package will be used to information about people involved with a sports club, the package will be called club. The structure of the club is as follows
* Package: club
  * Subpackage: members:
    * Module: member:
      Class: member:
       * Attributes:
         * Name
         * Nationality
         * Salary (Private Attribute)
         * Years with Club
       * Functions: 
         * Initialize Member
         * Remove Member
         * Update Nationality
         * Set Salary
         * Get Salary
    * Module: membertype:
      * Class: player (Inherits Member Properties)
        * Attributes:
          * Position
        * Functions:
          * Initialize Player: will call Initialize Member
          * Update Position
      * Class: staff (Inherits Member Properties)
        * Attributes:
          * Title
        * Functions:
          * Initialize Staff: will call Initialize Member
          * Update Title
  * Subpackage: 
   * Module: fan:
    * Class: fan
     * Attributes:
       * Name
       * Favourite Player
       * Purchased Merchandise
       * Current City
     * Functions:
       * Initialize Fan
       * Get and set Favourite Player
       * Get and set Purchased Merchandise Info (Count)
       * Get and set Current city 
    * Module: fantype (Inherits Fan Properties)
     * Class: domestic
      * Attributes:
        * hasSeasonTickets
        * years since fan
      * Functions:
        * Initialize Domestic Fan
        * updateTicketStatus
     * Class: International (Inherits Fan Properties)
       * Attributes:
         * Country
         * Views Matches
       * Functions:
         * Initialize Domestic Fan
         * update view matches
