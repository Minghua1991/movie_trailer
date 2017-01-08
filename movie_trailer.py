import webbrowser
import os
import re
import csv

# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html class="no-js" lang="">
    <head>
        <!-- Site Title -->
        <title>Hippo Movie Trailer: home</title>
        <!-- Site Meta Info -->
        <meta charset="utf-8">
        <meta http-equiv="x-ua-compatible" content="ie=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="description" content="Effacy is a bootstrap3 based creative one page HTML5 Template.">
        <meta name="keywords" content="creative, html5, portfolio, parallax, personal, responsive">
        <meta name="author" content="themebite.com">
        <!-- Essential CSS Files -->
        <link rel="stylesheet" href="assets/css/normalize.css">
        <link rel="stylesheet" href="assets/css/font-awesome.min.css">
        <link rel="stylesheet" href="assets/css/animate.css">
        <link rel="stylesheet" href="assets/css/simplelightbox.min.css">
        <link rel="stylesheet" href="assets/css/bootstrap.min.css">
        <link rel="stylesheet" href="assets/css/owl.carousel.css">
        <link rel="stylesheet" href="assets/css/owl.theme.css">
        <link rel="stylesheet" href="assets/css/style.css">
        <!--modal style css file-->
        <link rel="stylesheet" href="assets/css/modal.css">
        <!-- Responsive CSS -->
        <link rel="stylesheet" href="assets/css/responsive.css">
        <!-- Google Web Fonts =:= Raleway , Montserrat and Roboto -->
        <link href='https://fonts.googleapis.com/css?family=Raleway:400,500,600,700' rel='stylesheet' type='text/css'>
        <link href='https://fonts.googleapis.com/css?family=Montserrat:700,400' rel='stylesheet' type='text/css'>
        <link href='https://fonts.googleapis.com/css?family=Roboto:700,500,400' rel='stylesheet' type='text/css'>
        <!-- Essential JS Files -->
        <script src="assets/js/vendor/jquery-1.11.3.min.js"></script>
        <script src="assets/js/vendor/modernizr-2.8.3.min.js"></script>
        <!--modal js file-->
        <script src="assets/js/modal.js"></script>
        <!-- IE9 Scripts -->
        <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
        <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
        <![endif]-->
    </head>
