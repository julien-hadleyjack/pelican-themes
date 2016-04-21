Title: Markdown overview
Tags: markdown
Date: 2016-04-20 10:14
Category: Demonstration
Author: Julien Hadley Jack
Slug: markdown-overview
Summary:
  The result of different markdown elements in the current theme.
  You can see which elements have a corresponding CSS style.

Examples from [Daring Fireball](http://daringfireball.net/projects/markdown/syntax)

# Inline HTML

This is a regular paragraph.

<table>
    <tr>
        <td>Foo</td>
    </tr>
</table>

This is another regular paragraph.

# Block Elements

## Headers

### Header Level 3

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam non viverra dui. Cras a euismod leo, non iaculis massa. Pellentesque non massa ut velit sollicitudin finibus. Sed vitae nunc sed est mattis efficitur. Nulla maximus neque non dolor congue lacinia.

#### Header Level 4

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam non viverra dui. Cras a euismod leo, non iaculis massa. Pellentesque non massa ut velit sollicitudin finibus. Sed vitae nunc sed est mattis efficitur. Nulla maximus neque non dolor congue lacinia.

##### Header Level 5

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam non viverra dui. Cras a euismod leo, non iaculis massa. Pellentesque non massa ut velit sollicitudin finibus. Sed vitae nunc sed est mattis efficitur. Nulla maximus neque non dolor congue lacinia.

###### Header Level 6

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam non viverra dui. Cras a euismod leo, non iaculis massa. Pellentesque non massa ut velit sollicitudin finibus. Sed vitae nunc sed est mattis efficitur. Nulla maximus neque non dolor congue lacinia.

## Block Quote

Example 1:

> This is a blockquote with two paragraphs. Lorem ipsum dolor sit amet,
> consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus.
> Vestibulum enim wisi, viverra nec, fringilla in, laoreet vitae, risus.
> 
> Donec sit amet nisl. Aliquam semper ipsum sit amet velit. Suspendisse
> id sem consectetuer libero luctus adipiscing.

Example 2:

> This is the first level of quoting.
>
> > This is nested blockquote.
>
> Back to the first level.

Example 3:

> ## This is a header.
> 
> 1.   This is the first list item.
> 2.   This is the second list item.
> 
> Here's some example code:
> 
>     return shell_exec("echo $input | $markdown_script");


## Lists

Example 1: 

*   Red
*   Green
*   Blue

Example 2:

1.  Bird
2.  McHale
3.  Parish

Example 3:

1.  This is a list item with two paragraphs. Lorem ipsum dolor
    sit amet, consectetuer adipiscing elit. Aliquam hendrerit
    mi posuere lectus.

    Vestibulum enim wisi, viverra nec, fringilla in, laoreet
    vitae, risus. Donec sit amet nisl. Aliquam semper ipsum
    sit amet velit.

2.  Suspendisse id sem consectetuer libero luctus adipiscing.

Example 4:

*   A list item with a blockquote:

    > This is a blockquote
    > inside a list item.

Example 5:

*   A list item with a code block:

        <code goes here>


## Code Blocks

This is a normal paragraph:

    This is a code block.


-------------


# Span Elements

## Links

This is [an example](http://example.com/ "Title") inline link.

[This link](http://example.net/) has no title attribute.

## Emphasis

Emphasis, aka italics, with *asterisks* or _underscores_.

Strong emphasis, aka bold, with **asterisks** or __underscores__.

un*frigging*believable

## Code

Use the `printf()` function.

## Images

![Wake, Little Brother! I bring news.]({filename}/images/jungle_book.png)

# Other

## Youtube

<iframe width="560" height="315" src="https://www.youtube.com/embed/n1a7o44WxNo" frameborder="0" allowfullscreen></iframe>






