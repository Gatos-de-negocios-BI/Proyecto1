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
    //this.publicacionService.getPublicaciones().subscribe(
      //(publicaciones) => this.publicaciones = publicaciones
    //);
    this.publicacionService.getPublicaciones()
    this.publicaciones.push(new Publicacion(1, 'El suicidio ta feo, pls help me aa', '2020-01-01 11:20:00', 'suicide', 'TrashCam9'))
    this.publicaciones.push(new Publicacion(2, 'El suicidio ta feo, pls help me ai', '2020-01-01 11:20:00', 'suicide', 'TrashCam9'))
    this.publicaciones.push(new Publicacion(3, 'El suicidio ta feo, pls help me ai', '2020-01-01 11:20:00', 'suicide', 'TrashCam9'))
    this.publicaciones.push(new Publicacion(4, 'El suicidio ta feo, pls help me ai', '2020-01-01 11:20:00', 'suicide', 'TrashCam9'))
    this.publicaciones.push(new Publicacion(5, 'El suicidio ta feo, pls help me ai', '2020-01-01 11:20:00', 'suicide', 'TrashCam9'))
    this.publicaciones.push(new Publicacion(6, 'El suicidio ta feo, pls help me ai', '2020-01-01 11:20:00', 'suicide', 'TrashCam9'))
  }

}