'''

# The main page layout and title bar
main_page_content = '''
    <body>
        <!-- Heaser Area Start -->
        <header class="header-area">
            <!-- Navigation start -->
            <nav class="navbar navbar-custom tb-nav" role="navigation">
                <div class="container">
                    <div class="navbar-header">
                        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#tb-nav-collapse">
                        <span class="sr-only">Toggle navigation</span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        </button>
                        <a class="navbar-brand logo" href="#">
                            <h2>Hipp<span>o</span></h2>
                        </a>
                    </div>
                    <div class="collapse navbar-collapse" id="tb-nav-collapse">
                        <ul class="nav navbar-nav navbar-right">
                            <li class="active"><a class="page-scroll" href="#top">Home</a></li>
                            <li><a class="page-scroll" href="#blog">Movie</a></li>
                        </ul>
                    </div>
                </div>
            </nav>
        </header>
        <!-- Navigation end -->
        <!-- hero-section -->
        <section class="hero-section static-bg" id="top">
            <div class="slider-caption">
                <div class="container">
                    <div class="row">
                        <!-- Hero Title -->
                        <h1>Top Rated <span>Movies</span></h1>
                        <!-- Hero Subtitle -->
                        <h5>Art is an experience and every human need to get connect with any form of art for inspiration</h5>
                    </div>
                </div>
            </div>
        </section>
        <!-- End Of Hero Section -->
        <!-- BLog Section Start -->
        <section class="blog-section section-padding" id="blog">
            <div class="container">
                <!-- Blog Section Title -->
                <h2 class="section-title text-center">"When you realize you want to spend the rest of your life with somebody, you want the rest of your life to start as soon as possible."</h2>
                <p class="sub-title text-center">When Harry Met Sally, 1989</p>
                <div class="row mt-80 blog-section-padding">
                    <!-- Blog Post Carousel -->
                    <div id="blog-post-carousel" class="owl-carousel owl-theme">
                        {movie_tiles}
                    </div>
                </div>
            </div>
        </section>
        <!-- End Of Our Partners Section -->
        <!-- Trailer Video Modal -->
        <div class="modal" id="trailer">
            <div class="modal-dialog">
                <div class="modal-content">
                    <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
                    <img src="assets/img/close_button.png">
                    </a>
                    <div class="scale-media" id="trailer-video-container">
                    </div>
                </div>
            </div>
        </div>
        <!-- Footer Section -->
        <footer class="footer-section">
            <div class="container">
                <div class="row mt-30 mb-30">
                    <div class="col-md-12 text-center">
                        <!-- Footer Copy Right Text -->
                        <div class="copyright-info">
                            <a href="#">Theme Designed <span><i class="fa fa-heart"></i></span> By <span>ThemeBite</span></a>
                        </div>
                        <!-- Footer Social Icons -->
                        <div class="social-icons mt-30">
                            <a href="#"><i class="fa fa-facebook"></i></a>
                            <a href="#"><i class="fa fa-twitter"></i></a>
                            <a href="#"><i class="fa fa-google-plus"></i></a>
                            <a href="#"><i class="fa fa-github"></i></a>
                        </div>
                    </div>
                </div>
            </div>
        </footer>
        <!-- End Of Footer Section -->
        <!-- JS Files -->
        <!-- Bootstrap JS -->
        <script src="assets/js/bootstrap.min.js"></script>
        <!-- jQuery Easing -->
        <script src="assets/js/jquery.easing.min.js"></script>
        <!-- PreLoader -->
        <script src="assets/js/queryloader2.min.js"></script>
        <!-- WOW JS Animation -->
        <script src="assets/js/wow.min.js"></script>
        <!-- Simple Lightbox -->
        <script src="assets/js/simple-lightbox.min.js"></script>
        <!-- Sticky -->
        <script src="assets/js/jquery.sticky.js"></script>
        <!-- OWL-Carousel -->
        <script src="assets/js/owl.carousel.min.js"></script>
        <!-- jQuery inview -->
        <script src="assets/js/jquery.inview.js"></script>
        <!-- Shuffle jQuery -->
        <script src="assets/js/jquery.shuffle.min.js"></script>
        <!-- jQuery CountTo -->
        <script src="assets/js/jquery.countTo.js"></script>
        <!-- Main JS -->
        <script src="assets/js/main.js"></script>
    </body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
                        <!-- Single BLog Post 1 -->
                        <div class="item" >
                            <article class="single-blog-post">
                                <!-- BLog Post Image -->
                                <div class="col-md-6 blog-post-image">
                                    <figure class ="movie-tile" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
                                        <img class="img-responsive img-thumbnail" src="{poster_image_url}" style="width:450px;height:550px;">
                                    </figure>
                                </div>
                                <!-- Blog Post Details -->
                                <div class="col-md-5 col-md-offset-1 blog-post-details mt-30">
                                    <!-- Blog Post Heading -->
                                    <div class="post-heading mb-30">
                                        <h2>{title}</h2>
                                        <em>{release_year}</em>
                                    </div>
                                    <p>{description}</p>
                                    <a href="{watch_url}"><button class="btn-primary read-more-btn mt-30" >Watch Now</button></a>
                                </div>
                            </article>
                        </div>
'''

#create movie elements for every movie
def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            release_year=movie.release_year,
            description=movie.description,
            watch_url=movie.watch_url
        )
    return content

#finalise the html and launch it
def open_movies_page(movies):
  # Create or overwrite the output file
  output_file = open('index.html', 'w') #the first parameter is the file path

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))

  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible
  
  
  
class Movie():
    """This class provides a way to store movie related information"""
    #Constructor for Movie class
    def __init__(self, title, poster_image_url,
                trailer_youtube_url, release_year,
                description,watch_url):
        self.title = title
        self.poster_image_url=poster_image_url
        self.trailer_youtube_url=trailer_youtube_url
        self.release_year=release_year
        self.description=description
        self.watch_url=watch_url
        
        
# use csv module to fetch info from csv file. 
def get_all_movie_data(filename):
    """ fetch movie data from csv file and return a collection of all movie object """
    movies = []
    with open(filename, 'rb') as csvfile:
        reader = csv.DictReader(csvfile)
        for movie in reader:
            movies.append(Movie(title=movie['title'],
                                poster_image_url=movie['poster_image_url'],
                                trailer_youtube_url=movie['trailer_youtube_url'],
                                release_year=movie['release_year'],
                                description=movie['description'],
                                watch_url=movie['watch_url'],
                                ))
    return movies

#fetch info from csv file and create a collection of all movies instance    
movies=get_all_movie_data('all_movie_data.csv')  #don't forget to add file extension    

#generate html and launch it
open_movies_page(movies)
