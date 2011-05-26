/**
 * jquery.collapsibleList.js
 * 
 * Takes a list, and collapses it, while showing the currently selected item
 * 
 * 
 * Author: Adam Miller - adam@barbariangroup.com
 * License: http://unlicense.org/ (i.e. do what you want with it!)
 * 
 */
( function( $ ) {
	$.collapsibleList = {
		defaults: {
			'collapsedClass': 'cl-collapsed',
			'expandedClass': 'cl-expanded',
			'listClass': 'cl-list',
			'parentClass': 'cl-container',
			'headerHTML': '<h3 class="cl-current"></h3>'
		},
		cfg: {
			'collapsed': true
		},
		fn: {
			init: function ( context ) {
				$.collapsibleList.fn.setupDOM( context );
				$.collapsibleList.fn.setupEvents( context );
			},
			setupDOM: function( context ) {
				// take the list, wrap it in a div, add a h3 for displaying the current title
				context.$container = context.$list.wrap( '<div></div>' ).parent();
				context.$current = $( context.headerHTML )
					.text( context.$list.children( ':first' ).text() );
				context.$container
					.addClass( context.parentClass )
					.prepend( context.$current );
				// hide the list initially 
				context.$list
					.addClass( context.listClass )
					.hide();
			},
			setupEvents: function( context ) {
				context.$list.find( 'a' )
					.bind( 'click mouseup', function( e ) {
						e.preventDefault();
					} )
					.bind( 'mousedown', function( e ) {
						e.preventDefault();
						var $link = $( this );
						// consider the value to have changed if the new text is not equal to the current text
						var changed = ( $link.text() != context.$current.text() );
						if( changed ) {
							// update the current selection
							context.$current.text( $link.text() );
							// broadcast the event to the link
							$link.trigger( 'collapsibleList.select' );
						}
						// collapse the list
						$.collapsibleList.fn.collapse( context );
					} );
				context.$current
					.bind( 'click mouseup', function( e ) {
						e.preventDefault();
					} )
					.bind( 'mousedown', function() {
						if( context.collapsed ) {
							$.collapsibleList.fn.expand( context );
						} else {
							$.collapsibleList.fn.collapse( context );
						}
					} );
			},
			collapse: function ( context ) {
				// slide the list closed
				context.collapsed = true;
				context.$list.slideUp( 'fast' );
			},
			expand: function( context ) {
				// slide open the list
				context.collapsed = false;
				context.$list.slideDown( 'fast' );
			}
		}
	};
	
	$.fn.collapsibleList = function( options ) {
		return this.each( function( ) {
			var context = { };
			$.extend( context, $.collapsibleList.defaults, options );
			$.extend( context, $.collapsibleList.cfg, context );
			context.$list = $( this );
			$.collapsibleList.fn.init( context );
			// stash our context
			context.$container
				.data( 'collapsibleList-context', context );
		} );
	};

} )( jQuery );