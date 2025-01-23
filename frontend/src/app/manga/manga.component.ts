import { Component, OnInit, ViewChild } from '@angular/core';
import axios from 'axios';
import { MatPaginator } from '@angular/material/paginator';
import { Router } from '@angular/router';
import { MatCardModule } from '@angular/material/card';
import { MatButtonModule } from '@angular/material/button';
import { MatPaginatorModule } from '@angular/material/paginator';
import { NgIf, NgForOf } from '@angular/common';

@Component({
  selector: 'app-manga',
  standalone: true,
  imports: [MatCardModule, MatButtonModule, MatPaginatorModule, NgIf, NgForOf],
  templateUrl: './manga.component.html',
  styleUrls: ['./manga.component.css'],
})
export class MangaComponent implements OnInit {
  mangaList: any[] = [];
  displayedManga: any[] = [];
  pageSize: number = 50;
  currentPage: number = 0;

  @ViewChild(MatPaginator) paginator: MatPaginator | undefined;

  constructor(private router: Router) {}

  ngOnInit() {
    this.loadMangaData();
  }

  loadMangaData() {
    axios
      .get('http://localhost:5000/api/manga')
      .then((response) => {
        this.mangaList = response.data.sort(
          (a: any, b: any) => b.Score - a.Score
        );
        this.updatePageData();
      })
      .catch((error) => {
        console.error('Error loading manga data:', error);
      });
  }

  updatePageData() {
    const startIndex = this.currentPage * this.pageSize;
    const endIndex = startIndex + this.pageSize;
    this.displayedManga = this.mangaList.slice(startIndex, endIndex);
  }

  onPageChange(event: any) {
    this.currentPage = event.pageIndex;
    this.updatePageData();
  }

  onTileClick(manga: any) {
    this.router.navigate(['/manga-detail'], { state: { manga } });
  }
}
