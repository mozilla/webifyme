/*
 * WebifyMe Gallery Code
 * This is all the javascript for the gallery section of webifyme
 * It manages pagination, and filtering of the content all through ajax requests.
 *
 */
( function( $ ) {

	$.webifyme = $.webifyme || {};
	
	$.webifyme.gallery = {
		'cfg': {
			animateTime: 500,
			featuredOnly: false
		},
		'fn': {
			'init': function() {
				// fade the gallery container in
				$( '#gallery_container' )
					.fadeIn( $.webifyme.gallery.cfg.animateTime );
				// setup our link handlers
				$.webifyme.gallery.fn.setupLinks();
				// setup the filter
				$.webifyme.gallery.fn.setupFilter();
			},
			'setupFilter': function( ) {
				// set the featredOnly flag accordingly
				if( $( '#gallery-filter .active a' ).attr( 'href' ).match( /featured/ ) ) {
					$.webifyme.gallery.cfg.featuredOnly = true;
				}
				$( '#gallery-filter' )
					.collapsibleList( )
					.find( 'a' )
					.bind( 'collapsibleList.select', function( e ) {
						// set the featuredOnly flag based on the presence of 'featured' in the url
						$.webifyme.gallery.cfg.featuredOnly = !! $( this ).attr( 'href' ).match( /featured/ );
						// reload the navigation and page contents
						$.webifyme.gallery.fn.loadNavigation( '/gallery/chap/1/' );
					} );
			},
			'setupLinks': function() {
				$( 'span.pages a' ).each( function() {
					var $this = $( this );
					// not sure this is needed -- legacy code 
					$this.unbind();
					// bind click handlers
					$this.click( function( e ) {
						e.preventDefault();
						var href = $( this ).attr( 'href' );
						$.webifyme.gallery.fn.loadPage( $( this ).attr( 'href' ) );
						$( 'span.pages .active' ).removeClass( 'active' );
						$this.addClass( 'active' );
					} );
				} );
				$( 'a.gallery_nav' ).each( function() {
					var $this = $( this );
					$this.unbind( );
					$this.click( function( e ) {
						e.preventDefault();
						$.webifyme.gallery.fn.loadNavigation( $( this ).attr( 'href' ) );
					} );
				} );
			},
			'loadPage': function( href ) {
				/* The Old
					$('#gallery_container').fadeOut(ANIMATE_TIME, function() {
							$('#gallery_container').load(href, attachLinkFunctions);
					});

				*/
				// if we're only browsing featured content, append the featured flag to the url
				if( $.webifyme.gallery.cfg.featuredOnly ) href = href + 'featured';
				// fade out the current content 
				$( '#gallery_container' ).fadeOut( $.webifyme.gallery.cfg.animateTime, function() {
					// and load in our new content, then run the link setup function again
					$( '#gallery_container' ).load( href, function() {
						$( "#gallery_container" ).fadeIn( $.webifyme.gallery.cfg.animateTime );
						$.webifyme.gallery.fn.setupLinks();
					} );
				} );
			},
			'loadNavigation': function( href ) {
				/* The Old
				$('.pagination').load($(this).attr('href'), attachLinkFunctions);
				$('#gallery_container').fadeOut(ANIMATE_TIME, function() {
						$('#gallery_container').load(href, attachLinkFunctions);
				});
				*/
				// reference to the original href for passing to the loadPage function
				var oHref = href;
				if( $.webifyme.gallery.cfg.featuredOnly ) href = href + 'featured';
				// reload the navigation
				$( '.pagination' ).load( href, $.webifyme.gallery.fn.setupLinks );
				// reload the page
				$.webifyme.gallery.fn.loadPage( oHref + '1/' );
			}
		}
	};

}( jQuery ) );