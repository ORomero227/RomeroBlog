# RomeroBlog

This is a simple blog application built with Flask. It allows users to register, log in, view and comment on blog posts, and for administrators (users with special permissions), it provides the ability to add, edit, and delete posts.

## Features

- **User Registration**: New users can sign up by providing their name, email, and password.
- **User Login**: Registered users can log in and comment on posts.
- **Blog Posts**: Admin users can add, edit, and delete blog posts.
- **Comments**: Users can add comments to each blog post.
- **User Authentication**: Implemented with Flask-Login to protect specific routes.

## Technologies Used

- **Backend**: Flask, SQLAlchemy, Flask-Login
- **Frontend**: HTML, Bootstrap5, Flask-CKEditor
- **Database**: SQLite (via SQLAlchemy)
- **Environment**: Python, dotenv for managing environment variables

## Setup

1. Clone this repository:

    ```bash
    git clone https://github.com/ORomero227/RomeroBlog.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. **Create a `.env` file:**

   Copy the contents of the `.env-example` file and create a new `.env` file in the root directory of your project. The `.env-example` file contains placeholders for all the necessary environment variables.

4. Initialize the database and load example data by running the Flask application:

    ```bash
    flask run
    ```

   This will create the necessary tables and insert sample data into the database.

## Routes

- **/login**: Allows users to log in.
- **/register**: Allows users to sign up.
- **/logout**: Logs out the current user.
- **/**: Displays all blog posts.
- **/post/<int:post_id>**: Displays a specific blog post and its comments.
- **/add-post**: Allows admin users to add new blog posts.
- **/edit-post/<int:post_id>**: Allows admin users to edit an existing blog post.
- **/delete-post/<int:post_id>**: Allows admin users to delete a blog post.

## Admin Users

- The first user created will automatically have admin privileges.
- Admin users can add, edit, and delete blog posts.

## Gallery
![RomeroBlogHero](https://github.com/user-attachments/assets/95aa6a45-ff46-4329-85cf-59bb78c43fb9)
![LatestPosts](https://github.com/user-attachments/assets/2417277c-dd2b-4e6a-b9b3-b0b24fa438cf)
![PostIndex](https://github.com/user-attachments/assets/5d0bf199-be73-43d8-9c49-b2895eab9263)
![NewPostForm](https://github.com/user-attachments/assets/48af76f5-e48f-496c-81e6-cc6f1224cec8)
