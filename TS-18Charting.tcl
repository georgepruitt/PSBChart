#############################################################################
# Generated by PAGE version 6.0.1
#  in conjunction with Tcl version 8.6
#  Feb 19, 2021 05:03:59 PM EST  platform: Windows NT
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    tk_messageBox -title Error -message  "You must open project files from within PAGE."
    exit}


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_font_dft_desc)  TkDefaultFont
set vTcl(actual_gui_font_dft_name)  TkDefaultFont
set vTcl(actual_gui_font_text_desc)  TkTextFont
set vTcl(actual_gui_font_text_name)  TkTextFont
set vTcl(actual_gui_font_fixed_desc)  TkFixedFont
set vTcl(actual_gui_font_fixed_name)  TkFixedFont
set vTcl(actual_gui_font_menu_desc)  TkMenuFont
set vTcl(actual_gui_font_menu_name)  TkMenuFont
set vTcl(actual_gui_font_tooltip_desc)  TkDefaultFont
set vTcl(actual_gui_font_tooltip_name)  TkDefaultFont
set vTcl(actual_gui_font_treeview_desc)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(actual_gui_menu_active_fg)  #000000
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
}



    menu .pop52 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(pr,menubgcolor) -font TkMenuFont \
        -foreground $vTcl(pr,menufgcolor) -tearoff 1 
    vTcl:DefineAlias ".pop52" "Popupmenu1" vTcl:WidgetProc "" 1
    menu .pop53 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(pr,menubgcolor) -font TkMenuFont \
        -foreground $vTcl(pr,menufgcolor) -tearoff 1 
    vTcl:DefineAlias ".pop53" "Popupmenu2" vTcl:WidgetProc "" 1
    menu .pop54 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(pr,menubgcolor) -font TkMenuFont \
        -foreground $vTcl(pr,menufgcolor) -tearoff 1 
    vTcl:DefineAlias ".pop54" "Popupmenu3" vTcl:WidgetProc "" 1

proc vTclWindow.top44 {base} {
    global vTcl
    if {$base == ""} {
        set base .top44
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m50" -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 1418x757+251+101
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 3844 1061
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "New Toplevel"
    vTcl:DefineAlias "$top" "TopLevel" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    entry $top.ent45 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 124 
    vTcl:DefineAlias "$top.ent45" "Entry1" vTcl:WidgetProc "TopLevel" 1
    label $top.lab46 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {<---   Start Date YYYYMMDD} 
    vTcl:DefineAlias "$top.lab46" "Date" vTcl:WidgetProc "TopLevel" 1
    canvas $top.can47 \
        -background #070707 -borderwidth 2 -closeenough 1.0 -height 633 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -relief ridge -selectbackground blue \
        -selectforeground white -width 1307 
    vTcl:DefineAlias "$top.can47" "Canvas" vTcl:WidgetProc "TopLevel" 1
    canvas $top.can48 \
        -background $vTcl(actual_gui_bg) -borderwidth 2 -closeenough 1.0 \
        -height 143 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -insertbackground black -relief ridge \
        -selectbackground blue -selectforeground white -width 1307 
    vTcl:DefineAlias "$top.can48" "Canvas2" vTcl:WidgetProc "TopLevel" 1
    scale $top.sca49 \
        -activebackground $vTcl(analog_color_m) \
        -background $vTcl(actual_gui_bg) -bigincrement 0.0 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) -from 0.0 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -length 100 -orient horizontal -resolution 1.0 -tickinterval 0.0 \
        -to 100.0 -troughcolor #d9d9d9 
    vTcl:DefineAlias "$top.sca49" "Scale1" vTcl:WidgetProc "TopLevel" 1
    menu $top.m50 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(pr,menubgcolor) -font TkMenuFont \
        -foreground $vTcl(pr,menufgcolor) -tearoff 0 
    $top.m50 add command \
        -activebackground {} -activeforeground {} -background {} -command {#} \
        -font {} -foreground {} -label File 
    $top.m50 add cascade \
        -menu "$top.m50.men58" -activebackground {} -activeforeground {} \
        -background {} -command {{}} -font {} -foreground {} \
        -label NewCascade 
    set site_3_0 $top.m50
    menu $site_3_0.men58 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(pr,menubgcolor) -font TkMenuFont \
        -foreground $vTcl(pr,menufgcolor) -tearoff 0 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.ent45 \
        -in $top -x 0 -relx 0.008 -y 0 -rely 0.965 -width 124 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab46 \
        -in $top -x 0 -relx 0.106 -y 0 -rely 0.965 -width 0 -relwidth 0.128 \
        -height 0 -relheight 0.027 -anchor nw -bordermode ignore 
    place $top.can47 \
        -in $top -x 0 -relx -0.035 -y 0 -rely -0.077 -width 0 -relwidth 0.922 \
        -height 0 -relheight 0.815 -anchor nw -bordermode ignore 
    place $top.can48 \
        -in $top -x 0 -y 0 -rely 0.772 -width 0 -relwidth 0.922 -height 0 \
        -relheight 0.184 -anchor nw -bordermode ignore 
    place $top.sca49 \
        -in $top -x 0 -y 0 -rely 0.708 -width 0 -relwidth 0.922 -height 0 \
        -relheight 0.054 -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top44 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

