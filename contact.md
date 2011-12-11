---
layout: base
title: Contact
---

# Contact #

The preferred way to contact me is always by e-mail, unless your mail requires
significant action on my part or I am exceedingly busy I will reply swiftly:

<!-- If we don't have any JavaScript we use a simple form that really only can
    be translated into a single address (well, web-wise pretty much all e-mail
    has an "at" and a "dot", in that order) -->
<code id="obfuscated">
    pontus stenetorp se
</code>
<!-- But if we do have JavaScript we de-obfuscate the e-mail for the user -->
<script type="text/javascript">
// Store any existing onload
var oldOnload;
if (window.onload !== undefined) {
    oldOnload = window.onload;
}

window.onload = function (event) {
    obfuscated = document.getElementById('obfuscated');
    // This should be hard enough for most bots
    obfuscated.textContent = obfuscated.textContent
            .replace('s s', 's@s').replace('p s', 'p.s');

    // Lastly call the old unload, if it was a function
    if (typeof oldOnload === 'function') {
        oldOnload(event);
    }
}
</script>

Contrary to a popular misconception about people in academia, most (and myself
in particular) do not mind **you**, yes **you**, fellow student, researcher
and/or human, dropping a few lines asking for verification. Heck, even
criticism **is** usually welcome.

If I can in any way clarify or if you feel that you can correct (and thus
help) me in any way, taking the time to write me an e-mail is very much
appreciated.

## University of Tokyo (UT) ##

My main desk is at the [UT Hongo campus][gmap_hongo_campus], the address and
phone/fax number can be found below and here is a link to the [official UT
hongo access homepage][ut_hongo_access].

    Phone:  +81-3-5803-1697
    Fax:    +81-3-5802-8872

    Address:
        Room 615, Faculty of Science Building 7
        The University of Tokyo, Hongo 7-3-1
        Bunkyo-ku, Tokyo
        113-0033 Japan 

[gmap_hongo_campus]: http://maps.google.com/?ll=35.711726,139.761951&spn=0.012405,0.016673&z=16&vpsrc=6
[ut_hongo_access]: http://www.u-tokyo.ac.jp/campusmap/map01_02_e.html

## National Institute of Informatics (NII) ##

I also have a secondary desk at NII, here is the [official NII access
homepage][nii_access].

    Address:
        Room 1610, National Institute of Informatics
        2-1-2 Hitotsubashi
        Chiyoda-ku, Tokyo
        101-8430 Japan

[nii_access]: http://www.nii.ac.jp/en/access/
