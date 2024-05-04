$(document).ready(function() 
{
    var scrollTrigger = $('#Language').outerHeight()+$('#Title').outerHeight(); // Set scroll trigger point (navbar height + offset)
    var largeScreen = 992;
  
    function navSetup()
    {
      if ($(window).scrollTop() > scrollTrigger && $(window).width() >= largeScreen)
      {
        $('#MenuBar').addClass('fixed-top');
        $('#Home').addClass('d-none');
        $('#NavSearch').addClass('d-none');
        $('#NavLogo').removeClass('d-none');
        $('#NavLogin').removeClass('d-none');
      } else 
      {
        $('#MenuBar').removeClass('fixed-top');
        $('#Home').removeClass('d-none');
        $('#NavSearch').removeClass('d-none');
        $('#NavLogo').addClass('d-none');
        $('#NavLogin').addClass('d-none');
      }
    }

    // Call navSetup() on scroll
    $(window).scroll(function() 
    {
      navSetup();
    });

    // Call navSetup() on page load
    navSetup();  

    function toggleMenu(menuName) 
    {
      $('#' + menuName + 'MenuBtn').click(function() {

          $('#' + menuName + 'Menu').toggleClass('d-none');
  
          if($('#' + menuName + 'Menu').is(':visible')) {
              $('body').addClass('overflow-hidden');
              $('#DropDownMenu').addClass('my-shadow');
              $('#' + menuName + 'MenuBtn').parent().addClass('my-dropdown-menu-active');
          } else {
              $('body').removeClass('overflow-hidden');
              $('#DropDownMenu').removeClass('my-shadow');
              $('#' + menuName + 'MenuBtn').parent().removeClass('my-dropdown-menu-active');
          }
  
          var dropdownMenus = $('.my-dropdown-menu').not('#' + menuName + 'Menu');

          for (var i = 0; i < dropdownMenus.length; i++) 
          {
            $(dropdownMenus[i]).addClass('d-none');
            $('#' + dropdownMenus[i].id + 'Btn').parent().removeClass('my-dropdown-menu-active');
          }

      });
    }

    toggleMenu('Actualites');
    toggleMenu('Economie');
    toggleMenu('Videos');
    toggleMenu('Debats');
    toggleMenu('Culture');
    toggleMenu('LeGoutDuMonde');
    toggleMenu('Services');
     
  });    
  

 