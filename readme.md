# Wiki Encyclopedia

This project is a web-based encyclopedia application developed in Django as part of Harvard's CS50 Web Programming with Python and JavaScript course. The application allows users to create, edit, and view encyclopedia entries written in Markdown. Users can also search for specific entries and browse through a list of available entries.

## Getting Started

To get started with the project, follow the instructions below:

1. Clone the repository: `git clone https://github.com/TanjotSingh25/Knowledgepedia.git`
2. Navigate to the project directory: `cd Knowledgepedia`
3. Install the dependencies: `pip install -r requirements.txt`
4. Start the application: `python manage.py runserver`

By default, the application will be accessible at `http://localhost:8000` in your web browser.

## Usage

Once the application is up and running, you can start using the wiki:

- **Home**: The home page displays a list of all the available encyclopedia entries. Clicking on an entry will take you to its content.
- **Search**: You can search for specific entries by entering a query in the search box in the sidebar. The application will display a list of matching entries.
- **Entry Page**: Visiting `/wiki/TITLE`, where TITLE is the title of an encyclopedia entry, will render a page displaying the contents of that entry.
- **Create New Page**: Clicking on "Create New Page" will take you to a page where you can create a new encyclopedia entry. Enter a title and the Markdown content for the entry and click "Submit" to create it.
- **Edit Page**: On each entry page, you can click on the "Edit" link to edit the Markdown content. The existing content will be pre-populated in a textarea. Click "Submit" to save the changes.
- **Random Page**: Clicking on "Random Page" in the sidebar will take you to a random encyclopedia entry.

## Markdown to HTML Conversion

Each entry's Markdown content is converted to HTML before being displayed to the user. This conversion is done using the `md-block.js` library.

## Acknowledgments

This project is based on the specifications provided by Harvard's CS50 Web Programming with Python and JavaScript course. Special thanks to the course instructors and staff for their guidance and support throughout the project.

For more information about the project, refer to the [official project documentation](https://cs50.harvard.edu/web/2020/projects/1/wiki/).
