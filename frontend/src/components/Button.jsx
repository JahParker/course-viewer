const Button = ({ variant, onClick }) => {
  let color;
  let action;
  let content;

  // May change onClick prop to be a function within Button
  const addNew = () => {

  }

  const submit = () => {
    
  }

  const cancel = () => {
    
  }

  const deletion = () => {
    
  }

  switch (variant) {
    case "add":
      color = "darkblue";
      action = addNew;
      content = "+"
      break;
    case "submit":
      color = "darkblue";
      action = submit;
      content = "Submit"
      break;
    case "cancel":
      color = "lightblue";
      action = cancel;
      content = "Cancel"
      break;
    case "delete":
      color = "red";
      action = deletion;
      content = "Delete"
      break;
  }

  return (
    <button className={`button-${color}`} onClick={onClick}>
      {content}
    </button>
  )
}

export default Button;