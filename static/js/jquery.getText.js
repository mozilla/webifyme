/**
 * jquery.getText.js
 * 
 * Utility for pulling strings from the DOM
 * 
 * Useful for placing all localized strings in templates, and accessing them in javascript
 * 
 * Example Markup: 
 * 
 * <div class="translated-strings" style="display:none;">
 *  <span id="msg-hello-world">Hello World!</span>
 *  <ol id="alphabet">
 *   <li>A</li>
 *   <li>B</li>
 *   <li>C</li>
 *   <li>D</li>
 *   <li>E</li>
 *   <li>F</li>
 *  </ol>
 * </div>
 *
 * Accessing Strings: 
 *  
 * $._( 'msg-hello-word' ) -> "Hello World!"
 * $._( 'msg-alphabet', 3 ) -> "D"
 *
 *
 * Author: Adam Miller - adam@heyadammiller.com
 * License: http://unlicense.org/ (i.e. do what you want with it!)
 * 
 */
( function( $ ) {
	$.getText = {
		translatedStrings: {},
		fn: {
			// parses translated strings out of div.translated-strings
			// ol's are treated as arrays
			// everything else as is
			loadStrings: function( ) {
				$( 'div.translated-strings' ).each( function () {
					$( this ).children().each( function () {
						var $this = $( this );
						if ( $this.is( 'ol' ) ) {
							// if it's an ol, load the strings in each childnode as an array
							$.getText.translatedStrings[$this.attr( 'id' )] = [];
							$this.children().each( function () {
								$.getText.translatedStrings[$this.attr( 'id' )].push( $( this ).html() );
							} );
						} else {
							// otherwise just load the elements contents
							$.getText.translatedStrings[$this.attr( 'id' )] = $this.html();
						}
					} );
				} );
			},
			// looks for a match in translated stings
			// returns the match if found, else it returns the key
			getString: function ( key, index ) {
				if( key in $.getText.translatedStrings ) {
					if( typeof $.getText.translatedStrings[key] === "object" && typeof index === "number" ) {
						// if this tranlsation is an array of strings, and we were passed an index val
						return $.getText.translatedStrings[key][index];
					} else {
						// otherwise just return the match
						return $.getText.translatedStrings[key];
					}
				} else {
					// fallback to returning the passed key if we can't find the translation
					return key;
				}
			},
		}
	};
	
	// shortcut function
	$._ = $.getText.fn.getString;
	
	$( document ).ready( function() {
		$.getText.fn.loadStrings();
	} );
	
} )( jQuery );