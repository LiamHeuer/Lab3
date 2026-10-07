# Lab3
## Issues
- **Problem:** weather.gov doesn't give a forecast from coordinates directly.
  **Solution:** Use two API calls to create the forecast URL, then request that URL.
- **Problem:** An invalid city ended the program.
  **Solution:** Added a `while` loop that asks again and ends on `exit`, this also lets it loop to let them ask a different city's weather.
- **Problem:** I had problems with uploading to the repo from onedrive
  **Solution:** Cloned the repo first, then copied my files into it.
- **Problem:** certain modules weren't found when the program was run.
  **Solution:** I changed the python interpreter path to one that had it.
  
- I think I have very few commits because I had a problem with my project being on OneDrive, so I created a new folder and moved them to my local drive. I've never used github before and this took ages to figure out.

## Limitations
- Only works for US locations
- Cities are hardcoded because each needs coordinates
