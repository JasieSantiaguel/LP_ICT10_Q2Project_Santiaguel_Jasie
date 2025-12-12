from js import document, console

# Simple club descriptions (currently the club name; you can expand these later)
club_descriptions = {
	"Drawing Club": "Our drawing club aims to target students' maximum capacity in sketching and capturing the different aspects of life. This club is held every thursday at 3PM, led by Ms. Sunflower.",
	"Painters Club": "Our painters club allows students to fully express their emotions and feelings. Led by Mrs. Yueno every 3:30PM (Friday), Painters Club focuses on abstract and realism.",
	"Sculpting Club": "Our sculpting club, led by Mr. Kiko every 3PM (Monday), ensures that students would be able to precisely shape and mold clay into whatever they desire, increasing their artistic capabilities. ",
}


def show_club_description(*args, **kwargs):
	"""Called by the button's `py-click`. Shows a description for the selected club."""
	
    
	try:
		club_select = document.getElementById("club-select")
		if club_select is None:
			console.log("club-select element not found")
			return

		selected_club = club_select.value
		desc_area = document.getElementById("description-area")
		if desc_area is None:
			console.log("description-area element not found")
			return

		if selected_club and selected_club in club_descriptions:
			# show club name (you can replace this with full description text)
			desc_html = f"<h3 style='color: white;'>{club_descriptions[selected_club]}</h3>"
		else:
			desc_html = "<p style='color: white;'>Please select a club first.</p>"

		desc_area.innerHTML = desc_html
	except Exception as e:
		console.log("Error in show_club_description:", e)