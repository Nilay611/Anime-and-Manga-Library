import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { MatCardModule } from '@angular/material/card';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatTabsModule } from '@angular/material/tabs';
import { NgIf, NgForOf } from '@angular/common';
import axios from 'axios';

@Component({
  selector: 'app-my-list',
  standalone: true,
  imports: [
    MatCardModule,
    MatButtonModule,
    MatIconModule,
    MatTabsModule,
    NgIf,
    NgForOf,
  ],
  templateUrl: './my-list.component.html',
  styleUrls: ['./my-list.component.css'],
})
export class MyListComponent implements OnInit {
  savedAnime: any[] = [];
  savedManga: any[] = [];

  constructor(private router: Router) {}

  ngOnInit() {
    this.loadSavedItems();
  }

  loadSavedItems() {
    // Load saved anime
    axios
      .get('http://localhost:5000/api/saved/anime')
      .then((response) => {
        this.savedAnime = response.data;
      })
      .catch((error) => {
        console.error('Error loading saved anime:', error);
      });

    // Load saved manga
    axios
      .get('http://localhost:5000/api/saved/manga')
      .then((response) => {
        this.savedManga = response.data;
      })
      .catch((error) => {
        console.error('Error loading saved manga:', error);
      });
  }

  onAnimeClick(anime: any) {
    this.router.navigate(['/anime-detail'], { state: { anime } });
  }

  onMangaClick(manga: any) {
    this.router.navigate(['/manga-detail'], { state: { manga } });
  }
}
