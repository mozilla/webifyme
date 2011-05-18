// jquery.autoResize.js -- a simple way to bind resize handlers to DOM elements
// depends on jquery.delayedBind.js
( function( $ ) {
	
	$.autoResize = {
		// overwritten by options
		defaults: {
			delay: 300, 
			getAvailableSpace: null // can be overwritten with a function for calculating available space
		},
		// protected (somewhat)
		config: {
			$container: null
		},
		// event handlers
		evt: {
			resize: function( context, e ) {
				var availableSpace = $.autoResize.fn.getAvailableSpace( context );
				context
					.$container
					.find( '.autoResize' )
						.trigger( 'resize.autoResize', availableSpace );
			}
		},
		// functions
		fn: {
			getAvailableSpace: function( context ) {
				if ( typeof context.getAvailableSpace === 'function' ) {
					return context.getAvailableSpace( context );
				} else {
					return { 'width': $( window ).width(), 'height': $( window ).height() };
				}
			}
		}
	};
	
	$.fn.autoResize = function( options ) {
		return $( this ).each( function() {
			var context = $.extend( {}, $.autoResize.defaults, options );
			$.extend( context, context, $.autoResize.config );
			context.$container = $( this );
			$( window )
				.delayedBind( context.delay, 'resize', function( e ) {
					return $.autoResize.evt.resize( context, e );
				} );
			context.$container.data( 'autoResize-context', context );
		} );
	};
	
} )( jQuery );