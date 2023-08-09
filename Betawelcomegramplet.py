# "Welcome to Gramps!" Gramplet, a modular plugin for Gramps 
# (Gramps - the genealogy software suite built on GTK+/GNOME) 
#
# Copyright (C) 2007-2009  Douglas S. Blank <doug.blank@gmail.com>
# Copyright (C) 2020       Dave Scheipers
# Copyright (C) 2022       Brian McCullough
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of version 2 of the GNU General Public License as 
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# For the Gramps-Project volunteer community's contact information, visit:
# https://gramps-project.org/wiki/index.php/Contact

# ------------------------------------------------------------------------
#
# Gtk modules
#
# ------------------------------------------------------------------------
from gi.repository import Gtk

# ------------------------------------------------------------------------
#
# Gramps modules
#
# ------------------------------------------------------------------------
from gramps.gen.const import URL_WIKISTRING, URL_MANUAL_PAGE, URL_HOMEPAGE
from gramps.gen.const import WIKI_EXTRAPLUGINS
from gramps.gui.display import EXTENSION
from gramps.gen.plug import Gramplet
from gramps.gui.widgets.styledtexteditor import StyledTextEditor
from gramps.gen.lib import StyledText, StyledTextTag, StyledTextTagType
from gramps.gen.const import GRAMPS_LOCALE as glocale
_ = glocale.translation.sgettext

# ------------------------------------------------------------------------
#
# Functions
#
# ------------------------------------------------------------------------


def st(text):
    """ Return text as styled text
    """
    return StyledText(text)


def boldst(text):
    """ Return text as bold styled text
    """
    tags = [StyledTextTag(StyledTextTagType.BOLD, True, [(0, len(text))])]
    return StyledText(text, tags)


def linkst(text, url):
    """ Return text as link styled text
    """
    tags = [StyledTextTag(StyledTextTagType.LINK, url, [(0, len(text))])]
    return StyledText('  • ') + StyledText(text, tags)


def wiki(page, manual=False):
    """
    Build a link to a wiki page.
    """
    url = URL_WIKISTRING
    if manual:
        url += URL_MANUAL_PAGE
    url += page + EXTENSION
    return url

# ------------------------------------------------------------------------
#
# Gramplet class
#
# ------------------------------------------------------------------------


