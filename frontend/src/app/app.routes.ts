import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomepageComponent } from './homepage/homepage.component';
import { AnimeComponent } from './anime/anime.component';
import { MangaComponent } from './manga/manga.component';
import { AnimeDetailComponent } from './anime-detail/anime-detail.component';
import { MangaDetailComponent } from './manga-detail/manga-detail.component';
import { MyListComponent } from './my-list/my-list.component';

export const routes: Routes = [
  { path: '', component: HomepageComponent },
  { path: 'anime', component: AnimeComponent },
  { path: 'manga', component: MangaComponent },
  { path: 'anime-detail', component: AnimeDetailComponent },
  { path: 'manga-detail', component: MangaDetailComponent },
  { path: 'my-list', component: MyListComponent },
];
