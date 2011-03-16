var things = things || {};

things.Quiz = function() {
  var that = {};
  var ALPHABET = ['A','B','C','D','E','F','G','H','I','J','K','L'];
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
    return $('<a href="#">'+ALPHABET[i]+') '+answer['answer']+'</a>').click(function(){
      return onAnswerClick(answer, this);
    });
  }
  
  function moveProgressBar() {
    var progressWidth = Math.floor(qIdx/questionCount * 100);
    $('#question-container .progress').animate({'width':progressWidth+'%'}, ANIMATE_TIME);
    $('#question-container .progress .label span').text((questionCount - qIdx)+' More to go');
  }
  
  function populateQuestion() {
    activeEl = questionEl;
    questionEl.find('.question-num').text('Question '+(qIdx+1)+':');
    questionEl.find('.question').text(questions[qIdx]['question']);
    questionEl.find('.answers').html('');
    for(var i = 0, ii = questions[qIdx]['answers'].length; i < ii; i++) {
      $('<li></li>').append(createAnswer(questions[qIdx]['answers'][i], i)).appendTo(questionEl.find('.answers'));
    }
    
    /*var newHeight = questionEl.height();
    newHeight = (newHeight > minQuestionHeight) ? newHeight : minQuestionHeight;
    
    if(newHeight != lastQuestionHeight) {
      questionEl.height(lastQuestionHeight);
      questionEl.animate({'height':newHeight}, ANIMATE_TIME, null, function(){ questionEl.height('auto'); });
    }*/
    skipBtn.text('Skip');
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
  
  function submitAnswers() {
    var formData = quizForm.read();
    if(formData) {
      for(k in formData) { answers[k] = formData[k]; }
    } else {
      //didn't validate
      showForm();
      return;
    }
    
    var form = $('<form method="POST" action="/quiz/"></form>');
    for( var qid in answers ) {
      if(answers.hasOwnProperty(qid)) {
        form.append('<input type="hidden" name="'+qid+'" value="'+answers[qid]+'">');
      }
    }
    form.appendTo($('body')).submit();
  }
  
  function placeImages() {
      var positions = [200, 200, 500, 500, 300];
      
      for(var i = 0; i < things.images.length; i++) {
          var divContainer = document.createElement("div");
          var img = document.createElement("img");
          img.src = imagePath + things.images[i].file_name;
          divContainer.className = "object_progress";
          divContainer.style.position = "absolute";
          
          if(i % 2) {
              divContainer.style.left = "-" + (things.images[i].width / 2) + "px";
          } else {
              divContainer.style.right = 0;
              divContainer.style.width = (things.images[i].width / 2) + "px";
          }
          
          divContainer.style.top = positions[i] + "px";
          $("#question-container").append(divContainer);
          divContainer.appendChild(img);
          progressImages.push(divContainer);
      }
  }
  
  function revealImage(idx) {
      switch(idx) {
          case 2:
            $(progressImages[0]).fadeIn(ANIMATE_TIME);
            break;
          case 5:
            $(progressImages[1]).fadeIn(ANIMATE_TIME);
            $(progressImages[2]).fadeIn(ANIMATE_TIME);
            break;
          case 8:
            $(progressImages[3]).fadeIn(ANIMATE_TIME);
            $(progressImages[4]).fadeIn(ANIMATE_TIME);
            break;
      }
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
    finishBtn.click(onSkipClick);
    skipRestBtn.click(onSkipRestClick);
    questionEl.hide();
    populateQuestion();
    placeImages();
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
      addError('name','Name required, may only use alphanumeric characters.');
    }
    
    if(data['download_reminder']) {
      //email is required if download reminder is requested
      var email_re = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i
      if( ! email_re.test(data['email'])) {
        addError('email','Valid email required.')
      }
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