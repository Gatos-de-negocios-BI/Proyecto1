export class Publicacion {
  id: number;
  text: string;
  date: any;
  classification: string;
  person: string;

  constructor(
    id: number,
    text: string,
    date: any,
    classificacion: string,
    person: string
  ){
    this.id = id;
    this.text = text;
    this.date = date;
    this.classification = classificacion;
    this.person = person;
  }
}
