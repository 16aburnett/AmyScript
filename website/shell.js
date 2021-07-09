/*
    AmyScript Documentation Website
    
    Author: Amy Burnett
    Created: June 9 2021

*/

//========================================================================
// Global Variables


//========================================================================
/**
 * generates the header of the page as a child of a given parent
 * @param {HTMLDivElement} parent the element to place the header within
 */

function loadHeader (parentId)
{
    var parent = document.getElementById (parentId);

    parent.innerHTML = "<h2>AmyScript Documentation</h2>";

}

//========================================================================

function loadSidebar (parentID, currentPage)
{

    var t = `<h4 class="page_sidebar_link_header">AmyScript</h4>
    <ul class="page_sidebar_links">
        <a href="index.html"><li id="currentLink">Home</li></a>
        <a href="types.html"><li>Types</li></a>
        <a href="variables.html"><li>Variables</li></a>
        <a href="arrays.html"><li>Arrays</li></a>
        <a href="conditionals.html"><li>Conditionals</li></a>
        <a href="loops.html"><li>Loops</li></a>
        <a href="functions.html"><li>Functions</li></a>
        <a href="classes.html"><li>Classes</li></a>
    </ul>
    <h4 class="page_sidebar_link_header">AmyAssembly</h4>
    <ul class="page_sidebar_links">
        <a href="assembly.html"><li>Home</li></a>
        <a href="assemblySyntax.html"><li>Syntax</li></a>
        <a href="assemblyVariables.html"><li>Variables</li></a>
        <a href="assemblyMemory.html"><li>Memory</li></a>
        <a href="assemblyArithmetic.html"><li>Arithmetic</li></a>
        <a href="assemblyConditionals.html"><li>Conditionals</li></a>
        <a href="assemblyFunctions.html"><li>Functions</li></a>
    </ul>`;

    var parent = document.getElementById (parentID);

    createNavHeader (parent, "AmyScript");
    // create nav list
    var navList = document.createElement ("ul");
    navList.className = "page_sidebar_links";
    createNavLink (navList, "Home",         "index.html", currentPage);
    createNavLink (navList, "Types",        "types.html", currentPage);
    createNavLink (navList, "Variables",    "variables.html", currentPage);
    createNavLink (navList, "Arrays",       "arrays.html", currentPage);
    createNavLink (navList, "Conditionals", "conditionals.html", currentPage);
    createNavLink (navList, "Loops",        "loops.html", currentPage);
    createNavLink (navList, "Functions",    "functions.html", currentPage);
    createNavLink (navList, "Classes",      "classes.html", currentPage);
    // add nav list to sidebar
    parent.appendChild (navList);

    createNavHeader (parent, "AmyAssembly");
    // create nav list
    navList = document.createElement ("ul");
    navList.className = "page_sidebar_links";
    createNavLink (navList, "Assembly",     "assembly.html", currentPage);
    createNavLink (navList, "Syntax",       "assemblySyntax.html", currentPage);
    createNavLink (navList, "Variables",    "assemblyVariables.html", currentPage);
    createNavLink (navList, "Memory",       "assemblyMemory.html", currentPage);
    createNavLink (navList, "Arithmetic",   "assemblyArithmetic.html", currentPage);
    createNavLink (navList, "Conditionals", "assemblyConditionals.html", currentPage);
    createNavLink (navList, "Functions",    "assemblyFunctions.html", currentPage);
    // add nav list to sidebar
    parent.appendChild (navList);



}

//========================================================================

function createNavHeader (parent, text)
{
    var header = document.createElement ('h4');
    header.className = "page_sidebar_link_header";
    header.textContent = text;
    parent.appendChild (header);
}

//========================================================================

// <a href="index.html"><li id="currentLink">Home</li></a>
function createNavLink (parent, text, link, currentPage)
{

    var a = document.createElement ("a");
    a.href = link;

    var li = document.createElement ("li");
    if (link == currentPage)
    {
        li.id = "currentLink";
    }
    li.textContent = text;

    a.appendChild (li);
    parent.appendChild (a);

}

//========================================================================
/**
 * Generates the footer element of the page to a given parent
 * @param {HTMLDivElement} parentId id of parent DOM element to generate footer
 */
function loadFooter (parentId, back_path = "../")
{
    // get parent
    var parent = document.getElementById (parentId);

    parent.innerHTML = "<h5>&copy; 2021 Amy Burnett</h5>";

}

//========================================================================