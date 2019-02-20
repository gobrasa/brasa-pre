import { Component, OnInit } from '@angular/core';
import { Mentee } from '../shared/mentee.model';

@Component({
  selector: 'app-mentee',
  templateUrl: './mentee.page.html',
  styleUrls: ['./mentee.page.scss'],
})
export class MenteePage implements OnInit {

  private menteeDecks: Mentee;

  constructor() { }

  ngOnInit() {
  }

}