class BetaWelcomeGramplet(Gramplet):
    """
    Displays a welcome note to the user.
    """
    def init(self):
        self.gui.WIDGET = self.build_gui()
        self.gui.get_container_widget().remove(self.gui.textview)
        self.gui.get_container_widget().add(self.gui.WIDGET)
        self.gui.WIDGET.show()

    def build_gui(self):
        """
        Build the GUI interface.
        """
        top = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        scrolledwindow = Gtk.ScrolledWindow()
        scrolledwindow.set_policy(Gtk.PolicyType.AUTOMATIC,
                                  Gtk.PolicyType.AUTOMATIC)
        self.texteditor = StyledTextEditor()
        self.texteditor.set_editable(False)
        self.texteditor.set_wrap_mode(Gtk.WrapMode.WORD)
        self.texteditor.set_left_margin(6)
        self.texteditor.set_right_margin(6)
        scrolledwindow.add(self.texteditor)

        self.display_text()

        top.pack_start(scrolledwindow, True, True, 0)
        top.show_all()
        return top

    def display_text(self):
        """
        Display the welcome text.
        """
        welcome = boldst(_('Introduction')) + '\n\n'
        welcome += _(
            'Gramps is a software package designed for genealogical research. While similar to other genealogical programs, Gramps offers some unique and powerful features. Gramps does not enforce a particular genealogical "best practice" on researchers. There are often several ways to do any task... so Gramps tries to be flexible and conform to your style of research.\n\n')
        welcome += _(
             'Since Gramps is "Free and Open Source Software", you are invited to modify Gramps to more closely suit your purposes. We just ask that you share any improvements so they can inspire the entire community! Another aspect of an Open Source Software package, is that you are free to make copies and distribute it to anyone you wish.\n\n')
        welcome += linkst(_('Learn more about Gramps by visiting the Gramps Project website.'), URL_HOMEPAGE) + '\n\n'
        welcome += boldst(_('Who makes Gramps?')) + '\n\n' + _(
            'Gramps is created by genealogists for genealogists, organized in the Gramps Project.\n\n')
        welcome += _(
            'It is developed and maintained by a worldwide team of volunteers whose goal is to make Gramps powerful, yet easy to use. (You have a standing invitation to join as one of those volunteers!)\n\n')
        welcome += _(
            'There is an active community of user volunteers available on the mailing lists and Discourse forum to answer questions, share ideas and techniques.\n\n')
        welcome += linkst(_('Explore the Gramps online manual'),
                          wiki('', manual=True)) + '\n'
        welcome += linkst(_('Ask questions on the gramps-users mailing list'),
                          '%(gramps_home_url)scontact/' %
                          {'gramps_home_url': URL_HOMEPAGE}) + '\n'
        welcome += linkst(_('Share knowledge on the Gramps Discourse Forum'),
                          'https://gramps.discourse.group/') + '\n\n'
        welcome += boldst(_('Getting Started')) + '\n\n' + _(
            'The first time Gramps is started, most of the Views will be blank. There will be very few menu or toolbar options. Gramps needs a Tree with People before more menu and toolbar options appear.\n\n')
        welcome += _(
            'This is because options are offered on a contextual basis. (If an option does not apply to what is displayed or selected, that option is not actively displayed.) The basic context of a Family Tree is needed for any activity to happen. Family Trees are your "blank document" or "new project" workspaces.\n\n')
        welcome += _(
            'To create a new Family Tree (sometimes called a \'database\'), select "Family Trees" menu, pick the "Manage Family Trees..." option, press the "New" button, and name your Family Tree. Then click the "Load Family Tree" button to make the selected tree active and ready to accept genealogical research data.\n\n')
        welcome += _(
            'If you are just exploring, scroll down to bottom of this text and learn about importing the example Tree that is included with Gramps. Make any "beginner mistakes" there instead in your research. After a bit of exploring, you will be ready to begin entering your first family, or importing a genealogy file. For one strategy for filling in the Tree, please read the information at the links below.\n')
        welcome += linkst(_('Start with Genealogy and Gramps'), wiki('Start_with_Genealogy')) + '\n'
        welcome += linkst(_('Discourse forum list of Gramps tutorial videos'), 'https://gramps.discourse.group/t/tutorial-videos/126') + '\n\n'
        welcome += boldst(_('Enter your first Family')) + '\n\n'
        welcome += _('Switch to the "Relationships" view and, from the "Add" menu, select the "Family" to bring up the "Edit Family" window. Here you can click the [+] icon beside the "Father/partner1" or "Mother/partner2" to begin entering that person. Start with just the basic Name information for one person. (We\'ll come back to add Birth and Death data later.) Clicking the "OK" stores the record, creating your first Person. You can add an immediate relative in one of the other spots or Click the "OK" button to store that first family.\n\n')
        welcome += _('This establishes a starting point for your tree. With the context of this first person and family, all of the menu options and toolbar icon functions will have become available. Spend some time moving your mouse over the icons. As your cursor passes over an icon, a hint message will appear telling you the icon\'s function. The same hint system is useful for exploring any of the edit windows. Moving the mouse cursor over an item will tell you what that control will do.\n\n')
        welcome += _(
            'You can now expand families by adding parents, a spouse and children. Under the tabs of the lower section of the Edit windows, the [+] icon under the Events tab allows adding landmark life occasions (with dates and places) to People and Families. Under the other tabs, you can add Sources, Citations, Notes and other types of information to provide documentation for your entries.\n\n')
        welcome += _(
            'As you start using Gramps, you will find that information can be entered from all the various Views. There are multiple ways of doing most activities in Gramps. The flexibility allows you to choose which fits your work style.\n')
        welcome += linkst(_('Entering and editing data (a brief overview)'),
                          wiki('_-_Entering_and_editing_data:_brief',
                               manual=True)) + '\n\n'
        welcome += boldst(_('Importing a Family Tree')) + '\n\n' + _(
            'To import a Family Tree from another program, first create a GEDCOM (or other data exchange format) file from your previous program.\n\n')
        welcome += _(
            'Create a new, blank Gramps database (Tree) file as described in the "Getting Started" section above. Then use the "Import" option under the "Family Trees" menu to import the GEDCOM data.\n')
        welcome += linkst(_('Import from another genealogy program'),
                          wiki('Import_from_another_genealogy_program')) + '\n\n'
        welcome += boldst(_('Dashboard View')) + '\n\n' + _(
            'You are currently reading from the "Dashboard" view, where you can'
            ' add your own gramplets. You can also add gramplets to any view by'
            ' adding a sidebar and/or bottombar, and right-clicking to the'
            ' right of the tab.\n\n')
        welcome += _(
            'The Configure... option in the View menu (or clicking the icon in the toolbar) opens the "Gramplet Layout" tab. This allows you to subdivide the dashboard into more or fewer columns. You can also drag the Properties button to reposition the gramplet within this dashboard or click to detach the gramplet to float above Gramps or place on a second monitor.\n\n')
        welcome += _(
            'While the Dashboard view is about using Gramps more efficiently, the other view categories allow data entry and understanding of how your data interconnects.\n\n')
        welcome += _(
            'There are several Views in Gramps that display lists of the database components. "People", "Families", "Events", "Places", "Media", "Notes", "Citations", "Sources" and "Repositories".\n\n')
        welcome += _(
            'There are views that display how People and Families interrelate. Rather than tabular lists, the "Relationships” and "Charts" view diagram the connections.  And view modes like the Charts\' "Pedigree" and "Fan Chart" offer different diagrams of similar information.\n')	
        welcome += linkst(_('Gramps View Categories'), wiki('_-_Categories', manual=True)) + '\n\n'
        welcome += boldst(_('Addons and "Gramplets"')) + '\n\n' + _(
            'There many Addons that are available to assist you in data entry and visualizing your family tree. These addons provide reports, filter rules, View modes, "Gramplets", and more.\n\n')
        welcome += _(
            'Many of these addon tools are already distributed with the basic installation of Gramps. Many more are freely available to download and install.\n')
        welcome += linkst(_('List of Addons and "Gramplets"'),
                          wiki(WIKI_EXTRAPLUGINS)) + '\n\n'
        welcome += boldst(_('Example Database')) + '\n\n' + _(
            'Want to see Gramps in use? There is a demonstration database that was used to illustrate the documentation. You can create a blank tree and then import that Example database.\n\n')
        welcome += _(
            'Create a new Family Tree as described in the "Getting Started" section above. (A good name for that Family Tree would be “EXAMPLE”.)\n\n')
        welcome += _(
            'Import the example.gramps Gramps archive file. (The webpage below describes what is in that archive and the file location for the different Operation Systems that run the Gramps program. It also describes where the file is available on the web.\n')
        welcome += linkst(_('Example.gramps'),
                          wiki('Example.gramps')) + '\n'
        self.texteditor.set_text(welcome)

    def get_has_data(self, obj):
        """
        Return True if the gramplet has data, else return False.
        """
        return True
