var things = things || {};

things.blockSize = 25;
things.COLLAGE_WIDTH = 35;
things.COLLAGE_HEIGHT = 24;
things.DEBUG = false;
things.objImgPath = '/static/objects/';

things.SCALES = {
	'large':{'factor':1.5},
	'medium':{'factor':1.0},
	'small':{'factor':0.75}
};

things.randomColor = function() {
	return 'rgb('+Math.floor(Math.random()*255)+','+Math.floor(Math.random()*255)+','+Math.floor(Math.random()*255)+')';
};

things.CollageObj = function(attrs, packed, scale) {
	var that = {};
	var tipEl = null;
	that.el = null;
	that.id = null;
	that.name = null;
	that.description = null;
	that.width = null;
	that.height = null;
	that.scaledWidth = null;
	that.scaledHeight = null;
	that.contextObj = null;
	
	that.fittedEl = function() {
		if( ! that.contextObj.place) return false;
		return that.el.css( {
			'top':that.contextObj.y * things.blockSize,
			'left':that.contextObj.x * things.blockSize,
			'width': that.scaledWidth,
			'height': that.scaledHeight,
			'background-image':'url(' + things.objImgPath + scale + '/' + attrs.img + ')'
		} );
	};
	
	that.tipEl = function() {
		if( ! tipEl ) {
			tipEl = $( '<div class="sticky">' +
				'<a class="close" href="#">X</a>' +
				'<div class="inner">' + 
					'<h3>' + that.name + '</h3>' + 
					'<p>' + that.description + '</p>' +
				'</div>' +
			'<div class="sticky-top"></div>' +
			'<div class="sticky-middle"></div>' +
			'<div class="sticky-bottom"></div>' +
			'</div>' );
		}
	
	
		var stickyWidth = 357;
		var top = (that.contextObj.y * things.blockSize) + (that.height / 4);
		var left = (that.contextObj.x * things.blockSize)	 + (that.width / 2);
		
		var rightPos = that.el.parent().position().left + left + stickyWidth;
		if(rightPos > $(window).width()) {
			tipEl.addClass('flip');
			left = left - stickyWidth;
		} else {
			tipEl.removeClass('flip');
		}
		
		return tipEl.css({
			'top': top,
			'left': left
		});
	};
	
	that.setScale = function(new_scale) {
		var scale = new_scale;
		var scaleFactor = things.SCALES[scale].factor;
		that.scaledWidth = Math.floor(that.width * scaleFactor);
		that.scaledHeight = Math.floor(that.height * scaleFactor);
		that.contextObj.setSize(that.scaledWidth, that.scaledHeight);
	};
	
	function init() {
		that.contextObj = things.Obj( attrs.width, attrs.height );
		
		if( typeof( attrs.x ) !== 'undefined' && typeof( attrs.y ) !== 'undefined' && packed ) {
			that.contextObj.setLocation(attrs.x, attrs.y );
		}
		
		that.id = attrs.id;
		that.name = attrs.name;
		that.description = attrs.description;
		that.width = attrs.width;
		that.height = attrs.height;
		that.setScale( scale );
		that.el = $( '<div class="obj"></div>' );
		if( things.DEBUG ) {
			that.el.css( 'background-color', things.randomColor() );
		}
	}
	
	init();
	
	return that;
};

things.Collage = function( anEl, collage ) {
	var that = {};
	var objs = [];
	var packed = false;
	var scale = 'small';
	var el = anEl;
	var ctx = things.Context();
	var openTip = null;
	
	that.selectScale = function() {
		var totalObjArea = 0;
		var contextArea = (things.COLLAGE_WIDTH * things.blockSize) * (things.COLLAGE_HEIGHT * things.blockSize);
		for( var i = 0; i < objs.length; i++ ) {
			totalObjArea += ( objs[i].width * objs[i].height );
		}
		
		if( totalObjArea > (contextArea * 0.9) ) {
			scale = 'small';
		} else if( totalObjArea > (contextArea * 0.5) && totalObjArea <= (contextArea * 0.9)	) {
			scale = 'medium';
		} else {
			scale = 'large';
		}
		
		for (var y = 0; y < objs.length; y++ ) {
			objs[y].setScale( scale );
		}
	};
	
	that.pack = function() {
		that.selectScale();
		ctx.simpleFit();
		packed = true;
	};
	
	that.draw = function() {
		if( ! packed ) {
			that.pack();
		}
		
		function hideTip() {
			openTip.remove();
			openTip = null;
		}
		
		function showTip(obj) {
			if(openTip) {
				hideTip();
			}
			var tipEl = obj.tipEl();
			tipEl.find('.close').click(function(){
				hideTip();
				return false;
			});
			
			tipEl.appendTo(el);
			
			var height_of_top_sticky_section = tipEl.find('.sticky-top').height();
			var height_of_content = tipEl.find('.inner').innerHeight();
			var height_of_middle_sticky_section = height_of_content - height_of_top_sticky_section;
			var height_of_el = height_of_content + tipEl.find('.sticky-bottom').height();
			tipEl.find('.sticky-middle').height(height_of_middle_sticky_section);
			tipEl.height(height_of_el);
			openTip = tipEl;
		}
		
		function createTipEvent( tipEl ) {
			return function(){ showTip( tipEl ); };
		}
		
		//TODO: clear divs
		for(var i = 0; i < objs.length; i++) {
			var objEl = objs[i].fittedEl();
			if( ! objEl) {
				continue; // ignore objects that haven't been placed
			}
			objEl.appendTo(el);
			
			objEl.click( createTipEvent( objs[i] ) );
		}
	};

	function saveCollage() {
		var data = {};
		for(var i = 0; i < objs.length; i++) {
			if(objs[i].contextObj.place) {
				data[objs[i].id] = objs[i].contextObj.x+','+objs[i].contextObj.y;
			}
		}
		data.scale = scale;
		$.post(window.location.href, data);
	}
	
	function init() {
		packed = collage.packed;
		if(collage.scale && collage.scale !== '') {
			scale = collage.scale;
		}
		
		for( var i = 0; i < collage.objects.length; i++ ) {
			var obj = things.CollageObj(collage.objects[i], packed, scale);
			ctx.addObj(obj.contextObj);
			objs[objs.length] = obj;
		}
		
		if( ! packed ) {
			that.pack();
			saveCollage();
		}
	}
	init();
	return that;
};


