# _Beta
 candidates for new default set of Dashboard gramplets
The 5.1.5-1 version of Gramps default to include a [Welcome to Gramps!](https://gramps-project.org/wiki/index.php/Gramps_5.1_Wiki_Manual_-_Gramplets#Welcome) gramplet and the [Top Surnames](https://gramps-project.org/wiki/index.php/Gramps_5.1_Wiki_Manual_-_Gramplets#Top_Surnames) gramplet in the Dashboard category view.
![image](https://user-images.githubusercontent.com/69127217/199575080-f32b024b-30d1-4327-a60b-8b9190660439.png)

The Welcome! is being updated but the proposed new instructions are still too generic and are only useful for the first few sessions of use.

A better set might be revisions of the "What's Next?", "To Do" and a more adaptive "Welcome to Gramps!"
![image](https://user-images.githubusercontent.com/69127217/199577268-d7f33faf-f564-4326-be9d-4bc3daa4da32.png)

The **Welcome to Gramps!** has had significant text changes and padding added to make lookore finished. But the process showed that a hard-coded text layout interferes with writing good content.  This Gramplet should be displaying a README.md file or Note that has provision for multiple languages.

The **To Do** Gramplet is mostly about having a communication channel from the Tree. It is unclear how this Gramplet determine which To Do note to display. So I duplicated the content of the one selected into a new note and replaced it in the Referenceing objects. Then highjacked the original note so that it describes the purpose of the Tree.

The **What's Next?** has the most important changes. Layered in at the front are leading prompts for typical choke points for first time users: no tree loaded, no people data in the tree, no Active Person & no Home Person. The default scope for the Gramplet is narrowed too. The is less latency because it only examines out 1 or 2 generations from the Home Person instead of at ALL their Ancestors.
