import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { MatCardModule } from '@angular/material/card';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatSnackBar } from '@angular/material/snack-bar';
import { NgIf, NgForOf } from '@angular/common';
import axios from 'axios';

@Component({
  selector: 'app-manga-detail',
  standalone: true,
  imports: [MatCardModule, MatButtonModule, MatIconModule, NgIf, NgForOf],
  templateUrl: './manga-detail.component.html',
  styleUrls: ['./manga-detail.component.css'],
})
export class MangaDetailComponent implements OnInit {
  manga: any;

  constructor(private router: Router, private snackBar: MatSnackBar) {
    const navigation = this.router.getCurrentNavigation();
    this.manga = navigation?.extras.state?.['manga'];
  }

  ngOnInit() {
    if (!this.manga) {
      this.router.navigate(['/manga']);
    }
  }

  addToList() {
    axios
      .post('http://localhost:5000/api/manga/save', {
        manga_id: this.manga.id,
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
