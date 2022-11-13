import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment';

import { Publicacion } from './publicacion';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PublicacionService {

  private apiUrl: string = environment.baseUrl;

  constructor(private http: HttpClient) { }

  getPublicaciones(): Observable<Publicacion[]> {

    return this.http.get<Publicacion[]>(this.apiUrl + 'lastpublic');
  }

}
