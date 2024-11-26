const select_element = document.querySelector("#id_user_type");
const username_field = document.querySelector("#id_username");
const email_field = document.querySelector("#id_email");
const password = document.querySelector("#id_password1");
const confirm_pass = document.querySelector("#id_password2");

const validateSelect = () => {
  return select_element.value === "";
};

const validateUsername = () => {
  return username_field.value == "";
};

const validateEmail = () => {
  return !/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/.test(
    email_field.value
  );
};

const validateFirstPassword = () => {
  return password.value == "";
};

const validateSecondPassword = () => {
  return password.value != confirm_pass.value;
};

const validateSelectMsg = () => {
  const res = validateSelect();
  if (res) {
    select_element.classList.add("error-focus");
    document.querySelector("#select-msg").innerHTML = "Choose one!";
  } else {
    select_element.classList.remove("error-focus");
    document.querySelector("#select-msg").innerHTML = "";  
  }
  validateFields();
};


const validateUsernameMsg = () => {
  const res = validateUsername();
  if (res) {
    username_field.classList.add("error-focus");
    document.querySelector("#username-msg").innerHTML =
      "Field cannot be empty!";
  } else {
    username_field.classList.remove("error-focus");
    document.querySelector("#username-msg").innerHTML = "";

  }
  validateFields();
};

const validateEmailMsg = () => {
  const res = validateEmail();
  if (res) {
    email_field.classList.add("error-focus");
    document.querySelector("#email-msg").innerHTML = "Enter a valid email!";
  } else {
    email_field.classList.remove("error-focus");
    document.querySelector("#email-msg").innerHTML = "";
  }
  validateFields();
};

const validateFirstPasswordMsg = () => {
  const res = validateFirstPassword();
  if (res) {
    password.classList.add("error-focus");
    document.querySelector("#pass1-msg").innerHTML =
      "Password cannot be empty!";
  } else {
    password.classList.remove("error-focus");
    document.querySelector("#pass1-msg").innerHTML =
      "";
  }
  validateFields();
};

const validateSecondPasswordMsg = () => {
  const res = validateSecondPassword();
  if (res) {
    confirm_pass.classList.add("error-focus");
    document.querySelector("#pass-msg").innerHTML =
      "The two passwords didn't match!";
  } else {
    confirm_pass.classList.remove("error-focus");
    document.querySelector("#pass-msg").innerHTML = "";
  }
  validateFields();
};

function validateFields() {
  const btn = document.getElementById("submit-btn");
  if (
    !(
      validateSelect() ||
      validateUsername() ||
      validateEmail() ||
      validateFirstPassword() ||
      validateSecondPassword()
    )
  ) {
    btn.disabled = false;
  } else {
    btn.disabled = true;
  }
}
