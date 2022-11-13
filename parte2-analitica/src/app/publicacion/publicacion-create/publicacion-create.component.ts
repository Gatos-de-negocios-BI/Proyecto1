import { Component, OnInit } from '@angular/core';
import { PublicacionService } from '../publicacion.service';
import { NgbModalConfig, NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Publicacion } from '../publicacion';

@Component({
  selector: 'app-publicacion-create',
  templateUrl: './publicacion-create.component.html',
  styleUrls: ['./publicacion-create.component.css'],
  providers: [NgbModalConfig, NgbModal],
})
export class PublicacionCreateComponent implements OnInit {

  prediction: string = 'non-suicide';
  constructor(private publicacionService: PublicacionService, config: NgbModalConfig, private modalService: NgbModal) {
    config.backdrop = 'static';
    config.keyboard = false;
  }

  ngOnInit() {
  }

  getPrediction(text: string, content:any, content1:any): void {
    this.publicacionService.predictText(text).subscribe((prediction) => {
      this.prediction = prediction;
      if (prediction == 'suicide'){
        this.modalService.open(content)
      }else{
        this.modalService.open(content1)
      }
    });
    this.publicacionService.postPublicacion({"text": text, "person": "TrashCam9"}).subscribe()
  }

}
