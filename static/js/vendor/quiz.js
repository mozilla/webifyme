var things = things || {};

things.Quiz = function() {
  var that = {};
  var ANIMATE_TIME = 500;
  
  var questions = {};
  var questionCount = 0;
  var answers = {};
  var questionEl = $('#question-body');
  var activeEl = questionEl;
  var backBtn = $('#question-container').find('.quiz-nav .back');
  var skipBtn = $('#question-container').find('.quiz-nav .skip');
  var finishBtn = $('#question-container').find('.quiz-nav .get-your-results-btn');
  var skipRestBtn = $('#question-container').find('.quiz-nav .skipRest');
  var quizForm = null;
  var qIdx = 0;
  var showingForm = false;
  var skipCounter = 0;
  var animating = false;
  var imagePath = '/static/objects/medium/';
  var progressImages = [];
  
  
  var minQuestionHeight = 200;
  var lastQuestionHeight = null;
  
  
  function onAnswerClick(answer, el) {
    if(animating) return;
    
    answers[questions[qIdx]['id']] = answer['id'];
    changeQuestion(qIdx + 1);
    revealImage(qIdx);
    
    return false;
  }
  
  function onSkipClick() {
    if(animating) return;
    
    if(qIdx < questions.length) {
      //remove any previous answers to this question, if they exist
      if(answers[questions[qIdx]['id']]) {
        delete answers[questions[qIdx]['id']];
      }
      skipCounter++; //TODO: what if the user goes back and answers it
    }
    changeQuestion(qIdx + 1);
    
    return false;
  }
  
  function onSkipRestClick() {
      if(animating) return;
      
      if(qIdx < questions.length) {
          skipCounter += questions.length - qIdx;
          
          qIdx = questions.length;
          
          changeQuestion(qIdx);
      }
      return false;
  }
  
  function onBackClick() {
    if(animating) return;
    
    changeQuestion(qIdx - 1);
    
    return false;
  }
  
  function changeQuestion(idx) {
    if(idx > questions.length) {
      submitAnswers();
    } else if( idx < 0 ) {
      return;
    } else {    
      qIdx = idx;
      animating = true;
      //lastQuestionHeight = questionEl.height();
      activeEl.fadeOut(ANIMATE_TIME, function(){
        animating = false;
        if( qIdx < questions.length ) {
          populateQuestion();
        } else {
          showForm();
        }
      });
    }    
  }
  
  function placeImage(idx) {
            
  }
  
  function createAnswer(answer, i) {
    return $( '<a href="#">' + $._( 'msg-alphabet', i ) + ') ' + answer['answer'] + '</a>' ).click( function() {
      return onAnswerClick(answer, this);
    });
  }
  
  function moveProgressBar() {
    var progressWidth = Math.floor(qIdx/questionCount * 100);
    $('#question-container .progress').animate({'width':progressWidth+'%'}, ANIMATE_TIME);
    $('#question-container .progress .label span').text( $._( 'msg-more-to-go', questionCount - qIdx ) );
  }
  
  function populateQuestion() {
    activeEl = questionEl;
    questionEl.find('.question-num').text( $._( 'msg-question' ) + ' ' + ( qIdx + 1 ) + ':' );
    questionEl.find('.question').text(questions[qIdx]['question']);
    questionEl.find('.answers').html('');
    for(var i = 0, ii = questions[qIdx]['answers'].length; i < ii; i++) {
      $('<li></li>').append(createAnswer(questions[qIdx]['answers'][i], i)).appendTo(questionEl.find('.answers'));
    }
		
		if( qIdx === 0 ) {
			// if this is the first question, show the note
			$( '.question-note' ).show();
		} else {
			// if it's not the first question, hide the note
			$( '.question-note' ).hide();
		}
    /*var newHeight = questionEl.height();
    newHeight = (newHeight > minQuestionHeight) ? newHeight : minQuestionHeight;
    
    if(newHeight != lastQuestionHeight) {
      questionEl.height(lastQuestionHeight);
      questionEl.animate({'height':newHeight}, ANIMATE_TIME, null, function(){ questionEl.height('auto'); });
    }*/
    skipBtn.text( $._( 'msg-skip' ) );
    questionEl.fadeIn(ANIMATE_TIME);
    moveProgressBar();
    if(qIdx == 10) {
        skipRestBtn.fadeIn(ANIMATE_TIME);
    }
  }
  
  function showForm() {
    activeEl = $('#form-body');
    activeEl.fadeIn(ANIMATE_TIME);
    //skipBtn.text('Finish');
    moveProgressBar();
    skipBtn.fadeOut(ANIMATE_TIME);
    skipRestBtn.fadeOut(ANIMATE_TIME);
    $('#question-container .progress-bar').hide();
    $('#question-container .get-your-results-btn').css('display','block');
  }
  
	function prepForm() {
		var formData = quizForm.read();
    if(formData) {
      for( var k in formData ) { answers[k] = formData[k]; }
    } else {
      //didn't validate
      showForm();
      return false;
    }
		// add all the answers to the form
		var $form = $( '#form-body form' );
    for( var qid in answers ) {
      if(answers.hasOwnProperty(qid)) {
        $form.append('<input type="hidden" name="'+qid+'" value="'+answers[qid]+'">');
      }
    }
    return true;
	}
	
  function submitAnswers() {
    var formData = quizForm.read();
    if(formData) {
      for(var k in formData) { answers[k] = formData[k]; }
    } else {
      //didn't validate
      showForm();
      return;
    }
    console.log(answers);
		// add all the answers to the form
		var $form = $( '#form-body form' );
    for( var qid in answers ) {
      if(answers.hasOwnProperty(qid)) {
        $form.append('<input type="hidden" name="'+qid+'" value="'+answers[qid]+'">');
      }
    }
    $form.submit();
  }

	function placeImages() {
		var positions = [-200, -100, 300, 250, 150];
		// add a container 
		var $imgContainer = $( '<div />' )
			.attr( 'id', 'progress_images_container' )
			.addClass( 'autoResize' )
			.bind( 'resize.autoResize', function( e, availableSpace ) {
				// if the screen width drops below 600, hide all the images and set the the bodies overflow-x to scroll
			} )
			.appendTo( '#question-container' );
		for( var i = 0; i < things.images.length; i++ ) {
			var $container = $( '<div />' )
				.addClass( 'object_progress' )
				.append( $( '<img />' )
					.attr( 'src', imagePath + things.images[i].file_name ) );
			// add it to the dom
			$container.appendTo( $imgContainer );
			// hide it
			$container.hide();
			$container.css( 'top', positions[i] );
			$container.data( 'left', i % 2 )
			progressImages.push( $container );
		}
	}
  
	function revealImage(idx) {
		var containers = [];
		switch( idx ) {
			case 2: 
				containers.push( progressImages[0] );
				break;
			case 5:
				containers.push( progressImages[1] );
				containers.push( progressImages[2] );
				break;
			case 8:
				containers.push( progressImages[3] );
				containers.push( progressImages[4] );
				break;
			default: 
				return;
		}
		$.each( containers, function() {
			var $container = $( this );
			// measure and then hide
			$container.show();
			var imgWidth = $container.find( 'img' ).width();
			var imgHeight = $container.find( 'img' ).height();
			$container.width( imgWidth ).height( imgHeight ).hide();
			// randomize buffer space
			var bufferSpace = Math.round( Math.random() * 200 ) + 50;
			// alternate sides
			if( !$container.data( 'left' ) ) {
				$container
					.css( 'left', - ( imgWidth + bufferSpace ) );
			} else {
				$container
					.css( 'left', 676 + bufferSpace );
			}
			$container.fadeIn( ANIMATE_TIME );
		} );
  }
  
  function init() {
    if( ! things.quizQuestions) return;
    
    quizForm = things.QuizForm($('#form-body'));
    
    questions = things.quizQuestions;
    questionCount = things.quizQuestions.length;
    questionEl.css({'min-height':minQuestionHeight});
    questionEl.parent().css({'min-height':minQuestionHeight});
    
    backBtn.click(onBackClick);
    skipBtn.click(onSkipClick);
    skipRestBtn.click(onSkipRestClick);
    questionEl.hide();
    populateQuestion();
    placeImages();
		$( '#form-body form' ).submit( function( e ) {
			return prepForm();
		} );
		$( '.get-your-results-btn' ).click( function( e ) {
			e.preventDefault();
			$( '#form-body form' ).submit();
		} )
  }
  init();
  
  return that;
}

