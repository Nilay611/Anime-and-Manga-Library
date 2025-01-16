import { Component, OnInit, ViewChild } from '@angular/core';
import axios from 'axios';
import { MatPaginator } from '@angular/material/paginator';
import { Router } from '@angular/router';
import { MatCardModule } from '@angular/material/card';
import { MatButtonModule } from '@angular/material/button';
import { MatPaginatorModule } from '@angular/material/paginator';
import { NgIf, NgForOf } from '@angular/common';

@Component({
  selector: 'app-anime',
  standalone: true,
  imports: [MatCardModule, MatButtonModule, MatPaginatorModule, NgIf, NgForOf],
  templateUrl: './anime.component.html',
  styleUrls: ['./anime.component.css'],
})
export class AnimeComponent implements OnInit {
  animeList: any[] = [];
  displayedAnime: any[] = [];
  pageSize: number = 50;
  currentPage: number = 0;

  @ViewChild(MatPaginator) paginator: MatPaginator | undefined;

  constructor(private router: Router) {}

  ngOnInit() {
    this.loadAnimeData();
  }

  loadAnimeData() {
    axios
      .get('anime-response.json')
      .then((response) => {
        this.animeList = response.data.sort(
          (a: any, b: any) => b.Score - a.Score
        );
        this.updatePageData();
      })
      .catch((error) => {
        console.error('Error loading anime data:', error);
      });
  }

  updatePageData() {
    const startIndex = this.currentPage * this.pageSize;
    const endIndex = startIndex + this.pageSize;
    this.displayedAnime = this.animeList.slice(startIndex, endIndex);
  }

  onPageChange(event: any) {
    this.currentPage = event.pageIndex;
    this.updatePageData();
  }

  onTileClick(anime: any) {
    this.router.navigate(['/anime-detail'], { state: { anime } });
  }
}
