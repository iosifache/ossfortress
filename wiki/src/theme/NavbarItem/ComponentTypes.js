import DefaultNavbarItem from '@theme/NavbarItem/DefaultNavbarItem';
import DocNavbarItem from '@theme/NavbarItem/DocNavbarItem';
import DocSidebarNavbarItem from '@theme/NavbarItem/DocSidebarNavbarItem';
import DocsVersionDropdownNavbarItem from '@theme/NavbarItem/DocsVersionDropdownNavbarItem';
import DocsVersionNavbarItem from '@theme/NavbarItem/DocsVersionNavbarItem';
import DropdownNavbarItem from '@theme/NavbarItem/DropdownNavbarItem';
import HtmlNavbarItem from '@theme/NavbarItem/HtmlNavbarItem';
import LocaleDropdownNavbarItem from '@theme/NavbarItem/LocaleDropdownNavbarItem';
import SearchNavbarItem from '@theme/NavbarItem/SearchNavbarItem';
import Cookies from 'js-cookie';
import React, { useState } from 'react';

function But() {
  const [mode, setMode] = useState(Cookies.get("wikiMode"));

  const toggleMode = () => {
    const wikiModeCookie = Cookies.get("wikiMode")
    const newWikiMode = wikiModeCookie == "advanced" ? "beginner" : "advanced"

    setMode(newWikiMode)

    Cookies.set("wikiMode", newWikiMode)

    window.location.reload()
  }

  var wikiModeCookie = Cookies.get("wikiMode")
  var wikiMode = wikiModeCookie ? wikiModeCookie : "beginner"
  var alternativeMode = wikiMode == "beginner" ? "advanced" : "beginner"

  return (
    <div className='navbar__item navbar__link mode-button' onClick={toggleMode}>
      Switch to the {alternativeMode} mode
    </div>
  );
}

const ComponentTypes = {
  default: DefaultNavbarItem,
  localeDropdown: LocaleDropdownNavbarItem,
  search: SearchNavbarItem,
  dropdown: DropdownNavbarItem,
  html: HtmlNavbarItem,
  doc: DocNavbarItem,
  docSidebar: DocSidebarNavbarItem,
  docsVersion: DocsVersionNavbarItem,
  docsVersionDropdown: DocsVersionDropdownNavbarItem,
  "custom-mode-switcher": But
};
export default ComponentTypes;
