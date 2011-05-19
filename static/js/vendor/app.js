( function( $ ) {
	$( document ).ready( function() {
		
		// Page Specific Initialization Code 
		// give your page an id, then throw the init code in here rather than in the markup
		var $body = $( 'body' );
		switch ( $body.attr( 'id' ) ) {
			// The quiz page
			case 'quiz':
				things.Quiz();
				break;
			// The collage view page
			case 'collage':
				var collage = things.Collage( $( '#collage-canvas' ), things.collageData );
				things.snapshotChecker = null;
				collage.draw();
				if( things.collageData['background'] ) {
					things.setBackground( things.collageData['background'] );
				}
				if( things.isCollageOwner ) {
					things.BackgroundSelector( things.backgroundData );
					things.snapshotChecker = things.SnapshotChecker();
				}
				// zero clipboard config
				ZeroClipboard.setMoviePath( '/static/js/zeroclipboard/ZeroClipboard10.swf' );
				var clip = new ZeroClipboard.Client();
				clip.setHandCursor( true );
				clip.setCSSEffects( true );
				clip.addEventListener( 'mouseOver', function( client ) {
					$( '#copy-btn' ).css( 'background-image','url(/static/img/blue_arrow_right.png)' );
					$( '#copy-btn' ).css( 'background-position','100% 7px' );
					clip.setText( 'http://bit.ly/gyWp3m' );
				} );
				clip.addEventListener( 'mouseOut', function( client ) {
					$( '#copy-btn' ).css( 'background-image','url(/static/img/grey_arrow_right.png)' );
					$( '#copy-btn' ).css( 'background-position','100% 5px' );
				} );
				clip.addEventListener( 'mouseDown', function( client ) {
					clip.setText( 'http://bit.ly/gyWp3m' );
				} );
				clip.glue( 'copy-btn' );
				
				// social buttons 
				$( '.your-share .twitter' )
					.socialShare( {
						'share_params': $( '.your-share .twitter' ).data()
					} );
				$( '.your-share .facebook' )
					.socialShare( {
						'share_params':{ 't': $( '.your-share .facebook' ).data().t, 'u': $( '.your-share .facebook' ).data().u } 
					} );
				break;
			// The gallery page
			case 'gallery':
				break;
		}
		
		// GLOBLAL Initialization Code 
		$( '.facebook iframe' ).each( function() {
			var $this = $( this );
			$this
				.attr( 'src', $this.attr( 'src' ).replace( /SHARE_URL/, encodeURIComponent( window.location ) ) );
		} );
			
		// download click stuff -- copied from global.js
		$( 'a.download-reminder' ).click( function() {
			if( ! $( '#download_popup' ).hasClass( 'clicked' ) ) {
				$( '#download_popup' ).center().fadeIn().addClass( 'clicked' );
				return false;
			}
		} );
		$( 'body' ).click( function() {
			if( $( '#download_popup' ).hasClass( 'clicked' ) ) {
				$( '#download_popup' ).fadeOut();
				$( '#download_popup' ).removeClass( 'clicked' );
			}
		} );
		$( '#download_popup' ).click( function( event ) {
			event.stopPropagation();
		} );
		
	} );
	
	$.fn.center = function () {
		this.css( 'position','absolute' );
		this.css( 'top', ( $( window ).height() - this.height() ) / 2 + $( window ).scrollTop() + 'px' );
		this.css( 'left', ( $( window ).width() - this.width() ) / 2 + $( window ).scrollLeft() + 'px' );
		return this;
	};
	
} )( jQuery );