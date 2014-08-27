/*
 * auto-target.js
 *
 * Automatically set all links in web pages to use target="_blank"
 * for domains outside of current domain. Also sets external URL icon.
 *
 * >  This uses FortAwesome's FontAwesome service.
 *    http://fortawesome.github.io/Font-Awesome/get-started/
 *
 * >  Inject this script at the END OF YOUR HTML <body> TAG!
 *    <body>
 *        ...
 *        <script src="/path/to/auto-target.js"></script>
 *    </body>
 *
 * The MIT License (MIT)
 *
 * Copyright (c) 2014 Mitchell Barry
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */

(function() {
    var hostname = window.location.host;
    hostname = hostname.split('.').slice(-2).join('.');
    var new_tab = true;
    var set_icon = true;
    for (var links = document.links, i = 0, a; a = links[i]; i++) {
        if (a.hostname !== hostname) {
            if (new_tab)
                a.target = '_blank';
            if (set_icon)
                a.innerHTML +=
                    '<i class="fa fa-external-link fa-1 external-link-margin" />';
        }
    }
})();
