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
![pedia urls validation](documentation/images/valpedu.png) | Pass: No Errors |


## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Home | Suggestion | Articles | Article detail | Notes |
| --- | --- | --- | --- | --- | --- |
| Chrome | ![Google Chrome, home page](documentation/images/chromeh.png) | ![Google Chrome, suggestion page](documentation/images/chromes.png) | ![Google Chrome, articles page](documentation/images/chromea.png) | ![Google Chrome, article detail page](documentation/images/chromead.png) | Works as expected |
| Firefox | ![Firsfox, home page](documentation/images/foxh.png) | ![Firefox, suggestion page](documentation/images/foxs.png) | ![Firefox, articles page](documentation/images/foxa.png) | ![Firefox, article detail](documentation/images/foxad.png) | The article detail page has elements that are much wider than they should. |
| Edge | ![Edge, home page](documentation/images/edgeh.png) | ![Edge, suggestion page](documentation/images/edges.png) | ![Edge, article page](documentation/images/edgea.png) | ![Edge, article details page](documentation/images/edgead.png) | Works as expected |


## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Browser | Home | Suggestion | Articles | Article detail | Notes |
| --- | --- | --- | --- | --- | --- |
| Mobile (DevTools) | ![mobile home screen](documentation/images/mobileh.png) | ![Mobile suggestion page](documentation/images/mobiles.png) | ![Mobile aticles page](documentation/images/mobilea.png) | ![Mobile article detail](documentation/images/mobilead.png) | Works as expected |
| Tablet (DevTools) | ![Tablet home screen](documentation/images/tableth.png) | ![tablet suggestion page](documentation/images/tablets.png) | ![Tablet articles page](documentation/images/tableta.png) | ![Tablet article detail](documentation/images/tabletad.png) | Works as expected |
| Desktop | ![Desktop home screen](documentation/images/desktoph.png) | ![Desktop suggestion page](documentation/images/desktops.png) | ![Desktop articles page](documentation/images/desktopa.png) | ![desktop article page](documentation/images/desktopad.png) | Works as expected |


## Lighthouse audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Home | ![Lighthouse audit mobile home](documentation/images/lighthousemh.png) | ![Lighthouse audit desktop home](documentation/images/lighthousedh.png) | Some minor warnings |
| Articles | ![Lighthouse audit mobile articles](documentation/images/lighthousema.png) | ![Lighthouse audit desktop articles](documentation/images/lighthouseda.png) | Slow response due to multiple images |
| Article detail | ![Lighthouse audit mobile article detail](documentation/images/lighthousemad.png) | ![Lighthouse audit desktop article detail](documentation/images/lighthousedad.png) | Slow response time due to images not having distinct sizes |


### Existing bugs

- Minor issue with articles page where cards overlap around the 760px to 560px width screens, fixing the issue results in the cards being different sizes and distorting the intended design outlook

### Solved Bugs

Dealt with various issues during develpoment including:
- App non functioning; forgot to place new app into installed apps section of settings.py
- Issue loading page; forgot to migrate after changing model
- Difficulty getting responsiveness; had to experiment with bootstrap classes until it was right
- Images not uploading when using form; added request.FILES to view
- Internal server error when deploying to heroku; commented out the STATIC_FILE_STORAGE in settings.py
- Edit article page was titled 'add an article' despite it being hardcoded to say 'edit article'; Coded an if statement onto the add article templte which seemed to work.
