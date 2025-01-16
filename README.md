# Anime and Manga Tracker

A web application built using **Angular** and **Angular Material** to track and manage your favorite anime and manga. The application displays anime and manga data in an interactive and user-friendly grid of tiles, allowing users to click on each tile to view more details.

## Features
- Display anime/manga in a grid layout (tiles).
- View detailed information for each anime/manga.
- Pagination for fetching data in chunks (100 items per page).
- "Add to Library" button to manage your collection.

## Technologies Used
- **Angular**: Frontend framework for building the app.
- **Angular Material**: UI component library for providing Material Design components.
- **Axios**: Library used for fetching the data from a JSON file.
- **CSS Grid**: For creating a responsive grid layout.
  
## Setup Instructions

### Prerequisites
- Node.js and npm installed on your machine.
- Angular CLI installed globally. If you don’t have Angular CLI installed, run:
  ```bash
  npm install -g @angular/cli
  ```

## Installation
1. Clone the repository:
  ```bash
  git clone https://github.com/yourusername/anime-manga-tracker.git
  ```
2. Navigate into the project folder:
  ```bash
  cd anime-manga-tracker
  ```
3. Install the dependencies:
  ```bash
  npm install
  ```

## Running the App
Once the dependencies are installed, you can run the application using the Angular CLI:

  ```bash
  ng serve
  ```
The app will be available at http://localhost:4200.

## Folder Structure
  ```plaintext
src/
  assets/
    anime.json  <-- JSON file with anime data
  app/
    anime/
      anime.component.ts  <-- Anime list and tile display
      anime.component.html  <-- HTML for anime tiles
      anime.component.css  <-- Styles for anime tiles
    anime-detail/
      anime-detail.component.ts  <-- Detailed anime view
      anime-detail.component.html  <-- HTML for detailed anime view
      anime-detail.component.css  <-- Styles for detailed anime view
    manga/
      manga.component.ts  <-- Manga list and tile display
      manga.component.html  <-- HTML for manga tiles
      manga.component.css  <-- Styles for manga tiles
    manga-detail/
      manga-detail.component.ts  <-- Detailed manga view
      manga-detail.component.html  <-- HTML for detailed manga view
      manga-detail.component.css  <-- Styles for detailed manga view
    app-routing.module.ts  <-- App routing configuration
    app.module.ts  <-- Main Angular module
    app-routing.module.ts  <-- App routing configuration
    app.module.ts  <-- Main Angular module
  index.html  <-- Main HTML file
  styles.css  <-- Global styles
  ```

## Data
The app uses a static JSON file (anime-reponse.json/manga-response.json) stored in the assets folder for fetching anime details, which is displayed in a grid format. Each anime item contains:

- Title
- Rank
- Type (TV, Movie, etc.)
- Episodes
- Airing period
- Members (number of users who added it)
- Score
- Image URL
- Page URL

## Routing
- /anime: Displays the list of anime in tiles.
- /anime-detail: Shows detailed information for the selected anime, including an "Add to Library" button.

## Contributions
Feel free to fork this repository and contribute by submitting issues, suggestions, or pull requests.

## License
This project is licensed under the MIT License.
