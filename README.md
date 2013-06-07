##Requirements
Make sure you have installed the Haskell Platform and runghc in your path.

Install Elm with:

`cabal install elm`

##Installtion

`python setup.py install` will install all needed files

Now you can add `elm` to your INSTALLED_APPS in your django project.

##Usage in templates
inline:

    <script type="text/javascript" src="{{ STATIC_URL }}js/elm-runtime.js"></script>
    {% load elm_compiler %}
    {% elminline %}
    import Mouse
    main = lift asText Mouse.position
    {% endelminline %}
    <script type="text/javascript">Elm.fullscreen(Elm.Main)</script>
