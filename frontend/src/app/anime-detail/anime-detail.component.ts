import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { MatCardModule } from '@angular/material/card';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { NgIf, NgForOf } from '@angular/common';

@Component({
  selector: 'app-anime-detail',
  standalone: true,
  imports: [MatCardModule, MatButtonModule, MatIconModule, NgIf, NgForOf],
  templateUrl: './anime-detail.component.html',
  styleUrls: ['./anime-detail.component.css'],
})
export class AnimeDetailComponent implements OnInit {
  anime: any;

  constructor(private router: Router) {
    const navigation = this.router.getCurrentNavigation();
    this.anime = navigation?.extras.state?.['anime'];
  }

  ngOnInit() {
    if (!this.anime) {
      this.router.navigate(['/anime']);
    }
  }

  addToList() {
    console.log('Add to list clicked');
  }
}
