import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { MatCardModule } from '@angular/material/card';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatSnackBar } from '@angular/material/snack-bar';
import { NgIf, NgForOf } from '@angular/common';
import axios from 'axios';

@Component({
  selector: 'app-anime-detail',
  standalone: true,
  imports: [MatCardModule, MatButtonModule, MatIconModule, NgIf, NgForOf],
  templateUrl: './anime-detail.component.html',
  styleUrls: ['./anime-detail.component.css'],
})
export class AnimeDetailComponent implements OnInit {
  anime: any;

  constructor(private router: Router, private snackBar: MatSnackBar) {
    const navigation = this.router.getCurrentNavigation();
    this.anime = navigation?.extras.state?.['anime'];
  }

  ngOnInit() {
    if (!this.anime) {
      this.router.navigate(['/anime']);
    }
  }

  addToList() {
    axios
      .post('http://localhost:5000/api/anime/save', {
        anime_id: this.anime.id,
      })
      .then((response) => {
        this.snackBar.open('Added to your list!', 'Close', {
          duration: 3000,
        });
      })
      .catch((error) => {
        this.snackBar.open(
          error.response?.data?.message || 'Error adding to list',
          'Close',
          {
            duration: 3000,
          }
        );
      });
  }
}
