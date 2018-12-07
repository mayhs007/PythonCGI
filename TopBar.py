print ('<div id="app">');
        print ('<nav class="navbar navbar-default navbar-static-top">');
            print ('<div class="container">');
                print ('<div class="navbar-header">');

                   # <!-- Branding Image -->
                    print ('<a class="navbar-brand">');
                   print ('     BANK');
                    print ('</a>');
                print ('</div>');

                print ('<div class="collapse navbar-collapse" id="app-navbar-collapse">');
                 print ('   <!-- Left Side Of Navbar -->');
                print ('    <ul class="nav navbar-nav">');
                   print ('     &nbsp;');
                 print ('   </ul>');

                print ('    <!-- Right Side Of Navbar -->');
                print ('    <ul class="nav navbar-nav navbar-right">');
                     print ('   <!-- Authentication Links -->');
                  print ('      @guest');
                  print ('          <li><a href="">Login</a></li>');
                  print ('          <li><a href="">Register</a></li>');
                       print (' @else');
                            print ('<li class="dropdown">');
                               print (' <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false" aria-haspopup="true">');
                                 print ('   {{ Auth::user()->name }} <span class="caret"></span>');
                               print (' </a>');

                                print ('<ul class="dropdown-menu">');
                                   print (' <li>
                                       print (' <a href="{{ route('logout') }}"');
                                            print ('onclick="event.preventDefault();');
                                           print ('          document.getElementById('logout-form').submit();">');
                                           print (' Logout');
                                        print ('</a>');

                                       print (' <form id="logout-form" action="{{ route('logout') }}" method="POST" style="display: none;">');
                                          print ('  {{ csrf_field() }}');
                                       print (' </form>');
                                   print (' </li>');
                              print ('  </ul>');
                            print ('</li>');
                        @endguest
                  print ('  </ul>');
             print ('   </div>');
          print ('  </div>');
      print ('  </nav>');

   print (' </div>');