things.QuizForm = function(el) {
  var that = {};
  var data = {};
  var errors = [];
  
  that.read = function() {
    clearErrors();
    data = {};
    
    data['email'] = $('#email-field').val();
    data['username'] = $('#name-field').val();
    data['download_reminder'] = $('#download-reminder-field').attr('checked');
    data['gallery_include'] = $('#gallery-include-field').attr('checked');
    
    if(validate()) {
      return data;
    }
    return false;
  }
  
  function validate() {
    var name_re = /^[A-Za-z0-9_\'\-!\. ]{1,50}$/
    if( ! name_re.test(data['username'])) {
      addError('name', $._( 'msg-name-required-error' ) );
    }
    
    if( data['download_reminder'] || data['email'] ) {
      //email is required if download reminder is requested
      var email_re = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i
      if( ! email_re.test(data['email'])) {
        addError('email', $._( 'msg-email-required-error' ) )
      }
    }
    
		if( data['email'] && !data['download_reminder'] ) {
			addError( 'download-reminder', $._( 'msg-privacy-policy-required-error' ) )
		}
    return (errors.length > 0) ? false : true;
  }
  
  function clearErrors() {
    errors = [];
    el.find('.error').remove();
  }
  
  function addError(field, error) {
    errors[errors.length] = field;
    $('#'+field+'-field').parent().append('<div class="error"><span>'+error+'</span></div>');
  }
  
  return that;
}