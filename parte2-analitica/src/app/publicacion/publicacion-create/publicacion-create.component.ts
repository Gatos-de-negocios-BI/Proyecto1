import { Component, OnInit } from '@angular/core';
import { PublicacionService } from '../publicacion.service';

@Component({
  selector: 'app-publicacion-create',
  templateUrl: './publicacion-create.component.html',
  styleUrls: ['./publicacion-create.component.css']
})
export class PublicacionCreateComponent implements OnInit {

  prediction: string = 'non-suicide';
  constructor(private publicacionService: PublicacionService) {  }

  ngOnInit() {
  }

  getPrediction(text: string): void {
    this.publicacionService.predictText(text).subscribe((prediction) => {
      this.prediction = prediction;
      console.log(prediction);
    });
  }

}
