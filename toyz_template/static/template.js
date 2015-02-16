// Copyright 2015 by Fred Moolekamp
// License: MIT

// Define namespace to avoid collisions
Toyz.namespace('Toyz.Template');

// Check to see if all of the API's dependencies have loaded
// If not, return false
Toyz.Template.dependencies_loaded = function(){
    return true;
};
// Load any dependencies of the tile
Toyz.Template.load_dependencies = function(callback, params){
    // Check to see if ace loaded from the server
    if(!Toyz.Template.dependencies_loaded()){
        console.log('Loading Template dependencies');
        Toyz.Core.load_dependencies({
            core: true,
            css: [
                "/toyz/static/toyz_template/studio.css"
            ]
        });
    };
};

// This is the main object contained in the tile
Toyz.Template.Contents = function(params){
    this.type = 'template';
    this.tile = params.tile;
    this.$tile_div = params.$tile_div;
    this.$tile_div
        .removeClass('context-menu-tile')
        .addClass('context-menu-template');
    this.workspace = params.workspace;
    this.settings = {};
    
    //create tile context menu
    $.contextMenu({
        selector: '#'+this.$tile_div.prop('id'),
        callback: function(workspace, key, options){
            workspace[key](options);
        }.bind(null, workspace),
        items: this.contextMenu_items()
    });
    
    // Add things to the div
    var $new_div = $('<div/>')
        .html('New template tile!');
    this.$tile_div.append($new_div);
    
    console.log('Template contents created');
};
// Required function to allow for updates to the tile values
// (but may be modified)
Toyz.Template.Contents.prototype.update = function(params, param_val){
    // Allow user to either pass param_name, param_val to function or
    // dictionary with multiple parameters
    if(!(param_val===undefined)){
        params = {params:param_val};
    };
    for(var param in params){
        this[param] = params[param];
    }
};
// This required function is called when a workspace tile is loaded
Toyz.Template.Contents.prototype.set_tile = function(settings){
    console.log('settings', settings);
    // Add some initialization function here based on the settings
};
// This required function is called when a data source is updated
Toyz.Template.Contents.prototype.rx_info = function(options){
    // If this tile uses a common workspace data source perform some actions here
};
// This function is called when a workspace is saved and is used to save the 
// current tiles settings
Toyz.Template.Contents.prototype.save = function(options){
    console.log('saving tile', this.tile.id, this.type);
    // functions here to save the tile
};
// Often it is common to have additional options added to the context (right-click) menu for
// a tile, but still keep the default options of a general tile as well
Toyz.Template.Contents.prototype.contextMenu_items = function(){
    var items = $.extend(true,{
        option1: {
            name: "Remove selected points", 
            callback: function(key, options){
                console.log('key', key);
                console.log('options', options);
            }.bind(this)
        },
        option2: {
            name: "Remove selected points", 
            callback: function(key, options){
                console.log('key', key);
                console.log('options', options);
            }.bind(this)
        },
        template_sep1: "--------------",
    }, Toyz.Workspace.tile_contextMenu_items(this.workspace));
    return items;
};


// I like to log a message when the script is loaded to help track bugs
console.log('Toyz Template loaded');