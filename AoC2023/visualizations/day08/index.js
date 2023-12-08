var cy = cytoscape({
    // very commonly used options
    container: document.getElementById('cy'),
    elements: [ /* ... */ ],
    style: [ /* ... */ ],
    layout: { name: 'grid' /* , ... */ },
    data: { /* ... */ },
  
    // initial viewport state:
    zoom: 1,
    pan: { x: 0, y: 0 },
  
    // interaction options:
    minZoom: 1e-50,
    maxZoom: 1e50,
    zoomingEnabled: true,
    userZoomingEnabled: true,
    panningEnabled: true,
    userPanningEnabled: true,
    boxSelectionEnabled: true,
    selectionType: 'single',
    touchTapThreshold: 8,
    desktopTapThreshold: 4,
    autolock: false,
    autoungrabify: false,
    autounselectify: false,
    multiClickDebounceTime: 250,
  
    // rendering options:
    headless: false,
    styleEnabled: true,
    hideEdgesOnViewport: false,
    textureOnViewport: false,
    motionBlur: false,
    motionBlurOpacity: 0.2,
    wheelSensitivity: 1,
    pixelRatio: 'auto'
  });

cy.add(
    {
        group: 'nodes',
        data: { weight: 75},
        position: { x: 200, y: 200}
    }
);