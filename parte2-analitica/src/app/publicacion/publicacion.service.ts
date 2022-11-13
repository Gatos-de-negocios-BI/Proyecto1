import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment';

import { Publicacion } from './publicacion';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PublicacionService {

  private apiUrl: string = environment.baseUrl + 'publicaciones';

  constructor(private http: HttpClient) { }

  getPublicaciones(): Publicacion[] {

    return [new Publicacion(1, 'Hola', '11-09-2002', 'non-suicide', 'Trash')]
  }

}