things.Obj = function(pixelWidth, pixelHeight) {
	var that = {};
	that.width = 0;
	that.height = 0;
	that.buffer_x = 10;
	that.buffer_y = 10;
	that.x = 0;
	that.y = 0;
	that.pixelWidth = null;
	that.pixelHeight = null;
	that.place = false;
	
	that.setLocation = function(x,y) {
		that.x = x;
		that.y = y;
		that.place = true;
	};
	
	that.setSize = function(pWidth, pHeight) {
		that.pixelWidth = pWidth+that.buffer_x; // give 10px buffer for w & h
		that.pixelHeight = pHeight+that.buffer_y;
		that.width = Math.floor(that.pixelWidth/things.blockSize);
		that.height = Math.floor(that.pixelHeight/things.blockSize);
	};
	
	function init() {
		that.setSize(pixelWidth, pixelHeight);
	}
	init();
	
	return that;
};

things.LinkedList = function() {
	var that = {};
	
	that.head = null;
	that.tail = null;
	
	that.append = function(obj) {
		if( ! that.head ) {
			that.head = things.ListNode(obj);
			that.tail = that.head;
			return;
		}
		
		that.tail.next = things.ListNode(obj);
		that.tail = that.tail.next;
	};
	
	return that;
};

things.ListNode = function(obj) {
	var that = {};
	that.obj = obj;
	that.next = null;
	
	return that;
};



things.Context = function() {
	var that = {};
	that.objects = [];
	
	that.addObj = function(obj) {
		that.objects[that.objects.length] = obj;
	};
	
	that.simpleFit = function() {
		
		var fittedObjs = things.LinkedList();
		var coords = things.LinkedList();
		
		function collides( node, rect ) {
			if( ! node ) return false;
			
			if(rect.intersects(node.obj)) {
				return true;
			}
			
			return collides(node.next, rect);
		}
		
		function innerFit( node, obj ) {
			if( ! node ) return null;
			
			if( node.obj.x + obj.width < things.COLLAGE_WIDTH && 
				node.obj.y + obj.height < things.COLLAGE_HEIGHT && 
				! collides(fittedObjs.head, things.Rect(node.obj.x,node.obj.y,obj.width,obj.height) ) ) {
				 return node.obj;
			}
			
			return innerFit(node.next, obj);
		}
		
		function sortObjectsByPerimeter() {
			that.objects.sort(function(a,b){
				return (b.height + b.width) - (a.height + a.width);
			});
		}
		
		function sortObjectsByArea() {
			//sort objects in order of decreasing area
			that.objects.sort(function(a,b){
				return (b.height * b.width) - (a.height * a.width);
			});
		}

		function sortObjectsByWidth() {
			//sort objects in order of decreasing area
			that.objects.sort(function(a,b){
				return b.width - a.width;
			});
		}

		function sortObjectsByHeight() {
			//sort objects in order of decreasing area
			that.objects.sort(function(a,b){
				return b.height - a.height;
			});
		}
		
		sortObjectsByPerimeter();

		
		//populate coords linked list
		for(var y = 0; y < things.COLLAGE_HEIGHT; y++ ) {
			for(var x = 0; x < things.COLLAGE_WIDTH; x++) {
				coords.append({'x':x,'y':y});
			}
		}
		
		for( var i = 0; i < that.objects.length; i++ ) {
			var fittedCoord = innerFit(coords.head, that.objects[i]);
			if(fittedCoord) {
				that.objects[i].setLocation(fittedCoord.x,fittedCoord.y);
				fittedObjs.append(that.objects[i]);
			}
			
		}
		
	};
	
	return that;
};

