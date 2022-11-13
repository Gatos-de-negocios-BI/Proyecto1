import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PublicacionListComponent } from './publicacion/publicacion-list/publicacion-list.component';

const routes: Routes = [
  { path: '', component: PublicacionListComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
