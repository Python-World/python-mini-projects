## Get meta information of images

### usage

python get_meta_from_pic.py image_file

### note

Make sure the picture contains location information, otherwise the location cannot be obtained

you need fill in your email address to use the function in gps_utils.py: 
```python
geolocator = Nominatim(user_agent = "your email")
```
