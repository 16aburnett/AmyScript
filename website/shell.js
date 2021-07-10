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
    var parent = document.getElementById (parentID);

    createNavHeader (parent, "AmyScript");
    // create nav list
    var navList = document.createElement ("ul");
    navList.className = "page_sidebar_links";
    createNavLink (navList, "Home",         "index.html", currentPage);
    createNavLink (navList, "Comments",     "comments.html", currentPage);
    createNavLink (navList, "Data Types",   "types.html", currentPage);
    createNavLink (navList, "Variables",    "variables.html", currentPage);
    createNavLink (navList, "Operators",    "operators.html", currentPage);
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
function loadFooter (parentId)
{
    // get parent
    var parent = document.getElementById (parentId);

    parent.innerHTML = "<h5 style='text-align:center;padding:10px'>&copy; " + (new Date()).getFullYear() + " - Amy Burnett</h5>";

}

//========================================================================