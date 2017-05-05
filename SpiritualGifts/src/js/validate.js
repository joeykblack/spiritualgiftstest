function validate_required(field,alerttxt)
{
	with (field)
	{
		if (value==null||value=="")
		{
			alert(alerttxt);
			return false;
		}
		else
		{
			return true;
		}
	}
}


function validate_match(field1,field2,alerttxt)
{
	if (field1.value!=field2.value)
	{
		alert(alerttxt);
		return false;
	}
	else
	{
		return true;
	}
}


function validate_form (thisform)
{
	with (thisform)
	{
		if (validate_required(firstname ,"First Name must be filled out.")==false)
		{
			firstname.focus();
			return false;
		}
		else if (validate_required(lastname ,"Last Name must be filled out.")==false)
		{
			lastname.focus();
			return false;
		}
		else if (validate_required(email ,"Email must be filled out.")==false)
		{
			email.focus();
			return false;
		}
		else if (validate_required(email2 ,"Confirm Email must be filled out.")==false)
		{
			email2.focus();
			return false;
		}
		else if (validate_match(email,email2,"Email addresses do not match.")==false)
		{
			email.focus();
			return false;
		}
		else if (validate_required(gender, "Please select a gender.")==false)
		{
			return false;
		}
		else if (validate_required(age, "Please select an age.")==false)
		{
			return false;
		}
		else if (validate_required(interest, "Please select an interest.")==false)
		{
			return false;
		}
		else if (validate_required(state, "Please select a state.")==false)
		{
			state.focus();
			return false;
		}
		else if (validate_required(country, "Please select a country.")==false)
		{
			country.focus();
			return false;
		}
		return true;
	}
}