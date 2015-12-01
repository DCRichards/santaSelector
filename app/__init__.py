"""
                 _...
              o_.-"`    `\
       .--.  _ `'-._.-'""-;     _
     .'    \`_\_  {_.-a"a-}  _ / \
   _/     .-'  '. {c-._o_.){\|`  |
  (@`-._ /       \{    ^  } \\ _/
   `~\  '-._      /'.     }  \}  .-.
     |>:<   '-.__/   '._,} \_/  / ())  
     |     >:<   `'---. ____'-.|(`"`
     \            >:<  \\_\\_\ | ;
      \                 \\-{}-\/  \
       \                 '._\\'   /)
        '.                       /(
          `-._ _____ _ _____ __.'\ \
            / \     / \     / \   \ \ 
     jgs _.'/^\'._.'/^\'._.'/^\'.__) \
     ,=='  `---`   '---'   '---'      )
     `"""""""""""""""""""""""""""""""`

     SANTA SELECTOR
     A Secret Santa Selector
     
     by DCRichards
"""


from flask import Flask
from flask.ext.cors import CORS

app = Flask(__name__, static_url_path='')
# set correct CORS headers on all outgoing requests
CORS(app)
# defined here otherwise we'll get a circular reference
from app import views, persistence