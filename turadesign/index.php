<?php
    $lang = substr($_SERVER['HTTP_ACCEPT_LANGUAGE'], 0, 2);
    $acceptLang = ['en', 'es'];
    $lang = in_array($lang, $acceptLang) ? $lang : 'en';
?>


<!doctype html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="favicon.ico">

    <title>Alex Turati</title>

    <!-- Bootstrap core CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <!-- Font awesome -->
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.1/css/all.css" integrity="sha384-50oBUHEmvpQ+1lW4y57PTFmhCaXp0ML5d60M1M7uH2+nqUivzIebhndOJK28anvf" crossorigin="anonymous">
    <!-- Fancy App v3 -->
    <script src="//code.jquery.com/jquery-3.3.1.min.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/fancyapps/fancybox@3.5.7/dist/jquery.fancybox.min.css" />
    <script src="https://cdn.jsdelivr.net/gh/fancyapps/fancybox@3.5.7/dist/jquery.fancybox.min.js"></script>
    <!-- GOOGLE FONT -->
    <link href="https://fonts.googleapis.com/css?family=Abel" rel="stylesheet">
    <!-- CUSTOM CSS -->
    <link href="css/update.css" rel="stylesheet">
</head>

<body>
    <div class="d-flex align-items-center justify-content-center vertical-center">
        <div class="container">
            <div class="row d-flex justify-content-center flex-wrap-reverse">
                <div class="col-sm-6 col-md-7 col-lg-7 col-12 bg-* bg-mint d-flex align-items-center py-4">
                    <div class="text-center col-12">
                        <h1 class="display-4">Alex Turati Schnaider</h1>

                        <?php
    if ($lang == 'es') {
        echo '<p class="lead">Sitio en Remodelación</p>
        <p>Redes Sociales, Portafolio y/o Contacto.</p>';
    } else {
        echo '<p class="lead">Site is being Re-Designed</p>
        <p>Social Media, Portfolio & Contact</p>';
    }
?>

                        <p class="lead text-center">
                            <a href="https://twitter.com/taftera" target="_blank" class="link-mint"><i class="fab fa-twitter mx-2"></i></a>
                            <a href="https://www.behance.net/taftera" target="_blank" class="link-mint"><i class="fab fa-behance mx-2"></i></a>
                            <a href="https://github.com/taftera/" target="_blank" class="link-mint"><i class="fab fa-github mx-2"></i></a>
                            <a href="tel:+5215551044492" target="_blank" class="link-mint"><i class="fas fa-mobile-alt mx-2"></i></a>
                            <a href="mailto:a.turati@gmail.com" class="link-mint"><i class="far fa-envelope mx-2"></i></a>
                        </p>
                    </div>
                </div>
                <div class="col-sm-6 col-md-5 col-lg-4 col-12 no-padding"><img src="img/profile_650.jpg" class="img-fluid"></div>
            </div>
        </div>
    </div>

    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script>
        window.jQuery || document.write('<script src="../../assets/js/vendor/jquery-slim.min.js"><\/script>')
    </script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
</body>

</html>
