(function($, window, document, undefined) {
    'use strict';
    var animationObject;

    function addAnimation() {
        animationObject.each(function(index, element) {
            var $currentElement = $(element),
                animationType = $currentElement.attr('animation-type');

            if (onScreen($currentElement)) {
                $currentElement.addClass('animated ' + animationType);
            }
        });
    }

    // takes jQuery(element) a.k.a. $('element')
    function onScreen(element) {
        // window bottom edge
        var windowBottomEdge = $(window).scrollTop() + $(window).height();

        // element top edge
        var elementTopEdge = element.offset().top;
        var offset = 100;

        // if element is between window's top and bottom edges
        return elementTopEdge + offset <= windowBottomEdge;
    }

    $(window).load(function() {
        animationObject = $('[animation-type]');
        addAnimation();
    });

    $(window).on('scroll', function(e) {
        addAnimation();
    });
})(jQuery, window, document);