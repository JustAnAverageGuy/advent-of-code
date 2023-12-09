function get_path(from, to, graph, instructions) {
    let curr = from;
    for(let i = 0; i < instructions.length; i++, i%= instructions.length){
        return;
    }

}

(async function () {
    let raw;
    try {
        // const url = '../../day_08.txt';
        const url = '../../input_example_08.txt';
        const response = await fetch(url);
        raw = await response.text();
    } catch (err) {
        console.error(err);
    }

    let [instructions, grph] = raw.trim().split('\n\n');
    grph = grph.split('\n');

    let graph = {};
    grph.forEach(line => {
        let [_, key, l, r] = line.match(/(\w+) = \((\w+), (\w+)\)/);
        // console.log([key, l, r]);
        graph[key] = {l:l, r:r};
    });

    // console.log(graph);
    // console.log(grph);
    // for(let i = 0; i < instructions.length; i++, /*i%=instructions.length*/){

    // }

    var cy = cytoscape({
        container: document.getElementById('cy'),

        boxSelectionEnabled: false,
        autounselectify: true,

        style: cytoscape.stylesheet()
            .selector('node')
            .style({
                'content': 'data(id)',
                
            })
            .selector('edge')
            .style({
                'curve-style': 'bezier',
                'target-arrow-shape': 'triangle',
        //         'width': 4,
                'line-color': 'cyan',
                'target-arrow-color': '#ddd'
            }),
        //     .selector('.highlighted')
        //     .style({
        //         'background-color': '#61bffc',
        //         'line-color': '#61bffc',
        //         'target-arrow-color': '#61bffc',
        //         'transition-property': 'background-color, line-color, target-arrow-color',
        //         'transition-duration': '0.5s'
        //     }),
        
        layout: {
            name: 'preset',
            padding: 5
        }
    });

    // cy.add(
    //     {
    //         group: 'nodes', data: { id: 'n0' } 
    //     }
    // )
    for (const key in graph) {
        if (Object.hasOwnProperty.call(graph, key)) {
            const element = graph[key];

            cy.add({group: 'nodes', data: {id: key}/*,position: {x: Math.random()*750, y: Math.random()*750}*/})
        }
    }

    for (const key in graph) {
        if (Object.hasOwnProperty.call(graph, key)) {
            const element = graph[key];

            cy.add({group: 'edges', data: {id: `${key}_child_left`, source: key, target: element.l}})
            cy.add({group: 'edges', data: {id: `${key}_child_right`, source: key, target: element.r}})
        }
    }

    /*var bfs = cy.elements().bfs('#a', function () { }, true);

    var i = 0;
    var highlightNextEle = function () {
        if (i < bfs.path.length) {
            bfs.path[i].addClass('highlighted');

            i++;
            setTimeout(highlightNextEle, 1000);
        }
    };

    // kick off first highlight
    highlightNextEle();*/

})();