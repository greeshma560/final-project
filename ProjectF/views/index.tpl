<!DOCTYPE html>
<html>
<head>
    <title>University and Branches</title>
</head>
<body>
    <h1>University List</h1>
    
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Location</th>
            <th>Actions</th>
        </tr>
        % for university in universities:
            <tr>
                <td>{{ university[0] }}</td>
                <td>{{ university[1] }}</td>
                <td>{{ university[2] }}</td>
                <td>
                    <a href="/update/{{ university[0] }}">Update</a>
                    <a href="/delete/{{ university[0] }}">Delete</a>
                </td>
            </tr>
        % end
    </table>

    <h1>Add/Update University</h1>
    <form action="/add" method="post">
        <input type="hidden" name="update_id" value="{{ update_id }}">
        Name: <input type="text" name="name" value="{{ update_name }}" required><br>
        Location: <input type="text" name="location" value="{{ update_location }}" required><br>
        <input type="submit" value="{{ 'Update University' if update_id else 'Add University' }}">
    </form>
</body>
</html>
