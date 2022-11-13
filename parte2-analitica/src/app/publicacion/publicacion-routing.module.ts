import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { PublicacionListComponent } from './publicacion-list/publicacion-list.component';

const routes: Routes = [{
  path: 'posts',
  children: [
    {
      path: 'list',
      component: PublicacionListComponent
    }
  ]
}];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class PublicacionRoutingModule { }
