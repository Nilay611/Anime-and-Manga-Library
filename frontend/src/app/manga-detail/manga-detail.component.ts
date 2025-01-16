import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { MatCardModule } from '@angular/material/card';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { NgIf, NgForOf } from '@angular/common';

@Component({
  selector: 'app-manga-detail',
  standalone: true,
  imports: [MatCardModule, MatButtonModule, MatIconModule, NgIf, NgForOf],
  templateUrl: './manga-detail.component.html',
  styleUrls: ['./manga-detail.component.css'],
})
export class MangaDetailComponent implements OnInit {
  manga: any;

  constructor(private router: Router) {
    const navigation = this.router.getCurrentNavigation();
    this.manga = navigation?.extras.state?.['manga'];
  }

  ngOnInit() {
    if (!this.manga) {
      this.router.navigate(['/manga']);
    }
  }

  addToList() {
    // Implement add to list functionality
    console.log('Add to list clicked');
  }
}
