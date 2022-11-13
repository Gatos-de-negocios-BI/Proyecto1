import { Component, OnInit } from '@angular/core';
import { PublicacionService } from '../publicacion.service';
import { Publicacion } from '../publicacion';


@Component({
  selector: 'app-publicacion-list',
  templateUrl: './publicacion-list.component.html',
  styleUrls: ['./publicacion-list.component.css']
})

export class PublicacionListComponent implements OnInit {

  publicaciones: Array<Publicacion> = [];

  constructor(private publicacionService: PublicacionService) { }

  ngOnInit() {
    this.getPublicaciones();
  }

  getPublicaciones(): void{
    this.publicacionService.getPublicaciones().subscribe(
      (publicaciones) => this.publicaciones = publicaciones
    );
  }

}
