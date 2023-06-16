export function Student() {
  return (
    <div className="Student">
        <h3>Add New Student</h3>
        <form>
            <label> Name: </label>
            <input type="text" name="name" />
            <br/>
            <label> Phone Number: </label>
            <input type="text" name="phone" />
            <br/>
            <label> Number of Experiance</label>
            <input type="number" name="numberofexp"/>
        </form>
    </div>
  );
}