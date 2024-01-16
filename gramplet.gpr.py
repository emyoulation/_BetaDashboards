# encoding:utf-8
#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2009 Benny Malengier
# Copyright (C) 2011 Nick Hall
# Copyright (C) 2011 Tim G L Lyons
# Copyright (C) 2024 Brian McCullough
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
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

# ------------------------------------------------------------------------
#
# Gramps modules
#
# ------------------------------------------------------------------------

# from gramps.gen.plug._pluginreg import register, STABLE, BETA, EXPERIMENTAL, UNSTABLE, DEVELOPER, GRAMPLET
# from gramps.gen.const import GRAMPS_LOCALE as glocale
# _ = glocale.translation.sgettext

from gramps.version import major_version
MODULE_VERSION = major_version


# ------------------------------------------------------------------------
#
# Register Gramplet
#
# ------------------------------------------------------------------------


register(GRAMPLET,
         id="Beta Person To Do",
         name=_("Beta Person To Do"),
         description=_("Beta Gramplet showing the To Do notes for a person"),
         gramps_target_version=MODULE_VERSION,
         status=STABLE,
         fname="Betatodo.py",
         height=200,
         gramplet='BetaPersonToDo',
         gramplet_title=_("β Person To Do"),
         version="0.1.1",
         help_url="Gramps_5.2_Wiki_Manual_-_Gramplets#Person_To_Do",
         navtypes=["Person"],
         )

register(GRAMPLET,
         id="Beta To Do",
         name=_("Beta To Do"),
         description=_("Beta Gramplet for displaying a To Do list"),
         status=STABLE,
         fname="Betatodogramplet.py",
         height=300,
         expand=True,
         gramplet='BetaToDoGramplet',
         gramplet_title=_("β Dashboard To Do"),
         version="0.1.1",
         help_url="Gramps_5.2_Wiki_Manual_-_Gramplets#To_Do",
         gramps_target_version=MODULE_VERSION,
         navtypes=["Dashboard"],
         )

register(GRAMPLET,
         id="Beta Welcome",
         name=_("Beta Welcome"),
         description=_("Beta Gramplet showing a welcome message"),
         status=STABLE,
         fname="Betawelcomegramplet.py",
         height=300,
         expand=True,
         gramplet='BetaWelcomeGramplet',
         gramplet_title=_("β Welcome to Gramps!"),
         version="0.1.1",
         help_url="Gramps_5.2_Wiki_Manual_-_Gramplets#Welcome",
         gramps_target_version=MODULE_VERSION,
         )

register(GRAMPLET,
         id="Beta What's Next",
         name=_("Beta What's Next"),
         description=_("Beta Gramplet suggesting items to research"),
         status=STABLE,
         fname="Betawhatsnext.py",
         height=230,
         expand=True,
         gramplet='BetaWhatNextGramplet',
         gramplet_title=_("β What's Next?"),
         version="0.1.3",
         help_url="https://github.com/emyoulation/_BetaDashboards/blob/5.2/README.md",
         gramps_target_version=MODULE_VERSION,
         )
