import function

MobileNo = input("Enter the Mobile number:")
Checked_MobileNo = function.Validate_MobileNo(MobileNo)

Email = input("Enter the Email:")
Checked_email = function.Validate_Email(Email)

# will Generate OTP
OTP = function.Generate_OTP()

# send OTP to Number
function.send_OTP(Checked_MobileNo, OTP)

# send to email
function.send_email(Checked_email, OTP)
