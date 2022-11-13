import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PublicacionListComponent } from './publicacion/publicacion-list/publicacion-list.component';
import { PublicacionCreateComponent } from './publicacion/publicacion-create/publicacion-create.component';
import { PublicacionStatsComponent } from './publicacion/publicacion-stats/publicacion-stats.component';

const routes: Routes = [
  { path: '', component: PublicacionListComponent},
  { path: 'posts/create', component: PublicacionCreateComponent},
  { path: 'posts/stats', component: PublicacionStatsComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