things.Rect = function(x, y, width, height) {
	var that = {};
	
	that.x = x;
	that.y = y;
	that.width = width;
	that.height = height;
	
	that.area = function() {
		return that.width * that.height;
	};
	
	that.fits = function(obj) {
		return ( that.width > obj.width && that.height > obj.height );
	};
	
	that.intersects = function(obj) {
		return (
			(that.x < (obj.x + obj.width)) && 
			(that.x + that.width) > obj.x && 
			(that.y < (obj.y + obj.height)) && 
			((that.y + that.height) > obj.y)
		);
	};
	
	return that;
};

things.Slider = function(el, stepSize) {
	var that = {};
	var animating = false;
	var maxPos = 0;
	
	that.move = function(movement) {
		if( animating ) return;
		
		var pos = $(el).position().top;
		var newPos = (stepSize * movement) + pos;
		if(newPos > 0 || newPos < maxPos) return;
		
		animating = true;
		$(el).animate({'top':newPos}, 200, null, function(){ animating = false; });
	};
	
	function init() {
		maxPos = $(el).parent().height() - ($(el).children().length * stepSize);
	}
	init();
	
	return that;
};

things.BackgroundSelector = function( bgData ) {
	var that = {};
	var buttonEl = null;
	var selectEl = null;
	var slider = null;
	var backgroundData = bgData;
	var THUMBNAIL_PATH = '/static/backgrounds/thumbs/';
	
	function saveBackground() {
		if(things.snapshotChecker) { things.snapshotChecker.disableSnapshot(); }
		$.post(window.location.href, {'background':things.currentBgClass});
	}
	
	function onBackgroundSelect( bg ) {
		if( bg.class_name !== things.currentBgClass ) {
			things.setBackground( bg.class_name );
			saveBackground();
		}
		buttonEl.show(); 
		selectEl.hide();
		
		return false;
	}
	
	function onUp() {
		slider.move( 1 );
		return false;
	}
	
	function onDown() {
		slider.move( -1 );
		return false;
	}
	
	function createSelectEvent( bg ) {
		return function() { onBackgroundSelect( bg ); };
	}
	

	
	function init() {
		buttonEl = $( '#js-background-change-button' ).children().clone().appendTo( '#header' );
		selectEl = $( '#js-background-selector' ).children().clone().insertAfter(buttonEl).hide();
		var listEl = selectEl.find('.slide-wrapper ul');
		for(var i = 0; i < backgroundData.length; i++) {
			$('<li><img width="102" height="116" src="'+THUMBNAIL_PATH+backgroundData[i].thumbnail +'" /></li>').appendTo(listEl)
				.click(createSelectEvent(backgroundData[i]));
		}
		
		slider = things.Slider(listEl, 133);
		selectEl.find('.up').click(onUp);
		selectEl.find('.down').click(onDown);
		
		$(buttonEl).click(function(){ buttonEl.hide(); selectEl.show(); return false; });
	}
	init();
	
	return that;
};

things.SnapshotChecker = function() {
	var that = {};
	var pollTime = 5000;
	var pollUrl = window.location.href + 'snapshot/';
	var timeout = null;
	var buttonEl = $( '#snapshot-downloader' );
	var enabled = false;
	
	var doPoll = function() {
		$.ajax( {
			'method': 'get',
			'dataType': 'json',
			'url': pollUrl,
			'success': function( data, textStatus, request ) {
				that.setSnapshot( data.url );
			},
			'error': function( request, textStatus, errorThrown ) {
				that.schedulePoll();
			}
		} );
	};
	
	that.schedulePoll = function( ) {
		var timeout = setTimeout( doPoll, pollTime );
	};
	that.setSnapshot = function( url ) {
		enabled = true;
		buttonEl.attr( 'href', url );
		buttonEl.removeClass( 'disabled' );
	};
	
	that.disableSnapshot = function() {
		if( ! enabled) return;
		enabled = false;
		buttonEl.attr('href', '#');
		buttonEl.addClass('disabled');
		that.schedulePoll();
	};
	
	function init() {
		if(things.snapshotUrl && things.snapshotUrl !== '') {
			that.setSnapshot(things.snapshotUrl);
			return;
		}
		
		that.schedulePoll();
	}
	init();
	return that;
};

things.currentBgClass = null;
things.setBackground = function( bgClass ) {
	// always remove the none-bg first, because it's in the markup
	$( 'body' ).removeClass( 'none-bg' );
	if(things.currentBgClass) {
		$('body').removeClass(things.currentBgClass);
	}
	
	things.currentBgClass = bgClass;
	$('body').addClass(bgClass);
};
