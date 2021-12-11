function truecallerjsRun() {
    var i = 3;
    var j = 0;
    var a = 0;

    var command = '~$ npm install -g truecallerjs';
    var command2 = '~$ truecallerjs -s +919912345678 --name';

    function cmd1Color(i) {
        var green = [0];
        var yellow = [3, 4, 5]
        var blue = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
        var gray = [15, 16];

        if (green.includes(i)) {
            return "green";
        } else if (yellow.includes(i)) {
            return "yellow";
        } else if (blue.includes(i)) {
            return "rgb(18, 223, 238)";
        } else if (gray.includes(i)) {
            return "gray";
        } else {
            return "white";
        }

    }

    function cmd2Color(j) {
        var green = [0];
        var yellow = [3, 4, 5, , 6, 7, 8, 9, 10, 11, 12, 13, 14]
        var blue = [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
        var gray = [16, 17, 33, 34, 35, 36, 37, 38];

        if (green.includes(j)) {
            return "green";
        } else if (yellow.includes(j)) {
            return "yellow";
        } else if (blue.includes(j)) {
            return "rgb(18, 223, 238)";
        } else if (gray.includes(j)) {
            return "gray";
        } else {
            return "white";
        }

    }


    function callTruecallerjs() {
        if (i < command.length) {
            document.getElementById("cmd1").innerHTML += "<span style=\"color:" + cmd1Color(i) + ";\">" + command.charAt(i) + "<span>";
            i++;
            setTimeout(callTruecallerjs, 100);

        } else {

            document.getElementById("underScore").innerHTML = ""
        }
    }

    function npmLines() {
        if (a < 19) {
            var data = ['[#.................] / idealTree:<span style="color: yellow;">npm</span>: <span style="background-color: white;color: black;">sill</span> <span style="color: magenta;">idealTree </span>buildDeps',
                '[##................] \\ idealTree:<span style="color: yellow;">npm</span>: <span style="background-color: white;color: black;">sill</span> <span style="color: magenta;">idealTree </span>buildDeps',
                '[###...............] / idealTree:<span style="color: yellow;">npm</span>: <span style="background-color: white;color: black;">sill</span> <span style="color: magenta;">idealTree </span>buildDeps',
                '[####..............] \\ idealTree:<span style="color: yellow;">npm</span>: <span style="background-color: white;color: black;">sill</span> <span style="color: magenta;">idealTree </span>buildDeps',
                '[#####.............] / idealTree:<span style="color: yellow;">npm</span>: <span style="background-color: white;color: black;">sill</span> <span style="color: magenta;">idealTree </span>buildDeps',
                '[######............] \\ idealTree:<span style="color: yellow;">npm</span>: <span style="background-color: white;color: black;">sill</span> <span style="color: magenta;">idealTree </span>buildDeps',
                '[#######...........] / idealTree:<span style="color: yellow;">yargs</span>: <span style="color: magenta;">timing idealTree:#root</span> Completed in 1678ms',
                '[########..........] / idealTree:<span style="color: yellow;">yargs</span>: <span style="color: magenta;">timing idealTree:#root</span> Completed in 1678ms',
                '[#########.........] \\ idealTree:<span style="color: yellow;">yargs</span>: <span style="color: magenta;">timing idealTree:#root</span> Completed in 1678ms',
                '[##########........] / idealTree:<span style="color: yellow;">yargs</span>: <span style="color: magenta;">timing idealTree:#root</span> Completed in 1678ms',
                '[###########.......] \\ idealTree:<span style="color: yellow;">yargs</span>: <span style="color: magenta;">timing idealTree:#root</span> Completed in 1678ms',
                '[############......] / idealTree:<span style="color: yellow;">yargs</span>: <span style="color: magenta;">timing idealTree:#root</span> Completed in 1678ms',
                '[#############.....] \\ reify:npm:<span style="color: green;"> timing reifyNode:node_modules/truecallerjs/node_modules/axios</span> Completed in 352ms',
                '[##############....] / reify:npm:<span style="color: green;"> timing reifyNode:node_modules/truecallerjs/node_modules/axios</span> Completed in 352ms',
                '[###############...] \ reify:npm:<span style="color: green;"> timing reifyNode:node_modules/truecallerjs/node_modules/axios</span> Completed in 352ms',
                '[################..] / reify:npm:<span style="color: green;"> timing reifyNode:node_modules/truecallerjs/node_modules/axios</span> Completed in 352ms',
                '[#################.] \\ reify:npm:<span style="color: green;"> timing reifyNode:node_modules/truecallerjs/node_modules/axios</span> Completed in 352ms',
                '[##################] / reify:npm:<span style="color: green;"> timing reifyNode:node_modules/truecallerjs/node_modules/axios</span> Completed in 352ms',
                '<span style="color: white;"> changed 25 packages, and audited 26 packages in 5s</span><br><span style="color: white;"> 3 packages are looking for funding</span><br><span style="color: white;"> run `npm fund` for details </span><br><span style="color: white;"> found</span> <span style="color: green;">0</span> <span style="color: white;">vulnerabilities</span>'
            ]

            document.getElementById("npm-lines").innerHTML = data[a];
            a++;
            setTimeout(npmLines, 180);
        } else {
            document.getElementById("underScore2").innerHTML = "_"
        }

    }

    function callTruecallerjs2() {
        if (j < command2.length) {
            document.getElementById("cmd2").innerHTML += "<span style=\"color:" + cmd2Color(j) + ";\">" + command2.charAt(j) + "<span>";
            j++;
            setTimeout(callTruecallerjs2, 100);

        } else {
            document.getElementById("underScore2").innerHTML = ""
        }
    }

    function truecallerjsOutput() {
        document.getElementById("truecallerjsOutput").innerHTML = '<span style="color: yellow;">Name</span>: <span style="color: rgb(14, 236, 14);"> Sumith Emmadi</span>';

    }

    document.getElementById("cmd1").innerHTML = "<span style=\"color: green;\">~</span>$ ";
    document.getElementById("cmd2").innerHTML = "";
    document.getElementById("underScore").innerHTML = "_";
    document.getElementById("npm-lines").innerHTML = "";
    document.getElementById("underScore2").innerHTML = ""
    document.getElementById("truecallerjsOutput").innerHTML = ""

    callTruecallerjs();
    setTimeout(npmLines, 3500);
    setTimeout(callTruecallerjs2, 7000);
    setTimeout(truecallerjsOutput, 12000);
    // setTimeout(truecallerjsRun, 15000);

}