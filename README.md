# Beta What's Next? gramplet
 candidate for new default set of Dashboard gramplets
 
The 5.2.0 version of Gramps could include a [What's Next?](https://gramps-project.org/wiki/index.php/Gramps_5.1_Wiki_Manual_-_Gramplets#What.27s_Next) gramplet in the Dashboard category view by default.
![image](https://github.com/emyoulation/_BetaDashboards/assets/69127217/50e4fb0f-ef88-4c98-aafe-a8730ef259eb)


To date, the default Dashboard gramples have been too generic and are only useful for the first few sessions of use.
![image](https://user-images.githubusercontent.com/69127217/199575080-f32b024b-30d1-4327-a60b-8b9190660439.png)



A better set might be revisions of the "What's Next?", "To Do" and a more adaptive "Welcome to Gramps!"
![image](https://user-images.githubusercontent.com/69127217/199577268-d7f33faf-f564-4326-be9d-4bc3daa4da32.png)

The **Welcome to Gramps!** has had significant text changes and padding added to make look more finished. But the process showed that a hard-coded text layout interferes with writing good content.  This Gramplet should be displaying a README.md file or Note that has provision for multiple languages.

The **To Do** Gramplet is mostly about having a communication channel from the Tree. It is unclear how this Gramplet determine which To Do note to display. So I duplicated the content of the one selected into a new note and replaced it in the Referenceing objects. Then highjacked the original note so that it describes the purpose of the Tree.

The **What's Next?** has the most important changes. Layered in at the front are leading prompts for typical choke points for first time users: no tree loaded, no people data in the tree, no Active Person & no Home Person. The default scope for the Gramplet is narrowed too. There is less latency because it only examines out 1 or 2 generations from the Home Person instead of at ALL their Ancestors.
