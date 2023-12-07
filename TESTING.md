# Testing

Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Page | W3C URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2FCharlB96.github.io%2FCapstoneProject-Obscuripedia%2Findex.html) | ![home page validation](documentation/images/valhome.png) | Pass: No Errors |
| Suggestion | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2FCharlB96.github.io%2FCapstoneProject-Obscuripedia%2Fsuggestion.html) | ![Suggestion validation](documentation/images/valsug.png) | Pass: No Errors |
| Sign out | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2FCharlB96.github.io%2FCapstoneProject-Obscuripedia%2Flogout.html) | ![Sign out validation](documentation/images/valout.png) | Pass: No Errors |
| Login | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2FCharlB96.github.io%2FCapstoneProject-Obscuripedia%2Flogin.html) | ![login validation](documentation/images/vallog.png) | Pass: No Errors |
| Register | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2FCharlB96.github.io%2FCapstoneProject-Obscuripedia%2Fsignup.html) | ![Register validation](documentation/images/valreg.png) | Validation claims floating elements, but the elements are all present. Django allauth was used for this page so there may be an issue in the baseline code for that |
| Articles | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2FCharlB96.github.io%2FCapstoneProject-Obscuripedia%2Fpedia.html) | ![Articles validation](documentation/images/valart.png) | Pass: No Errors |
| Article detail | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2FCharlB96.github.io%2FCapstoneProject-Obscuripedia%2Fpedia/20.html) | ![Article detail validation](documentation/images/valartd.png) | Pass: No Errors |
| Add article | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2FCharlB96.github.io%2FCapstoneProject-Obscuripedia%2Fpedia/add.html) | ![Add article validation](documentation/images/valadd.png) | Pass: No Errors |
| Edit article | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2FCharlB96.github.io%2FCapstoneProject-Obscuripedia%2Fpedia/edit_article/20.html) | ![Edit article validation](documentation/images/valedit.png) | Pass: No Errors |


### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.


| File | Jigsaw URL | Screenshot | Notes |
| --- | --- | --- | --- |
| base.css | [Jigsaw](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2FCharlB96.github.io%2FCapstoneProject-Obscuripedia) | ![css validation](documentation/images/valcss.png) | Pass: No Errors |


### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| main settings.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/CharlB96/capstoneproject-obscuripedia/main/settings.py) | ![Settings.py validation text](documentation/images/valsett.png) | Pass: No Error |
| home views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/CharlB96/capstoneproject-obscuripedia/home/views.py) | ![Home views validation](documentation/images/valhv.png) | Pass: No Error |
| home urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/CharlB96/capstoneproject-obscuripedia/home/urls.py) | ![home urls validation](documentation/images/valhu.png) | Pass: No Errors |
| suggestion models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/CharlB96/capstoneproject-obscuripedia/suggestion/models.py) | ![Suggestion model validation](documentation/images/valsuggm.png) | Pass: No Errors |
| suggestion views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/CharlB96/capstoneproject-obscuripedia/suggestion/views.py) | ![Suggestion view validation](documentation/images/valsuggv.png) | Pass: No Errors |
| suggestion forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/CharlB96/capstoneproject-obscuripedia/suggestion/forms.py) | ![Suggestion forms validation](documentation/images/valsuggf.png) | Pass: No Errors |
| suggestion urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/CharlB96/capstoneproject-obscuripedia/suggestion/urls.py) |![Suggestion urls validation](documentation/images/valsuggu.png) | Pass: No Errors |
| pedia models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/CharlB96/capstoneproject-obscuripedia/pedia/models.py) | ![pedia models validation](documentation/images/valpedm.png) | Pass: No Errors |
| pedia views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/CharlB96/capstoneproject-obscuripedia/pedia/views.py) | ![pedia views validation](documentation/images/valpedv.png) | Pass: No Errors |
| pedia admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/CharlB96/capstoneproject-obscuripedia/pedia/admin.py) | ![pedia admin validation](documentation/images/valpeda.png) | Pass: No Errors |
| pedia fomrs.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/CharlB96/capstoneproject-obscuripedia/pedia/forms.py) | ![pedia forms validation](documentation/images/valpedf.png) | Pass: No Errors |
| pedia urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/CharlB96/capstoneproject-obscuripedia/pedia/urls.py) | 
![pedia urls validation](documentation/images/valpedv.png) | Pass: No Errors |
