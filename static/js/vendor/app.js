( function( $ ) {
	$( document ).ready( function() {
		jQuery.fn.exists = function(){return jQuery(this).length>0;}
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
 				if($( '#copy-btn' ).exists()) {
					ZeroClipboard.setMoviePath( '/static/js/vendor/zeroclipboard/ZeroClipboard10.swf' );
					var clip = new ZeroClipboard.Client();
					clip.setText( $('.short-url' ).attr( 'href' ) );
					clip.setHandCursor( true );
					clip.setCSSEffects( true );
					clip.addEventListener( 'mouseOver', function( client ) {
						$( '#copy-btn' ).css( 'background-image','url(/static/img/blue_arrow_right.png)' );
						$( '#copy-btn' ).css( 'background-position','100% 7px' );
					} );
					clip.addEventListener( 'mouseOut', function( client ) {
						$( '#copy-btn' ).css( 'background-image','url(/static/img/grey_arrow_right.png)' );
						$( '#copy-btn' ).css( 'background-position','100% 5px' );
					} );
					clip.glue( 'copy-btn', 'copy-wrapper' );
 				}
				// social buttons
				if($( '.your-share .twitter' ).exists()) {
					$( '.your-share .twitter' )
						.socialShare( {
							'share_params': $( '.your-share .twitter' ).data(),
							'wb_type': 'Twitter'
						} );
				}
				if($( '.your-share .facebook' ).exists()) {
					$( '.your-share .facebook' )
						.socialShare( {
							'share_params':{ 't': $( '.your-share .facebook' ).data().t, 'u': $( '.your-share .facebook' ).data().u },
							'wb_type': 'Facebook' 
						} );
				}
				break;
			// The gallery page
			case 'gallery':
				// initialize the gallery
				$.webifyme.gallery.fn.init();
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
	
	$(document).ajaxSend(function(event, xhr, settings) {
	    function getCookie(name) {
	        var cookieValue = null;
	        if (document.cookie && document.cookie != '') {
	            var cookies = document.cookie.split(';');
	            for (var i = 0; i < cookies.length; i++) {
	                var cookie = jQuery.trim(cookies[i]);
	                // Does this cookie string begin with the name we want?
	                if (cookie.substring(0, name.length + 1) == (name + '=')) {
	                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
	                    break;
	                }
	            }
	        }
	        return cookieValue;
	    }
	    function sameOrigin(url) {
	        // url could be relative or scheme relative or absolute
	        var host = document.location.host; // host + port
	        var protocol = document.location.protocol;
	        var sr_origin = '//' + host;
	        var origin = protocol + sr_origin;
	        // Allow absolute or scheme relative URLs to same origin
	        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
	            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
	            // or any other URL that isn't scheme relative or absolute i.e relative.
	            !(/^(\/\/|http:|https:).*/.test(url));
	    }
	    function safeMethod(method) {
	        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	    }

	    if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
	        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
	    }
	});
	
} )( jQuery );
